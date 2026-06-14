import pandas as pd
import numpy as np


def simulate_competing_risks(
    n_samples=10000,
    seed=None,
    baseline_hazard_event1=0.01,
    baseline_hazard_event2=0.05,
    censoring_rate=0.01
):
    """
    Synthetic competing-risks data.

    Event coding:
        0 = Censored
        1 = Event 1
        2 = Event 2
    """

    rng = np.random.default_rng(seed)

    # Continuous covariates
    X_cont = rng.normal(0, 1, size=(n_samples, 6))

    # Binary covariates
    X_bin = rng.binomial(1, 0.5, size=(n_samples, 6))

    X = np.hstack([X_cont, X_bin])

    feature_names = [f"x{i}" for i in range(1, 13)]

    # True coefficients
    beta_event1 = np.array([
        1.20, #x1
       -0.95, #x2
        0.00, #x3
        0.00, #x4
        0.60, #x5
       -0.40, #x6
        1.80, #x7
       -1.50, #x8
        0.00, #x9
        0.00, #x10
        0.90, #x11
       -0.70  #x12
    ])

    
    beta_event2 = np.array([
        0.00, #x1
        0.00, #x2
        1.10, #x3
       -0.80, #x4
        0.50, #x5
       -0.30, #x6
        0.00, #x7
        0.00, #x8
        1.60, #x9
       -1.20, #x10
        0.75, #x11
       -0.50  #x12
    ])

    # Linear predictors
    eta1 = X @ beta_event1
    eta2 = X @ beta_event2

    # Cause-specific hazards
    lambda1 = baseline_hazard_event1 * np.exp(eta1)
    lambda2 = baseline_hazard_event2 * np.exp(eta2)

    # Overall hazard
    total_hazard = lambda1 + lambda2

    # Event times
    event_time = -np.log(rng.uniform(size=n_samples)) / total_hazard

    # Event type
    prob_event1 = lambda1 / total_hazard
    event_type = np.where(
        rng.uniform(size=n_samples) < prob_event1,
        1,
        2
    )

    # Independent censoring
    censor_time = rng.exponential(
        scale=1 / censoring_rate,
        size=n_samples
    )

    # Observed outcome
    observed_time = np.minimum(event_time, censor_time)

    event = np.where(
        event_time <= censor_time,
        event_type,
        0
    )

    # DataFrame
    df = pd.DataFrame(X, columns=feature_names)

    df["time"] = observed_time
    df["event"] = event

    # Optional: retain true risk scores
    df["true_lp_event1"] = eta1
    df["true_lp_event2"] = eta2

    return df, beta_event1, beta_event2


