# Old versus new CSV results

All differences are new minus old. Values are descriptive run comparisons, not significance tests. Images were not inspected. Entropy retention is 0.1 throughout. Training duration is seconds per fold. Fold SD uses ddof=1 (sample SD), matching the recorded summary convention.

## Source selection

Synthetic old uses *_1test_old: FULL C-index 0.850110 and duration 58.1627 s match the thesis. PBC uses the archived non-IND folders: FULL 0.755646 matches the thesis. FH uses archived *_FH. Additional archived PBC_IND runs and FULL_1test are reported separately; Results/FullRisk is a separate baseline and is not silently substituted for Results/FULL.

Pooled Brier, fold-average Brier and integrated Brier (IBS) are separate metrics. Current pooled Brier is evaluated at the grid point nearest the median observed time. CSV summaries alone do not establish that old and new pooled evaluation protocols are identical. Changes include all run/pipeline differences, not an isolated estimate of the loss correction.

## Synthetic

### Pooled metrics and training duration

| Configuration | C-index old → new (delta) | IBS old → new (delta) | Brier old → new (delta) | Seconds/fold old → new (delta) |
|---|---|---|---|---|
| FULL | 0.8501 → 0.8510 (+0.0009) | 0.2254 → 0.1628 (-0.0626) | 0.1065 → 0.1044 (-0.0021) | 58.2 → 68.9 (+10.7) |
| NCC m=5 | 0.8346 → 0.8467 (+0.0122) | 0.3786 → 0.2520 (-0.1266) | 0.1394 → 0.1294 (-0.0099) | 65.9 → 70.2 (+4.3) |
| NCC m=10 | 0.8400 → 0.8497 (+0.0097) | 0.2674 → 0.1862 (-0.0812) | 0.1171 → 0.1109 (-0.0062) | 51.9 → 56.3 (+4.4) |
| NCC m=20 | 0.8446 → 0.8497 (+0.0052) | 0.2380 → 0.1688 (-0.0693) | 0.1102 → 0.1062 (-0.0040) | 63.8 → 57.7 (-6.1) |
| NCC m=50 | 0.8470 → 0.8500 (+0.0030) | 0.2289 → 0.1642 (-0.0647) | 0.1079 → 0.1051 (-0.0028) | 86.9 → 71.0 (-15.9) |
| NCC m=100 | 0.8493 → 0.8504 (+0.0011) | 0.2269 → 0.1632 (-0.0637) | 0.1069 → 0.1047 (-0.0021) | 85.1 → 73.9 (-11.3) |
| SCC a=0.05 | 0.8419 → 0.8485 (+0.0066) | 0.2346 → 0.1678 (-0.0668) | 0.1100 → 0.1054 (-0.0046) | 46.4 → 35.3 (-11.0) |
| SCC a=0.1 | 0.8482 → 0.8471 (-0.0011) | 0.2280 → 0.1660 (-0.0620) | 0.1073 → 0.1057 (-0.0016) | 64.6 → 46.5 (-18.0) |
| SCC a=0.2 | 0.8442 → 0.8511 (+0.0069) | 0.2280 → 0.1634 (-0.0645) | 0.1092 → 0.1040 (-0.0052) | 56.4 → 46.2 (-10.2) |
| SCC a=0.3 | 0.8468 → 0.8502 (+0.0033) | 0.2262 → 0.1640 (-0.0622) | 0.1081 → 0.1050 (-0.0031) | 60.9 → 53.7 (-7.2) |
| SCC a=0.5 | 0.8492 → 0.8517 (+0.0026) | 0.2253 → 0.1624 (-0.0629) | 0.1069 → 0.1039 (-0.0030) | 38.5 → 60.9 (+22.4) |
| Entropy t=0.1 | 0.8504 → 0.5629 (-0.2875) | 0.2727 → 0.4077 (+0.1350) | 0.1259 → 0.1760 (+0.0501) | 29.4 → 43.2 (+13.7) |
| Entropy t=0.5 | 0.8510 → 0.8499 (-0.0011) | 0.2252 → 0.1656 (-0.0595) | 0.1071 → 0.1052 (-0.0019) | 29.5 → 31.7 (+2.3) |
| Entropy t=1 | 0.8472 → 0.8505 (+0.0034) | 0.2266 → 0.1640 (-0.0627) | 0.1081 → 0.1047 (-0.0034) | 32.0 → 43.2 (+11.2) |
| Entropy t=5 | 0.8481 → 0.8512 (+0.0031) | 0.2265 → 0.1630 (-0.0635) | 0.1073 → 0.1045 (-0.0027) | 58.1 → 50.7 (-7.4) |
| Entropy t=10 | 0.8477 → 0.8509 (+0.0031) | 0.2269 → 0.1631 (-0.0638) | 0.1075 → 0.1047 (-0.0028) | 58.7 → 46.6 (-12.0) |

### Fold summaries

Mean ± SD across five folds. The Std column in the Brier source is within-fold variation across time; its mean and SD below are explicitly labelled separately.

| Configuration | Metric | Old mean ± SD | New mean ± SD | Mean delta |
|---|---|---|---|---|
| FULL | CIndex_scores:CIndex_Score | 0.849887 ± 0.006770 | 0.850771 ± 0.006677 | +0.000884 |
| FULL | IBS_scores:IBS_Score | 0.165930 ± 0.004161 | 0.162772 ± 0.004045 | -0.003159 |
| FULL | Training_Durations:Training_Duration | 58.162685 ± 21.868195 | 68.859840 ± 13.408420 | +10.697155 |
| FULL | brier_scores:Mean | 0.101414 ± 0.001141 | 0.100377 ± 0.001129 | -0.001036 |
| FULL | brier_scores:Std | 0.053387 ± 0.003014 | 0.052379 ± 0.002870 | -0.001008 |
| NCC m=5 | CIndex_scores:CIndex_Score | 0.834645 ± 0.009504 | 0.847091 ± 0.007631 | +0.012446 |
| NCC m=5 | IBS_scores:IBS_Score | 0.263229 ± 0.009735 | 0.251985 ± 0.013032 | -0.011244 |
| NCC m=5 | Training_Durations:Training_Duration | 65.889791 ± 19.104166 | 70.189016 ± 24.504326 | +4.299225 |
| NCC m=5 | brier_scores:Mean | 0.143891 ± 0.003321 | 0.136669 ± 0.004860 | -0.007221 |
| NCC m=5 | brier_scores:Std | 0.090666 ± 0.005219 | 0.086562 ± 0.006448 | -0.004104 |
| NCC m=10 | CIndex_scores:CIndex_Score | 0.840161 ± 0.008148 | 0.849531 ± 0.007946 | +0.009370 |
| NCC m=10 | IBS_scores:IBS_Score | 0.193549 ± 0.008313 | 0.186196 ± 0.005939 | -0.007353 |
| NCC m=10 | Training_Durations:Training_Duration | 51.931640 ± 11.225883 | 56.299824 ± 13.178209 | +4.368185 |
| NCC m=10 | brier_scores:Mean | 0.114358 ± 0.001653 | 0.109840 ± 0.001862 | -0.004518 |
| NCC m=10 | brier_scores:Std | 0.063552 ± 0.004707 | 0.060926 ± 0.003658 | -0.002625 |
| NCC m=20 | CIndex_scores:CIndex_Score | 0.844532 ± 0.009010 | 0.849530 ± 0.007482 | +0.004998 |
| NCC m=20 | IBS_scores:IBS_Score | 0.174923 ± 0.006732 | 0.168755 ± 0.004866 | -0.006168 |
| NCC m=20 | Training_Durations:Training_Duration | 63.818970 ± 20.056666 | 57.733171 ± 14.081289 | -6.085799 |
| NCC m=20 | brier_scores:Mean | 0.105854 ± 0.001349 | 0.102840 ± 0.001543 | -0.003014 |
| NCC m=20 | brier_scores:Std | 0.056681 ± 0.003930 | 0.054510 ± 0.003199 | -0.002171 |
| NCC m=50 | CIndex_scores:CIndex_Score | 0.846864 ± 0.007807 | 0.849891 ± 0.005887 | +0.003027 |
| NCC m=50 | IBS_scores:IBS_Score | 0.169085 ± 0.004281 | 0.164202 ± 0.004376 | -0.004883 |
| NCC m=50 | Training_Durations:Training_Duration | 86.942888 ± 55.757924 | 71.036376 ± 27.342686 | -15.906511 |
| NCC m=50 | brier_scores:Mean | 0.103141 ± 0.000929 | 0.101120 ± 0.001005 | -0.002021 |
| NCC m=50 | brier_scores:Std | 0.054540 ± 0.002997 | 0.052904 ± 0.003010 | -0.001636 |
| NCC m=100 | CIndex_scores:CIndex_Score | 0.849101 ± 0.008523 | 0.850314 ± 0.007767 | +0.001213 |
| NCC m=100 | IBS_scores:IBS_Score | 0.167123 ± 0.005005 | 0.163172 ± 0.004410 | -0.003951 |
| NCC m=100 | Training_Durations:Training_Duration | 85.118307 ± 32.299728 | 73.864162 ± 14.711849 | -11.254145 |
| NCC m=100 | brier_scores:Mean | 0.101938 ± 0.001066 | 0.100642 ± 0.000628 | -0.001297 |
| NCC m=100 | brier_scores:Std | 0.053880 ± 0.003237 | 0.052532 ± 0.003047 | -0.001349 |
| SCC a=0.05 | CIndex_scores:CIndex_Score | 0.842465 ± 0.006016 | 0.848730 ± 0.009042 | +0.006265 |
| SCC a=0.05 | IBS_scores:IBS_Score | 0.173757 ± 0.003243 | 0.167783 ± 0.007440 | -0.005974 |
| SCC a=0.05 | Training_Durations:Training_Duration | 46.387201 ± 12.424647 | 35.349168 ± 5.251096 | -11.038034 |
| SCC a=0.05 | brier_scores:Mean | 0.105409 ± 0.002472 | 0.102185 ± 0.002286 | -0.003225 |
| SCC a=0.05 | brier_scores:Std | 0.056339 ± 0.002365 | 0.054238 ± 0.004000 | -0.002101 |
| SCC a=0.1 | CIndex_scores:CIndex_Score | 0.848594 ± 0.008101 | 0.847106 ± 0.008826 | -0.001488 |
| SCC a=0.1 | IBS_scores:IBS_Score | 0.168015 ± 0.005669 | 0.165927 ± 0.005943 | -0.002088 |
| SCC a=0.1 | Training_Durations:Training_Duration | 64.574398 ± 13.605955 | 46.544828 ± 15.690127 | -18.029570 |
| SCC a=0.1 | brier_scores:Mean | 0.102453 ± 0.001638 | 0.101987 ± 0.002406 | -0.000466 |
| SCC a=0.1 | brier_scores:Std | 0.054194 ± 0.003495 | 0.053594 ± 0.003542 | -0.000600 |
| SCC a=0.2 | CIndex_scores:CIndex_Score | 0.844112 ± 0.007554 | 0.851062 ± 0.008761 | +0.006950 |
| SCC a=0.2 | IBS_scores:IBS_Score | 0.169781 ± 0.003784 | 0.163469 ± 0.005015 | -0.006312 |
| SCC a=0.2 | Training_Durations:Training_Duration | 56.358192 ± 11.737528 | 46.165303 ± 13.265325 | -10.192889 |
| SCC a=0.2 | brier_scores:Mean | 0.103949 ± 0.001931 | 0.100382 ± 0.001531 | -0.003567 |
| SCC a=0.2 | brier_scores:Std | 0.054760 ± 0.002659 | 0.052651 ± 0.003000 | -0.002110 |
| SCC a=0.3 | CIndex_scores:CIndex_Score | 0.846786 ± 0.006003 | 0.850121 ± 0.006148 | +0.003336 |
| SCC a=0.3 | IBS_scores:IBS_Score | 0.168077 ± 0.003457 | 0.163989 ± 0.004421 | -0.004088 |
| SCC a=0.3 | Training_Durations:Training_Duration | 60.882758 ± 9.567093 | 53.659461 ± 16.665219 | -7.223298 |
| SCC a=0.3 | brier_scores:Mean | 0.102913 ± 0.001460 | 0.101070 ± 0.002025 | -0.001843 |
| SCC a=0.3 | brier_scores:Std | 0.054180 ± 0.002566 | 0.052818 ± 0.002941 | -0.001362 |
| SCC a=0.5 | CIndex_scores:CIndex_Score | 0.849064 ± 0.007241 | 0.851584 ± 0.007378 | +0.002520 |
| SCC a=0.5 | IBS_scores:IBS_Score | 0.166379 ± 0.004664 | 0.162387 ± 0.004351 | -0.003992 |
| SCC a=0.5 | Training_Durations:Training_Duration | 38.465799 ± 4.960731 | 60.881578 ± 24.917293 | +22.415779 |
| SCC a=0.5 | brier_scores:Mean | 0.101700 ± 0.000367 | 0.100018 ± 0.001228 | -0.001681 |
| SCC a=0.5 | brier_scores:Std | 0.053578 ± 0.003112 | 0.052243 ± 0.002976 | -0.001335 |
| Entropy t=0.1 | CIndex_scores:CIndex_Score | 0.850542 ± 0.008998 | 0.562757 ± 0.037904 | -0.287785 |
| Entropy t=0.1 | IBS_scores:IBS_Score | 0.203584 ± 0.003378 | 0.407788 ± 0.007006 | +0.204204 |
| Entropy t=0.1 | Training_Durations:Training_Duration | 29.442671 ± 3.003934 | 43.185505 ± 15.766139 | +13.742835 |
| Entropy t=0.1 | brier_scores:Mean | 0.121296 ± 0.004407 | 0.201687 ± 0.003790 | +0.080391 |
| Entropy t=0.1 | brier_scores:Std | 0.067208 ± 0.001449 | 0.149178 ± 0.004075 | +0.081970 |
| Entropy t=0.5 | CIndex_scores:CIndex_Score | 0.850834 ± 0.008687 | 0.849676 ± 0.008515 | -0.001157 |
| Entropy t=0.5 | IBS_scores:IBS_Score | 0.166534 ± 0.004650 | 0.165617 ± 0.005358 | -0.000918 |
| Entropy t=0.5 | Training_Durations:Training_Duration | 29.461548 ± 1.149391 | 31.719365 ± 4.651146 | +2.257817 |
| Entropy t=0.5 | brier_scores:Mean | 0.101780 ± 0.000756 | 0.101524 ± 0.001124 | -0.000256 |
| Entropy t=0.5 | brier_scores:Std | 0.053683 ± 0.003148 | 0.053427 ± 0.003407 | -0.000257 |
| Entropy t=1 | CIndex_scores:CIndex_Score | 0.847074 ± 0.007398 | 0.850391 ± 0.006857 | +0.003317 |
| Entropy t=1 | IBS_scores:IBS_Score | 0.168280 ± 0.004966 | 0.163979 ± 0.004071 | -0.004300 |
| Entropy t=1 | Training_Durations:Training_Duration | 31.979745 ± 2.380998 | 43.205135 ± 10.356457 | +11.225391 |
| Entropy t=1 | brier_scores:Mean | 0.102876 ± 0.000527 | 0.100818 ± 0.000925 | -0.002057 |
| Entropy t=1 | brier_scores:Std | 0.054342 ± 0.003277 | 0.052845 ± 0.002842 | -0.001496 |
| Entropy t=5 | CIndex_scores:CIndex_Score | 0.847817 ± 0.007497 | 0.851085 ± 0.005862 | +0.003268 |
| Entropy t=5 | IBS_scores:IBS_Score | 0.167456 ± 0.004268 | 0.162993 ± 0.003741 | -0.004463 |
| Entropy t=5 | Training_Durations:Training_Duration | 58.109348 ± 14.048594 | 50.723470 ± 21.465991 | -7.385879 |
| Entropy t=5 | brier_scores:Mean | 0.102282 ± 0.000799 | 0.100467 ± 0.000936 | -0.001815 |
| Entropy t=5 | brier_scores:Std | 0.053984 ± 0.003028 | 0.052419 ± 0.002836 | -0.001565 |
| Entropy t=10 | CIndex_scores:CIndex_Score | 0.847536 ± 0.007563 | 0.850749 ± 0.005232 | +0.003213 |
| Entropy t=10 | IBS_scores:IBS_Score | 0.167739 ± 0.004224 | 0.163137 ± 0.003712 | -0.004602 |
| Entropy t=10 | Training_Durations:Training_Duration | 58.653840 ± 3.227694 | 46.618423 ± 13.038156 | -12.035417 |
| Entropy t=10 | brier_scores:Mean | 0.102474 ± 0.000800 | 0.100611 ± 0.001244 | -0.001863 |
| Entropy t=10 | brier_scores:Std | 0.054077 ± 0.003017 | 0.052494 ± 0.002766 | -0.001583 |

### Synthetic truth correlations

Event 2 columns correlate the cause-1 model score with the event-2 generating predictor; they are not independent cause-2 model performance.

| Configuration | Pearson event 1 | Spearman event 1 | Pearson event 2 | Spearman event 2 |
|---|---|---|---|---|
| FULL | 0.8427 → 0.8571 (+0.0144) | 0.8330 → 0.8488 (+0.0158) | -0.3267 → -0.3357 (-0.0090) | -0.3101 → -0.3190 (-0.0089) |
| NCC m=5 | 0.8055 → 0.8496 (+0.0441) | 0.7947 → 0.8412 (+0.0465) | -0.4351 → -0.3581 (+0.0770) | -0.4169 → -0.3415 (+0.0754) |
| NCC m=10 | 0.8220 → 0.8589 (+0.0369) | 0.8118 → 0.8501 (+0.0384) | -0.4007 → -0.3418 (+0.0589) | -0.3833 → -0.3257 (+0.0576) |
| NCC m=20 | 0.8370 → 0.8529 (+0.0159) | 0.8276 → 0.8435 (+0.0159) | -0.3760 → -0.3414 (+0.0347) | -0.3583 → -0.3255 (+0.0328) |
| NCC m=50 | 0.8414 → 0.8600 (+0.0186) | 0.8324 → 0.8516 (+0.0192) | -0.3606 → -0.3431 (+0.0175) | -0.3430 → -0.3265 (+0.0165) |
| NCC m=100 | 0.8560 → 0.8592 (+0.0032) | 0.8474 → 0.8507 (+0.0032) | -0.3473 → -0.3392 (+0.0081) | -0.3304 → -0.3224 (+0.0079) |
| SCC a=0.05 | 0.8346 → 0.8534 (+0.0188) | 0.8246 → 0.8433 (+0.0186) | -0.3709 → -0.3168 (+0.0541) | -0.3545 → -0.3032 (+0.0514) |
| SCC a=0.1 | 0.8528 → 0.8298 (-0.0230) | 0.8437 → 0.8206 (-0.0230) | -0.3412 → -0.3330 (+0.0082) | -0.3249 → -0.3173 (+0.0076) |
| SCC a=0.2 | 0.8357 → 0.8633 (+0.0275) | 0.8265 → 0.8548 (+0.0283) | -0.3662 → -0.3271 (+0.0391) | -0.3485 → -0.3113 (+0.0372) |
| SCC a=0.3 | 0.8403 → 0.8497 (+0.0094) | 0.8324 → 0.8401 (+0.0078) | -0.3606 → -0.3319 (+0.0287) | -0.3431 → -0.3160 (+0.0271) |
| SCC a=0.5 | 0.8490 → 0.8618 (+0.0127) | 0.8398 → 0.8536 (+0.0138) | -0.3329 → -0.3318 (+0.0011) | -0.3169 → -0.3150 (+0.0019) |
| Entropy t=0.1 | 0.8596 → 0.8056 (-0.0540) | 0.8513 → 0.7949 (-0.0565) | -0.3116 → -0.4273 (-0.1158) | -0.2968 → -0.4093 (-0.1125) |
| Entropy t=0.5 | 0.8656 → 0.8479 (-0.0177) | 0.8568 → 0.8378 (-0.0189) | -0.3251 → -0.3330 (-0.0079) | -0.3099 → -0.3174 (-0.0075) |
| Entropy t=1 | 0.8526 → 0.8599 (+0.0073) | 0.8431 → 0.8510 (+0.0080) | -0.3493 → -0.3355 (+0.0137) | -0.3334 → -0.3191 (+0.0143) |
| Entropy t=5 | 0.8390 → 0.8460 (+0.0070) | 0.8298 → 0.8364 (+0.0066) | -0.3533 → -0.3200 (+0.0333) | -0.3359 → -0.3043 (+0.0316) |
| Entropy t=10 | 0.8494 → 0.8613 (+0.0120) | 0.8405 → 0.8533 (+0.0128) | -0.3582 → -0.3356 (+0.0225) | -0.3407 → -0.3189 (+0.0218) |

## PBC

### Pooled metrics and training duration

| Configuration | C-index old → new (delta) | IBS old → new (delta) | Brier old → new (delta) | Seconds/fold old → new (delta) |
|---|---|---|---|---|
| FULL | 0.7556 → 0.7614 (+0.0057) | 0.1671 → 0.1095 (-0.0576) | 0.1800 → 0.1531 (-0.0269) | 28.6 → 32.1 (+3.5) |
| NCC m=5 | 0.6661 → 0.6531 (-0.0129) | 0.2391 → 0.1383 (-0.1008) | 0.2318 → 0.2013 (-0.0304) | 21.0 → 26.0 (+5.0) |
| NCC m=10 | 0.7790 → 0.7476 (-0.0314) | 0.1613 → 0.1156 (-0.0457) | 0.1681 → 0.1669 (-0.0013) | 27.6 → 31.1 (+3.5) |
| NCC m=20 | 0.7402 → 0.7676 (+0.0273) | 0.1795 → 0.1105 (-0.0691) | 0.1793 → 0.1581 (-0.0212) | 25.6 → 31.4 (+5.8) |
| NCC m=50 | 0.7739 → 0.7607 (-0.0133) | 0.1621 → 0.1091 (-0.0530) | 0.1762 → 0.1548 (-0.0214) | 27.1 → 41.7 (+14.6) |
| NCC m=100 | 0.7716 → 0.7628 (-0.0087) | 0.1627 → 0.1104 (-0.0523) | 0.1750 → 0.1574 (-0.0176) | 33.8 → 46.5 (+12.7) |
| SCC a=0.05 | 0.3375 → 0.6385 (+0.3010) | 0.3044 → 0.1384 (-0.1660) | 0.2847 → 0.2012 (-0.0834) | 17.1 → 27.7 (+10.6) |
| SCC a=0.1 | 0.6090 → 0.6829 (+0.0740) | 0.2475 → 0.1269 (-0.1207) | 0.2366 → 0.1898 (-0.0468) | 19.2 → 29.0 (+9.8) |
| SCC a=0.2 | 0.7162 → 0.7240 (+0.0078) | 0.1920 → 0.1172 (-0.0747) | 0.1995 → 0.1644 (-0.0350) | 19.4 → 24.7 (+5.3) |
| SCC a=0.3 | 0.7299 → 0.7101 (-0.0197) | 0.1803 → 0.1207 (-0.0596) | 0.1862 → 0.1681 (-0.0181) | 23.5 → 23.7 (+0.2) |
| SCC a=0.5 | 0.7326 → 0.7548 (+0.0222) | 0.1739 → 0.1103 (-0.0635) | 0.1855 → 0.1570 (-0.0285) | 29.7 → 34.7 (+5.0) |
| Entropy t=0.1 | missing pooled CSV | missing pooled CSV | missing pooled CSV | 12.6 → 15.4 (+2.8) |
| Entropy t=0.5 | 0.7336 → 0.7252 (-0.0084) | 0.2248 → 0.1360 (-0.0888) | 0.2091 → 0.1914 (-0.0177) | 16.1 → 14.7 (-1.4) |
| Entropy t=1 | 0.7273 → 0.7289 (+0.0016) | 0.1879 → 0.1181 (-0.0699) | 0.1852 → 0.1690 (-0.0163) | 17.1 → 16.2 (-0.8) |
| Entropy t=5 | 0.7532 → 0.7641 (+0.0110) | 0.1756 → 0.1080 (-0.0676) | 0.1803 → 0.1507 (-0.0296) | 16.5 → 26.5 (+10.0) |
| Entropy t=10 | 0.7520 → 0.7752 (+0.0232) | 0.1704 → 0.1058 (-0.0646) | 0.1744 → 0.1470 (-0.0274) | 25.8 → 30.5 (+4.7) |

### Fold summaries

Mean ± SD across five folds. The Std column in the Brier source is within-fold variation across time; its mean and SD below are explicitly labelled separately.

| Configuration | Metric | Old mean ± SD | New mean ± SD | Mean delta |
|---|---|---|---|---|
| FULL | CIndex_scores:CIndex_Score | 0.758401 ± 0.065039 | 0.767479 ± 0.070047 | +0.009077 |
| FULL | IBS_scores:IBS_Score | 0.117625 ± 0.028666 | 0.112406 ± 0.026862 | -0.005219 |
| FULL | Training_Durations:Training_Duration | 28.625319 ± 11.405430 | 32.121704 ± 15.085353 | +3.496385 |
| FULL | brier_scores:Mean | 0.130387 ± 0.033366 | 0.124573 ± 0.030947 | -0.005814 |
| FULL | brier_scores:Std | 0.060709 ± 0.021848 | 0.056827 ± 0.019370 | -0.003882 |
| NCC m=5 | CIndex_scores:CIndex_Score | 0.766815 ± 0.006763 | 0.781850 ± 0.025783 | +0.015035 |
| NCC m=5 | IBS_scores:IBS_Score | 0.151857 ± 0.025043 | 0.143369 ± 0.057756 | -0.008488 |
| NCC m=5 | Training_Durations:Training_Duration | 20.995384 ± 13.887946 | 26.011878 ± 14.010200 | +5.016494 |
| NCC m=5 | brier_scores:Mean | 0.169142 ± 0.028177 | 0.160541 ± 0.069096 | -0.008601 |
| NCC m=5 | brier_scores:Std | 0.086705 ± 0.016119 | 0.084269 ± 0.050377 | -0.002436 |
| NCC m=10 | CIndex_scores:CIndex_Score | 0.783676 ± 0.034869 | 0.781303 ± 0.031793 | -0.002373 |
| NCC m=10 | IBS_scores:IBS_Score | 0.112117 ± 0.023471 | 0.117046 ± 0.022149 | +0.004928 |
| NCC m=10 | Training_Durations:Training_Duration | 27.649880 ± 9.896813 | 31.149153 ± 18.941416 | +3.499274 |
| NCC m=10 | brier_scores:Mean | 0.124011 ± 0.027704 | 0.129031 ± 0.025048 | +0.005020 |
| NCC m=10 | brier_scores:Std | 0.055782 ± 0.017459 | 0.058481 ± 0.014626 | +0.002699 |
| NCC m=20 | CIndex_scores:CIndex_Score | 0.775780 ± 0.065833 | 0.776058 ± 0.015328 | +0.000278 |
| NCC m=20 | IBS_scores:IBS_Score | 0.118214 ± 0.030532 | 0.112169 ± 0.018965 | -0.006046 |
| NCC m=20 | Training_Durations:Training_Duration | 25.580249 ± 11.307052 | 31.355992 ± 19.360449 | +5.775743 |
| NCC m=20 | brier_scores:Mean | 0.131950 ± 0.036365 | 0.123568 ± 0.021541 | -0.008382 |
| NCC m=20 | brier_scores:Std | 0.067102 ± 0.031277 | 0.054652 ± 0.011011 | -0.012450 |
| NCC m=50 | CIndex_scores:CIndex_Score | 0.761880 ± 0.063034 | 0.771350 ± 0.025364 | +0.009470 |
| NCC m=50 | IBS_scores:IBS_Score | 0.114566 ± 0.028992 | 0.110195 ± 0.014328 | -0.004371 |
| NCC m=50 | Training_Durations:Training_Duration | 27.088289 ± 10.384341 | 41.720679 ± 16.177339 | +14.632389 |
| NCC m=50 | brier_scores:Mean | 0.126291 ± 0.032713 | 0.121403 ± 0.015947 | -0.004888 |
| NCC m=50 | brier_scores:Std | 0.056534 ± 0.018015 | 0.053373 ± 0.007196 | -0.003161 |
| NCC m=100 | CIndex_scores:CIndex_Score | 0.777921 ± 0.051286 | 0.772699 ± 0.025824 | -0.005222 |
| NCC m=100 | IBS_scores:IBS_Score | 0.114480 ± 0.029535 | 0.112504 ± 0.023905 | -0.001976 |
| NCC m=100 | Training_Durations:Training_Duration | 33.821344 ± 11.988474 | 46.542165 ± 25.655632 | +12.720821 |
| NCC m=100 | brier_scores:Mean | 0.126386 ± 0.034552 | 0.123765 ± 0.026715 | -0.002621 |
| NCC m=100 | brier_scores:Std | 0.056317 ± 0.021030 | 0.053933 ± 0.012605 | -0.002384 |
| SCC a=0.05 | CIndex_scores:CIndex_Score | 0.347184 ± 0.384651 | 0.730841 ± 0.050792 | +0.383657 |
| SCC a=0.05 | IBS_scores:IBS_Score | 0.192263 ± 0.043965 | 0.143214 ± 0.046708 | -0.049048 |
| SCC a=0.05 | Training_Durations:Training_Duration | 17.055821 ± 5.666400 | 27.675099 ± 9.093875 | +10.619278 |
| SCC a=0.05 | brier_scores:Mean | 0.217331 ± 0.053148 | 0.159433 ± 0.054512 | -0.057899 |
| SCC a=0.05 | brier_scores:Std | 0.131670 ± 0.044767 | 0.082072 ± 0.040593 | -0.049598 |
| SCC a=0.1 | CIndex_scores:CIndex_Score | 0.635070 ± 0.265250 | 0.751133 ± 0.044731 | +0.116064 |
| SCC a=0.1 | IBS_scores:IBS_Score | 0.157056 ± 0.038337 | 0.127556 ± 0.028441 | -0.029500 |
| SCC a=0.1 | Training_Durations:Training_Duration | 19.202665 ± 3.232750 | 28.976224 ± 13.289719 | +9.773558 |
| SCC a=0.1 | brier_scores:Mean | 0.176838 ± 0.047176 | 0.140977 ± 0.032742 | -0.035861 |
| SCC a=0.1 | brier_scores:Std | 0.101000 ± 0.050736 | 0.068350 ± 0.018678 | -0.032650 |
| SCC a=0.2 | CIndex_scores:CIndex_Score | 0.747168 ± 0.027781 | 0.741233 ± 0.075793 | -0.005935 |
| SCC a=0.2 | IBS_scores:IBS_Score | 0.130341 ± 0.023878 | 0.119792 ± 0.023945 | -0.010548 |
| SCC a=0.2 | Training_Durations:Training_Duration | 19.439350 ± 1.897853 | 24.700582 ± 9.965217 | +5.261233 |
| SCC a=0.2 | brier_scores:Mean | 0.144883 ± 0.027937 | 0.132545 ± 0.027529 | -0.012338 |
| SCC a=0.2 | brier_scores:Std | 0.070359 ± 0.019077 | 0.061720 ± 0.018799 | -0.008640 |
| SCC a=0.3 | CIndex_scores:CIndex_Score | 0.746216 ± 0.033525 | 0.733793 ± 0.084801 | -0.012424 |
| SCC a=0.3 | IBS_scores:IBS_Score | 0.122194 ± 0.017726 | 0.123235 ± 0.027929 | +0.001041 |
| SCC a=0.3 | Training_Durations:Training_Duration | 23.500281 ± 2.651977 | 23.678602 ± 6.771636 | +0.178321 |
| SCC a=0.3 | brier_scores:Mean | 0.135348 ± 0.020288 | 0.136237 ± 0.032180 | +0.000889 |
| SCC a=0.3 | brier_scores:Std | 0.062365 ± 0.013228 | 0.062674 ± 0.021490 | +0.000309 |
| SCC a=0.5 | CIndex_scores:CIndex_Score | 0.731034 ± 0.082057 | 0.767960 ± 0.026653 | +0.036926 |
| SCC a=0.5 | IBS_scores:IBS_Score | 0.120476 ± 0.022658 | 0.112609 ± 0.024386 | -0.007867 |
| SCC a=0.5 | Training_Durations:Training_Duration | 29.658522 ± 14.422382 | 34.708294 ± 13.280578 | +5.049771 |
| SCC a=0.5 | brier_scores:Mean | 0.133151 ± 0.026721 | 0.124444 ± 0.028235 | -0.008707 |
| SCC a=0.5 | brier_scores:Std | 0.061167 ± 0.016425 | 0.056332 ± 0.017046 | -0.004835 |
| Entropy t=0.1 | CIndex_scores:CIndex_Score | 0.000000 ± 0.000000 | 0.025448 ± 0.035119 | +0.025448 |
| Entropy t=0.1 | IBS_scores:IBS_Score | incomplete (1/5) | incomplete (2/5) | not calculated |
| Entropy t=0.1 | Training_Durations:Training_Duration | 12.639374 ± 2.735679 | 15.424242 ± 7.890074 | +2.784868 |
| Entropy t=0.1 | brier_scores:Mean | incomplete (1/5) | incomplete (2/5) | not calculated |
| Entropy t=0.1 | brier_scores:Std | incomplete (1/5) | incomplete (2/5) | not calculated |
| Entropy t=0.5 | CIndex_scores:CIndex_Score | 0.767458 ± 0.028901 | 0.764573 ± 0.047383 | -0.002885 |
| Entropy t=0.5 | IBS_scores:IBS_Score | 0.138522 ± 0.012727 | 0.137435 ± 0.016548 | -0.001087 |
| Entropy t=0.5 | Training_Durations:Training_Duration | 16.094670 ± 3.539540 | 14.731468 ± 3.043484 | -1.363202 |
| Entropy t=0.5 | brier_scores:Mean | 0.154744 ± 0.016949 | 0.153643 ± 0.020061 | -0.001100 |
| Entropy t=0.5 | brier_scores:Std | 0.081572 ± 0.024234 | 0.080620 ± 0.025321 | -0.000952 |
| Entropy t=1 | CIndex_scores:CIndex_Score | 0.757443 ± 0.057616 | 0.762501 ± 0.036960 | +0.005058 |
| Entropy t=1 | IBS_scores:IBS_Score | 0.122907 ± 0.025057 | 0.119660 ± 0.019155 | -0.003247 |
| Entropy t=1 | Training_Durations:Training_Duration | 17.077947 ± 3.801890 | 16.234695 ± 4.312145 | -0.843251 |
| Entropy t=1 | brier_scores:Mean | 0.137123 ± 0.030542 | 0.132150 ± 0.022048 | -0.004974 |
| Entropy t=1 | brier_scores:Std | 0.069107 ± 0.026435 | 0.062340 ± 0.017605 | -0.006768 |
| Entropy t=5 | CIndex_scores:CIndex_Score | 0.761191 ± 0.036713 | 0.775873 ± 0.058850 | +0.014682 |
| Entropy t=5 | IBS_scores:IBS_Score | 0.117740 ± 0.026972 | 0.110379 ± 0.020672 | -0.007361 |
| Entropy t=5 | Training_Durations:Training_Duration | 16.529150 ± 6.564233 | 26.488565 ± 12.195000 | +9.959416 |
| Entropy t=5 | brier_scores:Mean | 0.130498 ± 0.031858 | 0.122025 ± 0.024458 | -0.008473 |
| Entropy t=5 | brier_scores:Std | 0.062400 ± 0.021407 | 0.054267 ± 0.015614 | -0.008133 |
| Entropy t=10 | CIndex_scores:CIndex_Score | 0.764449 ± 0.016854 | 0.789561 ± 0.037605 | +0.025113 |
| Entropy t=10 | IBS_scores:IBS_Score | 0.113892 ± 0.017070 | 0.108079 ± 0.021004 | -0.005813 |
| Entropy t=10 | Training_Durations:Training_Duration | 25.787274 ± 13.694937 | 30.468103 ± 12.611837 | +4.680829 |
| Entropy t=10 | brier_scores:Mean | 0.125610 ± 0.020731 | 0.119374 ± 0.024882 | -0.006236 |
| Entropy t=10 | brier_scores:Std | 0.055177 ± 0.013415 | 0.052175 ± 0.014886 | -0.003002 |

## FH

### Pooled metrics and training duration

| Configuration | C-index old → new (delta) | IBS old → new (delta) | Brier old → new (delta) | Seconds/fold old → new (delta) |
|---|---|---|---|---|
| FULL | 0.6452 → 0.6629 (+0.0176) | 0.0941 → 0.0740 (-0.0201) | 0.6704 → 0.1367 (-0.5337) | 19.7 → 27.6 (+7.9) |
| NCC m=5 | 0.6637 → 0.6815 (+0.0178) | 0.0929 → 0.0740 (-0.0189) | 0.6437 → 0.1352 (-0.5085) | 33.7 → 36.1 (+2.4) |
| NCC m=10 | 0.6688 → 0.6780 (+0.0092) | 0.0930 → 0.0739 (-0.0192) | 0.6464 → 0.1348 (-0.5116) | 43.6 → 47.9 (+4.3) |
| NCC m=20 | 0.6662 → 0.6910 (+0.0247) | 0.0931 → 0.0733 (-0.0198) | 0.6493 → 0.1332 (-0.5161) | 26.5 → 62.4 (+36.0) |
| NCC m=50 | 0.6773 → 0.7006 (+0.0233) | 0.0942 → 0.0731 (-0.0211) | 0.6617 → 0.1325 (-0.5292) | 41.5 → 87.7 (+46.2) |
| NCC m=100 | 0.6517 → 0.6805 (+0.0288) | 0.0942 → 0.0740 (-0.0202) | 0.6661 → 0.1359 (-0.5301) | 33.5 → 48.4 (+14.9) |
| SCC a=0.05 | 0.5881 → 0.6620 (+0.0739) | 0.0976 → 0.0743 (-0.0232) | 0.7538 → 0.1366 (-0.6172) | 23.4 → 31.1 (+7.7) |
| SCC a=0.1 | 0.6210 → 0.6799 (+0.0589) | 0.0958 → 0.0743 (-0.0215) | 0.7006 → 0.1370 (-0.5636) | 24.8 → 30.8 (+6.1) |
| SCC a=0.2 | 0.6287 → 0.6690 (+0.0402) | 0.0955 → 0.0742 (-0.0213) | 0.6964 → 0.1363 (-0.5601) | 25.0 → 20.0 (-5.0) |
| SCC a=0.3 | 0.6284 → 0.6713 (+0.0429) | 0.0954 → 0.0746 (-0.0208) | 0.6973 → 0.1366 (-0.5608) | 22.5 → 33.4 (+10.9) |
| SCC a=0.5 | 0.6373 → 0.6537 (+0.0164) | 0.0949 → 0.0751 (-0.0198) | 0.6808 → 0.1380 (-0.5428) | 22.6 → 27.0 (+4.4) |
| Entropy t=0.1 | 0.5753 → 0.6150 (+0.0397) | 0.1008 → 0.0833 (-0.0175) | 0.8633 → 0.1609 (-0.7024) | 38.2 → 30.2 (-8.1) |
| Entropy t=0.5 | 0.6376 → 0.6677 (+0.0301) | 0.0945 → 0.0739 (-0.0206) | 0.6727 → 0.1357 (-0.5371) | 19.2 → 19.6 (+0.4) |
| Entropy t=1 | 0.6332 → 0.6755 (+0.0423) | 0.0943 → 0.0737 (-0.0205) | 0.6845 → 0.1357 (-0.5488) | 22.0 → 40.4 (+18.5) |
| Entropy t=5 | 0.6626 → 0.6845 (+0.0220) | 0.0939 → 0.0739 (-0.0200) | 0.6555 → 0.1350 (-0.5205) | 27.8 → 50.5 (+22.7) |
| Entropy t=10 | 0.6280 → 0.6845 (+0.0565) | 0.0945 → 0.0739 (-0.0206) | 0.6888 → 0.1350 (-0.5539) | 28.6 → 49.8 (+21.2) |

### Fold summaries

Mean ± SD across five folds. The Std column in the Brier source is within-fold variation across time; its mean and SD below are explicitly labelled separately.

| Configuration | Metric | Old mean ± SD | New mean ± SD | Mean delta |
|---|---|---|---|---|
| FULL | CIndex_scores:CIndex_Score | 0.650064 ± 0.027404 | 0.664770 ± 0.003985 | +0.014706 |
| FULL | IBS_scores:IBS_Score | 0.074804 ± 0.003826 | 0.074004 ± 0.004189 | -0.000800 |
| FULL | Training_Durations:Training_Duration | 19.670367 ± 2.201674 | 27.608402 ± 21.769580 | +7.938035 |
| FULL | brier_scores:Mean | 0.072641 ± 0.003773 | 0.071879 ± 0.004135 | -0.000762 |
| FULL | brier_scores:Std | 0.037812 ± 0.001235 | 0.037366 ± 0.001711 | -0.000446 |
| NCC m=5 | CIndex_scores:CIndex_Score | 0.665250 ± 0.023013 | 0.682973 ± 0.010751 | +0.017723 |
| NCC m=5 | IBS_scores:IBS_Score | 0.075287 ± 0.003092 | 0.074018 ± 0.003114 | -0.001269 |
| NCC m=5 | Training_Durations:Training_Duration | 33.721605 ± 16.697777 | 36.127223 ± 18.622975 | +2.405617 |
| NCC m=5 | brier_scores:Mean | 0.073100 ± 0.003076 | 0.071886 ± 0.003142 | -0.001214 |
| NCC m=5 | brier_scores:Std | 0.038066 ± 0.002071 | 0.037101 ± 0.001722 | -0.000965 |
| NCC m=10 | CIndex_scores:CIndex_Score | 0.672316 ± 0.018919 | 0.681997 ± 0.022918 | +0.009681 |
| NCC m=10 | IBS_scores:IBS_Score | 0.074982 ± 0.002319 | 0.073852 ± 0.003329 | -0.001130 |
| NCC m=10 | Training_Durations:Training_Duration | 43.591110 ± 19.212032 | 47.868912 ± 36.288462 | +4.277802 |
| NCC m=10 | brier_scores:Mean | 0.072799 ± 0.002359 | 0.071728 ± 0.003294 | -0.001071 |
| NCC m=10 | brier_scores:Std | 0.037777 ± 0.002401 | 0.036936 ± 0.002036 | -0.000841 |
| NCC m=20 | CIndex_scores:CIndex_Score | 0.672563 ± 0.013911 | 0.695157 ± 0.007953 | +0.022594 |
| NCC m=20 | IBS_scores:IBS_Score | 0.074146 ± 0.004232 | 0.073274 ± 0.003584 | -0.000872 |
| NCC m=20 | Training_Durations:Training_Duration | 26.471814 ± 14.334673 | 62.442556 ± 27.631707 | +35.970742 |
| NCC m=20 | brier_scores:Mean | 0.071996 ± 0.004182 | 0.071177 ± 0.003570 | -0.000819 |
| NCC m=20 | brier_scores:Std | 0.037348 ± 0.001674 | 0.036498 ± 0.001486 | -0.000850 |
| NCC m=50 | CIndex_scores:CIndex_Score | 0.683093 ± 0.020992 | 0.701385 ± 0.021439 | +0.018292 |
| NCC m=50 | IBS_scores:IBS_Score | 0.074568 ± 0.003490 | 0.073134 ± 0.004142 | -0.001434 |
| NCC m=50 | Training_Durations:Training_Duration | 41.496240 ± 29.024689 | 87.726670 ± 33.326746 | +46.230429 |
| NCC m=50 | brier_scores:Mean | 0.072423 ± 0.003428 | 0.071035 ± 0.004112 | -0.001388 |
| NCC m=50 | brier_scores:Std | 0.037523 ± 0.002462 | 0.036290 ± 0.001418 | -0.001233 |
| NCC m=100 | CIndex_scores:CIndex_Score | 0.652624 ± 0.023642 | 0.682523 ± 0.026340 | +0.029899 |
| NCC m=100 | IBS_scores:IBS_Score | 0.074755 ± 0.003902 | 0.073976 ± 0.004333 | -0.000778 |
| NCC m=100 | Training_Durations:Training_Duration | 33.543797 ± 32.017849 | 48.412763 ± 41.132635 | +14.868966 |
| NCC m=100 | brier_scores:Mean | 0.072592 ± 0.003828 | 0.071839 ± 0.004248 | -0.000753 |
| NCC m=100 | brier_scores:Std | 0.037926 ± 0.002126 | 0.037259 ± 0.002294 | -0.000667 |
| SCC a=0.05 | CIndex_scores:CIndex_Score | 0.655760 ± 0.043276 | 0.666802 ± 0.009581 | +0.011042 |
| SCC a=0.05 | IBS_scores:IBS_Score | 0.080296 ± 0.007767 | 0.074319 ± 0.003786 | -0.005976 |
| SCC a=0.05 | Training_Durations:Training_Duration | 23.425840 ± 6.034893 | 31.112892 ± 9.328461 | +7.687053 |
| SCC a=0.05 | brier_scores:Mean | 0.077980 ± 0.007578 | 0.072195 ± 0.003741 | -0.005785 |
| SCC a=0.05 | brier_scores:Std | 0.041376 ± 0.004189 | 0.037244 ± 0.001607 | -0.004132 |
| SCC a=0.1 | CIndex_scores:CIndex_Score | 0.659270 ± 0.019727 | 0.681735 ± 0.023650 | +0.022464 |
| SCC a=0.1 | IBS_scores:IBS_Score | 0.075827 ± 0.002388 | 0.074332 ± 0.004138 | -0.001495 |
| SCC a=0.1 | Training_Durations:Training_Duration | 24.752400 ± 7.073981 | 30.823282 ± 8.088680 | +6.070882 |
| SCC a=0.1 | brier_scores:Mean | 0.073651 ± 0.002413 | 0.072195 ± 0.004065 | -0.001456 |
| SCC a=0.1 | brier_scores:Std | 0.038217 ± 0.001933 | 0.037490 ± 0.002043 | -0.000726 |
| SCC a=0.2 | CIndex_scores:CIndex_Score | 0.654103 ± 0.029144 | 0.669016 ± 0.023976 | +0.014913 |
| SCC a=0.2 | IBS_scores:IBS_Score | 0.076479 ± 0.002533 | 0.074186 ± 0.004441 | -0.002293 |
| SCC a=0.2 | Training_Durations:Training_Duration | 24.981469 ± 4.863966 | 20.016895 ± 1.895574 | -4.964574 |
| SCC a=0.2 | brier_scores:Mean | 0.074286 ± 0.002590 | 0.072057 ± 0.004371 | -0.002229 |
| SCC a=0.2 | brier_scores:Std | 0.038642 ± 0.002551 | 0.037175 ± 0.001980 | -0.001466 |
| SCC a=0.3 | CIndex_scores:CIndex_Score | 0.674566 ± 0.023663 | 0.674797 ± 0.025072 | +0.000232 |
| SCC a=0.3 | IBS_scores:IBS_Score | 0.075813 ± 0.004736 | 0.074544 ± 0.003932 | -0.001269 |
| SCC a=0.3 | Training_Durations:Training_Duration | 22.520954 ± 4.815999 | 33.440889 ± 30.819850 | +10.919935 |
| SCC a=0.3 | brier_scores:Mean | 0.073617 ± 0.004653 | 0.072399 ± 0.003898 | -0.001218 |
| SCC a=0.3 | brier_scores:Std | 0.038319 ± 0.002257 | 0.037560 ± 0.001682 | -0.000759 |
| SCC a=0.5 | CIndex_scores:CIndex_Score | 0.650901 ± 0.051925 | 0.661963 ± 0.019337 | +0.011061 |
| SCC a=0.5 | IBS_scores:IBS_Score | 0.076040 ± 0.004443 | 0.075122 ± 0.004668 | -0.000917 |
| SCC a=0.5 | Training_Durations:Training_Duration | 22.600371 ± 5.063120 | 27.020776 ± 17.536982 | +4.420405 |
| SCC a=0.5 | brier_scores:Mean | 0.073835 ± 0.004397 | 0.072957 ± 0.004588 | -0.000877 |
| SCC a=0.5 | brier_scores:Std | 0.038452 ± 0.001799 | 0.037932 ± 0.001798 | -0.000520 |
| Entropy t=0.1 | CIndex_scores:CIndex_Score | 0.647839 ± 0.036928 | 0.661462 ± 0.019728 | +0.013624 |
| Entropy t=0.1 | IBS_scores:IBS_Score | 0.084915 ± 0.005261 | 0.083286 ± 0.000676 | -0.001629 |
| Entropy t=0.1 | Training_Durations:Training_Duration | 38.235489 ± 15.799015 | 30.176846 ± 4.840883 | -8.058643 |
| Entropy t=0.1 | brier_scores:Mean | 0.082461 ± 0.005175 | 0.080811 ± 0.000740 | -0.001650 |
| Entropy t=0.1 | brier_scores:Std | 0.044640 ± 0.003041 | 0.044392 ± 0.003053 | -0.000248 |
| Entropy t=0.5 | CIndex_scores:CIndex_Score | 0.643752 ± 0.040429 | 0.670339 ± 0.035663 | +0.026587 |
| Entropy t=0.5 | IBS_scores:IBS_Score | 0.077384 ± 0.005876 | 0.073888 ± 0.003911 | -0.003497 |
| Entropy t=0.5 | Training_Durations:Training_Duration | 19.203329 ± 2.893113 | 19.588708 ± 7.369521 | +0.385379 |
| Entropy t=0.5 | brier_scores:Mean | 0.075140 ± 0.005721 | 0.071750 ± 0.003838 | -0.003390 |
| Entropy t=0.5 | brier_scores:Std | 0.039371 ± 0.002622 | 0.037117 ± 0.002236 | -0.002254 |
| Entropy t=1 | CIndex_scores:CIndex_Score | 0.664800 ± 0.019825 | 0.678884 ± 0.018131 | +0.014084 |
| Entropy t=1 | IBS_scores:IBS_Score | 0.075242 ± 0.004060 | 0.073728 ± 0.003810 | -0.001514 |
| Entropy t=1 | Training_Durations:Training_Duration | 21.976545 ± 6.628912 | 40.433502 ± 29.789026 | +18.456958 |
| Entropy t=1 | brier_scores:Mean | 0.073075 ± 0.003971 | 0.071603 ± 0.003758 | -0.001472 |
| Entropy t=1 | brier_scores:Std | 0.037860 ± 0.001256 | 0.037121 ± 0.002457 | -0.000739 |
| Entropy t=5 | CIndex_scores:CIndex_Score | 0.668313 ± 0.014828 | 0.685571 ± 0.010608 | +0.017258 |
| Entropy t=5 | IBS_scores:IBS_Score | 0.075400 ± 0.003706 | 0.073853 ± 0.003926 | -0.001547 |
| Entropy t=5 | Training_Durations:Training_Duration | 27.825290 ± 14.631141 | 50.529769 ± 18.751237 | +22.704479 |
| Entropy t=5 | brier_scores:Mean | 0.073236 ± 0.003613 | 0.071724 ± 0.003904 | -0.001512 |
| Entropy t=5 | brier_scores:Std | 0.037834 ± 0.001782 | 0.037007 ± 0.001149 | -0.000827 |
| Entropy t=10 | CIndex_scores:CIndex_Score | 0.664868 ± 0.018474 | 0.685577 ± 0.012260 | +0.020709 |
| Entropy t=10 | IBS_scores:IBS_Score | 0.075457 ± 0.004569 | 0.073858 ± 0.003945 | -0.001599 |
| Entropy t=10 | Training_Durations:Training_Duration | 28.644157 ± 18.815526 | 49.803873 ± 18.371808 | +21.159716 |
| Entropy t=10 | brier_scores:Mean | 0.073278 ± 0.004469 | 0.071729 ± 0.003920 | -0.001549 |
| Entropy t=10 | brier_scores:Std | 0.038104 ± 0.001389 | 0.037008 ± 0.001166 | -0.001095 |

## Alternative archive comparisons

These are separate alternatives, not mixed into the primary comparisons. PBC_IND provenance must be verified before treating it as the same experimental cohort.

### PBC_IND

| Configuration | C-index old → new (delta) | IBS old → new (delta) | Brier old → new (delta) |
|---|---|---|---|
| FULL | 0.7744 → 0.7614 (-0.0130) | 0.1637 → 0.1095 (-0.0542) | 0.1694 → 0.1531 (-0.0163) |
| NCC m=5 | 0.7402 → 0.6531 (-0.0870) | 0.1885 → 0.1383 (-0.0502) | 0.1859 → 0.2013 (+0.0154) |
| NCC m=10 | 0.7302 → 0.7476 (+0.0174) | 0.1790 → 0.1156 (-0.0634) | 0.1773 → 0.1669 (-0.0105) |
| NCC m=20 | 0.7538 → 0.7676 (+0.0138) | 0.1702 → 0.1105 (-0.0597) | 0.1747 → 0.1581 (-0.0166) |
| NCC m=50 | 0.7647 → 0.7607 (-0.0040) | 0.1669 → 0.1091 (-0.0578) | 0.1720 → 0.1548 (-0.0172) |
| NCC m=100 | 0.7728 → 0.7628 (-0.0100) | 0.1617 → 0.1104 (-0.0513) | 0.1686 → 0.1574 (-0.0112) |
| SCC a=0.05 | 0.5714 → 0.6385 (+0.0671) | 0.2983 → 0.1384 (-0.1599) | 0.2758 → 0.2012 (-0.0746) |
| SCC a=0.1 | 0.6400 → 0.6829 (+0.0429) | 0.2762 → 0.1269 (-0.1493) | 0.2617 → 0.1898 (-0.0719) |
| SCC a=0.2 | 0.6134 → 0.7240 (+0.1106) | 0.2491 → 0.1172 (-0.1319) | 0.2423 → 0.1644 (-0.0779) |
| SCC a=0.3 | 0.6583 → 0.7101 (+0.0519) | 0.2004 → 0.1207 (-0.0797) | 0.2058 → 0.1681 (-0.0377) |
| SCC a=0.5 | 0.6872 → 0.7548 (+0.0677) | 0.1852 → 0.1103 (-0.0749) | 0.1915 → 0.1570 (-0.0345) |
| Entropy t=0.5 | 0.6653 → 0.7252 (+0.0599) | 0.2208 → 0.1360 (-0.0848) | 0.2112 → 0.1914 (-0.0198) |
| Entropy t=1 | 0.7666 → 0.7289 (-0.0377) | 0.1777 → 0.1181 (-0.0597) | 0.1776 → 0.1690 (-0.0087) |
| Entropy t=5 | 0.7684 → 0.7641 (-0.0042) | 0.1662 → 0.1080 (-0.0581) | 0.1713 → 0.1507 (-0.0206) |
| Entropy t=10 | 0.7416 → 0.7752 (+0.0336) | 0.1863 → 0.1058 (-0.0805) | 0.1865 → 0.1470 (-0.0395) |

### Synthetic alternate FULL

| Configuration | C-index old → new (delta) | IBS old → new (delta) | Brier old → new (delta) |
|---|---|---|---|
| FULL | 0.8510 → 0.8510 (-0.0001) | 0.2251 → 0.1628 (-0.0623) | 0.1058 → 0.1044 (-0.0015) |

## Raw Brier curve comparisons

No interpolation is performed. Differences are only calculated when all saved time points match. Each row covers every saved point in the corresponding fold CSV.

| Dataset | Configuration | Fold file | Old n | New n | Time grid | Old mean | New mean | Mean delta | Max absolute delta |
|---|---|---|---|---|---|---|---|---|---|
| Synthetic | FULL | brier_raw_fold_0 | 100 | 100 | same | 0.101226 | 0.099922 | -0.001304 | 0.008775 |
| Synthetic | FULL | brier_raw_fold_1 | 100 | 100 | same | 0.102654 | 0.101727 | -0.000928 | 0.006592 |
| Synthetic | FULL | brier_raw_fold_2 | 100 | 100 | same | 0.099825 | 0.098896 | -0.000929 | 0.007230 |
| Synthetic | FULL | brier_raw_fold_3 | 100 | 100 | same | 0.102376 | 0.101264 | -0.001111 | 0.008661 |
| Synthetic | FULL | brier_raw_fold_4 | 100 | 100 | same | 0.100987 | 0.100077 | -0.000911 | 0.007595 |
| Synthetic | NCC m=10 | brier_raw_fold_0 | 100 | 100 | same | 0.113696 | 0.109033 | -0.004662 | 0.008310 |
| Synthetic | NCC m=10 | brier_raw_fold_1 | 100 | 100 | same | 0.113029 | 0.112907 | -0.000122 | 0.004732 |
| Synthetic | NCC m=10 | brier_raw_fold_2 | 100 | 100 | same | 0.112987 | 0.108265 | -0.004722 | 0.012316 |
| Synthetic | NCC m=10 | brier_raw_fold_3 | 100 | 100 | same | 0.116813 | 0.108756 | -0.008057 | 0.017146 |
| Synthetic | NCC m=10 | brier_raw_fold_4 | 100 | 100 | same | 0.115263 | 0.110237 | -0.005026 | 0.016666 |
| Synthetic | NCC m=100 | brier_raw_fold_0 | 100 | 100 | same | 0.101561 | 0.100155 | -0.001406 | 0.008927 |
| Synthetic | NCC m=100 | brier_raw_fold_1 | 100 | 100 | same | 0.102348 | 0.100899 | -0.001449 | 0.007848 |
| Synthetic | NCC m=100 | brier_raw_fold_2 | 100 | 100 | same | 0.100249 | 0.099975 | -0.000273 | 0.007692 |
| Synthetic | NCC m=100 | brier_raw_fold_3 | 100 | 100 | same | 0.102824 | 0.101553 | -0.001271 | 0.009646 |
| Synthetic | NCC m=100 | brier_raw_fold_4 | 100 | 100 | same | 0.102710 | 0.100626 | -0.002083 | 0.009921 |
| Synthetic | NCC m=20 | brier_raw_fold_0 | 100 | 100 | same | 0.104922 | 0.101403 | -0.003519 | 0.009509 |
| Synthetic | NCC m=20 | brier_raw_fold_1 | 100 | 100 | same | 0.104685 | 0.104300 | -0.000385 | 0.002872 |
| Synthetic | NCC m=20 | brier_raw_fold_2 | 100 | 100 | same | 0.105047 | 0.101111 | -0.003936 | 0.012699 |
| Synthetic | NCC m=20 | brier_raw_fold_3 | 100 | 100 | same | 0.107585 | 0.104356 | -0.003229 | 0.011857 |
| Synthetic | NCC m=20 | brier_raw_fold_4 | 100 | 100 | same | 0.107033 | 0.103032 | -0.004001 | 0.013218 |
| Synthetic | NCC m=5 | brier_raw_fold_0 | 100 | 100 | same | 0.140118 | 0.138054 | -0.002064 | 0.012286 |
| Synthetic | NCC m=5 | brier_raw_fold_1 | 100 | 100 | same | 0.146418 | 0.141105 | -0.005313 | 0.012610 |
| Synthetic | NCC m=5 | brier_raw_fold_2 | 100 | 100 | same | 0.140846 | 0.128607 | -0.012239 | 0.029419 |
| Synthetic | NCC m=5 | brier_raw_fold_3 | 100 | 100 | same | 0.147620 | 0.136147 | -0.011473 | 0.021922 |
| Synthetic | NCC m=5 | brier_raw_fold_4 | 100 | 100 | same | 0.144451 | 0.139433 | -0.005019 | 0.008785 |
| Synthetic | NCC m=50 | brier_raw_fold_0 | 100 | 100 | same | 0.103722 | 0.100282 | -0.003441 | 0.011960 |
| Synthetic | NCC m=50 | brier_raw_fold_1 | 100 | 100 | same | 0.103153 | 0.102724 | -0.000429 | 0.008756 |
| Synthetic | NCC m=50 | brier_raw_fold_2 | 100 | 100 | same | 0.101717 | 0.100569 | -0.001148 | 0.009303 |
| Synthetic | NCC m=50 | brier_raw_fold_3 | 100 | 100 | same | 0.104165 | 0.101480 | -0.002685 | 0.010496 |
| Synthetic | NCC m=50 | brier_raw_fold_4 | 100 | 100 | same | 0.102945 | 0.100544 | -0.002400 | 0.006767 |
| Synthetic | SCC a=0.05 | brier_raw_fold_0 | 100 | 100 | same | 0.105799 | 0.103491 | -0.002308 | 0.014838 |
| Synthetic | SCC a=0.05 | brier_raw_fold_1 | 100 | 100 | same | 0.105851 | 0.103142 | -0.002709 | 0.005434 |
| Synthetic | SCC a=0.05 | brier_raw_fold_2 | 100 | 100 | same | 0.105877 | 0.099852 | -0.006025 | 0.011849 |
| Synthetic | SCC a=0.05 | brier_raw_fold_3 | 100 | 100 | same | 0.108155 | 0.099684 | -0.008470 | 0.019427 |
| Synthetic | SCC a=0.05 | brier_raw_fold_4 | 100 | 100 | same | 0.101366 | 0.104753 | +0.003387 | 0.007251 |
| Synthetic | SCC a=0.1 | brier_raw_fold_0 | 100 | 100 | same | 0.103199 | 0.099988 | -0.003212 | 0.009724 |
| Synthetic | SCC a=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.104067 | 0.101965 | -0.002102 | 0.008178 |
| Synthetic | SCC a=0.1 | brier_raw_fold_2 | 100 | 100 | same | 0.100106 | 0.099655 | -0.000451 | 0.005688 |
| Synthetic | SCC a=0.1 | brier_raw_fold_3 | 100 | 100 | same | 0.101433 | 0.105619 | +0.004186 | 0.009177 |
| Synthetic | SCC a=0.1 | brier_raw_fold_4 | 100 | 100 | same | 0.103461 | 0.102709 | -0.000753 | 0.006419 |
| Synthetic | SCC a=0.2 | brier_raw_fold_0 | 100 | 100 | same | 0.102832 | 0.099697 | -0.003135 | 0.008785 |
| Synthetic | SCC a=0.2 | brier_raw_fold_1 | 100 | 100 | same | 0.104037 | 0.100950 | -0.003087 | 0.005881 |
| Synthetic | SCC a=0.2 | brier_raw_fold_2 | 100 | 100 | same | 0.104977 | 0.102742 | -0.002235 | 0.007206 |
| Synthetic | SCC a=0.2 | brier_raw_fold_3 | 100 | 100 | same | 0.106460 | 0.098760 | -0.007700 | 0.016448 |
| Synthetic | SCC a=0.2 | brier_raw_fold_4 | 100 | 100 | same | 0.101440 | 0.099762 | -0.001678 | 0.008895 |
| Synthetic | SCC a=0.3 | brier_raw_fold_0 | 100 | 100 | same | 0.102847 | 0.099362 | -0.003485 | 0.008992 |
| Synthetic | SCC a=0.3 | brier_raw_fold_1 | 100 | 100 | same | 0.105022 | 0.103264 | -0.001759 | 0.007722 |
| Synthetic | SCC a=0.3 | brier_raw_fold_2 | 100 | 100 | same | 0.103557 | 0.098811 | -0.004746 | 0.011904 |
| Synthetic | SCC a=0.3 | brier_raw_fold_3 | 100 | 100 | same | 0.101723 | 0.102956 | +0.001233 | 0.005214 |
| Synthetic | SCC a=0.3 | brier_raw_fold_4 | 100 | 100 | same | 0.101418 | 0.100957 | -0.000461 | 0.004350 |
| Synthetic | SCC a=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.101429 | 0.098831 | -0.002597 | 0.007764 |
| Synthetic | SCC a=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.102027 | 0.101228 | -0.000799 | 0.006031 |
| Synthetic | SCC a=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.101539 | 0.098697 | -0.002842 | 0.009347 |
| Synthetic | SCC a=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.102157 | 0.101201 | -0.000956 | 0.007789 |
| Synthetic | SCC a=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.101347 | 0.100134 | -0.001213 | 0.009206 |
| Synthetic | Entropy t=0.1 | brier_raw_fold_0 | 100 | 100 | same | 0.119113 | 0.200904 | +0.081791 | 0.331765 |
| Synthetic | Entropy t=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.128833 | 0.207709 | +0.078876 | 0.315022 |
| Synthetic | Entropy t=0.1 | brier_raw_fold_2 | 100 | 100 | same | 0.118979 | 0.202524 | +0.083546 | 0.325927 |
| Synthetic | Entropy t=0.1 | brier_raw_fold_3 | 100 | 100 | same | 0.121529 | 0.199495 | +0.077966 | 0.310230 |
| Synthetic | Entropy t=0.1 | brier_raw_fold_4 | 100 | 100 | same | 0.118028 | 0.197803 | +0.079774 | 0.326157 |
| Synthetic | Entropy t=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.102956 | 0.101460 | -0.001496 | 0.004746 |
| Synthetic | Entropy t=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.101337 | 0.100848 | -0.000489 | 0.004747 |
| Synthetic | Entropy t=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.101085 | 0.100183 | -0.000901 | 0.002531 |
| Synthetic | Entropy t=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.102095 | 0.103128 | +0.001032 | 0.003122 |
| Synthetic | Entropy t=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.101425 | 0.102000 | +0.000575 | 0.002238 |
| Synthetic | Entropy t=10 | brier_raw_fold_0 | 100 | 100 | same | 0.102992 | 0.100589 | -0.002403 | 0.009264 |
| Synthetic | Entropy t=10 | brier_raw_fold_1 | 100 | 100 | same | 0.102815 | 0.102510 | -0.000305 | 0.008302 |
| Synthetic | Entropy t=10 | brier_raw_fold_2 | 100 | 100 | same | 0.101340 | 0.099368 | -0.001972 | 0.008391 |
| Synthetic | Entropy t=10 | brier_raw_fold_3 | 100 | 100 | same | 0.103263 | 0.100942 | -0.002322 | 0.009823 |
| Synthetic | Entropy t=10 | brier_raw_fold_4 | 100 | 100 | same | 0.101960 | 0.099645 | -0.002314 | 0.008825 |
| Synthetic | Entropy t=1 | brier_raw_fold_0 | 100 | 100 | same | 0.103450 | 0.099757 | -0.003693 | 0.008689 |
| Synthetic | Entropy t=1 | brier_raw_fold_1 | 100 | 100 | same | 0.103387 | 0.101630 | -0.001758 | 0.005206 |
| Synthetic | Entropy t=1 | brier_raw_fold_2 | 100 | 100 | same | 0.102806 | 0.100922 | -0.001884 | 0.008230 |
| Synthetic | Entropy t=1 | brier_raw_fold_3 | 100 | 100 | same | 0.102361 | 0.101790 | -0.000571 | 0.006802 |
| Synthetic | Entropy t=1 | brier_raw_fold_4 | 100 | 100 | same | 0.102374 | 0.099994 | -0.002380 | 0.008915 |
| Synthetic | Entropy t=5 | brier_raw_fold_0 | 100 | 100 | same | 0.102857 | 0.100583 | -0.002274 | 0.009022 |
| Synthetic | Entropy t=5 | brier_raw_fold_1 | 100 | 100 | same | 0.102786 | 0.101757 | -0.001029 | 0.008331 |
| Synthetic | Entropy t=5 | brier_raw_fold_2 | 100 | 100 | same | 0.101045 | 0.099629 | -0.001415 | 0.007398 |
| Synthetic | Entropy t=5 | brier_raw_fold_3 | 100 | 100 | same | 0.102823 | 0.100877 | -0.001945 | 0.008980 |
| Synthetic | Entropy t=5 | brier_raw_fold_4 | 100 | 100 | same | 0.101898 | 0.099488 | -0.002410 | 0.009165 |
| PBC | FULL | brier_raw_fold_0 | 100 | 100 | same | 0.133011 | 0.131085 | -0.001926 | 0.030894 |
| PBC | FULL | brier_raw_fold_1 | 100 | 100 | same | 0.096569 | 0.097134 | +0.000564 | 0.004352 |
| PBC | FULL | brier_raw_fold_2 | 100 | 100 | same | 0.115445 | 0.106718 | -0.008727 | 0.018115 |
| PBC | FULL | brier_raw_fold_3 | 100 | 100 | same | 0.185196 | 0.175307 | -0.009889 | 0.026302 |
| PBC | FULL | brier_raw_fold_4 | 100 | 100 | same | 0.121713 | 0.112624 | -0.009089 | 0.021623 |
| PBC | NCC m=10 | brier_raw_fold_0 | 100 | 100 | same | 0.118265 | 0.115944 | -0.002321 | 0.007448 |
| PBC | NCC m=10 | brier_raw_fold_1 | 100 | 100 | same | 0.097580 | 0.132802 | +0.035222 | 0.068480 |
| PBC | NCC m=10 | brier_raw_fold_2 | 100 | 100 | same | 0.112131 | 0.107131 | -0.004999 | 0.015429 |
| PBC | NCC m=10 | brier_raw_fold_3 | 100 | 100 | same | 0.170806 | 0.170689 | -0.000117 | 0.011536 |
| PBC | NCC m=10 | brier_raw_fold_4 | 100 | 100 | same | 0.121273 | 0.118589 | -0.002684 | 0.013246 |
| PBC | NCC m=100 | brier_raw_fold_0 | 100 | 100 | same | 0.115467 | 0.111269 | -0.004198 | 0.016225 |
| PBC | NCC m=100 | brier_raw_fold_1 | 100 | 100 | same | 0.096530 | 0.112431 | +0.015901 | 0.031476 |
| PBC | NCC m=100 | brier_raw_fold_2 | 100 | 100 | same | 0.113665 | 0.108628 | -0.005038 | 0.016439 |
| PBC | NCC m=100 | brier_raw_fold_3 | 100 | 100 | same | 0.186088 | 0.171372 | -0.014716 | 0.048054 |
| PBC | NCC m=100 | brier_raw_fold_4 | 100 | 100 | same | 0.120180 | 0.115124 | -0.005056 | 0.011813 |
| PBC | NCC m=20 | brier_raw_fold_0 | 100 | 100 | same | 0.153579 | 0.115720 | -0.037859 | 0.187237 |
| PBC | NCC m=20 | brier_raw_fold_1 | 100 | 100 | same | 0.096056 | 0.114179 | +0.018124 | 0.038186 |
| PBC | NCC m=20 | brier_raw_fold_2 | 100 | 100 | same | 0.108165 | 0.109221 | +0.001056 | 0.005031 |
| PBC | NCC m=20 | brier_raw_fold_3 | 100 | 100 | same | 0.184470 | 0.161740 | -0.022730 | 0.068108 |
| PBC | NCC m=20 | brier_raw_fold_4 | 100 | 100 | same | 0.117481 | 0.116982 | -0.000499 | 0.005614 |
| PBC | NCC m=5 | brier_raw_fold_0 | 100 | 100 | same | 0.121461 | 0.119698 | -0.001763 | 0.012443 |
| PBC | NCC m=5 | brier_raw_fold_1 | 100 | 100 | same | 0.172742 | 0.098541 | -0.074201 | 0.165076 |
| PBC | NCC m=5 | brier_raw_fold_2 | 100 | 100 | same | 0.171772 | 0.182124 | +0.010352 | 0.058166 |
| PBC | NCC m=5 | brier_raw_fold_3 | 100 | 100 | same | 0.186445 | 0.271233 | +0.084788 | 0.214299 |
| PBC | NCC m=5 | brier_raw_fold_4 | 100 | 100 | same | 0.193288 | 0.131109 | -0.062178 | 0.156379 |
| PBC | NCC m=50 | brier_raw_fold_0 | 100 | 100 | same | 0.121403 | 0.113953 | -0.007450 | 0.048231 |
| PBC | NCC m=50 | brier_raw_fold_1 | 100 | 100 | same | 0.096445 | 0.119251 | +0.022806 | 0.049130 |
| PBC | NCC m=50 | brier_raw_fold_2 | 100 | 100 | same | 0.115110 | 0.108641 | -0.006469 | 0.017005 |
| PBC | NCC m=50 | brier_raw_fold_3 | 100 | 100 | same | 0.182315 | 0.149081 | -0.033234 | 0.067012 |
| PBC | NCC m=50 | brier_raw_fold_4 | 100 | 100 | same | 0.116184 | 0.116091 | -0.000093 | 0.007136 |
| PBC | SCC a=0.05 | brier_raw_fold_0 | 100 | 100 | same | 0.215696 | 0.134927 | -0.080769 | 0.329551 |
| PBC | SCC a=0.05 | brier_raw_fold_1 | 100 | 100 | same | 0.168980 | 0.114416 | -0.054563 | 0.136145 |
| PBC | SCC a=0.05 | brier_raw_fold_2 | 100 | 100 | same | 0.195918 | 0.111891 | -0.084028 | 0.280136 |
| PBC | SCC a=0.05 | brier_raw_fold_3 | 100 | 100 | same | 0.307578 | 0.226546 | -0.081032 | 0.287257 |
| PBC | SCC a=0.05 | brier_raw_fold_4 | 100 | 100 | same | 0.198485 | 0.209383 | +0.010898 | 0.061526 |
| PBC | SCC a=0.1 | brier_raw_fold_0 | 100 | 100 | same | 0.213000 | 0.130156 | -0.082844 | 0.347593 |
| PBC | SCC a=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.117462 | 0.110601 | -0.006861 | 0.011845 |
| PBC | SCC a=0.1 | brier_raw_fold_2 | 100 | 100 | same | 0.135430 | 0.184488 | +0.049058 | 0.137063 |
| PBC | SCC a=0.1 | brier_raw_fold_3 | 100 | 100 | same | 0.220688 | 0.165827 | -0.054861 | 0.145121 |
| PBC | SCC a=0.1 | brier_raw_fold_4 | 100 | 100 | same | 0.197612 | 0.113816 | -0.083796 | 0.234254 |
| PBC | SCC a=0.2 | brier_raw_fold_0 | 100 | 100 | same | 0.128016 | 0.129212 | +0.001197 | 0.025536 |
| PBC | SCC a=0.2 | brier_raw_fold_1 | 100 | 100 | same | 0.125367 | 0.112156 | -0.013211 | 0.034724 |
| PBC | SCC a=0.2 | brier_raw_fold_2 | 100 | 100 | same | 0.123017 | 0.104145 | -0.018872 | 0.037487 |
| PBC | SCC a=0.2 | brier_raw_fold_3 | 100 | 100 | same | 0.185881 | 0.173431 | -0.012449 | 0.037733 |
| PBC | SCC a=0.2 | brier_raw_fold_4 | 100 | 100 | same | 0.162136 | 0.143783 | -0.018353 | 0.047528 |
| PBC | SCC a=0.3 | brier_raw_fold_0 | 100 | 100 | same | 0.126708 | 0.126692 | -0.000017 | 0.005745 |
| PBC | SCC a=0.3 | brier_raw_fold_1 | 100 | 100 | same | 0.125498 | 0.103086 | -0.022412 | 0.045390 |
| PBC | SCC a=0.3 | brier_raw_fold_2 | 100 | 100 | same | 0.112849 | 0.111513 | -0.001336 | 0.013610 |
| PBC | SCC a=0.3 | brier_raw_fold_3 | 100 | 100 | same | 0.163858 | 0.164117 | +0.000260 | 0.021840 |
| PBC | SCC a=0.3 | brier_raw_fold_4 | 100 | 100 | same | 0.147827 | 0.175779 | +0.027952 | 0.086515 |
| PBC | SCC a=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.130645 | 0.111324 | -0.019321 | 0.083602 |
| PBC | SCC a=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.098255 | 0.112335 | +0.014080 | 0.028583 |
| PBC | SCC a=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.148687 | 0.109028 | -0.039659 | 0.080266 |
| PBC | SCC a=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.168081 | 0.174820 | +0.006739 | 0.047232 |
| PBC | SCC a=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.120086 | 0.114712 | -0.005374 | 0.011689 |
| PBC | Entropy t=0.1 | brier_raw_fold_0 | 100 | 100 | same | missing values | missing values | not calculated | not calculated |
| PBC | Entropy t=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.176591 | 0.175146 | -0.001445 | 0.003160 |
| PBC | Entropy t=0.1 | brier_raw_fold_2 | 100 | 100 | same | missing values | missing values | not calculated | not calculated |
| PBC | Entropy t=0.1 | brier_raw_fold_3 | 100 | 100 | same | missing values | missing values | not calculated | not calculated |
| PBC | Entropy t=0.1 | brier_raw_fold_4 | 100 | 100 | same | missing values | missing values | not calculated | not calculated |
| PBC | Entropy t=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.166095 | 0.162842 | -0.003252 | 0.012613 |
| PBC | Entropy t=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.140726 | 0.140561 | -0.000165 | 0.004636 |
| PBC | Entropy t=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.147803 | 0.127132 | -0.020671 | 0.072997 |
| PBC | Entropy t=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.178644 | 0.178567 | -0.000077 | 0.006025 |
| PBC | Entropy t=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.140450 | 0.159115 | +0.018665 | 0.068942 |
| PBC | Entropy t=10 | brier_raw_fold_0 | 100 | 100 | same | 0.122994 | 0.114835 | -0.008159 | 0.030393 |
| PBC | Entropy t=10 | brier_raw_fold_1 | 100 | 100 | same | 0.108847 | 0.098254 | -0.010593 | 0.024019 |
| PBC | Entropy t=10 | brier_raw_fold_2 | 100 | 100 | same | 0.113423 | 0.109335 | -0.004088 | 0.015911 |
| PBC | Entropy t=10 | brier_raw_fold_3 | 100 | 100 | same | 0.161199 | 0.162440 | +0.001241 | 0.009126 |
| PBC | Entropy t=10 | brier_raw_fold_4 | 100 | 100 | same | 0.121588 | 0.112008 | -0.009580 | 0.021058 |
| PBC | Entropy t=1 | brier_raw_fold_0 | 100 | 100 | same | 0.148905 | 0.141324 | -0.007581 | 0.047883 |
| PBC | Entropy t=1 | brier_raw_fold_1 | 100 | 100 | same | 0.093910 | 0.123051 | +0.029141 | 0.071412 |
| PBC | Entropy t=1 | brier_raw_fold_2 | 100 | 100 | same | 0.140954 | 0.108078 | -0.032876 | 0.089584 |
| PBC | Entropy t=1 | brier_raw_fold_3 | 100 | 100 | same | 0.176708 | 0.165480 | -0.011228 | 0.058134 |
| PBC | Entropy t=1 | brier_raw_fold_4 | 100 | 100 | same | 0.125140 | 0.122816 | -0.002324 | 0.021880 |
| PBC | Entropy t=5 | brier_raw_fold_0 | 100 | 100 | same | 0.130229 | 0.127625 | -0.002604 | 0.047279 |
| PBC | Entropy t=5 | brier_raw_fold_1 | 100 | 100 | same | 0.110804 | 0.097972 | -0.012832 | 0.026990 |
| PBC | Entropy t=5 | brier_raw_fold_2 | 100 | 100 | same | 0.109784 | 0.107204 | -0.002580 | 0.007746 |
| PBC | Entropy t=5 | brier_raw_fold_3 | 100 | 100 | same | 0.185588 | 0.161130 | -0.024458 | 0.061950 |
| PBC | Entropy t=5 | brier_raw_fold_4 | 100 | 100 | same | 0.116085 | 0.116195 | +0.000110 | 0.013565 |
| FH | FULL | brier_raw_fold_0 | 100 | 100 | same | 0.067860 | 0.066845 | -0.001015 | 0.002279 |
| FH | FULL | brier_raw_fold_1 | 100 | 100 | same | 0.072161 | 0.072477 | +0.000316 | 0.002633 |
| FH | FULL | brier_raw_fold_2 | 100 | 100 | same | 0.077808 | 0.077671 | -0.000137 | 0.001368 |
| FH | FULL | brier_raw_fold_3 | 100 | 100 | same | 0.074578 | 0.073227 | -0.001351 | 0.003701 |
| FH | FULL | brier_raw_fold_4 | 100 | 100 | same | 0.070797 | 0.069172 | -0.001625 | 0.004219 |
| FH | NCC m=10 | brier_raw_fold_0 | 100 | 100 | same | 0.071197 | 0.067622 | -0.003575 | 0.008813 |
| FH | NCC m=10 | brier_raw_fold_1 | 100 | 100 | same | 0.072747 | 0.072265 | -0.000482 | 0.003867 |
| FH | NCC m=10 | brier_raw_fold_2 | 100 | 100 | same | 0.076246 | 0.076361 | +0.000115 | 0.000741 |
| FH | NCC m=10 | brier_raw_fold_3 | 100 | 100 | same | 0.073663 | 0.072652 | -0.001011 | 0.003235 |
| FH | NCC m=10 | brier_raw_fold_4 | 100 | 100 | same | 0.070142 | 0.069741 | -0.000402 | 0.001589 |
| FH | NCC m=100 | brier_raw_fold_0 | 100 | 100 | same | 0.067768 | 0.066527 | -0.001241 | 0.005113 |
| FH | NCC m=100 | brier_raw_fold_1 | 100 | 100 | same | 0.073670 | 0.073084 | -0.000586 | 0.001429 |
| FH | NCC m=100 | brier_raw_fold_2 | 100 | 100 | same | 0.077220 | 0.077259 | +0.000040 | 0.000998 |
| FH | NCC m=100 | brier_raw_fold_3 | 100 | 100 | same | 0.074637 | 0.073623 | -0.001014 | 0.002495 |
| FH | NCC m=100 | brier_raw_fold_4 | 100 | 100 | same | 0.069663 | 0.068700 | -0.000962 | 0.002770 |
| FH | NCC m=20 | brier_raw_fold_0 | 100 | 100 | same | 0.066625 | 0.067555 | +0.000931 | 0.003306 |
| FH | NCC m=20 | brier_raw_fold_1 | 100 | 100 | same | 0.071773 | 0.070389 | -0.001384 | 0.004178 |
| FH | NCC m=20 | brier_raw_fold_2 | 100 | 100 | same | 0.078104 | 0.076348 | -0.001756 | 0.004703 |
| FH | NCC m=20 | brier_raw_fold_3 | 100 | 100 | same | 0.073085 | 0.073055 | -0.000030 | 0.002132 |
| FH | NCC m=20 | brier_raw_fold_4 | 100 | 100 | same | 0.070395 | 0.068539 | -0.001857 | 0.005519 |
| FH | NCC m=5 | brier_raw_fold_0 | 100 | 100 | same | 0.069675 | 0.069463 | -0.000212 | 0.000473 |
| FH | NCC m=5 | brier_raw_fold_1 | 100 | 100 | same | 0.073218 | 0.070942 | -0.002277 | 0.006633 |
| FH | NCC m=5 | brier_raw_fold_2 | 100 | 100 | same | 0.077824 | 0.076940 | -0.000884 | 0.003710 |
| FH | NCC m=5 | brier_raw_fold_3 | 100 | 100 | same | 0.073568 | 0.072740 | -0.000828 | 0.002290 |
| FH | NCC m=5 | brier_raw_fold_4 | 100 | 100 | same | 0.071214 | 0.069344 | -0.001870 | 0.004839 |
| FH | NCC m=50 | brier_raw_fold_0 | 100 | 100 | same | 0.068084 | 0.066406 | -0.001678 | 0.005820 |
| FH | NCC m=50 | brier_raw_fold_1 | 100 | 100 | same | 0.073656 | 0.070177 | -0.003479 | 0.009472 |
| FH | NCC m=50 | brier_raw_fold_2 | 100 | 100 | same | 0.076907 | 0.077034 | +0.000127 | 0.000719 |
| FH | NCC m=50 | brier_raw_fold_3 | 100 | 100 | same | 0.073407 | 0.072940 | -0.000467 | 0.001620 |
| FH | NCC m=50 | brier_raw_fold_4 | 100 | 100 | same | 0.070063 | 0.068619 | -0.001445 | 0.005268 |
| FH | SCC a=0.05 | brier_raw_fold_0 | 100 | 100 | same | 0.072420 | 0.068306 | -0.004113 | 0.009138 |
| FH | SCC a=0.05 | brier_raw_fold_1 | 100 | 100 | same | 0.072463 | 0.072213 | -0.000250 | 0.003081 |
| FH | SCC a=0.05 | brier_raw_fold_2 | 100 | 100 | same | 0.090185 | 0.078092 | -0.012093 | 0.033989 |
| FH | SCC a=0.05 | brier_raw_fold_3 | 100 | 100 | same | 0.074355 | 0.072604 | -0.001751 | 0.003589 |
| FH | SCC a=0.05 | brier_raw_fold_4 | 100 | 100 | same | 0.080479 | 0.069761 | -0.010718 | 0.025497 |
| FH | SCC a=0.1 | brier_raw_fold_0 | 100 | 100 | same | 0.072132 | 0.066987 | -0.005145 | 0.011125 |
| FH | SCC a=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.073202 | 0.072624 | -0.000579 | 0.001493 |
| FH | SCC a=0.1 | brier_raw_fold_2 | 100 | 100 | same | 0.077014 | 0.078087 | +0.001073 | 0.003524 |
| FH | SCC a=0.1 | brier_raw_fold_3 | 100 | 100 | same | 0.075013 | 0.072950 | -0.002063 | 0.004031 |
| FH | SCC a=0.1 | brier_raw_fold_4 | 100 | 100 | same | 0.070893 | 0.070326 | -0.000567 | 0.001273 |
| FH | SCC a=0.2 | brier_raw_fold_0 | 100 | 100 | same | 0.075178 | 0.067671 | -0.007506 | 0.015614 |
| FH | SCC a=0.2 | brier_raw_fold_1 | 100 | 100 | same | 0.073747 | 0.072439 | -0.001308 | 0.003587 |
| FH | SCC a=0.2 | brier_raw_fold_2 | 100 | 100 | same | 0.078210 | 0.078998 | +0.000788 | 0.002304 |
| FH | SCC a=0.2 | brier_raw_fold_3 | 100 | 100 | same | 0.072921 | 0.072096 | -0.000825 | 0.001902 |
| FH | SCC a=0.2 | brier_raw_fold_4 | 100 | 100 | same | 0.071374 | 0.069080 | -0.002294 | 0.007026 |
| FH | SCC a=0.3 | brier_raw_fold_0 | 100 | 100 | same | 0.069426 | 0.068692 | -0.000734 | 0.003374 |
| FH | SCC a=0.3 | brier_raw_fold_1 | 100 | 100 | same | 0.073794 | 0.071658 | -0.002136 | 0.005904 |
| FH | SCC a=0.3 | brier_raw_fold_2 | 100 | 100 | same | 0.081163 | 0.078608 | -0.002555 | 0.005267 |
| FH | SCC a=0.3 | brier_raw_fold_3 | 100 | 100 | same | 0.073556 | 0.073305 | -0.000251 | 0.001852 |
| FH | SCC a=0.3 | brier_raw_fold_4 | 100 | 100 | same | 0.070146 | 0.069731 | -0.000415 | 0.002098 |
| FH | SCC a=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.069679 | 0.068057 | -0.001622 | 0.004876 |
| FH | SCC a=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.072780 | 0.072965 | +0.000186 | 0.000786 |
| FH | SCC a=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.081224 | 0.079376 | -0.001849 | 0.002943 |
| FH | SCC a=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.073737 | 0.075180 | +0.001443 | 0.004822 |
| FH | SCC a=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.071753 | 0.069209 | -0.002544 | 0.007586 |
| FH | Entropy t=0.1 | brier_raw_fold_0 | 100 | 100 | same | 0.080292 | 0.080217 | -0.000074 | 0.000461 |
| FH | Entropy t=0.1 | brier_raw_fold_1 | 100 | 100 | same | 0.074428 | 0.080398 | +0.005970 | 0.022187 |
| FH | Entropy t=0.1 | brier_raw_fold_2 | 100 | 100 | same | 0.085751 | 0.082003 | -0.003748 | 0.007406 |
| FH | Entropy t=0.1 | brier_raw_fold_3 | 100 | 100 | same | 0.084657 | 0.081056 | -0.003601 | 0.014112 |
| FH | Entropy t=0.1 | brier_raw_fold_4 | 100 | 100 | same | 0.087177 | 0.080381 | -0.006796 | 0.016289 |
| FH | Entropy t=0.5 | brier_raw_fold_0 | 100 | 100 | same | 0.067514 | 0.066925 | -0.000590 | 0.003710 |
| FH | Entropy t=0.5 | brier_raw_fold_1 | 100 | 100 | same | 0.073515 | 0.072556 | -0.000960 | 0.002725 |
| FH | Entropy t=0.5 | brier_raw_fold_2 | 100 | 100 | same | 0.082900 | 0.077486 | -0.005414 | 0.013060 |
| FH | Entropy t=0.5 | brier_raw_fold_3 | 100 | 100 | same | 0.073784 | 0.071441 | -0.002343 | 0.006652 |
| FH | Entropy t=0.5 | brier_raw_fold_4 | 100 | 100 | same | 0.077984 | 0.070342 | -0.007642 | 0.019126 |
| FH | Entropy t=10 | brier_raw_fold_0 | 100 | 100 | same | 0.067544 | 0.067322 | -0.000222 | 0.002681 |
| FH | Entropy t=10 | brier_raw_fold_1 | 100 | 100 | same | 0.074073 | 0.070568 | -0.003505 | 0.006676 |
| FH | Entropy t=10 | brier_raw_fold_2 | 100 | 100 | same | 0.078070 | 0.077107 | -0.000963 | 0.002618 |
| FH | Entropy t=10 | brier_raw_fold_3 | 100 | 100 | same | 0.076773 | 0.074251 | -0.002521 | 0.011434 |
| FH | Entropy t=10 | brier_raw_fold_4 | 100 | 100 | same | 0.069932 | 0.069399 | -0.000533 | 0.001368 |
| FH | Entropy t=1 | brier_raw_fold_0 | 100 | 100 | same | 0.067667 | 0.068156 | +0.000490 | 0.001777 |
| FH | Entropy t=1 | brier_raw_fold_1 | 100 | 100 | same | 0.074144 | 0.073011 | -0.001133 | 0.003750 |
| FH | Entropy t=1 | brier_raw_fold_2 | 100 | 100 | same | 0.077580 | 0.077271 | -0.000310 | 0.001371 |
| FH | Entropy t=1 | brier_raw_fold_3 | 100 | 100 | same | 0.075477 | 0.071184 | -0.004293 | 0.012589 |
| FH | Entropy t=1 | brier_raw_fold_4 | 100 | 100 | same | 0.070505 | 0.068391 | -0.002114 | 0.005761 |
| FH | Entropy t=5 | brier_raw_fold_0 | 100 | 100 | same | 0.067515 | 0.067413 | -0.000101 | 0.002309 |
| FH | Entropy t=5 | brier_raw_fold_1 | 100 | 100 | same | 0.073900 | 0.070513 | -0.003387 | 0.006478 |
| FH | Entropy t=5 | brier_raw_fold_2 | 100 | 100 | same | 0.077525 | 0.077126 | -0.000399 | 0.001132 |
| FH | Entropy t=5 | brier_raw_fold_3 | 100 | 100 | same | 0.074033 | 0.074205 | +0.000172 | 0.000843 |
| FH | Entropy t=5 | brier_raw_fold_4 | 100 | 100 | same | 0.073205 | 0.069362 | -0.003843 | 0.007908 |

## Individual fold values

Matching fold labels do not prove identical patient membership. These are descriptive differences by stored label.

| Dataset | Configuration | Metric | Fold | Old | New | Delta |
|---|---|---|---|---|---|---|
| Synthetic | FULL | CIndex_scores:CIndex_Score | Fold_0 | 0.8503558931391588 | 0.8518741345979447 | 0.001518241458785874 |
| Synthetic | FULL | CIndex_scores:CIndex_Score | Fold_1 | 0.8588612760639132 | 0.8595329159818277 | 0.0006716399179145238 |
| Synthetic | FULL | CIndex_scores:CIndex_Score | Fold_2 | 0.8501003497649525 | 0.8508591466453544 | 0.0007587968804019241 |
| Synthetic | FULL | CIndex_scores:CIndex_Score | Fold_3 | 0.8503447358792133 | 0.8508323113947528 | 0.0004875755155394623 |
| Synthetic | FULL | CIndex_scores:CIndex_Score | Fold_4 | 0.8397705168116143 | 0.8407540683267216 | 0.000983551515107317 |
| Synthetic | FULL | IBS_scores:IBS_Score | Fold_0 | 0.1654741253372996 | 0.16164836161603285 | -0.0038257637212667506 |
| Synthetic | FULL | IBS_scores:IBS_Score | Fold_1 | 0.16193733392842175 | 0.15957600182398204 | -0.0023613321044397007 |
| Synthetic | FULL | IBS_scores:IBS_Score | Fold_2 | 0.164216797740197 | 0.16131589190205153 | -0.002900905838145479 |
| Synthetic | FULL | IBS_scores:IBS_Score | Fold_3 | 0.1650638336305498 | 0.1614636890305521 | -0.00360014459999769 |
| Synthetic | FULL | IBS_scores:IBS_Score | Fold_4 | 0.17295967398890613 | 0.16985378187938927 | -0.003105892109516867 |
| Synthetic | FULL | Training_Durations:Training_Duration | Fold_0 | 58.508477449417114 | 88.71798920631409 | 30.209511756896973 |
| Synthetic | FULL | Training_Durations:Training_Duration | Fold_1 | 26.117918729782104 | 60.270891427993774 | 34.15297269821167 |
| Synthetic | FULL | Training_Durations:Training_Duration | Fold_2 | 77.33234024047852 | 55.67954111099243 | -21.652799129486084 |
| Synthetic | FULL | Training_Durations:Training_Duration | Fold_3 | 79.25835227966309 | 63.67208528518677 | -15.586266994476318 |
| Synthetic | FULL | Training_Durations:Training_Duration | Fold_4 | 49.59633684158325 | 75.9586923122406 | 26.36235547065735 |
| Synthetic | FULL | brier_scores:Mean | Fold_0 | 0.10122631087372744 | 0.09992220990991196 | -0.0013041009638154744 |
| Synthetic | FULL | brier_scores:Mean | Fold_1 | 0.10265441496655718 | 0.10172659175022693 | -0.0009278232163302536 |
| Synthetic | FULL | brier_scores:Mean | Fold_2 | 0.09982482315834348 | 0.0988961058751324 | -0.000928717283211089 |
| Synthetic | FULL | brier_scores:Mean | Fold_3 | 0.10237560025976944 | 0.10126437276653893 | -0.0011112274932305044 |
| Synthetic | FULL | brier_scores:Mean | Fold_4 | 0.1009873625211712 | 0.100076763084483 | -0.0009105994366881975 |
| Synthetic | FULL | brier_scores:Std | Fold_0 | 0.05369654140381431 | 0.05240830496848624 | -0.0012882364353280704 |
| Synthetic | FULL | brier_scores:Std | Fold_1 | 0.0500838247884403 | 0.04956351805358585 | -0.0005203067348544463 |
| Synthetic | FULL | brier_scores:Std | Fold_2 | 0.052362824734359305 | 0.051375880249277896 | -0.000986944485081409 |
| Synthetic | FULL | brier_scores:Std | Fold_3 | 0.05255086344568124 | 0.051372295491019085 | -0.0011785679546621533 |
| Synthetic | FULL | brier_scores:Std | Fold_4 | 0.0582431593781189 | 0.05717561044802338 | -0.001067548930095523 |
| Synthetic | NCC m=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.8416994395070139 | 0.8525775156933613 | 0.010878076186347396 |
| Synthetic | NCC m=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.8514109198610674 | 0.8571908314227081 | 0.005779911561640705 |
| Synthetic | NCC m=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.8407011462771808 | 0.8482882170967264 | 0.007587070819545572 |
| Synthetic | NCC m=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.8383708893951022 | 0.8531154858676976 | 0.014744596472595406 |
| Synthetic | NCC m=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.8286229913834318 | 0.83648410442069 | 0.007861113037258227 |
| Synthetic | NCC m=100 | CIndex_scores:CIndex_Score | Fold_0 | 0.8502267187493088 | 0.8518759041101345 | 0.0016491853608257001 |
| Synthetic | NCC m=100 | CIndex_scores:CIndex_Score | Fold_1 | 0.8603577521181325 | 0.861357422356781 | 0.0009996702386485534 |
| Synthetic | NCC m=100 | CIndex_scores:CIndex_Score | Fold_2 | 0.8495606610961697 | 0.8485046313549238 | -0.0010560297412458564 |
| Synthetic | NCC m=100 | CIndex_scores:CIndex_Score | Fold_3 | 0.8490019476947065 | 0.8501796033516689 | 0.001177655656962373 |
| Synthetic | NCC m=100 | CIndex_scores:CIndex_Score | Fold_4 | 0.8363600199994891 | 0.8396537314740135 | 0.0032937114745243967 |
| Synthetic | NCC m=20 | CIndex_scores:CIndex_Score | Fold_0 | 0.847022132173713 | 0.8530889047161924 | 0.006066772542479337 |
| Synthetic | NCC m=20 | CIndex_scores:CIndex_Score | Fold_1 | 0.8567122014296583 | 0.8585817146032347 | 0.0018695131735764203 |
| Synthetic | NCC m=20 | CIndex_scores:CIndex_Score | Fold_2 | 0.84337265008688 | 0.8491422003313562 | 0.005769550244476229 |
| Synthetic | NCC m=20 | CIndex_scores:CIndex_Score | Fold_3 | 0.844002777702937 | 0.8486377870155425 | 0.00463500931260552 |
| Synthetic | NCC m=20 | CIndex_scores:CIndex_Score | Fold_4 | 0.8315508362925035 | 0.8381993890667027 | 0.006648552774199179 |
| Synthetic | NCC m=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.8375225059831631 | 0.8488270346072346 | 0.011304528624071497 |
| Synthetic | NCC m=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.847656314237468 | 0.8532354262360209 | 0.005579111998552877 |
| Synthetic | NCC m=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.8340479793104377 | 0.8481948267114462 | 0.014146847401008467 |
| Synthetic | NCC m=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.832764205525682 | 0.851275561863425 | 0.018511356337743035 |
| Synthetic | NCC m=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.8212354063947271 | 0.8339221260770711 | 0.012686719682343917 |
| Synthetic | NCC m=50 | CIndex_scores:CIndex_Score | Fold_0 | 0.8458692949821058 | 0.8519015620368855 | 0.006032267054779661 |
| Synthetic | NCC m=50 | CIndex_scores:CIndex_Score | Fold_1 | 0.8581662672313289 | 0.8573648000096937 | -0.0008014672216352103 |
| Synthetic | NCC m=50 | CIndex_scores:CIndex_Score | Fold_2 | 0.846661069230113 | 0.8470947957309818 | 0.00043372650086881404 |
| Synthetic | NCC m=50 | CIndex_scores:CIndex_Score | Fold_3 | 0.8474670843071083 | 0.8514728517779124 | 0.004005767470804167 |
| Synthetic | NCC m=50 | CIndex_scores:CIndex_Score | Fold_4 | 0.8361547332732375 | 0.8416190097333279 | 0.0054642764600904 |
| Synthetic | NCC m=10 | IBS_scores:IBS_Score | Fold_0 | 0.1896187556188021 | 0.1845248396460728 | -0.00509391597272929 |
| Synthetic | NCC m=10 | IBS_scores:IBS_Score | Fold_1 | 0.1839561074487644 | 0.18624158758898215 | 0.0022854801402177605 |
| Synthetic | NCC m=10 | IBS_scores:IBS_Score | Fold_2 | 0.19339857741173264 | 0.18409409020472914 | -0.009304487207003498 |
| Synthetic | NCC m=10 | IBS_scores:IBS_Score | Fold_3 | 0.19424240683098082 | 0.18009431918314137 | -0.014148087647839452 |
| Synthetic | NCC m=10 | IBS_scores:IBS_Score | Fold_4 | 0.2065283495341425 | 0.19602557133392845 | -0.010502778200214058 |
| Synthetic | NCC m=100 | IBS_scores:IBS_Score | Fold_0 | 0.16598029596727235 | 0.16195102305998668 | -0.004029272907285664 |
| Synthetic | NCC m=100 | IBS_scores:IBS_Score | Fold_1 | 0.16259436454558965 | 0.15881363976270282 | -0.003780724782886824 |
| Synthetic | NCC m=100 | IBS_scores:IBS_Score | Fold_2 | 0.16518777440567198 | 0.16248482136961484 | -0.0027029530360571374 |
| Synthetic | NCC m=100 | IBS_scores:IBS_Score | Fold_3 | 0.16614405073995706 | 0.1619929675707372 | -0.00415108316921986 |
| Synthetic | NCC m=100 | IBS_scores:IBS_Score | Fold_4 | 0.1757073753698197 | 0.1706186440521883 | -0.005088731317631406 |
| Synthetic | NCC m=20 | IBS_scores:IBS_Score | Fold_0 | 0.1725637093811482 | 0.1660098155212269 | -0.006553893859921306 |
| Synthetic | NCC m=20 | IBS_scores:IBS_Score | Fold_1 | 0.16694037378518892 | 0.1661003387056845 | -0.0008400350795044198 |
| Synthetic | NCC m=20 | IBS_scores:IBS_Score | Fold_2 | 0.17459244342080146 | 0.16641644246134255 | -0.008176000959458918 |
| Synthetic | NCC m=20 | IBS_scores:IBS_Score | Fold_3 | 0.17501983750149613 | 0.1678959045664573 | -0.007123932935038824 |
| Synthetic | NCC m=20 | IBS_scores:IBS_Score | Fold_4 | 0.18549875579826727 | 0.1773531906636836 | -0.008145565134583671 |
| Synthetic | NCC m=5 | IBS_scores:IBS_Score | Fold_0 | 0.25195028442908884 | 0.2549540750884451 | 0.0030037906593562425 |
| Synthetic | NCC m=5 | IBS_scores:IBS_Score | Fold_1 | 0.26227709178440106 | 0.25256141460933834 | -0.00971567717506272 |
| Synthetic | NCC m=5 | IBS_scores:IBS_Score | Fold_2 | 0.2579860910434579 | 0.23450748532973978 | -0.023478605713718098 |
| Synthetic | NCC m=5 | IBS_scores:IBS_Score | Fold_3 | 0.2660142746146333 | 0.24738143528298995 | -0.018632839331643336 |
| Synthetic | NCC m=5 | IBS_scores:IBS_Score | Fold_4 | 0.27791651378363763 | 0.27051887530849017 | -0.007397638475147461 |
| Synthetic | NCC m=50 | IBS_scores:IBS_Score | Fold_0 | 0.16985094205439283 | 0.162549382190317 | -0.007301559864075824 |
| Synthetic | NCC m=50 | IBS_scores:IBS_Score | Fold_1 | 0.16406967305956563 | 0.16087623240622353 | -0.0031934406533420945 |
| Synthetic | NCC m=50 | IBS_scores:IBS_Score | Fold_2 | 0.16779747150297955 | 0.16373051959869173 | -0.004066951904287824 |
| Synthetic | NCC m=50 | IBS_scores:IBS_Score | Fold_3 | 0.167945183518248 | 0.16204173186113793 | -0.005903451657110065 |
| Synthetic | NCC m=50 | IBS_scores:IBS_Score | Fold_4 | 0.17576335991134495 | 0.17181155703169815 | -0.003951802879646804 |
| Synthetic | NCC m=10 | Training_Durations:Training_Duration | Fold_0 | 45.67356038093567 | 77.37056565284729 | 31.69700527191162 |
| Synthetic | NCC m=10 | Training_Durations:Training_Duration | Fold_1 | 43.37217450141907 | 60.55576181411743 | 17.183587312698364 |
| Synthetic | NCC m=10 | Training_Durations:Training_Duration | Fold_2 | 59.08761262893677 | 51.28382849693298 | -7.803784132003784 |
| Synthetic | NCC m=10 | Training_Durations:Training_Duration | Fold_3 | 43.29053711891174 | 46.90259623527527 | 3.6120591163635254 |
| Synthetic | NCC m=10 | Training_Durations:Training_Duration | Fold_4 | 68.23431444168091 | 45.386369705200195 | -22.847944736480713 |
| Synthetic | NCC m=100 | Training_Durations:Training_Duration | Fold_0 | 85.23079109191895 | 57.5098512172699 | -27.720939874649048 |
| Synthetic | NCC m=100 | Training_Durations:Training_Duration | Fold_1 | 56.99626016616821 | 95.78046703338623 | 38.78420686721802 |
| Synthetic | NCC m=100 | Training_Durations:Training_Duration | Fold_2 | 137.01403379440308 | 64.28953576087952 | -72.72449803352356 |
| Synthetic | NCC m=100 | Training_Durations:Training_Duration | Fold_3 | 87.38414216041565 | 78.89057660102844 | -8.493565559387207 |
| Synthetic | NCC m=100 | Training_Durations:Training_Duration | Fold_4 | 58.96630644798279 | 72.85037922859192 | 13.88407278060913 |
| Synthetic | NCC m=20 | Training_Durations:Training_Duration | Fold_0 | 83.47091841697693 | 77.94775724411011 | -5.523161172866821 |
| Synthetic | NCC m=20 | Training_Durations:Training_Duration | Fold_1 | 42.2282555103302 | 60.44084692001343 | 18.212591409683228 |
| Synthetic | NCC m=20 | Training_Durations:Training_Duration | Fold_2 | 85.9169111251831 | 43.660078048706055 | -42.25683307647705 |
| Synthetic | NCC m=20 | Training_Durations:Training_Duration | Fold_3 | 48.02946591377258 | 44.94306468963623 | -3.0864012241363525 |
| Synthetic | NCC m=20 | Training_Durations:Training_Duration | Fold_4 | 59.44930148124695 | 61.674110412597656 | 2.224808931350708 |
| Synthetic | NCC m=5 | Training_Durations:Training_Duration | Fold_0 | 46.3097243309021 | 97.60344362258911 | 51.29371929168701 |
| Synthetic | NCC m=5 | Training_Durations:Training_Duration | Fold_1 | 71.8342182636261 | 46.92078948020935 | -24.913428783416748 |
| Synthetic | NCC m=5 | Training_Durations:Training_Duration | Fold_2 | 89.67586374282837 | 54.097686529159546 | -35.57817721366882 |
| Synthetic | NCC m=5 | Training_Durations:Training_Duration | Fold_3 | 46.256612062454224 | 56.43073034286499 | 10.174118280410767 |
| Synthetic | NCC m=5 | Training_Durations:Training_Duration | Fold_4 | 75.3725368976593 | 95.89243054389954 | 20.519893646240234 |
| Synthetic | NCC m=50 | Training_Durations:Training_Duration | Fold_0 | 179.94720816612244 | 57.598989486694336 | -122.3482186794281 |
| Synthetic | NCC m=50 | Training_Durations:Training_Duration | Fold_1 | 53.52105450630188 | 48.27756667137146 | -5.24348783493042 |
| Synthetic | NCC m=50 | Training_Durations:Training_Duration | Fold_2 | 96.33521580696106 | 49.88742995262146 | -46.4477858543396 |
| Synthetic | NCC m=50 | Training_Durations:Training_Duration | Fold_3 | 62.504944801330566 | 89.69764184951782 | 27.192697048187256 |
| Synthetic | NCC m=50 | Training_Durations:Training_Duration | Fold_4 | 42.406015157699585 | 109.72025322914124 | 67.31423807144165 |
| Synthetic | NCC m=10 | brier_scores:Mean | Fold_0 | 0.113695523535444 | 0.10903306659577265 | -0.00466245693967135 |
| Synthetic | NCC m=10 | brier_scores:Mean | Fold_1 | 0.11302888701868082 | 0.11290708044236121 | -0.00012180657631960523 |
| Synthetic | NCC m=10 | brier_scores:Mean | Fold_2 | 0.11298702549295787 | 0.10826515165013101 | -0.004721873842826865 |
| Synthetic | NCC m=10 | brier_scores:Mean | Fold_3 | 0.11681289503808985 | 0.1087561130630616 | -0.008056781975028252 |
| Synthetic | NCC m=10 | brier_scores:Mean | Fold_4 | 0.11526323940744002 | 0.11023739499184235 | -0.005025844415597669 |
| Synthetic | NCC m=10 | brier_scores:Std | Fold_0 | 0.06219321473623924 | 0.060425522766519184 | -0.001767691969720056 |
| Synthetic | NCC m=10 | brier_scores:Std | Fold_1 | 0.05812982480307591 | 0.0591183587066799 | 0.00098853390360399 |
| Synthetic | NCC m=10 | brier_scores:Std | Fold_2 | 0.0632040667800102 | 0.05978403521592045 | -0.003420031564089751 |
| Synthetic | NCC m=10 | brier_scores:Std | Fold_3 | 0.06312314492080999 | 0.05802820277817414 | -0.005094942142635853 |
| Synthetic | NCC m=10 | brier_scores:Std | Fold_4 | 0.0711074531277422 | 0.06727424401292964 | -0.0038332091148125663 |
| Synthetic | NCC m=100 | brier_scores:Mean | Fold_0 | 0.10156060948205217 | 0.10015475342144825 | -0.0014058560606039217 |
| Synthetic | NCC m=100 | brier_scores:Mean | Fold_1 | 0.10234819789907391 | 0.10089907794499119 | -0.0014491199540827282 |
| Synthetic | NCC m=100 | brier_scores:Mean | Fold_2 | 0.1002486419436223 | 0.09997548917165805 | -0.00027315277196425514 |
| Synthetic | NCC m=100 | brier_scores:Mean | Fold_3 | 0.10282398568365984 | 0.10155294737304647 | -0.0012710383106133705 |
| Synthetic | NCC m=100 | brier_scores:Mean | Fold_4 | 0.10270971686012417 | 0.10062623486283258 | -0.0020834819972915947 |
| Synthetic | NCC m=100 | brier_scores:Std | Fold_0 | 0.05384722612751429 | 0.05249518984501652 | -0.0013520362824977691 |
| Synthetic | NCC m=100 | brier_scores:Std | Fold_1 | 0.0505593642562352 | 0.049245521066789005 | -0.0013138431894461969 |
| Synthetic | NCC m=100 | brier_scores:Std | Fold_2 | 0.052732804987084006 | 0.05180281565126168 | -0.0009299893358223274 |
| Synthetic | NCC m=100 | brier_scores:Std | Fold_3 | 0.05301213674242237 | 0.051591568526629085 | -0.001420568215793283 |
| Synthetic | NCC m=100 | brier_scores:Std | Fold_4 | 0.05924886803034266 | 0.057522801370247234 | -0.001726066660095428 |
| Synthetic | NCC m=20 | brier_scores:Mean | Fold_0 | 0.10492197650914696 | 0.10140309031342921 | -0.0035188861957177464 |
| Synthetic | NCC m=20 | brier_scores:Mean | Fold_1 | 0.10468493155424596 | 0.10429957979873025 | -0.00038535175551571155 |
| Synthetic | NCC m=20 | brier_scores:Mean | Fold_2 | 0.10504699557338389 | 0.10111123297550917 | -0.003935762597874717 |
| Synthetic | NCC m=20 | brier_scores:Mean | Fold_3 | 0.10758511446545846 | 0.10435616178215859 | -0.0032289526832998683 |
| Synthetic | NCC m=20 | brier_scores:Mean | Fold_4 | 0.10703322499723443 | 0.10303193284548065 | -0.00400129215175378 |
| Synthetic | NCC m=20 | brier_scores:Std | Fold_0 | 0.056107661409359896 | 0.05381906483246892 | -0.0022885965768909763 |
| Synthetic | NCC m=20 | brier_scores:Std | Fold_1 | 0.05208784724911977 | 0.05182091608012447 | -0.0002669311689953019 |
| Synthetic | NCC m=20 | brier_scores:Std | Fold_2 | 0.056082818436955825 | 0.053199207898799644 | -0.002883610538156181 |
| Synthetic | NCC m=20 | brier_scores:Std | Fold_3 | 0.056146261737732 | 0.053653050618440876 | -0.0024932111192911277 |
| Synthetic | NCC m=20 | brier_scores:Std | Fold_4 | 0.062981617457216 | 0.06005704884522435 | -0.002924568611991654 |
| Synthetic | NCC m=5 | brier_scores:Mean | Fold_0 | 0.14011782422967697 | 0.13805369587740737 | -0.002064128352269601 |
| Synthetic | NCC m=5 | brier_scores:Mean | Fold_1 | 0.14641819717096763 | 0.14110495009678733 | -0.005313247074180294 |
| Synthetic | NCC m=5 | brier_scores:Mean | Fold_2 | 0.14084607524436152 | 0.12860740628364842 | -0.0122386689607131 |
| Synthetic | NCC m=5 | brier_scores:Mean | Fold_3 | 0.14761959355544146 | 0.13614681472096524 | -0.011472778834476227 |
| Synthetic | NCC m=5 | brier_scores:Mean | Fold_4 | 0.14445122034199528 | 0.1394325675139446 | -0.005018652828050696 |
| Synthetic | NCC m=5 | brier_scores:Std | Fold_0 | 0.08605960464824325 | 0.08768204490057988 | 0.0016224402523366266 |
| Synthetic | NCC m=5 | brier_scores:Std | Fold_1 | 0.08826770009878089 | 0.08453522052618247 | -0.003732479572598424 |
| Synthetic | NCC m=5 | brier_scores:Std | Fold_2 | 0.08834335150716234 | 0.07956786792604115 | -0.008775483581121193 |
| Synthetic | NCC m=5 | brier_scores:Std | Fold_3 | 0.09126192924269622 | 0.08415408675413899 | -0.0071078424885572256 |
| Synthetic | NCC m=5 | brier_scores:Std | Fold_4 | 0.09939757820121359 | 0.09686924096344834 | -0.0025283372377652436 |
| Synthetic | NCC m=50 | brier_scores:Mean | Fold_0 | 0.10372245214457611 | 0.1002815725468539 | -0.003440879597722213 |
| Synthetic | NCC m=50 | brier_scores:Mean | Fold_1 | 0.1031534758299602 | 0.10272405152668808 | -0.00042942430327212733 |
| Synthetic | NCC m=50 | brier_scores:Mean | Fold_2 | 0.10171705518029445 | 0.10056908822228491 | -0.001147966958009533 |
| Synthetic | NCC m=50 | brier_scores:Mean | Fold_3 | 0.1041651691013359 | 0.10148027576546147 | -0.002684893335874433 |
| Synthetic | NCC m=50 | brier_scores:Mean | Fold_4 | 0.10294467339668861 | 0.10054432668635112 | -0.002400346710337495 |
| Synthetic | NCC m=50 | brier_scores:Std | Fold_0 | 0.05521560160327622 | 0.05271143321156908 | -0.00250416839170714 |
| Synthetic | NCC m=50 | brier_scores:Std | Fold_1 | 0.051060724112918725 | 0.05003345933392337 | -0.0010272647789953543 |
| Synthetic | NCC m=50 | brier_scores:Std | Fold_2 | 0.053668677212557914 | 0.05222908875856763 | -0.0014395884539902815 |
| Synthetic | NCC m=50 | brier_scores:Std | Fold_3 | 0.05356250037382921 | 0.05157060671254034 | -0.0019918936612888724 |
| Synthetic | NCC m=50 | brier_scores:Std | Fold_4 | 0.05919357738492494 | 0.057976424855705026 | -0.001217152529219917 |
| Synthetic | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_0 | 0.8426965596259252 | 0.8456773029095204 | 0.002980743283595211 |
| Synthetic | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_1 | 0.8526979411986176 | 0.8587176005144623 | 0.006019659315844694 |
| Synthetic | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_2 | 0.8374908517831726 | 0.8498067088420042 | 0.012315857058831536 |
| Synthetic | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_3 | 0.8394233919785571 | 0.8543348592158291 | 0.014911467237271991 |
| Synthetic | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_4 | 0.8400150361122161 | 0.8351137014747798 | -0.00490133463743625 |
| Synthetic | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.8481316163166719 | 0.8510477724053421 | 0.002916156088670241 |
| Synthetic | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.857151883231592 | 0.8580883708490965 | 0.0009364876175045334 |
| Synthetic | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.8494573928816771 | 0.8491098728902977 | -0.00034751999137938583 |
| Synthetic | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.8527209060387227 | 0.8423940392372268 | -0.01032686680149597 |
| Synthetic | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.8355078519891828 | 0.8348892546540782 | -0.0006185973351046092 |
| Synthetic | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_0 | 0.8468345638816019 | 0.8528093217902155 | 0.0059747579086135705 |
| Synthetic | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_1 | 0.8561574060850923 | 0.861937317646733 | 0.005779911561640705 |
| Synthetic | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_2 | 0.8379856412282631 | 0.8429434135083804 | 0.00495777228011729 |
| Synthetic | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_3 | 0.8404498210050313 | 0.8562147626741388 | 0.01576494166910747 |
| Synthetic | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_4 | 0.8391309346111596 | 0.8414045991525764 | 0.0022736645414167533 |
| Synthetic | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_0 | 0.8471548455879425 | 0.8535808291049365 | 0.006425983516993972 |
| Synthetic | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_1 | 0.8540169866044188 | 0.8565304432044495 | 0.0025134566000306613 |
| Synthetic | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_2 | 0.8421154718234922 | 0.8511554815217245 | 0.009040009698232265 |
| Synthetic | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_3 | 0.8510478527991268 | 0.8490097697618006 | -0.0020380830373261105 |
| Synthetic | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_4 | 0.839593514034313 | 0.8403307214779184 | 0.0007372074436053921 |
| Synthetic | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.8492959553375123 | 0.8544735480046538 | 0.005177592667141462 |
| Synthetic | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.8599907736062823 | 0.8605992309030528 | 0.0006084572967705038 |
| Synthetic | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.8463539585400568 | 0.8511141742359275 | 0.0047602156958707065 |
| Synthetic | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.8496989807846577 | 0.851457207643724 | 0.0017582268590663475 |
| Synthetic | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.8399803654651159 | 0.8402750659654681 | 0.0002947005003521852 |
| Synthetic | SCC a=0.05 | IBS_scores:IBS_Score | Fold_0 | 0.1753143068491196 | 0.16705121965571756 | -0.008263087193402047 |
| Synthetic | SCC a=0.05 | IBS_scores:IBS_Score | Fold_1 | 0.1680143367632317 | 0.1657813339082054 | -0.0022330028550262837 |
| Synthetic | SCC a=0.05 | IBS_scores:IBS_Score | Fold_2 | 0.17546582894855722 | 0.16580166324279136 | -0.009664165705765865 |
| Synthetic | SCC a=0.05 | IBS_scores:IBS_Score | Fold_3 | 0.17558235259790772 | 0.1600929518712978 | -0.015489400726609925 |
| Synthetic | SCC a=0.05 | IBS_scores:IBS_Score | Fold_4 | 0.1744067200213536 | 0.18018581831897304 | 0.005779098297619439 |
| Synthetic | SCC a=0.1 | IBS_scores:IBS_Score | Fold_0 | 0.16875491070089033 | 0.16266231918792504 | -0.00609259151296529 |
| Synthetic | SCC a=0.1 | IBS_scores:IBS_Score | Fold_1 | 0.16530987957225898 | 0.1605895773812475 | -0.004720302191011494 |
| Synthetic | SCC a=0.1 | IBS_scores:IBS_Score | Fold_2 | 0.1647170124876122 | 0.1627241652311291 | -0.0019928472564831046 |
| Synthetic | SCC a=0.1 | IBS_scores:IBS_Score | Fold_3 | 0.16371931715181426 | 0.16850003816707743 | 0.004780721015263167 |
| Synthetic | SCC a=0.1 | IBS_scores:IBS_Score | Fold_4 | 0.17757383576204938 | 0.17516085887365107 | -0.0024129768883983105 |
| Synthetic | SCC a=0.2 | IBS_scores:IBS_Score | Fold_0 | 0.16785273566500847 | 0.1619639051521532 | -0.00588883051285527 |
| Synthetic | SCC a=0.2 | IBS_scores:IBS_Score | Fold_1 | 0.16419685955961336 | 0.16014894303490704 | -0.004047916524706319 |
| Synthetic | SCC a=0.2 | IBS_scores:IBS_Score | Fold_2 | 0.17168722136211348 | 0.16771616888213675 | -0.003971052479976728 |
| Synthetic | SCC a=0.2 | IBS_scores:IBS_Score | Fold_3 | 0.1713549707698647 | 0.1578811439952216 | -0.013473826774643094 |
| Synthetic | SCC a=0.2 | IBS_scores:IBS_Score | Fold_4 | 0.17381378527883817 | 0.1696367111557206 | -0.0041770741231175745 |
| Synthetic | SCC a=0.3 | IBS_scores:IBS_Score | Fold_0 | 0.16762250777608861 | 0.16141705243219331 | -0.0062054553438953 |
| Synthetic | SCC a=0.3 | IBS_scores:IBS_Score | Fold_1 | 0.16607517804957533 | 0.1621525441219125 | -0.003922633927662844 |
| Synthetic | SCC a=0.3 | IBS_scores:IBS_Score | Fold_2 | 0.16967383872120922 | 0.16103299030457782 | -0.008640848416631403 |
| Synthetic | SCC a=0.3 | IBS_scores:IBS_Score | Fold_3 | 0.16399816485003535 | 0.16365150879419574 | -0.00034665605583961145 |
| Synthetic | SCC a=0.3 | IBS_scores:IBS_Score | Fold_4 | 0.17301593937509094 | 0.17169138521739077 | -0.001324554157700164 |
| Synthetic | SCC a=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.16545444754085842 | 0.1606785183768877 | -0.00477592916397071 |
| Synthetic | SCC a=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.16103042230374703 | 0.15879299927012558 | -0.002237423033621455 |
| Synthetic | SCC a=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.16692070587654867 | 0.16107590499952282 | -0.005844800877025852 |
| Synthetic | SCC a=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.16472783007971917 | 0.1614337379743169 | -0.0032940921054022687 |
| Synthetic | SCC a=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.17376229786723082 | 0.16995413277808075 | -0.0038081650891500785 |
| Synthetic | SCC a=0.05 | Training_Durations:Training_Duration | Fold_0 | 41.85759520530701 | 29.06949758529663 | -12.788097620010376 |
| Synthetic | SCC a=0.05 | Training_Durations:Training_Duration | Fold_1 | 33.0139901638031 | 42.69993185997009 | 9.685941696166992 |
| Synthetic | SCC a=0.05 | Training_Durations:Training_Duration | Fold_2 | 43.25733780860901 | 37.55808734893799 | -5.6992504596710205 |
| Synthetic | SCC a=0.05 | Training_Durations:Training_Duration | Fold_3 | 66.57681369781494 | 31.89677357673645 | -34.68004012107849 |
| Synthetic | SCC a=0.05 | Training_Durations:Training_Duration | Fold_4 | 47.23027014732361 | 35.52154874801636 | -11.708721399307251 |
| Synthetic | SCC a=0.1 | Training_Durations:Training_Duration | Fold_0 | 74.2907338142395 | 70.18153119087219 | -4.10920262336731 |
| Synthetic | SCC a=0.1 | Training_Durations:Training_Duration | Fold_1 | 60.36484098434448 | 38.60653281211853 | -21.758308172225952 |
| Synthetic | SCC a=0.1 | Training_Durations:Training_Duration | Fold_2 | 44.96273183822632 | 44.64182639122009 | -0.3209054470062256 |
| Synthetic | SCC a=0.1 | Training_Durations:Training_Duration | Fold_3 | 80.12004828453064 | 51.14129900932312 | -28.97874927520752 |
| Synthetic | SCC a=0.1 | Training_Durations:Training_Duration | Fold_4 | 63.133636474609375 | 28.152950048446655 | -34.98068642616272 |
| Synthetic | SCC a=0.2 | Training_Durations:Training_Duration | Fold_0 | 65.22365593910217 | 68.33443689346313 | 3.110780954360962 |
| Synthetic | SCC a=0.2 | Training_Durations:Training_Duration | Fold_1 | 39.75058627128601 | 35.11801552772522 | -4.632570743560791 |
| Synthetic | SCC a=0.2 | Training_Durations:Training_Duration | Fold_2 | 68.36508679389954 | 41.018858671188354 | -27.34622812271118 |
| Synthetic | SCC a=0.2 | Training_Durations:Training_Duration | Fold_3 | 58.88465595245361 | 47.97467041015625 | -10.909985542297363 |
| Synthetic | SCC a=0.2 | Training_Durations:Training_Duration | Fold_4 | 49.5669732093811 | 38.38053369522095 | -11.186439514160156 |
| Synthetic | SCC a=0.3 | Training_Durations:Training_Duration | Fold_0 | 64.79627466201782 | 56.004026889801025 | -8.792247772216797 |
| Synthetic | SCC a=0.3 | Training_Durations:Training_Duration | Fold_1 | 63.52962779998779 | 73.39953708648682 | 9.869909286499023 |
| Synthetic | SCC a=0.3 | Training_Durations:Training_Duration | Fold_2 | 44.73790383338928 | 38.8578577041626 | -5.880046129226685 |
| Synthetic | SCC a=0.3 | Training_Durations:Training_Duration | Fold_3 | 69.98824048042297 | 34.68592119216919 | -35.302319288253784 |
| Synthetic | SCC a=0.3 | Training_Durations:Training_Duration | Fold_4 | 61.36174416542053 | 65.34996032714844 | 3.9882161617279053 |
| Synthetic | SCC a=0.5 | Training_Durations:Training_Duration | Fold_0 | 44.435649394989014 | 98.46012854576111 | 54.024479150772095 |
| Synthetic | SCC a=0.5 | Training_Durations:Training_Duration | Fold_1 | 31.50584077835083 | 56.57597374916077 | 25.070132970809937 |
| Synthetic | SCC a=0.5 | Training_Durations:Training_Duration | Fold_2 | 41.67276406288147 | 68.78601956367493 | 27.113255500793457 |
| Synthetic | SCC a=0.5 | Training_Durations:Training_Duration | Fold_3 | 38.25553584098816 | 31.85097861289978 | -6.404557228088379 |
| Synthetic | SCC a=0.5 | Training_Durations:Training_Duration | Fold_4 | 36.45920467376709 | 48.734790563583374 | 12.275585889816284 |
| Synthetic | SCC a=0.05 | brier_scores:Mean | Fold_0 | 0.10579908880408195 | 0.10349119193217154 | -0.0023078968719104087 |
| Synthetic | SCC a=0.05 | brier_scores:Mean | Fold_1 | 0.10585058396621211 | 0.10314167340621166 | -0.0027089105600004437 |
| Synthetic | SCC a=0.05 | brier_scores:Mean | Fold_2 | 0.10587693746313835 | 0.09985232079871306 | -0.006024616664425289 |
| Synthetic | SCC a=0.05 | brier_scores:Mean | Fold_3 | 0.10815453246604818 | 0.09968436688981581 | -0.008470165576232369 |
| Synthetic | SCC a=0.05 | brier_scores:Mean | Fold_4 | 0.10136590492851366 | 0.10475317326617095 | 0.00338726833765729 |
| Synthetic | SCC a=0.05 | brier_scores:Std | Fold_0 | 0.05720802603196591 | 0.054241399836096986 | -0.0029666261958689252 |
| Synthetic | SCC a=0.05 | brier_scores:Std | Fold_1 | 0.05246960944381582 | 0.05189982778981873 | -0.000569781653997091 |
| Synthetic | SCC a=0.05 | brier_scores:Std | Fold_2 | 0.05643434927085846 | 0.053255823806295705 | -0.003178525464562758 |
| Synthetic | SCC a=0.05 | brier_scores:Std | Fold_3 | 0.056691666132886946 | 0.05079328893138857 | -0.005898377201498377 |
| Synthetic | SCC a=0.05 | brier_scores:Std | Fold_4 | 0.0588897993459376 | 0.06099937894306346 | 0.002109579597125863 |
| Synthetic | SCC a=0.1 | brier_scores:Mean | Fold_0 | 0.10319944751117531 | 0.09998752774100118 | -0.0032119197701741264 |
| Synthetic | SCC a=0.1 | brier_scores:Mean | Fold_1 | 0.10406689555489775 | 0.10196456106103804 | -0.0021023344938597005 |
| Synthetic | SCC a=0.1 | brier_scores:Mean | Fold_2 | 0.10010595306810954 | 0.0996553729548536 | -0.0004505801132559384 |
| Synthetic | SCC a=0.1 | brier_scores:Mean | Fold_3 | 0.10143331961772882 | 0.10561930299122854 | 0.0041859833734997215 |
| Synthetic | SCC a=0.1 | brier_scores:Mean | Fold_4 | 0.10346140245970997 | 0.10270858831272815 | -0.00075281414698182 |
| Synthetic | SCC a=0.1 | brier_scores:Std | Fold_0 | 0.05473929671591236 | 0.0526090853856563 | -0.0021302113302560585 |
| Synthetic | SCC a=0.1 | brier_scores:Std | Fold_1 | 0.05155301740512018 | 0.04990297611586409 | -0.0016500412892560892 |
| Synthetic | SCC a=0.1 | brier_scores:Std | Fold_2 | 0.05255837377634647 | 0.05191304925086633 | -0.0006453245254801412 |
| Synthetic | SCC a=0.1 | brier_scores:Std | Fold_3 | 0.05206454348341648 | 0.05426784950497203 | 0.002203306021555551 |
| Synthetic | SCC a=0.1 | brier_scores:Std | Fold_4 | 0.060057077130590414 | 0.059277966374235165 | -0.0007791107563552488 |
| Synthetic | SCC a=0.2 | brier_scores:Mean | Fold_0 | 0.10283181905533756 | 0.09969714077597906 | -0.0031346782793584965 |
| Synthetic | SCC a=0.2 | brier_scores:Mean | Fold_1 | 0.1040370498780401 | 0.10094956187404393 | -0.0030874880039961777 |
| Synthetic | SCC a=0.2 | brier_scores:Mean | Fold_2 | 0.10497738771867836 | 0.10274195526007376 | -0.0022354324586045943 |
| Synthetic | SCC a=0.2 | brier_scores:Mean | Fold_3 | 0.10646038217548588 | 0.09876039080836195 | -0.007699991367123932 |
| Synthetic | SCC a=0.2 | brier_scores:Mean | Fold_4 | 0.10143964621629548 | 0.09976183995140171 | -0.0016778062648937636 |
| Synthetic | SCC a=0.2 | brier_scores:Std | Fold_0 | 0.0544893942177116 | 0.05244617655302677 | -0.002043217664684835 |
| Synthetic | SCC a=0.2 | brier_scores:Std | Fold_1 | 0.050967511022741 | 0.04989116499355677 | -0.0010763460291842233 |
| Synthetic | SCC a=0.2 | brier_scores:Std | Fold_2 | 0.05497467753979121 | 0.05373693082874702 | -0.0012377467110441936 |
| Synthetic | SCC a=0.2 | brier_scores:Std | Fold_3 | 0.05490264317962174 | 0.05002590655472915 | -0.004876736624892589 |
| Synthetic | SCC a=0.2 | brier_scores:Std | Fold_4 | 0.05846797220164575 | 0.05715280349531897 | -0.0013151687063267803 |
| Synthetic | SCC a=0.3 | brier_scores:Mean | Fold_0 | 0.10284670486921435 | 0.09936171371936227 | -0.003484991149852082 |
| Synthetic | SCC a=0.3 | brier_scores:Mean | Fold_1 | 0.10502246804904386 | 0.10326390811256125 | -0.0017585599364826066 |
| Synthetic | SCC a=0.3 | brier_scores:Mean | Fold_2 | 0.10355718187540575 | 0.09881119393124688 | -0.004745987944158869 |
| Synthetic | SCC a=0.3 | brier_scores:Mean | Fold_3 | 0.10172282017329753 | 0.10295614220385012 | 0.0012333220305525833 |
| Synthetic | SCC a=0.3 | brier_scores:Mean | Fold_4 | 0.10141805998773443 | 0.1009574555178072 | -0.0004606044699272255 |
| Synthetic | SCC a=0.3 | brier_scores:Std | Fold_0 | 0.05437528800375872 | 0.05227760143583618 | -0.0020976865679225437 |
| Synthetic | SCC a=0.3 | brier_scores:Std | Fold_1 | 0.051681518159364705 | 0.05044860775185713 | -0.001232910407507573 |
| Synthetic | SCC a=0.3 | brier_scores:Std | Fold_2 | 0.0543254223027901 | 0.0513745372187936 | -0.0029508850839964976 |
| Synthetic | SCC a=0.3 | brier_scores:Std | Fold_3 | 0.05228246431328842 | 0.05206745150955921 | -0.00021501280372920872 |
| Synthetic | SCC a=0.3 | brier_scores:Std | Fold_4 | 0.05823419965549021 | 0.05792114225108862 | -0.0003130574044015941 |
| Synthetic | SCC a=0.5 | brier_scores:Mean | Fold_0 | 0.10142876331350945 | 0.09883145204768731 | -0.002597311265822133 |
| Synthetic | SCC a=0.5 | brier_scores:Mean | Fold_1 | 0.10202703886719915 | 0.10122844147792458 | -0.000798597389274569 |
| Synthetic | SCC a=0.5 | brier_scores:Mean | Fold_2 | 0.10153934028613235 | 0.09869725520533283 | -0.002842085080799514 |
| Synthetic | SCC a=0.5 | brier_scores:Mean | Fold_3 | 0.10215682283310587 | 0.10120094331526261 | -0.0009558795178432611 |
| Synthetic | SCC a=0.5 | brier_scores:Mean | Fold_4 | 0.10134701520065048 | 0.10013404056036045 | -0.0012129746402900349 |
| Synthetic | SCC a=0.5 | brier_scores:Std | Fold_0 | 0.053680663538306105 | 0.05201128554120764 | -0.001669377997098466 |
| Synthetic | SCC a=0.5 | brier_scores:Std | Fold_1 | 0.04987578890562564 | 0.04927738506561828 | -0.0005984038400073596 |
| Synthetic | SCC a=0.5 | brier_scores:Std | Fold_2 | 0.05334418563305123 | 0.05133053013912987 | -0.0020136554939213652 |
| Synthetic | SCC a=0.5 | brier_scores:Std | Fold_3 | 0.05252670295283211 | 0.051357191794415426 | -0.0011695111584166876 |
| Synthetic | SCC a=0.5 | brier_scores:Std | Fold_4 | 0.058463994461359886 | 0.05723842013423742 | -0.0012255743271224681 |
| Synthetic | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.853901995567372 | 0.5691290903380211 | -0.28477290522935095 |
| Synthetic | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.8631776011549437 | 0.6101917895482096 | -0.25298581160673406 |
| Synthetic | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.8510998064843459 | 0.5219911907723116 | -0.3291086157120343 |
| Synthetic | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.8450639714720521 | 0.5270039484056455 | -0.3180600230664067 |
| Synthetic | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.839468517227662 | 0.5854713565711824 | -0.2539971606564796 |
| Synthetic | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.8477901004640546 | 0.8510283077712552 | 0.0032382073072005912 |
| Synthetic | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.8637921170592212 | 0.8616196735102966 | -0.002172443548924652 |
| Synthetic | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.8481598053169661 | 0.8490892192473992 | 0.0009294139304331095 |
| Synthetic | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.8539698294180991 | 0.8490002094575744 | -0.004969619960524696 |
| Synthetic | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.8404557182845693 | 0.8376446587130986 | -0.0028110595714707642 |
| Synthetic | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.8463382157123834 | 0.8505390376507956 | 0.0042008219384122025 |
| Synthetic | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.8587271211834019 | 0.8578434300027437 | -0.0008836911806582304 |
| Synthetic | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.8462551802479336 | 0.8502583950323499 | 0.004003214784416342 |
| Synthetic | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.8487698930375781 | 0.8519343537364711 | 0.003164460698892979 |
| Synthetic | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.8375871784297482 | 0.8431682402274394 | 0.005581061797691245 |
| Synthetic | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_0 | 0.8455507827879549 | 0.8530181242286032 | 0.007467341440648312 |
| Synthetic | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_1 | 0.8579862400368363 | 0.8603179384116582 | 0.0023316983748218334 |
| Synthetic | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_2 | 0.8439778916222539 | 0.8464069396240139 | 0.0024290480017600258 |
| Synthetic | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_3 | 0.8497650337956755 | 0.8499823134371814 | 0.00021727964150597412 |
| Synthetic | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_4 | 0.8380908151981519 | 0.8422303079848324 | 0.004139492786680576 |
| Synthetic | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.8465443638824867 | 0.850582390699444 | 0.0040380268169573075 |
| Synthetic | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.858734045306267 | 0.8596324502480134 | 0.0008984049417464224 |
| Synthetic | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.8473525172749763 | 0.8498848334912289 | 0.002532316216252606 |
| Synthetic | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.8487777151046723 | 0.8520907950783554 | 0.0033130799736831307 |
| Synthetic | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.8376747674329488 | 0.8432321072089399 | 0.005557339775991155 |
| Synthetic | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_0 | 0.2015772400160477 | 0.4091797673676224 | 0.2076025273515747 |
| Synthetic | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_1 | 0.2091829824055322 | 0.4109874899512657 | 0.2018045075457335 |
| Synthetic | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_2 | 0.20065617556690388 | 0.41086046870670473 | 0.21020429313980085 |
| Synthetic | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_3 | 0.20239274482508368 | 0.39543004538568927 | 0.19303730056060558 |
| Synthetic | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_4 | 0.20411046635560345 | 0.4124804560839252 | 0.20836998972832174 |
| Synthetic | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.16786790591745357 | 0.16473763372067554 | -0.003130272196778028 |
| Synthetic | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.1607084300162706 | 0.15930510545148616 | -0.0014033245647844528 |
| Synthetic | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.1661596201784896 | 0.16453843635736481 | -0.0016211838211247775 |
| Synthetic | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.1645642469425736 | 0.1653424653538093 | 0.0007782184112357093 |
| Synthetic | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.17337218262100149 | 0.17416101730424444 | 0.0007888346832429505 |
| Synthetic | Entropy t=10 | IBS_scores:IBS_Score | Fold_0 | 0.16775520449318246 | 0.16250860061855 | -0.005246603874632466 |
| Synthetic | Entropy t=10 | IBS_scores:IBS_Score | Fold_1 | 0.16321281321554393 | 0.16056689235566596 | -0.0026459208598779704 |
| Synthetic | Entropy t=10 | IBS_scores:IBS_Score | Fold_2 | 0.16654822185940607 | 0.16185608515862865 | -0.004692136700777422 |
| Synthetic | Entropy t=10 | IBS_scores:IBS_Score | Fold_3 | 0.16651343387019732 | 0.16110620799743186 | -0.005407225872765459 |
| Synthetic | Entropy t=10 | IBS_scores:IBS_Score | Fold_4 | 0.1746652299063816 | 0.169645655254578 | -0.00501957465180361 |
| Synthetic | Entropy t=1 | IBS_scores:IBS_Score | Fold_0 | 0.16828678044150944 | 0.16163632023229355 | -0.0066504602092158915 |
| Synthetic | Entropy t=1 | IBS_scores:IBS_Score | Fold_1 | 0.16299721600645173 | 0.16048044286215543 | -0.002516773144296297 |
| Synthetic | Entropy t=1 | IBS_scores:IBS_Score | Fold_2 | 0.16956973358894775 | 0.1646324363269103 | -0.0049372972620374544 |
| Synthetic | Entropy t=1 | IBS_scores:IBS_Score | Fold_3 | 0.16474230266932208 | 0.16240967082070465 | -0.002332631848617428 |
| Synthetic | Entropy t=1 | IBS_scores:IBS_Score | Fold_4 | 0.1758015271066893 | 0.17073827179836276 | -0.0050632553083265475 |
| Synthetic | Entropy t=5 | IBS_scores:IBS_Score | Fold_0 | 0.16757032393704102 | 0.1625246498342488 | -0.005045674102792219 |
| Synthetic | Entropy t=5 | IBS_scores:IBS_Score | Fold_1 | 0.16315500789931792 | 0.1595239021917515 | -0.0036311057075664177 |
| Synthetic | Entropy t=5 | IBS_scores:IBS_Score | Fold_2 | 0.16636664242119223 | 0.16260237603290026 | -0.0037642663882919702 |
| Synthetic | Entropy t=5 | IBS_scores:IBS_Score | Fold_3 | 0.16566440568859683 | 0.16102324913481894 | -0.004641156553777892 |
| Synthetic | Entropy t=5 | IBS_scores:IBS_Score | Fold_4 | 0.17452447731957324 | 0.16929303586400538 | -0.0052314414555678646 |
| Synthetic | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_0 | 28.06131887435913 | 32.18582892417908 | 4.124510049819946 |
| Synthetic | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_1 | 29.49776601791382 | 66.18442749977112 | 36.6866614818573 |
| Synthetic | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_2 | 28.11536931991577 | 30.032658576965332 | 1.9172892570495605 |
| Synthetic | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_3 | 26.968073844909668 | 34.52438306808472 | 7.556309223175049 |
| Synthetic | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_4 | 34.57082462310791 | 53.00022888183594 | 18.429404258728027 |
| Synthetic | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_0 | 28.60036611557007 | 39.52314615249634 | 10.92278003692627 |
| Synthetic | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_1 | 28.468445539474487 | 29.11356282234192 | 0.6451172828674316 |
| Synthetic | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_2 | 29.94702959060669 | 29.169992685317993 | -0.7770369052886963 |
| Synthetic | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_3 | 31.237738847732544 | 32.497034311294556 | 1.2592954635620117 |
| Synthetic | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_4 | 29.054158926010132 | 28.293089866638184 | -0.7610690593719482 |
| Synthetic | Entropy t=10 | Training_Durations:Training_Duration | Fold_0 | 59.9449028968811 | 52.05744242668152 | -7.887460470199585 |
| Synthetic | Entropy t=10 | Training_Durations:Training_Duration | Fold_1 | 59.69744944572449 | 36.76853895187378 | -22.928910493850708 |
| Synthetic | Entropy t=10 | Training_Durations:Training_Duration | Fold_2 | 57.19319486618042 | 39.53753066062927 | -17.655664205551147 |
| Synthetic | Entropy t=10 | Training_Durations:Training_Duration | Fold_3 | 62.48301029205322 | 37.579145669937134 | -24.90386462211609 |
| Synthetic | Entropy t=10 | Training_Durations:Training_Duration | Fold_4 | 53.95064425468445 | 67.1494574546814 | 13.198813199996948 |
| Synthetic | Entropy t=1 | Training_Durations:Training_Duration | Fold_0 | 29.08612823486328 | 37.680861473083496 | 8.594733238220215 |
| Synthetic | Entropy t=1 | Training_Durations:Training_Duration | Fold_1 | 30.45727849006653 | 59.36420559883118 | 28.90692710876465 |
| Synthetic | Entropy t=1 | Training_Durations:Training_Duration | Fold_2 | 32.13408541679382 | 38.202903270721436 | 6.068817853927612 |
| Synthetic | Entropy t=1 | Training_Durations:Training_Duration | Fold_3 | 35.31074905395508 | 33.44240045547485 | -1.8683485984802246 |
| Synthetic | Entropy t=1 | Training_Durations:Training_Duration | Fold_4 | 32.91048240661621 | 47.33530569076538 | 14.42482328414917 |
| Synthetic | Entropy t=5 | Training_Durations:Training_Duration | Fold_0 | 59.524192333221436 | 52.803603410720825 | -6.72058892250061 |
| Synthetic | Entropy t=5 | Training_Durations:Training_Duration | Fold_1 | 59.67187571525574 | 28.998268842697144 | -30.673606872558594 |
| Synthetic | Entropy t=5 | Training_Durations:Training_Duration | Fold_2 | 78.54401421546936 | 49.29808044433594 | -29.245933771133423 |
| Synthetic | Entropy t=5 | Training_Durations:Training_Duration | Fold_3 | 39.570637941360474 | 37.354408502578735 | -2.2162294387817383 |
| Synthetic | Entropy t=5 | Training_Durations:Training_Duration | Fold_4 | 53.23602032661438 | 85.16298651695251 | 31.926966190338135 |
| Synthetic | Entropy t=0.1 | brier_scores:Mean | Fold_0 | 0.11911294436274349 | 0.20090404595624015 | 0.08179110159349666 |
| Synthetic | Entropy t=0.1 | brier_scores:Mean | Fold_1 | 0.12883299950010169 | 0.20770865112740433 | 0.07887565162730265 |
| Synthetic | Entropy t=0.1 | brier_scores:Mean | Fold_2 | 0.11897860081091541 | 0.20252422850252041 | 0.083545627691605 |
| Synthetic | Entropy t=0.1 | brier_scores:Mean | Fold_3 | 0.12152893425340207 | 0.19949465060784705 | 0.07796571635444498 |
| Synthetic | Entropy t=0.1 | brier_scores:Mean | Fold_4 | 0.11802834842803003 | 0.19780280376785786 | 0.07977445533982783 |
| Synthetic | Entropy t=0.1 | brier_scores:Std | Fold_0 | 0.06694438869694436 | 0.14991680347110498 | 0.08297241477416062 |
| Synthetic | Entropy t=0.1 | brier_scores:Std | Fold_1 | 0.06736488887304691 | 0.14816888537430828 | 0.08080399650126137 |
| Synthetic | Entropy t=0.1 | brier_scores:Std | Fold_2 | 0.06574225775764732 | 0.1502151152301119 | 0.0844728574724646 |
| Synthetic | Entropy t=0.1 | brier_scores:Std | Fold_3 | 0.06642769339915623 | 0.14316013741520026 | 0.07673244401604402 |
| Synthetic | Entropy t=0.1 | brier_scores:Std | Fold_4 | 0.0695631325716753 | 0.15442939615446186 | 0.08486626358278655 |
| Synthetic | Entropy t=0.5 | brier_scores:Mean | Fold_0 | 0.10295551172704599 | 0.10145968088509137 | -0.0014958308419546207 |
| Synthetic | Entropy t=0.5 | brier_scores:Mean | Fold_1 | 0.10133699040139152 | 0.10084832989205679 | -0.000488660509334729 |
| Synthetic | Entropy t=0.5 | brier_scores:Mean | Fold_2 | 0.1010846082477354 | 0.10018319664698629 | -0.000901411600749108 |
| Synthetic | Entropy t=0.5 | brier_scores:Mean | Fold_3 | 0.10209514857182608 | 0.1031275173787123 | 0.0010323688068862164 |
| Synthetic | Entropy t=0.5 | brier_scores:Mean | Fold_4 | 0.10142549658204839 | 0.10200006766794457 | 0.0005745710858961889 |
| Synthetic | Entropy t=0.5 | brier_scores:Std | Fold_0 | 0.054706513303057105 | 0.05342791779641585 | -0.0012785955066412572 |
| Synthetic | Entropy t=0.5 | brier_scores:Std | Fold_1 | 0.04981057282498611 | 0.04941238224438519 | -0.00039819058060092116 |
| Synthetic | Entropy t=0.5 | brier_scores:Std | Fold_2 | 0.05310129784641556 | 0.05268263766883797 | -0.0004186601775775928 |
| Synthetic | Entropy t=0.5 | brier_scores:Std | Fold_3 | 0.05245203898258023 | 0.05276870833103813 | 0.0003166693484579 |
| Synthetic | Entropy t=0.5 | brier_scores:Std | Fold_4 | 0.058346605730629456 | 0.05884120073852565 | 0.0004945950078961911 |
| Synthetic | Entropy t=10 | brier_scores:Mean | Fold_0 | 0.10299195226462425 | 0.10058895353393485 | -0.0024029987306894013 |
| Synthetic | Entropy t=10 | brier_scores:Mean | Fold_1 | 0.10281514038355657 | 0.10251027543892396 | -0.00030486494463261016 |
| Synthetic | Entropy t=10 | brier_scores:Mean | Fold_2 | 0.10134034144672302 | 0.09936826890148255 | -0.001972072545240469 |
| Synthetic | Entropy t=10 | brier_scores:Mean | Fold_3 | 0.10326329943156852 | 0.1009416183385486 | -0.002321681093019917 |
| Synthetic | Entropy t=10 | brier_scores:Mean | Fold_4 | 0.1019599898858167 | 0.09964549299522657 | -0.0023144968905901286 |
| Synthetic | Entropy t=10 | brier_scores:Std | Fold_0 | 0.05448741516923134 | 0.052713256478818686 | -0.0017741586904126555 |
| Synthetic | Entropy t=10 | brier_scores:Std | Fold_1 | 0.05070085758934888 | 0.049869491426440274 | -0.0008313661629086033 |
| Synthetic | Entropy t=10 | brier_scores:Std | Fold_2 | 0.053205921123053765 | 0.051555670697720234 | -0.0016502504253335312 |
| Synthetic | Entropy t=10 | brier_scores:Std | Fold_3 | 0.053104785876321704 | 0.051233268932172456 | -0.0018715169441492485 |
| Synthetic | Entropy t=10 | brier_scores:Std | Fold_4 | 0.05888633855510246 | 0.05709771293372204 | -0.0017886256213804214 |
| Synthetic | Entropy t=1 | brier_scores:Mean | Fold_0 | 0.10344960480034811 | 0.0997566568798746 | -0.003692947920473505 |
| Synthetic | Entropy t=1 | brier_scores:Mean | Fold_1 | 0.10338731506547601 | 0.10162957999471063 | -0.001757735070765376 |
| Synthetic | Entropy t=1 | brier_scores:Mean | Fold_2 | 0.10280575477524419 | 0.10092150547797765 | -0.0018842492972665353 |
| Synthetic | Entropy t=1 | brier_scores:Mean | Fold_3 | 0.10236068420542091 | 0.10178974896518246 | -0.0005709352402384488 |
| Synthetic | Entropy t=1 | brier_scores:Mean | Fold_4 | 0.10237425720524984 | 0.09999391917541939 | -0.0023803380298304533 |
| Synthetic | Entropy t=1 | brier_scores:Std | Fold_0 | 0.05483242044124292 | 0.052369795538143867 | -0.0024626249030990505 |
| Synthetic | Entropy t=1 | brier_scores:Std | Fold_1 | 0.05059255485082677 | 0.04996627227813624 | -0.0006262825726905258 |
| Synthetic | Entropy t=1 | brier_scores:Std | Fold_2 | 0.054389995128486704 | 0.0525774412076849 | -0.0018125539208018043 |
| Synthetic | Entropy t=1 | brier_scores:Std | Fold_3 | 0.05251850048937501 | 0.05172778061061854 | -0.0007907198787564657 |
| Synthetic | Entropy t=1 | brier_scores:Std | Fold_4 | 0.05937560143386983 | 0.057585720964803314 | -0.0017898804690665154 |
| Synthetic | Entropy t=5 | brier_scores:Mean | Fold_0 | 0.10285688729897387 | 0.10058252752835653 | -0.0022743597706173374 |
| Synthetic | Entropy t=5 | brier_scores:Mean | Fold_1 | 0.1027859350325162 | 0.10175717501810264 | -0.0010287600144135711 |
| Synthetic | Entropy t=5 | brier_scores:Mean | Fold_2 | 0.10104483703489928 | 0.0996294590052759 | -0.001415378029623382 |
| Synthetic | Entropy t=5 | brier_scores:Mean | Fold_3 | 0.10282274319372497 | 0.10087734576807472 | -0.0019453974256502526 |
| Synthetic | Entropy t=5 | brier_scores:Mean | Fold_4 | 0.10189797613317567 | 0.0994875616278949 | -0.0024104145052807613 |
| Synthetic | Entropy t=5 | brier_scores:Std | Fold_0 | 0.0544260011365004 | 0.05271797381436159 | -0.0017080273221388095 |
| Synthetic | Entropy t=5 | brier_scores:Std | Fold_1 | 0.050681873530966225 | 0.04934558588673662 | -0.0013362876442296057 |
| Synthetic | Entropy t=5 | brier_scores:Std | Fold_2 | 0.053159249828644305 | 0.05184584732681372 | -0.0013134025018305823 |
| Synthetic | Entropy t=5 | brier_scores:Std | Fold_3 | 0.052817471647737514 | 0.05120340303339251 | -0.0016140686143450017 |
| Synthetic | Entropy t=5 | brier_scores:Std | Fold_4 | 0.05883580259741081 | 0.05698424582899999 | -0.0018515567684108183 |
| PBC | FULL | CIndex_scores:CIndex_Score | Fold_0 | 0.6720111943561787 | 0.6811357607206366 | 0.009124566364457909 |
| PBC | FULL | CIndex_scores:CIndex_Score | Fold_1 | 0.8466492058533772 | 0.8472499219069131 | 0.0006007160535358436 |
| PBC | FULL | CIndex_scores:CIndex_Score | Fold_2 | 0.7781134525117347 | 0.8089483671227404 | 0.030834914611005737 |
| PBC | FULL | CIndex_scores:CIndex_Score | Fold_3 | 0.7247235872235872 | 0.7083230958230958 | -0.01640049140049138 |
| PBC | FULL | CIndex_scores:CIndex_Score | Fold_4 | 0.7705100427475552 | 0.7917374246061955 | 0.02122738185864026 |
| PBC | FULL | IBS_scores:IBS_Score | Fold_0 | 0.11747279622976543 | 0.1161748136401469 | -0.0012979825896185376 |
| PBC | FULL | IBS_scores:IBS_Score | Fold_1 | 0.09062348023495238 | 0.09124989370587584 | 0.0006264134709234592 |
| PBC | FULL | IBS_scores:IBS_Score | Fold_2 | 0.10384463542557237 | 0.09528949520895268 | -0.008555140216619697 |
| PBC | FULL | IBS_scores:IBS_Score | Fold_3 | 0.1657512936998493 | 0.15737235750997122 | -0.008378936189878089 |
| PBC | FULL | IBS_scores:IBS_Score | Fold_4 | 0.11043250906929508 | 0.10194316615049227 | -0.008489342918802809 |
| PBC | FULL | Training_Durations:Training_Duration | Fold_0 | 17.20373773574829 | 16.310558557510376 | -0.893179178237915 |
| PBC | FULL | Training_Durations:Training_Duration | Fold_1 | 42.080055713653564 | 35.951008319854736 | -6.129047393798828 |
| PBC | FULL | Training_Durations:Training_Duration | Fold_2 | 27.956526041030884 | 47.143765687942505 | 19.18723964691162 |
| PBC | FULL | Training_Durations:Training_Duration | Fold_3 | 17.757981777191162 | 16.19097590446472 | -1.5670058727264404 |
| PBC | FULL | Training_Durations:Training_Duration | Fold_4 | 38.12829375267029 | 45.01221251487732 | 6.883918762207031 |
| PBC | FULL | brier_scores:Mean | Fold_0 | 0.13301106945197122 | 0.13108496748373166 | -0.0019261019682395575 |
| PBC | FULL | brier_scores:Mean | Fold_1 | 0.0965693455509195 | 0.09713355514688567 | 0.0005642095959661614 |
| PBC | FULL | brier_scores:Mean | Fold_2 | 0.11544535213186881 | 0.10671817917546647 | -0.008727172956402338 |
| PBC | FULL | brier_scores:Mean | Fold_3 | 0.18519598218244382 | 0.17530654774108662 | -0.009889434441357203 |
| PBC | FULL | brier_scores:Mean | Fold_4 | 0.12171298365797717 | 0.11262396241789473 | -0.009089021240082443 |
| PBC | FULL | brier_scores:Std | Fold_0 | 0.07717906984083228 | 0.0725555545492512 | -0.004623515291581087 |
| PBC | FULL | brier_scores:Std | Fold_1 | 0.034200449564577566 | 0.03439722067637132 | 0.00019677111179375317 |
| PBC | FULL | brier_scores:Std | Fold_2 | 0.04597241183553815 | 0.04308694813637575 | -0.0028854636991623994 |
| PBC | FULL | brier_scores:Std | Fold_3 | 0.08743843022337856 | 0.08032493668185098 | -0.007113493541527585 |
| PBC | FULL | brier_scores:Std | Fold_4 | 0.058753918256074844 | 0.053771943520561145 | -0.004981974735513699 |
| PBC | NCC m=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.7644520887385943 | 0.7693496195668017 | 0.00489753082820743 |
| PBC | NCC m=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.8372540067760771 | 0.816589374534445 | -0.020664632241632064 |
| PBC | NCC m=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.796764206531509 | 0.8089983022071308 | 0.012234095675621726 |
| PBC | NCC m=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.7471744471744471 | 0.7386670761670762 | -0.008507371007370979 |
| PBC | NCC m=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.7727352579492885 | 0.7729109328336359 | 0.00017567488434733214 |
| PBC | NCC m=100 | CIndex_scores:CIndex_Score | Fold_0 | 0.7693787715360173 | 0.7756755968865697 | 0.006296825350552426 |
| PBC | NCC m=100 | CIndex_scores:CIndex_Score | Fold_1 | 0.8491001273518034 | 0.7602181800706442 | -0.08888194728115917 |
| PBC | NCC m=100 | CIndex_scores:CIndex_Score | Fold_2 | 0.7946669329871168 | 0.8066763207829821 | 0.012009387795865356 |
| PBC | NCC m=100 | CIndex_scores:CIndex_Score | Fold_3 | 0.707002457002457 | 0.7375614250614251 | 0.030558968058968072 |
| PBC | NCC m=100 | CIndex_scores:CIndex_Score | Fold_4 | 0.769455993441471 | 0.7833635884523042 | 0.013907595010833274 |
| PBC | NCC m=20 | CIndex_scores:CIndex_Score | Fold_0 | 0.6720986502638253 | 0.7534326443751276 | 0.08133399411130227 |
| PBC | NCC m=20 | CIndex_scores:CIndex_Score | Fold_1 | 0.851190619218108 | 0.7825407886200351 | -0.06864983059807295 |
| PBC | NCC m=20 | CIndex_scores:CIndex_Score | Fold_2 | 0.8039049235993209 | 0.7910965744532108 | -0.012808349146110065 |
| PBC | NCC m=20 | CIndex_scores:CIndex_Score | Fold_3 | 0.7684889434889435 | 0.7676904176904177 | -0.0007985257985257954 |
| PBC | NCC m=20 | CIndex_scores:CIndex_Score | Fold_4 | 0.7832171927153482 | 0.7855302453592551 | 0.00231305264390691 |
| PBC | NCC m=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.7662886627991721 | 0.7679503250444567 | 0.0016616622452846341 |
| PBC | NCC m=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.7761972270946969 | 0.8255760866953409 | 0.04937885960064403 |
| PBC | NCC m=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.7661290322580645 | 0.759213023070009 | -0.006916009188055461 |
| PBC | NCC m=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.7682432432432432 | 0.775460687960688 | 0.0072174447174447875 |
| PBC | NCC m=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.7572173098319377 | 0.7810505358083972 | 0.023833225976459538 |
| PBC | NCC m=50 | CIndex_scores:CIndex_Score | Fold_0 | 0.7083345479987173 | 0.762586362708801 | 0.05425181471008367 |
| PBC | NCC m=50 | CIndex_scores:CIndex_Score | Fold_1 | 0.8467933777062259 | 0.7356609078021001 | -0.11113246990412573 |
| PBC | NCC m=50 | CIndex_scores:CIndex_Score | Fold_2 | 0.7819584540097873 | 0.8054279436732248 | 0.023469489663437537 |
| PBC | NCC m=50 | CIndex_scores:CIndex_Score | Fold_3 | 0.6909398034398034 | 0.7745700245700246 | 0.08363022113022112 |
| PBC | NCC m=50 | CIndex_scores:CIndex_Score | Fold_4 | 0.7813726064297007 | 0.7785032499853605 | -0.0028693564443402764 |
| PBC | NCC m=10 | IBS_scores:IBS_Score | Fold_0 | 0.10662229048393286 | 0.10463193438394232 | -0.0019903560999905423 |
| PBC | NCC m=10 | IBS_scores:IBS_Score | Fold_1 | 0.09177746338624582 | 0.12493936621737221 | 0.0331619028311264 |
| PBC | NCC m=10 | IBS_scores:IBS_Score | Fold_2 | 0.10030665095090596 | 0.09611772699904339 | -0.004188923951862572 |
| PBC | NCC m=10 | IBS_scores:IBS_Score | Fold_3 | 0.15228892325010876 | 0.151952099630626 | -0.00033682361948275674 |
| PBC | NCC m=10 | IBS_scores:IBS_Score | Fold_4 | 0.10959108911898381 | 0.10758758541767367 | -0.0020035037013101387 |
| PBC | NCC m=100 | IBS_scores:IBS_Score | Fold_0 | 0.10438945279579837 | 0.10081330423395028 | -0.003576148561848083 |
| PBC | NCC m=100 | IBS_scores:IBS_Score | Fold_1 | 0.09063211622115824 | 0.10569649471538602 | 0.015064378494227773 |
| PBC | NCC m=100 | IBS_scores:IBS_Score | Fold_2 | 0.10221593612754822 | 0.09699653554051027 | -0.005219400587037945 |
| PBC | NCC m=100 | IBS_scores:IBS_Score | Fold_3 | 0.16587532352611978 | 0.15484529329446223 | -0.01103003023165755 |
| PBC | NCC m=100 | IBS_scores:IBS_Score | Fold_4 | 0.10928914582871804 | 0.10416900706901985 | -0.0051201387596981895 |
| PBC | NCC m=20 | IBS_scores:IBS_Score | Fold_0 | 0.13435641141432525 | 0.10433844038005546 | -0.030017971034269786 |
| PBC | NCC m=20 | IBS_scores:IBS_Score | Fold_1 | 0.09014934111282887 | 0.10712444212418136 | 0.016975101011352495 |
| PBC | NCC m=20 | IBS_scores:IBS_Score | Fold_2 | 0.09647934303914511 | 0.09791310147192517 | 0.001433758432780055 |
| PBC | NCC m=20 | IBS_scores:IBS_Score | Fold_3 | 0.16369442115670801 | 0.1454908460122104 | -0.018203575144497608 |
| PBC | NCC m=20 | IBS_scores:IBS_Score | Fold_4 | 0.10639146459025839 | 0.10597635796752769 | -0.00041510662273069876 |
| PBC | NCC m=5 | IBS_scores:IBS_Score | Fold_0 | 0.10919095158408425 | 0.10793907943876625 | -0.0012518721453179948 |
| PBC | NCC m=5 | IBS_scores:IBS_Score | Fold_1 | 0.15961959376841808 | 0.09271828578080903 | -0.06690130798760906 |
| PBC | NCC m=5 | IBS_scores:IBS_Score | Fold_2 | 0.15240876652658614 | 0.16130533870963545 | 0.008896572183049317 |
| PBC | NCC m=5 | IBS_scores:IBS_Score | Fold_3 | 0.1646873865445548 | 0.23608641765668548 | 0.07139903111213067 |
| PBC | NCC m=5 | IBS_scores:IBS_Score | Fold_4 | 0.17337736067469806 | 0.11879566623273238 | -0.05458169444196567 |
| PBC | NCC m=50 | IBS_scores:IBS_Score | Fold_0 | 0.10825744271747326 | 0.10288226582693735 | -0.005375176890535904 |
| PBC | NCC m=50 | IBS_scores:IBS_Score | Fold_1 | 0.09080575868297946 | 0.11172890527016167 | 0.02092314658718221 |
| PBC | NCC m=50 | IBS_scores:IBS_Score | Fold_2 | 0.10337380950193431 | 0.09698258078901889 | -0.00639122871291542 |
| PBC | NCC m=50 | IBS_scores:IBS_Score | Fold_3 | 0.16504110267653332 | 0.13401501018377943 | -0.0310260924927539 |
| PBC | NCC m=50 | IBS_scores:IBS_Score | Fold_4 | 0.10535138102669214 | 0.10536515248131911 | 1.3771454626970714e-05 |
| PBC | NCC m=10 | Training_Durations:Training_Duration | Fold_0 | 44.17704248428345 | 60.053452253341675 | 15.876409769058228 |
| PBC | NCC m=10 | Training_Durations:Training_Duration | Fold_1 | 27.40217900276184 | 13.678423404693604 | -13.723755598068237 |
| PBC | NCC m=10 | Training_Durations:Training_Duration | Fold_2 | 24.57729482650757 | 23.307830095291138 | -1.2694647312164307 |
| PBC | NCC m=10 | Training_Durations:Training_Duration | Fold_3 | 17.735278129577637 | 18.71147084236145 | 0.9761927127838135 |
| PBC | NCC m=10 | Training_Durations:Training_Duration | Fold_4 | 24.357603788375854 | 39.994590282440186 | 15.636986494064331 |
| PBC | NCC m=100 | Training_Durations:Training_Duration | Fold_0 | 47.76945376396179 | 80.55760622024536 | 32.78815245628357 |
| PBC | NCC m=100 | Training_Durations:Training_Duration | Fold_1 | 38.99651050567627 | 18.251915216445923 | -20.744595289230347 |
| PBC | NCC m=100 | Training_Durations:Training_Duration | Fold_2 | 23.481252670288086 | 52.40330624580383 | 28.922053575515747 |
| PBC | NCC m=100 | Training_Durations:Training_Duration | Fold_3 | 19.22994112968445 | 23.80817985534668 | 4.5782387256622314 |
| PBC | NCC m=100 | Training_Durations:Training_Duration | Fold_4 | 39.62956428527832 | 57.68981957435608 | 18.06025528907776 |
| PBC | NCC m=20 | Training_Durations:Training_Duration | Fold_0 | 16.455644607543945 | 42.21318292617798 | 25.757538318634033 |
| PBC | NCC m=20 | Training_Durations:Training_Duration | Fold_1 | 25.841957807540894 | 15.206016540527344 | -10.63594126701355 |
| PBC | NCC m=20 | Training_Durations:Training_Duration | Fold_2 | 24.45821762084961 | 19.758497953414917 | -4.699719667434692 |
| PBC | NCC m=20 | Training_Durations:Training_Duration | Fold_3 | 16.843865156173706 | 19.265002965927124 | 2.421137809753418 |
| PBC | NCC m=20 | Training_Durations:Training_Duration | Fold_4 | 44.301559925079346 | 60.337257385253906 | 16.03569746017456 |
| PBC | NCC m=5 | Training_Durations:Training_Duration | Fold_0 | 45.565030097961426 | 43.86853790283203 | -1.6964921951293945 |
| PBC | NCC m=5 | Training_Durations:Training_Duration | Fold_1 | 12.146738767623901 | 19.73608660697937 | 7.589347839355469 |
| PBC | NCC m=5 | Training_Durations:Training_Duration | Fold_2 | 13.665700435638428 | 13.631866693496704 | -0.03383374214172363 |
| PBC | NCC m=5 | Training_Durations:Training_Duration | Fold_3 | 17.348724842071533 | 14.72143268585205 | -2.6272921562194824 |
| PBC | NCC m=5 | Training_Durations:Training_Duration | Fold_4 | 16.250725746154785 | 38.1014666557312 | 21.850740909576416 |
| PBC | NCC m=50 | Training_Durations:Training_Duration | Fold_0 | 20.914753198623657 | 53.78820991516113 | 32.873456716537476 |
| PBC | NCC m=50 | Training_Durations:Training_Duration | Fold_1 | 35.72487020492554 | 15.23166036605835 | -20.493209838867188 |
| PBC | NCC m=50 | Training_Durations:Training_Duration | Fold_2 | 20.91530418395996 | 52.954243183135986 | 32.038938999176025 |
| PBC | NCC m=50 | Training_Durations:Training_Duration | Fold_3 | 17.246090173721313 | 49.156617879867554 | 31.91052770614624 |
| PBC | NCC m=50 | Training_Durations:Training_Duration | Fold_4 | 40.64042854309082 | 37.47266221046448 | -3.1677663326263428 |
| PBC | NCC m=10 | brier_scores:Mean | Fold_0 | 0.11826474846856813 | 0.11594352658187741 | -0.002321221886690719 |
| PBC | NCC m=10 | brier_scores:Mean | Fold_1 | 0.09758015638647435 | 0.13280249277356865 | 0.035222336387094294 |
| PBC | NCC m=10 | brier_scores:Mean | Fold_2 | 0.1121305124573231 | 0.10713145159817068 | -0.0049990608591524155 |
| PBC | NCC m=10 | brier_scores:Mean | Fold_3 | 0.17080569281268332 | 0.17068908273294714 | -0.0001166100797361791 |
| PBC | NCC m=10 | brier_scores:Mean | Fold_4 | 0.1212730465073319 | 0.11858882786578712 | -0.0026842186415447777 |
| PBC | NCC m=10 | brier_scores:Std | Fold_0 | 0.05736614787614521 | 0.05658295756046594 | -0.0007831903156792705 |
| PBC | NCC m=10 | brier_scores:Std | Fold_1 | 0.034638238785373185 | 0.055048185519873394 | 0.02040994673450021 |
| PBC | NCC m=10 | brier_scores:Std | Fold_2 | 0.04545917463463941 | 0.04140626480519424 | -0.004052909829445166 |
| PBC | NCC m=10 | brier_scores:Std | Fold_3 | 0.0811329937376906 | 0.08188450292291646 | 0.0007515091852258599 |
| PBC | NCC m=10 | brier_scores:Std | Fold_4 | 0.06031319799669361 | 0.05748113040517602 | -0.0028320675915175855 |
| PBC | NCC m=100 | brier_scores:Mean | Fold_0 | 0.11546735764490455 | 0.11126948217377856 | -0.004197875471125989 |
| PBC | NCC m=100 | brier_scores:Mean | Fold_1 | 0.09652995033367448 | 0.1124312702556629 | 0.015901319921988413 |
| PBC | NCC m=100 | brier_scores:Mean | Fold_2 | 0.11366538982425586 | 0.10862780572956794 | -0.005037584094687922 |
| PBC | NCC m=100 | brier_scores:Mean | Fold_3 | 0.18608814002591614 | 0.17137190099489386 | -0.014716239031022288 |
| PBC | NCC m=100 | brier_scores:Mean | Fold_4 | 0.1201800412059937 | 0.11512382159688268 | -0.005056219609111012 |
| PBC | NCC m=100 | brier_scores:Std | Fold_0 | 0.0544578468424644 | 0.05251522402641262 | -0.0019426228160517797 |
| PBC | NCC m=100 | brier_scores:Std | Fold_1 | 0.034352379409005235 | 0.04313103177830413 | 0.008778652369298895 |
| PBC | NCC m=100 | brier_scores:Std | Fold_2 | 0.045575182916133446 | 0.043969085723546214 | -0.0016060971925872317 |
| PBC | NCC m=100 | brier_scores:Std | Fold_3 | 0.09048682798049265 | 0.07428427429641161 | -0.016202553684081036 |
| PBC | NCC m=100 | brier_scores:Std | Fold_4 | 0.05671458520108653 | 0.05576481118721438 | -0.0009497740138721469 |
| PBC | NCC m=20 | brier_scores:Mean | Fold_0 | 0.15357914261216027 | 0.1157198827058574 | -0.03785925990630287 |
| PBC | NCC m=20 | brier_scores:Mean | Fold_1 | 0.0960555090434273 | 0.11417949743879699 | 0.01812398839536969 |
| PBC | NCC m=20 | brier_scores:Mean | Fold_2 | 0.10816519484070203 | 0.10922130570484229 | 0.0010561108641402583 |
| PBC | NCC m=20 | brier_scores:Mean | Fold_3 | 0.18447016639445712 | 0.16173996315279987 | -0.022730203241657254 |
| PBC | NCC m=20 | brier_scores:Mean | Fold_4 | 0.11748087547493183 | 0.11698151501155785 | -0.0004993604633739823 |
| PBC | NCC m=20 | brier_scores:Std | Fold_0 | 0.10624387882881016 | 0.056071190814485694 | -0.050172688014324465 |
| PBC | NCC m=20 | brier_scores:Std | Fold_1 | 0.034291278003500965 | 0.04517500248194063 | 0.010883724478439667 |
| PBC | NCC m=20 | brier_scores:Std | Fold_2 | 0.04492836712840646 | 0.043974764615356786 | -0.000953602513049677 |
| PBC | NCC m=20 | brier_scores:Std | Fold_3 | 0.09355877920025385 | 0.07121815140228652 | -0.022340627797967333 |
| PBC | NCC m=20 | brier_scores:Std | Fold_4 | 0.05648725922674006 | 0.05682290432428295 | 0.00033564509754288596 |
| PBC | NCC m=5 | brier_scores:Mean | Fold_0 | 0.12146103495597135 | 0.11969784400506896 | -0.0017631909509023963 |
| PBC | NCC m=5 | brier_scores:Mean | Fold_1 | 0.17274183134618665 | 0.09854088639506027 | -0.07420094495112638 |
| PBC | NCC m=5 | brier_scores:Mean | Fold_2 | 0.17177201442027523 | 0.1821240695101868 | 0.010352055089911577 |
| PBC | NCC m=5 | brier_scores:Mean | Fold_3 | 0.1864449130033996 | 0.2712327069009642 | 0.08478779389756458 |
| PBC | NCC m=5 | brier_scores:Mean | Fold_4 | 0.19328780192111472 | 0.131109361231111 | -0.06217844069000372 |
| PBC | NCC m=5 | brier_scores:Std | Fold_0 | 0.06112218589891222 | 0.05888459383272415 | -0.0022375920661880655 |
| PBC | NCC m=5 | brier_scores:Std | Fold_1 | 0.08297903759556942 | 0.03660045146729665 | -0.04637858612827277 |
| PBC | NCC m=5 | brier_scores:Std | Fold_2 | 0.08931502770966636 | 0.09956067243578146 | 0.010245644726115097 |
| PBC | NCC m=5 | brier_scores:Std | Fold_3 | 0.09809037314402014 | 0.1647866281240256 | 0.06669625498000548 |
| PBC | NCC m=5 | brier_scores:Std | Fold_4 | 0.10201949039603442 | 0.06151194421872711 | -0.040507546177307306 |
| PBC | NCC m=50 | brier_scores:Mean | Fold_0 | 0.12140276292449792 | 0.11395284343481553 | -0.007449919489682391 |
| PBC | NCC m=50 | brier_scores:Mean | Fold_1 | 0.09644466486708836 | 0.11925052683750774 | 0.02280586197041938 |
| PBC | NCC m=50 | brier_scores:Mean | Fold_2 | 0.1151099543087619 | 0.10864128629660844 | -0.0064686680121534695 |
| PBC | NCC m=50 | brier_scores:Mean | Fold_3 | 0.1823148921774895 | 0.14908070105842436 | -0.03323419111906514 |
| PBC | NCC m=50 | brier_scores:Mean | Fold_4 | 0.11618410667886855 | 0.11609122975810969 | -9.287692075886367e-05 |
| PBC | NCC m=50 | brier_scores:Std | Fold_0 | 0.0667599444067682 | 0.05475727361445961 | -0.012002670792308594 |
| PBC | NCC m=50 | brier_scores:Std | Fold_1 | 0.03325336296948716 | 0.049256460967557016 | 0.016003097998069857 |
| PBC | NCC m=50 | brier_scores:Std | Fold_2 | 0.04690528414992233 | 0.04411045324888265 | -0.0027948309010396785 |
| PBC | NCC m=50 | brier_scores:Std | Fold_3 | 0.08015615163028897 | 0.06327731139037 | -0.016878840239918966 |
| PBC | NCC m=50 | brier_scores:Std | Fold_4 | 0.05559671776735575 | 0.05546553988241032 | -0.0001311778849454326 |
| PBC | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_0 | 0.037460280441943855 | 0.6786578433373175 | 0.6411975628953737 |
| PBC | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_1 | 0.762813273421919 | 0.7725208448470577 | 0.009707571425138783 |
| PBC | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_2 | 0.09854688904424248 | 0.7903475481873564 | 0.691800659143114 |
| PBC | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_3 | 0.06418918918918919 | 0.72997542997543 | 0.6657862407862408 |
| PBC | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_4 | 0.7729109328336359 | 0.6827018797212625 | -0.09020905311237337 |
| PBC | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.16450456228318222 | 0.7104043378130193 | 0.545899775529837 |
| PBC | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.7842227935699354 | 0.7868178869212101 | 0.0025950933512747243 |
| PBC | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.6963197842804354 | 0.6958204334365325 | -0.000499350843902846 |
| PBC | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.774078624078624 | 0.7715601965601966 | -0.0025184275184274574 |
| PBC | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.756221818820636 | 0.7910640042161973 | 0.034842185395561276 |
| PBC | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_0 | 0.7046322479083462 | 0.6935836515756639 | -0.011048596332682292 |
| PBC | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_1 | 0.7341711319893313 | 0.7908066415166879 | 0.05663550952735663 |
| PBC | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_2 | 0.7722460800958754 | 0.8219564566064117 | 0.049710376510536336 |
| PBC | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_3 | 0.759551597051597 | 0.764404176904177 | 0.004852579852579919 |
| PBC | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_4 | 0.7652397962171341 | 0.6354160566844294 | -0.12982373953270476 |
| PBC | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_0 | 0.7095006267673382 | 0.6945456665597761 | -0.01495496020756204 |
| PBC | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_1 | 0.7449599923108345 | 0.8240382535982892 | 0.07907826128745465 |
| PBC | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_2 | 0.8003095975232198 | 0.789423749126136 | -0.010885848397083842 |
| PBC | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_3 | 0.7314496314496315 | 0.7522420147420148 | 0.02079238329238331 |
| PBC | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_4 | 0.7448615096328395 | 0.6087134742636294 | -0.13614803536921005 |
| PBC | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.6742558959857738 | 0.7681543888289654 | 0.09389849284319152 |
| PBC | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.8444866280606483 | 0.7432299300766514 | -0.10125669798399695 |
| PBC | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.6357485269150105 | 0.8048287226605413 | 0.1690801957455308 |
| PBC | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.7278255528255528 | 0.7418611793611793 | 0.01403562653562651 |
| PBC | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.7728523745388535 | 0.7817239561983955 | 0.00887158165954205 |
| PBC | SCC a=0.05 | IBS_scores:IBS_Score | Fold_0 | 0.1857488104670865 | 0.12106137924180567 | -0.06468743122528083 |
| PBC | SCC a=0.05 | IBS_scores:IBS_Score | Fold_1 | 0.15603639591669835 | 0.10757828847614771 | -0.04845810744055064 |
| PBC | SCC a=0.05 | IBS_scores:IBS_Score | Fold_2 | 0.1737551214297284 | 0.10067028626002704 | -0.07308483516970136 |
| PBC | SCC a=0.05 | IBS_scores:IBS_Score | Fold_3 | 0.26848690108712786 | 0.2012088484137982 | -0.06727805267332965 |
| PBC | SCC a=0.05 | IBS_scores:IBS_Score | Fold_4 | 0.17728659367128238 | 0.18555365854356565 | 0.008267064872283264 |
| PBC | SCC a=0.1 | IBS_scores:IBS_Score | Fold_0 | 0.18325811376638615 | 0.11699244869918006 | -0.06626566506720609 |
| PBC | SCC a=0.1 | IBS_scores:IBS_Score | Fold_1 | 0.11002065806488905 | 0.10333306013997354 | -0.006687597924915509 |
| PBC | SCC a=0.1 | IBS_scores:IBS_Score | Fold_2 | 0.12193759673520829 | 0.1659711816110119 | 0.04403358487580361 |
| PBC | SCC a=0.1 | IBS_scores:IBS_Score | Fold_3 | 0.1945584551158026 | 0.1487095195047857 | -0.04584893561101691 |
| PBC | SCC a=0.1 | IBS_scores:IBS_Score | Fold_4 | 0.1755049768405048 | 0.10277504844612 | -0.07272992839438482 |
| PBC | SCC a=0.2 | IBS_scores:IBS_Score | Fold_0 | 0.11404206215204751 | 0.11568911026718041 | 0.0016470481151329014 |
| PBC | SCC a=0.2 | IBS_scores:IBS_Score | Fold_1 | 0.116452145388091 | 0.10506930886902009 | -0.011382836519070905 |
| PBC | SCC a=0.2 | IBS_scores:IBS_Score | Fold_2 | 0.11080945185149195 | 0.09324766696214845 | -0.0175617848893435 |
| PBC | SCC a=0.2 | IBS_scores:IBS_Score | Fold_3 | 0.16531352941830973 | 0.15524502383925604 | -0.0100685055790537 |
| PBC | SCC a=0.2 | IBS_scores:IBS_Score | Fold_4 | 0.14508642628812607 | 0.1297101819934216 | -0.015376244294704466 |
| PBC | SCC a=0.3 | IBS_scores:IBS_Score | Fold_0 | 0.11349282177860863 | 0.1132944487538122 | -0.00019837302479643049 |
| PBC | SCC a=0.3 | IBS_scores:IBS_Score | Fold_1 | 0.11676282069545067 | 0.09674374532584624 | -0.020019075369604428 |
| PBC | SCC a=0.3 | IBS_scores:IBS_Score | Fold_2 | 0.10121626179544477 | 0.10042354195998934 | -0.0007927198354554243 |
| PBC | SCC a=0.3 | IBS_scores:IBS_Score | Fold_3 | 0.1466481922956621 | 0.14815346355535108 | 0.001505271259688995 |
| PBC | SCC a=0.3 | IBS_scores:IBS_Score | Fold_4 | 0.1328485130822209 | 0.157560088795518 | 0.0247115757132971 |
| PBC | SCC a=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.1164875252986246 | 0.1003440067927021 | -0.016143518505922508 |
| PBC | SCC a=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.0923628395428623 | 0.10539092365687384 | 0.013028084114011546 |
| PBC | SCC a=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.13340000889243359 | 0.09744480478171762 | -0.03595520411071597 |
| PBC | SCC a=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.15123438835404737 | 0.15587459681679536 | 0.004640208462747986 |
| PBC | SCC a=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.1088929706073451 | 0.10398940181561338 | -0.004903568791731719 |
| PBC | SCC a=0.05 | Training_Durations:Training_Duration | Fold_0 | 15.286603212356567 | 38.45727849006653 | 23.17067527770996 |
| PBC | SCC a=0.05 | Training_Durations:Training_Duration | Fold_1 | 14.720638275146484 | 27.879282236099243 | 13.158643960952759 |
| PBC | SCC a=0.05 | Training_Durations:Training_Duration | Fold_2 | 12.194469928741455 | 26.449791431427002 | 14.255321502685547 |
| PBC | SCC a=0.05 | Training_Durations:Training_Duration | Fold_3 | 16.24605917930603 | 31.887335062026978 | 15.641275882720947 |
| PBC | SCC a=0.05 | Training_Durations:Training_Duration | Fold_4 | 26.831336736679077 | 13.701808452606201 | -13.129528284072876 |
| PBC | SCC a=0.1 | Training_Durations:Training_Duration | Fold_0 | 13.74579405784607 | 32.57676362991333 | 18.83096957206726 |
| PBC | SCC a=0.1 | Training_Durations:Training_Duration | Fold_1 | 21.32888960838318 | 22.346076011657715 | 1.0171864032745361 |
| PBC | SCC a=0.1 | Training_Durations:Training_Duration | Fold_2 | 21.870708465576172 | 11.781413078308105 | -10.089295387268066 |
| PBC | SCC a=0.1 | Training_Durations:Training_Duration | Fold_3 | 19.822437286376953 | 30.446422338485718 | 10.623985052108765 |
| PBC | SCC a=0.1 | Training_Durations:Training_Duration | Fold_4 | 19.245497941970825 | 47.730443239212036 | 28.48494529724121 |
| PBC | SCC a=0.2 | Training_Durations:Training_Duration | Fold_0 | 21.887791872024536 | 24.350125551223755 | 2.4623336791992188 |
| PBC | SCC a=0.2 | Training_Durations:Training_Duration | Fold_1 | 17.243263483047485 | 20.299394607543945 | 3.05613112449646 |
| PBC | SCC a=0.2 | Training_Durations:Training_Duration | Fold_2 | 20.385615348815918 | 38.615002155303955 | 18.229386806488037 |
| PBC | SCC a=0.2 | Training_Durations:Training_Duration | Fold_3 | 19.83400869369507 | 28.549484968185425 | 8.715476274490356 |
| PBC | SCC a=0.2 | Training_Durations:Training_Duration | Fold_4 | 17.8460693359375 | 11.688904285430908 | -6.157165050506592 |
| PBC | SCC a=0.3 | Training_Durations:Training_Duration | Fold_0 | 23.862112283706665 | 25.342625617980957 | 1.480513334274292 |
| PBC | SCC a=0.3 | Training_Durations:Training_Duration | Fold_1 | 19.91298532485962 | 22.782185077667236 | 2.869199752807617 |
| PBC | SCC a=0.3 | Training_Durations:Training_Duration | Fold_2 | 26.451884746551514 | 32.66194272041321 | 6.210057973861694 |
| PBC | SCC a=0.3 | Training_Durations:Training_Duration | Fold_3 | 25.423667669296265 | 23.882834672927856 | -1.5408329963684082 |
| PBC | SCC a=0.3 | Training_Durations:Training_Duration | Fold_4 | 21.850756406784058 | 13.723423957824707 | -8.12733244895935 |
| PBC | SCC a=0.5 | Training_Durations:Training_Duration | Fold_0 | 23.29353094100952 | 45.72538375854492 | 22.4318528175354 |
| PBC | SCC a=0.5 | Training_Durations:Training_Duration | Fold_1 | 35.45706105232239 | 19.791417837142944 | -15.665643215179443 |
| PBC | SCC a=0.5 | Training_Durations:Training_Duration | Fold_2 | 16.178434133529663 | 45.58134484291077 | 29.402910709381104 |
| PBC | SCC a=0.5 | Training_Durations:Training_Duration | Fold_3 | 21.22995162010193 | 20.75578498840332 | -0.4741666316986084 |
| PBC | SCC a=0.5 | Training_Durations:Training_Duration | Fold_4 | 52.13363432884216 | 41.68753790855408 | -10.446096420288086 |
| PBC | SCC a=0.05 | brier_scores:Mean | Fold_0 | 0.21569637141664263 | 0.13492728890867448 | -0.08076908250796816 |
| PBC | SCC a=0.05 | brier_scores:Mean | Fold_1 | 0.16897997917681717 | 0.11441648252586187 | -0.05456349665095531 |
| PBC | SCC a=0.05 | brier_scores:Mean | Fold_2 | 0.1959181495144276 | 0.11189059788205175 | -0.08402755163237585 |
| PBC | SCC a=0.05 | brier_scores:Mean | Fold_3 | 0.3075780307278961 | 0.22654562050468216 | -0.08103241022321392 |
| PBC | SCC a=0.05 | brier_scores:Mean | Fold_4 | 0.19848490598247448 | 0.20938288340088673 | 0.010897977418412252 |
| PBC | SCC a=0.05 | brier_scores:Std | Fold_0 | 0.1680573751514966 | 0.07504323034735307 | -0.09301414480414354 |
| PBC | SCC a=0.05 | brier_scores:Std | Fold_1 | 0.0801736065281642 | 0.0435606315178731 | -0.0366129750102911 |
| PBC | SCC a=0.05 | brier_scores:Std | Fold_2 | 0.11186225534496569 | 0.043519684880694694 | -0.068342570464271 |
| PBC | SCC a=0.05 | brier_scores:Std | Fold_3 | 0.18810481073134622 | 0.11982231208485185 | -0.06828249864649437 |
| PBC | SCC a=0.05 | brier_scores:Std | Fold_4 | 0.11014960783587695 | 0.12841234287959316 | 0.018262735043716213 |
| PBC | SCC a=0.1 | brier_scores:Mean | Fold_0 | 0.21300002511502086 | 0.1301564805648203 | -0.08284354455020057 |
| PBC | SCC a=0.1 | brier_scores:Mean | Fold_1 | 0.11746167216011125 | 0.1106007209548958 | -0.006860951205215446 |
| PBC | SCC a=0.1 | brier_scores:Mean | Fold_2 | 0.13542984364701488 | 0.1844876869515536 | 0.04905784330453872 |
| PBC | SCC a=0.1 | brier_scores:Mean | Fold_3 | 0.22068803088351413 | 0.16582679198434108 | -0.05486123889917305 |
| PBC | SCC a=0.1 | brier_scores:Mean | Fold_4 | 0.1976115219053553 | 0.11381577072849076 | -0.08379575117686454 |
| PBC | SCC a=0.1 | brier_scores:Std | Fold_0 | 0.1673496584398863 | 0.06972762168820018 | -0.09762203675168613 |
| PBC | SCC a=0.1 | brier_scores:Std | Fold_1 | 0.04579322480780467 | 0.04565410987215082 | -0.00013911493565384875 |
| PBC | SCC a=0.1 | brier_scores:Std | Fold_2 | 0.054114888602104914 | 0.09453533090597309 | 0.040420442303868175 |
| PBC | SCC a=0.1 | brier_scores:Std | Fold_3 | 0.121044676399346 | 0.07543140015227257 | -0.04561327624707344 |
| PBC | SCC a=0.1 | brier_scores:Std | Fold_4 | 0.11669869977117585 | 0.0564035313431611 | -0.06029516842801475 |
| PBC | SCC a=0.2 | brier_scores:Mean | Fold_0 | 0.128015626804681 | 0.12921215327326036 | 0.0011965264685793453 |
| PBC | SCC a=0.2 | brier_scores:Mean | Fold_1 | 0.12536678520403735 | 0.11215571560749545 | -0.013211069596541905 |
| PBC | SCC a=0.2 | brier_scores:Mean | Fold_2 | 0.12301730151522185 | 0.10414514401310015 | -0.018872157502121692 |
| PBC | SCC a=0.2 | brier_scores:Mean | Fold_3 | 0.18588054628020922 | 0.17343115966669248 | -0.012449386613516744 |
| PBC | SCC a=0.2 | brier_scores:Mean | Fold_4 | 0.16213623573140798 | 0.1437830295443322 | -0.018353206187075782 |
| PBC | SCC a=0.2 | brier_scores:Std | Fold_0 | 0.07570084736702981 | 0.07183564829699643 | -0.0038651990700333816 |
| PBC | SCC a=0.2 | brier_scores:Std | Fold_1 | 0.05245694851700414 | 0.043044054171125085 | -0.009412894345879053 |
| PBC | SCC a=0.2 | brier_scores:Std | Fold_2 | 0.048394185400626094 | 0.040105566055353564 | -0.00828861934527253 |
| PBC | SCC a=0.2 | brier_scores:Std | Fold_3 | 0.09138079835445166 | 0.08128535609801274 | -0.010095442256438922 |
| PBC | SCC a=0.2 | brier_scores:Std | Fold_4 | 0.08386454794816016 | 0.07232771849909571 | -0.01153682944906445 |
| PBC | SCC a=0.3 | brier_scores:Mean | Fold_0 | 0.12670809598983712 | 0.12669150877971866 | -1.658721011846276e-05 |
| PBC | SCC a=0.3 | brier_scores:Mean | Fold_1 | 0.12549832613783207 | 0.10308629669229127 | -0.0224120294455408 |
| PBC | SCC a=0.3 | brier_scores:Mean | Fold_2 | 0.11284931621600208 | 0.11151288128054254 | -0.0013364349354595406 |
| PBC | SCC a=0.3 | brier_scores:Mean | Fold_3 | 0.16385764180063997 | 0.16411733581207585 | 0.0002596940114358848 |
| PBC | SCC a=0.3 | brier_scores:Mean | Fold_4 | 0.14782663553402 | 0.17577894134822766 | 0.027952305814207656 |
| PBC | SCC a=0.3 | brier_scores:Std | Fold_0 | 0.0680689574869322 | 0.0687055367105228 | 0.0006365792235906026 |
| PBC | SCC a=0.3 | brier_scores:Std | Fold_1 | 0.05090958954624274 | 0.03944437124876269 | -0.011465218297480047 |
| PBC | SCC a=0.3 | brier_scores:Std | Fold_2 | 0.04570609188827005 | 0.04326504943079239 | -0.0024410424574776643 |
| PBC | SCC a=0.3 | brier_scores:Std | Fold_3 | 0.07552002652735809 | 0.07038020125803329 | -0.005139825269324799 |
| PBC | SCC a=0.3 | brier_scores:Std | Fold_4 | 0.07161884405971268 | 0.09157317421382906 | 0.01995433015411638 |
| PBC | SCC a=0.5 | brier_scores:Mean | Fold_0 | 0.13064503452963433 | 0.11132387734856426 | -0.019321157181070067 |
| PBC | SCC a=0.5 | brier_scores:Mean | Fold_1 | 0.09825523368207253 | 0.11233510585198662 | 0.01407987216991409 |
| PBC | SCC a=0.5 | brier_scores:Mean | Fold_2 | 0.14868699547982883 | 0.10902769088810717 | -0.039659304591721664 |
| PBC | SCC a=0.5 | brier_scores:Mean | Fold_3 | 0.1680810426578546 | 0.1748197393280033 | 0.006738696670148703 |
| PBC | SCC a=0.5 | brier_scores:Mean | Fold_4 | 0.12008641836664513 | 0.11471192070663891 | -0.005374497660006222 |
| PBC | SCC a=0.5 | brier_scores:Std | Fold_0 | 0.07465787517898831 | 0.05364232178706448 | -0.021015553391923826 |
| PBC | SCC a=0.5 | brier_scores:Std | Fold_1 | 0.03476719136878601 | 0.04437624831112169 | 0.00960905694233568 |
| PBC | SCC a=0.5 | brier_scores:Std | Fold_2 | 0.06414336727341725 | 0.04380425180516219 | -0.020339115468255065 |
| PBC | SCC a=0.5 | brier_scores:Std | Fold_3 | 0.07455955212279088 | 0.08550702581127877 | 0.010947473688487891 |
| PBC | SCC a=0.5 | brier_scores:Std | Fold_4 | 0.05770674697709643 | 0.05432892915432134 | -0.0033778178227750894 |
| PBC | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.0 | 0.0 | 0.0 |
| PBC | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.0 | 0.05742845471802389 | 0.05742845471802389 |
| PBC | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.0 | 0.0 | 0.0 |
| PBC | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.0 | 0.06980958230958231 | 0.06980958230958231 |
| PBC | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.0 | 0.0 | 0.0 |
| PBC | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.7459114363175232 | 0.711337200827916 | -0.03457423548960725 |
| PBC | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.8066655453300334 | 0.8344907129298124 | 0.027825167599778933 |
| PBC | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.7846549485668631 | 0.7854788774593029 | 0.0008239288924397625 |
| PBC | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.7352579852579852 | 0.7382063882063882 | 0.0029484029484029284 |
| PBC | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.7648006090062658 | 0.7533524623762956 | -0.01144814662997018 |
| PBC | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.7378946447832551 | 0.7616826516631199 | 0.02378800687986482 |
| PBC | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.7588966047528655 | 0.8418675060672322 | 0.08297090131436669 |
| PBC | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.7776141016678318 | 0.8054778787576151 | 0.02786377708978327 |
| PBC | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.769041769041769 | 0.7461916461916462 | -0.022850122850122778 |
| PBC | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.7787960414592727 | 0.7925865198805411 | 0.013790478421268348 |
| PBC | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_0 | 0.7031454974783546 | 0.7124158236888902 | 0.009270326210535584 |
| PBC | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_1 | 0.8512386765023908 | 0.793257563015114 | -0.05798111348727686 |
| PBC | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_2 | 0.7219115150304604 | 0.8040297613102966 | 0.08211824627983622 |
| PBC | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_3 | 0.7440110565110565 | 0.7558046683046683 | 0.011793611793611825 |
| PBC | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_4 | 0.7669087076184341 | 0.7469988873923992 | -0.019909820226034936 |
| PBC | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.7027082179401218 | 0.6927673964376294 | -0.009940821502492425 |
| PBC | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.7491169474013023 | 0.8461446043684071 | 0.0970276569671048 |
| PBC | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.7946419654449216 | 0.808873464496155 | 0.014231499051233443 |
| PBC | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.7827395577395577 | 0.7468673218673219 | -0.03587223587223587 |
| PBC | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.7767465011418867 | 0.7847104292323007 | 0.007963928090414019 |
| PBC | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.14482007342475353 | 0.14175521665331095 | -0.003064856771442581 |
| PBC | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.1307834118065778 | 0.13022662058724718 | -0.0005567912193306102 |
| PBC | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.13152056665045758 | 0.11375777508475388 | -0.017762791565703706 |
| PBC | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.1579691251286017 | 0.15817521305586807 | 0.0002060879272663685 |
| PBC | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.12751687274453657 | 0.14326175537001148 | 0.01574488262547491 |
| PBC | Entropy t=10 | IBS_scores:IBS_Score | Fold_0 | 0.11086504903254003 | 0.10378986995661084 | -0.007075179075929194 |
| PBC | Entropy t=10 | IBS_scores:IBS_Score | Fold_1 | 0.10261844229210144 | 0.09226228695034625 | -0.0103561553417552 |
| PBC | Entropy t=10 | IBS_scores:IBS_Score | Fold_2 | 0.102091184834918 | 0.09811876387954661 | -0.0039724209553713835 |
| PBC | Entropy t=10 | IBS_scores:IBS_Score | Fold_3 | 0.14351729714826575 | 0.14484916600315767 | 0.001331868854891921 |
| PBC | Entropy t=10 | IBS_scores:IBS_Score | Fold_4 | 0.11036786928328352 | 0.10137719998630172 | -0.008990669296981793 |
| PBC | Entropy t=1 | IBS_scores:IBS_Score | Fold_0 | 0.13023321186051326 | 0.12537499155608398 | -0.004858220304429284 |
| PBC | Entropy t=1 | IBS_scores:IBS_Score | Fold_1 | 0.08830744522840002 | 0.11507353962619471 | 0.02676609439779469 |
| PBC | Entropy t=1 | IBS_scores:IBS_Score | Fold_2 | 0.125728179601082 | 0.09692712013051137 | -0.028801059470570642 |
| PBC | Entropy t=1 | IBS_scores:IBS_Score | Fold_3 | 0.1569710329063036 | 0.14868093124065052 | -0.008290101665653082 |
| PBC | Entropy t=1 | IBS_scores:IBS_Score | Fold_4 | 0.11329526823850791 | 0.11224567109189279 | -0.0010495971466151222 |
| PBC | Entropy t=5 | IBS_scores:IBS_Score | Fold_0 | 0.1161231911508993 | 0.11510437157378829 | -0.001018819577111002 |
| PBC | Entropy t=5 | IBS_scores:IBS_Score | Fold_1 | 0.10385392521008643 | 0.09193350966267226 | -0.011920415547414173 |
| PBC | Entropy t=5 | IBS_scores:IBS_Score | Fold_2 | 0.09862187595156091 | 0.09621137572533112 | -0.0024105002262297948 |
| PBC | Entropy t=5 | IBS_scores:IBS_Score | Fold_3 | 0.1646291183221247 | 0.14378061516624313 | -0.020848503155881576 |
| PBC | Entropy t=5 | IBS_scores:IBS_Score | Fold_4 | 0.10547250590729107 | 0.1048659138892321 | -0.000606592018058974 |
| PBC | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_0 | 9.6609628200531 | 15.199207305908203 | 5.5382444858551025 |
| PBC | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_1 | 16.77077889442444 | 22.90253257751465 | 6.13175368309021 |
| PBC | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_2 | 12.699423551559448 | 7.111953258514404 | -5.587470293045044 |
| PBC | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_3 | 13.308974981307983 | 23.808141708374023 | 10.49916672706604 |
| PBC | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_4 | 10.75673222541809 | 8.09937572479248 | -2.6573565006256104 |
| PBC | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_0 | 14.221815347671509 | 13.670416831970215 | -0.551398515701294 |
| PBC | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_1 | 13.203039169311523 | 11.769685983657837 | -1.4333531856536865 |
| PBC | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_2 | 13.19983196258545 | 13.65974473953247 | 0.4599127769470215 |
| PBC | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_3 | 20.439860105514526 | 19.830937147140503 | -0.6089229583740234 |
| PBC | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_4 | 19.40880560874939 | 14.726555824279785 | -4.6822497844696045 |
| PBC | Entropy t=10 | Training_Durations:Training_Duration | Fold_0 | 28.37902045249939 | 49.449960708618164 | 21.070940256118774 |
| PBC | Entropy t=10 | Training_Durations:Training_Duration | Fold_1 | 11.176550388336182 | 25.33640480041504 | 14.159854412078857 |
| PBC | Entropy t=10 | Training_Durations:Training_Duration | Fold_2 | 14.183369159698486 | 16.216874599456787 | 2.033505439758301 |
| PBC | Entropy t=10 | Training_Durations:Training_Duration | Fold_3 | 45.22576856613159 | 25.851455450057983 | -19.37431311607361 |
| PBC | Entropy t=10 | Training_Durations:Training_Duration | Fold_4 | 29.971662521362305 | 35.48582172393799 | 5.514159202575684 |
| PBC | Entropy t=1 | Training_Durations:Training_Duration | Fold_0 | 13.688682794570923 | 14.185442447662354 | 0.49675965309143066 |
| PBC | Entropy t=1 | Training_Durations:Training_Duration | Fold_1 | 19.720829486846924 | 12.289443016052246 | -7.431386470794678 |
| PBC | Entropy t=1 | Training_Durations:Training_Duration | Fold_2 | 12.352858066558838 | 17.18293523788452 | 4.830077171325684 |
| PBC | Entropy t=1 | Training_Durations:Training_Duration | Fold_3 | 18.801115036010742 | 14.231109619140625 | -4.570005416870117 |
| PBC | Entropy t=1 | Training_Durations:Training_Duration | Fold_4 | 20.82624840736389 | 23.28454613685608 | 2.4582977294921875 |
| PBC | Entropy t=5 | Training_Durations:Training_Duration | Fold_0 | 14.375534534454346 | 19.246341228485107 | 4.870806694030762 |
| PBC | Entropy t=5 | Training_Durations:Training_Duration | Fold_1 | 11.692704200744629 | 23.806448459625244 | 12.113744258880615 |
| PBC | Entropy t=5 | Training_Durations:Training_Duration | Fold_2 | 17.349960327148438 | 15.32180142402649 | -2.0281589031219482 |
| PBC | Entropy t=5 | Training_Durations:Training_Duration | Fold_3 | 11.71998643875122 | 27.335806131362915 | 15.615819692611694 |
| PBC | Entropy t=5 | Training_Durations:Training_Duration | Fold_4 | 27.507564067840576 | 46.73243021965027 | 19.224866151809692 |
| PBC | Entropy t=0.5 | brier_scores:Mean | Fold_0 | 0.16609460377835397 | 0.16284241083812023 | -0.003252192940233739 |
| PBC | Entropy t=0.5 | brier_scores:Mean | Fold_1 | 0.1407260462838812 | 0.14056111664668086 | -0.00016492963720032838 |
| PBC | Entropy t=0.5 | brier_scores:Mean | Fold_2 | 0.1478032083822555 | 0.12713214017105082 | -0.02067106821120468 |
| PBC | Entropy t=0.5 | brier_scores:Mean | Fold_3 | 0.17864390912875514 | 0.17856706962213476 | -7.683950662037975e-05 |
| PBC | Entropy t=0.5 | brier_scores:Mean | Fold_4 | 0.1404497983869265 | 0.1591147389064011 | 0.018664940519474593 |
| PBC | Entropy t=0.5 | brier_scores:Std | Fold_0 | 0.12117152767935872 | 0.11928292099921237 | -0.001888606680146357 |
| PBC | Entropy t=0.5 | brier_scores:Std | Fold_1 | 0.06371107475882946 | 0.06398341192432294 | 0.00027233716549347753 |
| PBC | Entropy t=0.5 | brier_scores:Std | Fold_2 | 0.06953491587815648 | 0.05351297304400698 | -0.016021942834149504 |
| PBC | Entropy t=0.5 | brier_scores:Std | Fold_3 | 0.08834280762069428 | 0.08792252561833626 | -0.0004202820023580245 |
| PBC | Entropy t=0.5 | brier_scores:Std | Fold_4 | 0.06510163662322506 | 0.07839868235340651 | 0.01329704573018145 |
| PBC | Entropy t=10 | brier_scores:Mean | Fold_0 | 0.1229939139709649 | 0.11483532653080271 | -0.008158587440162193 |
| PBC | Entropy t=10 | brier_scores:Mean | Fold_1 | 0.10884704884556397 | 0.0982535672042337 | -0.010593481641330268 |
| PBC | Entropy t=10 | brier_scores:Mean | Fold_2 | 0.11342341806582099 | 0.1093350010069506 | -0.004088417058870392 |
| PBC | Entropy t=10 | brier_scores:Mean | Fold_3 | 0.16119899548903016 | 0.1624398838920931 | 0.0012408884030629397 |
| PBC | Entropy t=10 | brier_scores:Mean | Fold_4 | 0.12158769282033484 | 0.1120080439102749 | -0.00957964891005994 |
| PBC | Entropy t=10 | brier_scores:Std | Fold_0 | 0.06081884446713118 | 0.05504550795772947 | -0.005773336509401705 |
| PBC | Entropy t=10 | brier_scores:Std | Fold_1 | 0.03968130347844787 | 0.035052280255345784 | -0.004629023223102088 |
| PBC | Entropy t=10 | brier_scores:Std | Fold_2 | 0.04416077664339157 | 0.04275924868933033 | -0.0014015279540612394 |
| PBC | Entropy t=10 | brier_scores:Std | Fold_3 | 0.07298817241004121 | 0.07440515363436265 | 0.0014169812243214341 |
| PBC | Entropy t=10 | brier_scores:Std | Fold_4 | 0.058235199979443646 | 0.05361160559642221 | -0.004623594383021436 |
| PBC | Entropy t=1 | brier_scores:Mean | Fold_0 | 0.14890483426401904 | 0.14132431098756182 | -0.007580523276457224 |
| PBC | Entropy t=1 | brier_scores:Mean | Fold_1 | 0.09391044578300517 | 0.12305104939453665 | 0.02914060361153148 |
| PBC | Entropy t=1 | brier_scores:Mean | Fold_2 | 0.1409537907109913 | 0.10807781576434738 | -0.032875974946643904 |
| PBC | Entropy t=1 | brier_scores:Mean | Fold_3 | 0.17670773763937053 | 0.1654797031748613 | -0.011228034464509234 |
| PBC | Entropy t=1 | brier_scores:Mean | Fold_4 | 0.1251399528549036 | 0.12281576620793104 | -0.002324186646972551 |
| PBC | Entropy t=1 | brier_scores:Std | Fold_0 | 0.10284149486369498 | 0.08738278549455399 | -0.015458709369140997 |
| PBC | Entropy t=1 | brier_scores:Std | Fold_1 | 0.03250562683662563 | 0.05225597012920223 | 0.0197503432925766 |
| PBC | Entropy t=1 | brier_scores:Std | Fold_2 | 0.06416639287268801 | 0.04246581999116883 | -0.02170057288151918 |
| PBC | Entropy t=1 | brier_scores:Std | Fold_3 | 0.08447303851242058 | 0.07200285481229676 | -0.012470183700123816 |
| PBC | Entropy t=1 | brier_scores:Std | Fold_4 | 0.061550212943593405 | 0.05759129139811972 | -0.003958921545473684 |
| PBC | Entropy t=5 | brier_scores:Mean | Fold_0 | 0.13022931669099083 | 0.12762549289883984 | -0.002603823792150989 |
| PBC | Entropy t=5 | brier_scores:Mean | Fold_1 | 0.11080444876377374 | 0.09797231023299283 | -0.012832138530780912 |
| PBC | Entropy t=5 | brier_scores:Mean | Fold_2 | 0.1097838864422992 | 0.10720427026218983 | -0.0025796161801093648 |
| PBC | Entropy t=5 | brier_scores:Mean | Fold_3 | 0.18558829851437644 | 0.16113019618193852 | -0.02445810233243792 |
| PBC | Entropy t=5 | brier_scores:Mean | Fold_4 | 0.11608483165451453 | 0.1161950656993043 | 0.00011023404478976984 |
| PBC | Entropy t=5 | brier_scores:Std | Fold_0 | 0.07623206242043638 | 0.06319771653602982 | -0.013034345884406565 |
| PBC | Entropy t=5 | brier_scores:Std | Fold_1 | 0.044889862274368704 | 0.03512008298206052 | -0.009769779292308184 |
| PBC | Entropy t=5 | brier_scores:Std | Fold_2 | 0.043168643163941436 | 0.04174858157678817 | -0.0014200615871532637 |
| PBC | Entropy t=5 | brier_scores:Std | Fold_3 | 0.0926012155385058 | 0.07317582379242647 | -0.019425391746079324 |
| PBC | Entropy t=5 | brier_scores:Std | Fold_4 | 0.05510575483152117 | 0.05809174944875338 | 0.0029859946172322085 |
| FH | FULL | CIndex_scores:CIndex_Score | Fold_0 | 0.6838696505336705 | 0.6672980728877194 | -0.016571577645951185 |
| FH | FULL | CIndex_scores:CIndex_Score | Fold_1 | 0.6705681869142114 | 0.6625297098524597 | -0.008038477061751648 |
| FH | FULL | CIndex_scores:CIndex_Score | Fold_2 | 0.6153277177332995 | 0.6588798975502589 | 0.04355217981695936 |
| FH | FULL | CIndex_scores:CIndex_Score | Fold_3 | 0.635666991563876 | 0.6666442599625808 | 0.03097726839870485 |
| FH | FULL | CIndex_scores:CIndex_Score | Fold_4 | 0.6448863312631758 | 0.668497521508746 | 0.023611190245570124 |
| FH | FULL | IBS_scores:IBS_Score | Fold_0 | 0.06978024762487664 | 0.06877160712760978 | -0.0010086404972668578 |
| FH | FULL | IBS_scores:IBS_Score | Fold_1 | 0.07450843558227188 | 0.07481654752391673 | 0.00030811194164484523 |
| FH | FULL | IBS_scores:IBS_Score | Fold_2 | 0.07992325320222196 | 0.07975846200659806 | -0.00016479119562390343 |
| FH | FULL | IBS_scores:IBS_Score | Fold_3 | 0.0767733147201319 | 0.07535351232662103 | -0.0014198023935108606 |
| FH | FULL | IBS_scores:IBS_Score | Fold_4 | 0.07303396771054343 | 0.07131994158166191 | -0.001714026128881524 |
| FH | FULL | Training_Durations:Training_Duration | Fold_0 | 22.844584465026855 | 17.713239431381226 | -5.13134503364563 |
| FH | FULL | Training_Durations:Training_Duration | Fold_1 | 17.240116357803345 | 17.76178765296936 | 0.5216712951660156 |
| FH | FULL | Training_Durations:Training_Duration | Fold_2 | 19.24963617324829 | 66.51715302467346 | 47.26751685142517 |
| FH | FULL | Training_Durations:Training_Duration | Fold_3 | 18.248106479644775 | 19.291982650756836 | 1.0438761711120605 |
| FH | FULL | Training_Durations:Training_Duration | Fold_4 | 20.76939034461975 | 16.757844924926758 | -4.011545419692993 |
| FH | FULL | brier_scores:Mean | Fold_0 | 0.06786034555904064 | 0.06684490418309653 | -0.0010154413759441011 |
| FH | FULL | brier_scores:Mean | Fold_1 | 0.07216135773178715 | 0.07247731764162185 | 0.00031595990983469824 |
| FH | FULL | brier_scores:Mean | Fold_2 | 0.07780791602821935 | 0.07767107326991676 | -0.00013684275830258552 |
| FH | FULL | brier_scores:Mean | Fold_3 | 0.07457800765109222 | 0.07322731926683743 | -0.0013506883842547973 |
| FH | FULL | brier_scores:Mean | Fold_4 | 0.0707969703933534 | 0.06917203567583999 | -0.0016249347175134182 |
| FH | FULL | brier_scores:Std | Fold_0 | 0.037428163280802444 | 0.037212964235873766 | -0.00021519904492867808 |
| FH | FULL | brier_scores:Std | Fold_1 | 0.03984721813269713 | 0.04033645608981575 | 0.0004892379571186239 |
| FH | FULL | brier_scores:Std | Fold_2 | 0.03667308047654306 | 0.03650195034181415 | -0.0001711301347289071 |
| FH | FULL | brier_scores:Std | Fold_3 | 0.03711730765855885 | 0.03606228985384818 | -0.0010550178047106715 |
| FH | FULL | brier_scores:Std | Fold_4 | 0.037995708965133476 | 0.03671771807107259 | -0.0012779908940608875 |
| FH | NCC m=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.6845955786441024 | 0.6974921452309926 | 0.012896566586890201 |
| FH | NCC m=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.6468899950670434 | 0.664984976904794 | 0.0180949818377506 |
| FH | NCC m=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.6764332475905543 | 0.6822291650566896 | 0.005795917466135281 |
| FH | NCC m=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.693812388666689 | 0.7106622301392577 | 0.016849841472568627 |
| FH | NCC m=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.6598484416842345 | 0.6546179704860122 | -0.005230471198222286 |
| FH | NCC m=100 | CIndex_scores:CIndex_Score | Fold_0 | 0.6653471410909338 | 0.7243401426902442 | 0.05899300159931031 |
| FH | NCC m=100 | CIndex_scores:CIndex_Score | Fold_1 | 0.6362505045069285 | 0.6672720749809409 | 0.031021570474012328 |
| FH | NCC m=100 | CIndex_scores:CIndex_Score | Fold_2 | 0.6734083306653713 | 0.6577869531137877 | -0.01562137755158366 |
| FH | NCC m=100 | CIndex_scores:CIndex_Score | Fold_3 | 0.6192876908771104 | 0.6721114957595312 | 0.05282380488242078 |
| FH | NCC m=100 | CIndex_scores:CIndex_Score | Fold_4 | 0.6688279870092873 | 0.6911059198906045 | 0.022277932881317297 |
| FH | NCC m=20 | CIndex_scores:CIndex_Score | Fold_0 | 0.6781643092907456 | 0.6989213161984053 | 0.020757006907659692 |
| FH | NCC m=20 | CIndex_scores:CIndex_Score | Fold_1 | 0.666397596304767 | 0.6992690255168393 | 0.03287142921207231 |
| FH | NCC m=20 | CIndex_scores:CIndex_Score | Fold_2 | 0.6668727437321292 | 0.6820966869431779 | 0.015223943211048696 |
| FH | NCC m=20 | CIndex_scores:CIndex_Score | Fold_3 | 0.6937563719064744 | 0.7021028691784582 | 0.008346497271983777 |
| FH | NCC m=20 | CIndex_scores:CIndex_Score | Fold_4 | 0.6576263460771467 | 0.6933963876702183 | 0.03577004159307162 |
| FH | NCC m=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.6894048523757131 | 0.6883386454635164 | -0.001066206912196721 |
| FH | NCC m=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.6414188977084174 | 0.684447733082201 | 0.04302883537378355 |
| FH | NCC m=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.6615846590344554 | 0.6755279804815579 | 0.01394332144710253 |
| FH | NCC m=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.6886924567830695 | 0.6969829372948386 | 0.008290480511769172 |
| FH | NCC m=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.6451484245911914 | 0.6695686855449832 | 0.024420260953791795 |
| FH | NCC m=50 | CIndex_scores:CIndex_Score | Fold_0 | 0.7036171636627611 | 0.7293195558227374 | 0.025702392159976384 |
| FH | NCC m=50 | CIndex_scores:CIndex_Score | Fold_1 | 0.6505448674828468 | 0.7064554464325754 | 0.05591057894972862 |
| FH | NCC m=50 | CIndex_scores:CIndex_Score | Fold_2 | 0.6799107980702355 | 0.6712445214780142 | -0.0086662765922213 |
| FH | NCC m=50 | CIndex_scores:CIndex_Score | Fold_3 | 0.699537301560627 | 0.7076933418478809 | 0.008156040287253918 |
| FH | NCC m=50 | CIndex_scores:CIndex_Score | Fold_4 | 0.6818528858754487 | 0.6922112700131047 | 0.010358384137655996 |
| FH | NCC m=10 | IBS_scores:IBS_Score | Fold_0 | 0.07329116919550409 | 0.0695510315371842 | -0.003740137658319889 |
| FH | NCC m=10 | IBS_scores:IBS_Score | Fold_1 | 0.0751690993462805 | 0.07465745625366679 | -0.0005116430926137006 |
| FH | NCC m=10 | IBS_scores:IBS_Score | Fold_2 | 0.07828666185085914 | 0.07838706295642835 | 0.00010040110556920612 |
| FH | NCC m=10 | IBS_scores:IBS_Score | Fold_3 | 0.07582328798216842 | 0.07475924680202617 | -0.00106404118014225 |
| FH | NCC m=10 | IBS_scores:IBS_Score | Fold_4 | 0.0723377235921885 | 0.07190273290671512 | -0.0004349906854733826 |
| FH | NCC m=100 | IBS_scores:IBS_Score | Fold_0 | 0.06968328246615299 | 0.06842398339305134 | -0.0012592990731016551 |
| FH | NCC m=100 | IBS_scores:IBS_Score | Fold_1 | 0.07611628119424188 | 0.07549697639766495 | -0.0006193047965769305 |
| FH | NCC m=100 | IBS_scores:IBS_Score | Fold_2 | 0.07930431885193139 | 0.07935896254217856 | 5.464369024717197e-05 |
| FH | NCC m=100 | IBS_scores:IBS_Score | Fold_3 | 0.07681386732099252 | 0.07575920882914736 | -0.0010546584918451618 |
| FH | NCC m=100 | IBS_scores:IBS_Score | Fold_4 | 0.07185594948751751 | 0.07084216768848893 | -0.0010137817990285847 |
| FH | NCC m=20 | IBS_scores:IBS_Score | Fold_0 | 0.06854770465690473 | 0.06944849524136666 | 0.0009007905844619357 |
| FH | NCC m=20 | IBS_scores:IBS_Score | Fold_1 | 0.0741514805346932 | 0.07269897582791292 | -0.0014525047067802804 |
| FH | NCC m=20 | IBS_scores:IBS_Score | Fold_2 | 0.08021267886403011 | 0.0783756194851435 | -0.0018370593788866046 |
| FH | NCC m=20 | IBS_scores:IBS_Score | Fold_3 | 0.07520667438796974 | 0.07517502047692935 | -3.1653911040388505e-05 |
| FH | NCC m=20 | IBS_scores:IBS_Score | Fold_4 | 0.07261188964451357 | 0.07067194593493303 | -0.0019399437095805327 |
| FH | NCC m=5 | IBS_scores:IBS_Score | Fold_0 | 0.07169269282756428 | 0.07147624319326949 | -0.0002164496342947908 |
| FH | NCC m=5 | IBS_scores:IBS_Score | Fold_1 | 0.07566510192742006 | 0.07328585530818521 | -0.0023792466192348455 |
| FH | NCC m=5 | IBS_scores:IBS_Score | Fold_2 | 0.07992323454973886 | 0.0789915985301674 | -0.0009316360195714551 |
| FH | NCC m=5 | IBS_scores:IBS_Score | Fold_3 | 0.07573453905685722 | 0.07484482714486386 | -0.0008897119119933572 |
| FH | NCC m=5 | IBS_scores:IBS_Score | Fold_4 | 0.07341815429716564 | 0.07149264863543153 | -0.001925505661734106 |
| FH | NCC m=50 | IBS_scores:IBS_Score | Fold_0 | 0.06999378790670828 | 0.06829828916583461 | -0.0016954987408736716 |
| FH | NCC m=50 | IBS_scores:IBS_Score | Fold_1 | 0.07608605334452212 | 0.07247584036576742 | -0.003610212978754704 |
| FH | NCC m=50 | IBS_scores:IBS_Score | Fold_2 | 0.07895160545534777 | 0.079091903443485 | 0.00014029798813723626 |
| FH | NCC m=50 | IBS_scores:IBS_Score | Fold_3 | 0.07554578478308428 | 0.07504917311896726 | -0.0004966116641170193 |
| FH | NCC m=50 | IBS_scores:IBS_Score | Fold_4 | 0.07226401791486847 | 0.07075538679151208 | -0.001508631123356391 |
| FH | NCC m=10 | Training_Durations:Training_Duration | Fold_0 | 16.713932991027832 | 35.48914122581482 | 18.775208234786987 |
| FH | NCC m=10 | Training_Durations:Training_Duration | Fold_1 | 33.946003675460815 | 15.684058666229248 | -18.261945009231567 |
| FH | NCC m=10 | Training_Durations:Training_Duration | Fold_2 | 65.321692943573 | 69.99073696136475 | 4.669044017791748 |
| FH | NCC m=10 | Training_Durations:Training_Duration | Fold_3 | 57.2870614528656 | 99.93802762031555 | 42.65096616744995 |
| FH | NCC m=10 | Training_Durations:Training_Duration | Fold_4 | 44.68686079978943 | 18.242596864700317 | -26.44426393508911 |
| FH | NCC m=100 | Training_Durations:Training_Duration | Fold_0 | 21.788971662521362 | 109.88486099243164 | 88.09588932991028 |
| FH | NCC m=100 | Training_Durations:Training_Duration | Fold_1 | 20.26200819015503 | 19.3107693195343 | -0.9512388706207275 |
| FH | NCC m=100 | Training_Durations:Training_Duration | Fold_2 | 17.708662271499634 | 21.8981454372406 | 4.189483165740967 |
| FH | NCC m=100 | Training_Durations:Training_Duration | Fold_3 | 17.237409830093384 | 18.82361125946045 | 1.5862014293670654 |
| FH | NCC m=100 | Training_Durations:Training_Duration | Fold_4 | 90.72193169593811 | 72.14642763137817 | -18.575504064559937 |
| FH | NCC m=20 | Training_Durations:Training_Duration | Fold_0 | 16.231394290924072 | 19.21289324760437 | 2.981498956680298 |
| FH | NCC m=20 | Training_Durations:Training_Duration | Fold_1 | 50.68484377861023 | 89.04567098617554 | 38.36082720756531 |
| FH | NCC m=20 | Training_Durations:Training_Duration | Fold_2 | 17.82897162437439 | 78.24818158149719 | 60.4192099571228 |
| FH | NCC m=20 | Training_Durations:Training_Duration | Fold_3 | 19.23022699356079 | 52.190916776657104 | 32.96068978309631 |
| FH | NCC m=20 | Training_Durations:Training_Duration | Fold_4 | 28.38363242149353 | 73.5151162147522 | 45.13148379325867 |
| FH | NCC m=5 | Training_Durations:Training_Duration | Fold_0 | 16.21939730644226 | 15.362048149108887 | -0.857349157333374 |
| FH | NCC m=5 | Training_Durations:Training_Duration | Fold_1 | 34.057103872299194 | 53.877923011779785 | 19.82081913948059 |
| FH | NCC m=5 | Training_Durations:Training_Duration | Fold_2 | 19.787523984909058 | 41.85611844062805 | 22.068594455718994 |
| FH | NCC m=5 | Training_Durations:Training_Duration | Fold_3 | 41.17771315574646 | 17.385008096694946 | -23.792705059051514 |
| FH | NCC m=5 | Training_Durations:Training_Duration | Fold_4 | 57.36628866195679 | 52.15501546859741 | -5.211273193359375 |
| FH | NCC m=50 | Training_Durations:Training_Duration | Fold_0 | 20.784123420715332 | 136.0290722846985 | 115.24494886398315 |
| FH | NCC m=50 | Training_Durations:Training_Duration | Fold_1 | 19.74436378479004 | 71.90573263168335 | 52.16136884689331 |
| FH | NCC m=50 | Training_Durations:Training_Duration | Fold_2 | 71.92293357849121 | 53.26588726043701 | -18.6570463180542 |
| FH | NCC m=50 | Training_Durations:Training_Duration | Fold_3 | 74.61989283561707 | 70.41660714149475 | -4.2032856941223145 |
| FH | NCC m=50 | Training_Durations:Training_Duration | Fold_4 | 20.409887552261353 | 107.01604890823364 | 86.60616135597229 |
| FH | NCC m=10 | brier_scores:Mean | Fold_0 | 0.07119676232038513 | 0.06762217866546812 | -0.0035745836549170157 |
| FH | NCC m=10 | brier_scores:Mean | Fold_1 | 0.07274687713654664 | 0.07226489159631605 | -0.0004819855402305867 |
| FH | NCC m=10 | brier_scores:Mean | Fold_2 | 0.07624582863852404 | 0.0763606126863343 | 0.00011478404781026241 |
| FH | NCC m=10 | brier_scores:Mean | Fold_3 | 0.07366261531252649 | 0.07265160426663089 | -0.001011011045895599 |
| FH | NCC m=10 | brier_scores:Mean | Fold_4 | 0.07014241835201514 | 0.06974061735206276 | -0.0004018009999523786 |
| FH | NCC m=10 | brier_scores:Std | Fold_0 | 0.03962193070772645 | 0.03718350874724677 | -0.002438421960479678 |
| FH | NCC m=10 | brier_scores:Std | Fold_1 | 0.04088101513462203 | 0.04007937347628376 | -0.0008016416583382716 |
| FH | NCC m=10 | brier_scores:Std | Fold_2 | 0.03541530333697079 | 0.03547062236318844 | 5.531902621765117e-05 |
| FH | NCC m=10 | brier_scores:Std | Fold_3 | 0.03574038329399989 | 0.034825555940924395 | -0.0009148273530754925 |
| FH | NCC m=10 | brier_scores:Std | Fold_4 | 0.0372276591353519 | 0.03712201975741837 | -0.00010563937793352934 |
| FH | NCC m=100 | brier_scores:Mean | Fold_0 | 0.06776810810373689 | 0.06652712641665444 | -0.0012409816870824486 |
| FH | NCC m=100 | brier_scores:Mean | Fold_1 | 0.07366981280658154 | 0.07308416616550843 | -0.0005856466410731065 |
| FH | NCC m=100 | brier_scores:Mean | Fold_2 | 0.07721963082576724 | 0.07725925497952335 | 3.962415375610706e-05 |
| FH | NCC m=100 | brier_scores:Mean | Fold_3 | 0.07463738036448263 | 0.07362333270404296 | -0.0010140476604396653 |
| FH | NCC m=100 | brier_scores:Mean | Fold_4 | 0.06966288885591725 | 0.0687004858185217 | -0.0009624030373955456 |
| FH | NCC m=100 | brier_scores:Std | Fold_0 | 0.037538893687876586 | 0.03602769760602305 | -0.0015111960818535372 |
| FH | NCC m=100 | brier_scores:Std | Fold_1 | 0.04163787044248518 | 0.04135483675314231 | -0.0002830336893428695 |
| FH | NCC m=100 | brier_scores:Std | Fold_2 | 0.03625876167557296 | 0.0364024242191708 | 0.00014366254359784308 |
| FH | NCC m=100 | brier_scores:Std | Fold_3 | 0.03704139210312069 | 0.036335635317381806 | -0.0007057567857388855 |
| FH | NCC m=100 | brier_scores:Std | Fold_4 | 0.03715549288792245 | 0.03617553054315896 | -0.0009799623447634895 |
| FH | NCC m=20 | brier_scores:Mean | Fold_0 | 0.06662453576953792 | 0.06755507679325552 | 0.0009305410237176043 |
| FH | NCC m=20 | brier_scores:Mean | Fold_1 | 0.07177328572410037 | 0.07038885172431643 | -0.0013844339997839405 |
| FH | NCC m=20 | brier_scores:Mean | Fold_2 | 0.07810403394008697 | 0.07634842826913618 | -0.0017556056709507883 |
| FH | NCC m=20 | brier_scores:Mean | Fold_3 | 0.07308465498481917 | 0.07305514788971852 | -2.950709510064764e-05 |
| FH | NCC m=20 | brier_scores:Mean | Fold_4 | 0.07039535300665131 | 0.06853870403919764 | -0.0018566489674536751 |
| FH | NCC m=20 | brier_scores:Std | Fold_0 | 0.03708867872142437 | 0.03694680777030905 | -0.00014187095111532072 |
| FH | NCC m=20 | brier_scores:Std | Fold_1 | 0.040040912231460446 | 0.038858563286058495 | -0.001182348945401951 |
| FH | NCC m=20 | brier_scores:Std | Fold_2 | 0.036495494849030884 | 0.03545341036912139 | -0.0010420844799094928 |
| FH | NCC m=20 | brier_scores:Std | Fold_3 | 0.03558122296441361 | 0.035159827904629154 | -0.0004213950597844532 |
| FH | NCC m=20 | brier_scores:Std | Fold_4 | 0.03753616510354678 | 0.03607296069879421 | -0.0014632044047525675 |
| FH | NCC m=5 | brier_scores:Mean | Fold_0 | 0.06967512937637722 | 0.06946264359233552 | -0.00021248578404170493 |
| FH | NCC m=5 | brier_scores:Mean | Fold_1 | 0.0732182504466238 | 0.07094167741095468 | -0.0022765730356691244 |
| FH | NCC m=5 | brier_scores:Mean | Fold_2 | 0.07782411978729419 | 0.07693996333195545 | -0.000884156455338736 |
| FH | NCC m=5 | brier_scores:Mean | Fold_3 | 0.07356752004356001 | 0.07273957112271302 | -0.0008279489208469909 |
| FH | NCC m=5 | brier_scores:Mean | Fold_4 | 0.07121442096747041 | 0.06934392680986173 | -0.0018704941576086764 |
| FH | NCC m=5 | brier_scores:Std | Fold_0 | 0.03833802446573224 | 0.03833762376958476 | -4.006961474845028e-07 |
| FH | NCC m=5 | brier_scores:Std | Fold_1 | 0.04126604727954809 | 0.039352931298531665 | -0.0019131159810164278 |
| FH | NCC m=5 | brier_scores:Std | Fold_2 | 0.036694951273160574 | 0.035868784741500785 | -0.0008261665316597888 |
| FH | NCC m=5 | brier_scores:Std | Fold_3 | 0.035843644394143025 | 0.03520023222433077 | -0.0006434121698122575 |
| FH | NCC m=5 | brier_scores:Std | Fold_4 | 0.03818954880679124 | 0.03674576102908579 | -0.0014437877777054506 |
| FH | NCC m=50 | brier_scores:Mean | Fold_0 | 0.06808364818613816 | 0.06640553665204404 | -0.0016781115340941122 |
| FH | NCC m=50 | brier_scores:Mean | Fold_1 | 0.07365602468013155 | 0.07017715354032475 | -0.0034788711398067995 |
| FH | NCC m=50 | brier_scores:Mean | Fold_2 | 0.07690697311843703 | 0.07703364413825886 | 0.00012667101982183349 |
| FH | NCC m=50 | brier_scores:Mean | Fold_3 | 0.07340700179057924 | 0.07293999469930544 | -0.00046700709127379947 |
| FH | NCC m=50 | brier_scores:Mean | Fold_4 | 0.07006342384194458 | 0.0686188027459629 | -0.001444621095981688 |
| FH | NCC m=50 | brier_scores:Std | Fold_0 | 0.03743403814596665 | 0.035733046977326245 | -0.0017009911686404061 |
| FH | NCC m=50 | brier_scores:Std | Fold_1 | 0.04160800152287876 | 0.03869000271073705 | -0.002917998812141713 |
| FH | NCC m=50 | brier_scores:Std | Fold_2 | 0.03577453556642423 | 0.03589864899440699 | 0.00012411342798276243 |
| FH | NCC m=50 | brier_scores:Std | Fold_3 | 0.03540532380228565 | 0.0349476937696234 | -0.00045763003266224844 |
| FH | NCC m=50 | brier_scores:Std | Fold_4 | 0.037392870609834275 | 0.03617894971104567 | -0.0012139208987886063 |
| FH | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_0 | 0.6808184839445118 | 0.6535054387895148 | -0.027313045154996995 |
| FH | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_1 | 0.677642495179156 | 0.6713753979999103 | -0.006267097179245673 |
| FH | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_2 | 0.6416687826365353 | 0.6658018789812433 | 0.02413309634470806 |
| FH | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_3 | 0.6924679864215373 | 0.6638770320079768 | -0.02859095441356052 |
| FH | SCC a=0.05 | CIndex_scores:CIndex_Score | Fold_4 | 0.5862002165118797 | 0.6794484644749587 | 0.09324824796307896 |
| FH | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.6868414187357508 | 0.7164797023694747 | 0.029638283633723894 |
| FH | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.6311942239562313 | 0.6787636216870712 | 0.0475693977308399 |
| FH | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.6572239211313631 | 0.6508208123116327 | -0.006403108819730385 |
| FH | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.6599110453847791 | 0.6870119539766298 | 0.02710090859185077 |
| FH | SCC a=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.6611816990484872 | 0.6755968320893396 | 0.014415133040852401 |
| FH | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_0 | 0.6758957839456461 | 0.6873064664314962 | 0.011410682485850088 |
| FH | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_1 | 0.6389187855957666 | 0.6421812637337997 | 0.0032624781380330425 |
| FH | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_2 | 0.6247557434782128 | 0.643357878583809 | 0.018602135105596163 |
| FH | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_3 | 0.69350989816153 | 0.6852530277058896 | -0.008256870455640386 |
| FH | SCC a=0.2 | CIndex_scores:CIndex_Score | Fold_4 | 0.6374337644578657 | 0.6869807988148824 | 0.049547034357016684 |
| FH | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_0 | 0.7141544638907478 | 0.657021653074419 | -0.057132810816328816 |
| FH | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_1 | 0.6659267231714426 | 0.7020269967263106 | 0.036100273554868 |
| FH | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_2 | 0.6677007319415772 | 0.641613583422572 | -0.026087148519005177 |
| FH | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_3 | 0.673937642142529 | 0.6927592735746535 | 0.018821631432124453 |
| FH | SCC a=0.3 | CIndex_scores:CIndex_Score | Fold_4 | 0.6511081989630221 | 0.6805652099595465 | 0.029457010996524424 |
| FH | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.6957340380885405 | 0.6794233408572757 | -0.01631069723126477 |
| FH | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.6765886362617157 | 0.6670366384142786 | -0.0095519978474371 |
| FH | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.63746260253254 | 0.6443404245923539 | 0.0068778220598139095 |
| FH | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.678508609776045 | 0.6389831837685835 | -0.03952542600746145 |
| FH | SCC a=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.566212751410176 | 0.6800296279414278 | 0.11381687653125183 |
| FH | SCC a=0.05 | IBS_scores:IBS_Score | Fold_0 | 0.0744008182412086 | 0.07020925940825916 | -0.0041915588329494435 |
| FH | SCC a=0.05 | IBS_scores:IBS_Score | Fold_1 | 0.07484039386197867 | 0.07457558678145167 | -0.0002648070805270075 |
| FH | SCC a=0.05 | IBS_scores:IBS_Score | Fold_2 | 0.09275667340823494 | 0.08020059597759732 | -0.012556077430637622 |
| FH | SCC a=0.05 | IBS_scores:IBS_Score | Fold_3 | 0.07650639173566928 | 0.0746735476633703 | -0.0018328440722989864 |
| FH | SCC a=0.05 | IBS_scores:IBS_Score | Fold_4 | 0.08297429808444205 | 0.07193749194022821 | -0.011036806144213845 |
| FH | SCC a=0.1 | IBS_scores:IBS_Score | Fold_0 | 0.07408679010560687 | 0.06885894802975741 | -0.005227842075849462 |
| FH | SCC a=0.1 | IBS_scores:IBS_Score | Fold_1 | 0.07562805978656324 | 0.07501495896425886 | -0.0006131008223043827 |
| FH | SCC a=0.1 | IBS_scores:IBS_Score | Fold_2 | 0.07909887649351476 | 0.08019420526105289 | 0.0010953287675381368 |
| FH | SCC a=0.1 | IBS_scores:IBS_Score | Fold_3 | 0.07717851178656332 | 0.0750458041009132 | -0.0021327076856501176 |
| FH | SCC a=0.1 | IBS_scores:IBS_Score | Fold_4 | 0.0731428238454413 | 0.07254594499283624 | -0.0005968788526050511 |
| FH | SCC a=0.2 | IBS_scores:IBS_Score | Fold_0 | 0.07720178393735162 | 0.06956623649400187 | -0.007635547443349752 |
| FH | SCC a=0.2 | IBS_scores:IBS_Score | Fold_1 | 0.0761893352772644 | 0.07480810482258601 | -0.0013812304546783893 |
| FH | SCC a=0.2 | IBS_scores:IBS_Score | Fold_2 | 0.08033767973618196 | 0.08114802772005207 | 0.0008103479838701133 |
| FH | SCC a=0.2 | IBS_scores:IBS_Score | Fold_3 | 0.07502746690235071 | 0.07416839240095618 | -0.0008590745013945245 |
| FH | SCC a=0.2 | IBS_scores:IBS_Score | Fold_4 | 0.07363885962383442 | 0.0712385273158538 | -0.0024003323079806183 |
| FH | SCC a=0.3 | IBS_scores:IBS_Score | Fold_0 | 0.07135916202811833 | 0.0706173710208 | -0.000741791007318332 |
| FH | SCC a=0.3 | IBS_scores:IBS_Score | Fold_1 | 0.07623371193370225 | 0.0740122604645588 | -0.0022214514691434456 |
| FH | SCC a=0.3 | IBS_scores:IBS_Score | Fold_2 | 0.08341792509883632 | 0.08075291513930187 | -0.002665009959534448 |
| FH | SCC a=0.3 | IBS_scores:IBS_Score | Fold_3 | 0.07568405947610755 | 0.07541075307856185 | -0.0002733063975457056 |
| FH | SCC a=0.3 | IBS_scores:IBS_Score | Fold_4 | 0.07237214294433923 | 0.07192885975577824 | -0.0004432831885609889 |
| FH | SCC a=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.07163130111670321 | 0.06995399107646431 | -0.0016773100402388968 |
| FH | SCC a=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.07518951473371156 | 0.07538060862204846 | 0.00019109388833689345 |
| FH | SCC a=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.08344236876708026 | 0.08155515521561364 | -0.001887213551466621 |
| FH | SCC a=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.07588804835278777 | 0.07734873395798998 | 0.001460685605202211 |
| FH | SCC a=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.07404782008144795 | 0.07137326443326936 | -0.0026745556481785893 |
| FH | SCC a=0.05 | Training_Durations:Training_Duration | Fold_0 | 18.76425313949585 | 33.44065570831299 | 14.676402568817139 |
| FH | SCC a=0.05 | Training_Durations:Training_Duration | Fold_1 | 20.80180048942566 | 19.764665365219116 | -1.037135124206543 |
| FH | SCC a=0.05 | Training_Durations:Training_Duration | Fold_2 | 21.779206037521362 | 45.08635425567627 | 23.307148218154907 |
| FH | SCC a=0.05 | Training_Durations:Training_Duration | Fold_3 | 33.99359750747681 | 30.419124126434326 | -3.5744733810424805 |
| FH | SCC a=0.05 | Training_Durations:Training_Duration | Fold_4 | 21.790340662002563 | 26.85366129875183 | 5.063320636749268 |
| FH | SCC a=0.1 | Training_Durations:Training_Duration | Fold_0 | 18.78024411201477 | 24.884435653686523 | 6.104191541671753 |
| FH | SCC a=0.1 | Training_Durations:Training_Duration | Fold_1 | 31.948872327804565 | 34.882911920547485 | 2.93403959274292 |
| FH | SCC a=0.1 | Training_Durations:Training_Duration | Fold_2 | 19.78130340576172 | 26.314969778060913 | 6.533666372299194 |
| FH | SCC a=0.1 | Training_Durations:Training_Duration | Fold_3 | 20.2626953125 | 24.818367958068848 | 4.555672645568848 |
| FH | SCC a=0.1 | Training_Durations:Training_Duration | Fold_4 | 32.98888564109802 | 43.2157244682312 | 10.226838827133179 |
| FH | SCC a=0.2 | Training_Durations:Training_Duration | Fold_0 | 17.750938653945923 | 21.36623477935791 | 3.6152961254119873 |
| FH | SCC a=0.2 | Training_Durations:Training_Duration | Fold_1 | 29.54829168319702 | 17.281676530838013 | -12.266615152359009 |
| FH | SCC a=0.2 | Training_Durations:Training_Duration | Fold_2 | 23.790448427200317 | 20.795992136001587 | -2.9944562911987305 |
| FH | SCC a=0.2 | Training_Durations:Training_Duration | Fold_3 | 24.394054651260376 | 18.857481718063354 | -5.5365729331970215 |
| FH | SCC a=0.2 | Training_Durations:Training_Duration | Fold_4 | 29.423611402511597 | 21.783088445663452 | -7.6405229568481445 |
| FH | SCC a=0.3 | Training_Durations:Training_Duration | Fold_0 | 18.22580599784851 | 21.320642471313477 | 3.094836473464966 |
| FH | SCC a=0.3 | Training_Durations:Training_Duration | Fold_1 | 28.41695261001587 | 17.199193477630615 | -11.217759132385254 |
| FH | SCC a=0.3 | Training_Durations:Training_Duration | Fold_2 | 17.228925704956055 | 20.24661087989807 | 3.0176851749420166 |
| FH | SCC a=0.3 | Training_Durations:Training_Duration | Fold_3 | 25.907052040100098 | 88.50610160827637 | 62.59904956817627 |
| FH | SCC a=0.3 | Training_Durations:Training_Duration | Fold_4 | 22.82603430747986 | 19.9318950176239 | -2.894139289855957 |
| FH | SCC a=0.5 | Training_Durations:Training_Duration | Fold_0 | 29.62209963798523 | 20.65381693840027 | -8.968282699584961 |
| FH | SCC a=0.5 | Training_Durations:Training_Duration | Fold_1 | 22.295106887817383 | 19.922934770584106 | -2.3721721172332764 |
| FH | SCC a=0.5 | Training_Durations:Training_Duration | Fold_2 | 17.919983863830566 | 16.861229419708252 | -1.0587544441223145 |
| FH | SCC a=0.5 | Training_Durations:Training_Duration | Fold_3 | 17.763690948486328 | 19.37794780731201 | 1.6142568588256836 |
| FH | SCC a=0.5 | Training_Durations:Training_Duration | Fold_4 | 25.4009747505188 | 58.28795075416565 | 32.88697600364685 |
| FH | SCC a=0.05 | brier_scores:Mean | Fold_0 | 0.07241957432866719 | 0.06830628350411043 | -0.004113290824556762 |
| FH | SCC a=0.05 | brier_scores:Mean | Fold_1 | 0.0724628176098643 | 0.07221298978170462 | -0.00024982782815967386 |
| FH | SCC a=0.05 | brier_scores:Mean | Fold_2 | 0.09018476358095744 | 0.07809186542540207 | -0.012092898155555365 |
| FH | SCC a=0.05 | brier_scores:Mean | Fold_3 | 0.0743550222172116 | 0.07260387937883632 | -0.001751142838375283 |
| FH | SCC a=0.05 | brier_scores:Mean | Fold_4 | 0.0804790242428911 | 0.06976085510753013 | -0.010718169135360972 |
| FH | SCC a=0.05 | brier_scores:Std | Fold_0 | 0.03899756375769773 | 0.0372902412573739 | -0.0017073225003238282 |
| FH | SCC a=0.05 | brier_scores:Std | Fold_1 | 0.040637834658394906 | 0.039697718930595136 | -0.0009401157277997702 |
| FH | SCC a=0.05 | brier_scores:Std | Fold_2 | 0.04687033234713622 | 0.03684339937671722 | -0.010026932970419004 |
| FH | SCC a=0.05 | brier_scores:Std | Fold_3 | 0.03625173227413279 | 0.03520760361904775 | -0.00104412865508504 |
| FH | SCC a=0.05 | brier_scores:Std | Fold_4 | 0.04412409003273423 | 0.03718134415995619 | -0.0069427458727780375 |
| FH | SCC a=0.1 | brier_scores:Mean | Fold_0 | 0.07213180164346614 | 0.06698712042696654 | -0.005144681216499594 |
| FH | SCC a=0.1 | brier_scores:Mean | Fold_1 | 0.07320232011460344 | 0.07262375069841441 | -0.0005785694161890287 |
| FH | SCC a=0.1 | brier_scores:Mean | Fold_2 | 0.07701408998661599 | 0.07808726469033175 | 0.0010731747037157624 |
| FH | SCC a=0.1 | brier_scores:Mean | Fold_3 | 0.0750131221614762 | 0.07294976508580284 | -0.0020633570756733582 |
| FH | SCC a=0.1 | brier_scores:Mean | Fold_4 | 0.07089283696633969 | 0.0703260560106358 | -0.0005667809557038939 |
| FH | SCC a=0.1 | brier_scores:Std | Fold_0 | 0.03862419039428912 | 0.03639424079851276 | -0.0022299495957763607 |
| FH | SCC a=0.1 | brier_scores:Std | Fold_1 | 0.041265823930093135 | 0.040832619720939156 | -0.0004332042091539784 |
| FH | SCC a=0.1 | brier_scores:Std | Fold_2 | 0.03639486381667724 | 0.03710195001257091 | 0.0007070861958936719 |
| FH | SCC a=0.1 | brier_scores:Std | Fold_3 | 0.03675317046948863 | 0.03545472859116239 | -0.0012984418783262425 |
| FH | SCC a=0.1 | brier_scores:Std | Fold_4 | 0.03804525322269785 | 0.03766805096724105 | -0.0003772022554567947 |
| FH | SCC a=0.2 | brier_scores:Mean | Fold_0 | 0.07517751209485239 | 0.06767138885413573 | -0.007506123240716658 |
| FH | SCC a=0.2 | brier_scores:Mean | Fold_1 | 0.07374718476635288 | 0.07243919271199874 | -0.0013079920543541401 |
| FH | SCC a=0.2 | brier_scores:Mean | Fold_2 | 0.07821040459450795 | 0.07899812132298673 | 0.0007877167284787712 |
| FH | SCC a=0.2 | brier_scores:Mean | Fold_3 | 0.0729210394106598 | 0.0720958227532031 | -0.0008252166574567038 |
| FH | SCC a=0.2 | brier_scores:Mean | Fold_4 | 0.07137384013505903 | 0.06907972542809387 | -0.002294114706965153 |
| FH | SCC a=0.2 | brier_scores:Std | Fold_0 | 0.04067246742609308 | 0.036855356879225115 | -0.003817110546867966 |
| FH | SCC a=0.2 | brier_scores:Std | Fold_1 | 0.04155729697528007 | 0.04013884407616241 | -0.0014184528991176629 |
| FH | SCC a=0.2 | brier_scores:Std | Fold_2 | 0.03726489949383154 | 0.037618698372301876 | 0.0003537988784703336 |
| FH | SCC a=0.2 | brier_scores:Std | Fold_3 | 0.03525520948680942 | 0.03467194686859886 | -0.0005832626182105602 |
| FH | SCC a=0.2 | brier_scores:Std | Fold_4 | 0.03845781087855284 | 0.03659182298935363 | -0.0018659878891992068 |
| FH | SCC a=0.3 | brier_scores:Mean | Fold_0 | 0.06942586549167488 | 0.06869228572008229 | -0.0007335797715925935 |
| FH | SCC a=0.3 | brier_scores:Mean | Fold_1 | 0.0737944519260482 | 0.07165819456188717 | -0.0021362573641610233 |
| FH | SCC a=0.3 | brier_scores:Mean | Fold_2 | 0.08116261482341428 | 0.07860787994267535 | -0.002554734880738929 |
| FH | SCC a=0.3 | brier_scores:Mean | Fold_3 | 0.07355644974869058 | 0.07330511106430274 | -0.0002513386843878418 |
| FH | SCC a=0.3 | brier_scores:Mean | Fold_4 | 0.07014592928130023 | 0.06973129752502265 | -0.00041463175627758087 |
| FH | SCC a=0.3 | brier_scores:Std | Fold_0 | 0.037310580050029865 | 0.037777652537093774 | 0.00046707248706390897 |
| FH | SCC a=0.3 | brier_scores:Std | Fold_1 | 0.04162084764987661 | 0.03999495710236171 | -0.0016258905475149063 |
| FH | SCC a=0.3 | brier_scores:Std | Fold_2 | 0.03940979226836774 | 0.03767553722609593 | -0.001734255042271808 |
| FH | SCC a=0.3 | brier_scores:Std | Fold_3 | 0.03574906607848732 | 0.03531096606348358 | -0.00043810001500373813 |
| FH | SCC a=0.3 | brier_scores:Std | Fold_4 | 0.03750719830025971 | 0.03704246739463597 | -0.0004647309056237392 |
| FH | SCC a=0.5 | brier_scores:Mean | Fold_0 | 0.06967874542234678 | 0.06805653344612163 | -0.0016222119762251547 |
| FH | SCC a=0.5 | brier_scores:Mean | Fold_1 | 0.07277955958324403 | 0.072965324579679 | 0.00018576499643496724 |
| FH | SCC a=0.5 | brier_scores:Mean | Fold_2 | 0.08122417770881782 | 0.07937561677165667 | -0.0018485609371611533 |
| FH | SCC a=0.5 | brier_scores:Mean | Fold_3 | 0.07373746938620276 | 0.07518020323384449 | 0.0014427338476417223 |
| FH | SCC a=0.5 | brier_scores:Mean | Fold_4 | 0.07175321292986385 | 0.06920920826923967 | -0.002544004660624183 |
| FH | SCC a=0.5 | brier_scores:Std | Fold_0 | 0.03860003394839988 | 0.03709870455131912 | -0.0015013293970807598 |
| FH | SCC a=0.5 | brier_scores:Std | Fold_1 | 0.04090032924760915 | 0.04103541369999208 | 0.00013508445238293032 |
| FH | SCC a=0.5 | brier_scores:Std | Fold_2 | 0.03815513456901077 | 0.037941859547262306 | -0.00021327502174846302 |
| FH | SCC a=0.5 | brier_scores:Std | Fold_3 | 0.03585257578258752 | 0.03685818657874641 | 0.0010056107961588928 |
| FH | SCC a=0.5 | brier_scores:Std | Fold_4 | 0.03875337617158111 | 0.036725610798010046 | -0.002027765373571064 |
| FH | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_0 | 0.6568061431666345 | 0.6531197894808479 | -0.0036863536857866253 |
| FH | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_1 | 0.6947957307502579 | 0.6563410915287681 | -0.03845463922148984 |
| FH | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_2 | 0.6499707444165995 | 0.6584714233669312 | 0.008500678950331686 |
| FH | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_3 | 0.6460076854995015 | 0.6953472478965707 | 0.04933956239706916 |
| FH | Entropy t=0.1 | CIndex_scores:CIndex_Score | Fold_4 | 0.591613013503504 | 0.6440316791066036 | 0.0524186656030996 |
| FH | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_0 | 0.6550480360241825 | 0.6968909860145412 | 0.04184294999035876 |
| FH | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_1 | 0.6871384367011973 | 0.6313511816673394 | -0.05578725503385795 |
| FH | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_2 | 0.6057672138748744 | 0.6760247734072267 | 0.07025755953235224 |
| FH | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_3 | 0.673780795213928 | 0.7111775843332325 | 0.03739678911930455 |
| FH | Entropy t=0.5 | CIndex_scores:CIndex_Score | Fold_4 | 0.5970258104951285 | 0.6362486468007521 | 0.03922283630562362 |
| FH | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_0 | 0.6492746390209044 | 0.7031974864739177 | 0.053922847453013234 |
| FH | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_1 | 0.666913314498408 | 0.6934503789407597 | 0.02653706444235171 |
| FH | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_2 | 0.6483037281549111 | 0.6752851039401199 | 0.02698137578520876 |
| FH | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_3 | 0.6938908121309896 | 0.6798866220773255 | -0.014004190053664045 |
| FH | Entropy t=10 | CIndex_scores:CIndex_Score | Fold_4 | 0.6659563557632043 | 0.6760640419349325 | 0.010107686171728192 |
| FH | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_0 | 0.6467906037680206 | 0.6848451164320634 | 0.038054512664042806 |
| FH | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_1 | 0.6740548903538275 | 0.6488183326606575 | -0.025236557693170014 |
| FH | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_2 | 0.6516819200494585 | 0.6760578929356046 | 0.024375972886146124 |
| FH | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_3 | 0.695111977503669 | 0.6938908121309896 | -0.001221165372679467 |
| FH | Entropy t=1 | CIndex_scores:CIndex_Score | Fold_4 | 0.6563614608854197 | 0.6908096404763261 | 0.0344481795909064 |
| FH | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_0 | 0.6509873756564545 | 0.7005886823270533 | 0.04960130667059881 |
| FH | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_1 | 0.6700636799856495 | 0.692878604421723 | 0.02281492443607347 |
| FH | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_2 | 0.655667303297601 | 0.6763449288482132 | 0.020677625550612144 |
| FH | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_3 | 0.6854322813385765 | 0.6794160812915224 | -0.006016200047054054 |
| FH | Entropy t=5 | CIndex_scores:CIndex_Score | Fold_4 | 0.6794142783886958 | 0.6786279984046493 | -0.0007862799840465673 |
| FH | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_0 | 0.08259236957086577 | 0.08250248586851879 | -8.988370234698506e-05 |
| FH | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_1 | 0.0768305472835327 | 0.08313756567796804 | 0.006307018394435343 |
| FH | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_2 | 0.08808237459045186 | 0.08428614893289442 | -0.0037962256575574393 |
| FH | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_3 | 0.0871761138548305 | 0.0835627366511448 | -0.0036133772036856943 |
| FH | Entropy t=0.1 | IBS_scores:IBS_Score | Fold_4 | 0.08989558670409052 | 0.0829435228980437 | -0.006952063806046821 |
| FH | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_0 | 0.0694138771833413 | 0.06879915682449991 | -0.0006147203588413863 |
| FH | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_1 | 0.07589632792857372 | 0.07497190283117013 | -0.0009244250974035917 |
| FH | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_2 | 0.0851985301790574 | 0.07956721542371128 | -0.005631314755346117 |
| FH | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_3 | 0.07597735344054778 | 0.07352910718047989 | -0.002448246260067885 |
| FH | Entropy t=0.5 | IBS_scores:IBS_Score | Fold_4 | 0.08043552923557017 | 0.0725705690962467 | -0.00786496013932346 |
| FH | Entropy t=10 | IBS_scores:IBS_Score | Fold_0 | 0.06944257270857826 | 0.06924337768145793 | -0.000199195027120333 |
| FH | Entropy t=10 | IBS_scores:IBS_Score | Fold_1 | 0.07649224480499076 | 0.07288429774320664 | -0.0036079470617841197 |
| FH | Entropy t=10 | IBS_scores:IBS_Score | Fold_2 | 0.0801762050583546 | 0.07916896793271713 | -0.0010072371256374668 |
| FH | Entropy t=10 | IBS_scores:IBS_Score | Fold_3 | 0.07904664463599152 | 0.07642396853504349 | -0.002622676100948032 |
| FH | Entropy t=10 | IBS_scores:IBS_Score | Fold_4 | 0.07212724477182353 | 0.07157097072386424 | -0.0005562740479592848 |
| FH | Entropy t=1 | IBS_scores:IBS_Score | Fold_0 | 0.06956975886940493 | 0.0701025300239099 | 0.0005327711545049657 |
| FH | Entropy t=1 | IBS_scores:IBS_Score | Fold_1 | 0.07654739741326924 | 0.07543814932193192 | -0.0011092480913373198 |
| FH | Entropy t=1 | IBS_scores:IBS_Score | Fold_2 | 0.07967227306223483 | 0.07933370727394361 | -0.00033856578829122297 |
| FH | Entropy t=1 | IBS_scores:IBS_Score | Fold_3 | 0.07770179375754488 | 0.07325300226771891 | -0.004448791489825965 |
| FH | Entropy t=1 | IBS_scores:IBS_Score | Fold_4 | 0.07271918674650683 | 0.070511368884282 | -0.002207817862224834 |
| FH | Entropy t=5 | IBS_scores:IBS_Score | Fold_0 | 0.0694168230879127 | 0.06933676458529488 | -8.005850261781633e-05 |
| FH | Entropy t=5 | IBS_scores:IBS_Score | Fold_1 | 0.07631570465854409 | 0.0728292918778738 | -0.0034864127806702866 |
| FH | Entropy t=5 | IBS_scores:IBS_Score | Fold_2 | 0.07960374496825158 | 0.07918860453825753 | -0.00041514042999404865 |
| FH | Entropy t=5 | IBS_scores:IBS_Score | Fold_3 | 0.07619724186464293 | 0.07637677960150581 | 0.00017953773686288366 |
| FH | Entropy t=5 | IBS_scores:IBS_Score | Fold_4 | 0.07546596768693943 | 0.07153285825037214 | -0.003933109436567286 |
| FH | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_0 | 44.53211569786072 | 32.71199941635132 | -11.8201162815094 |
| FH | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_1 | 15.676351547241211 | 37.43450689315796 | 21.758155345916748 |
| FH | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_2 | 54.30773591995239 | 28.11901021003723 | -26.18872570991516 |
| FH | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_3 | 48.1167848110199 | 25.81624484062195 | -22.30053997039795 |
| FH | Entropy t=0.1 | Training_Durations:Training_Duration | Fold_4 | 28.54445481300354 | 26.802467584609985 | -1.7419872283935547 |
| FH | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_0 | 18.21902847290039 | 17.366647481918335 | -0.8523809909820557 |
| FH | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_1 | 17.72476291656494 | 15.698694229125977 | -2.026068687438965 |
| FH | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_2 | 18.448716163635254 | 32.68498635292053 | 14.236270189285278 |
| FH | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_3 | 24.317770957946777 | 15.300508499145508 | -9.01726245880127 |
| FH | Entropy t=0.5 | Training_Durations:Training_Duration | Fold_4 | 17.306368112564087 | 16.89270257949829 | -0.4136655330657959 |
| FH | Entropy t=10 | Training_Durations:Training_Duration | Fold_0 | 18.19969868659973 | 39.537036418914795 | 21.337337732315063 |
| FH | Entropy t=10 | Training_Durations:Training_Duration | Fold_1 | 17.216683864593506 | 55.22271251678467 | 38.00602865219116 |
| FH | Entropy t=10 | Training_Durations:Training_Duration | Fold_2 | 30.395769357681274 | 36.83344650268555 | 6.4376771450042725 |
| FH | Entropy t=10 | Training_Durations:Training_Duration | Fold_3 | 16.670929193496704 | 37.6377272605896 | 20.966798067092896 |
| FH | Entropy t=10 | Training_Durations:Training_Duration | Fold_4 | 60.73770546913147 | 79.78844332695007 | 19.050737857818604 |
| FH | Entropy t=1 | Training_Durations:Training_Duration | Fold_0 | 18.24106216430664 | 23.30670666694641 | 5.0656445026397705 |
| FH | Entropy t=1 | Training_Durations:Training_Duration | Fold_1 | 17.178895473480225 | 30.932528495788574 | 13.75363302230835 |
| FH | Entropy t=1 | Training_Durations:Training_Duration | Fold_2 | 30.401188850402832 | 40.98834204673767 | 10.587153196334839 |
| FH | Entropy t=1 | Training_Durations:Training_Duration | Fold_3 | 16.207640171051025 | 15.88179063796997 | -0.3258495330810547 |
| FH | Entropy t=1 | Training_Durations:Training_Duration | Fold_4 | 27.853935956954956 | 91.05814409255981 | 63.20420813560486 |
| FH | Entropy t=5 | Training_Durations:Training_Duration | Fold_0 | 17.738698720932007 | 39.551098108291626 | 21.81239938735962 |
| FH | Entropy t=5 | Training_Durations:Training_Duration | Fold_1 | 17.298797130584717 | 55.24093818664551 | 37.94214105606079 |
| FH | Entropy t=5 | Training_Durations:Training_Duration | Fold_2 | 43.6190459728241 | 37.33978509902954 | -6.279260873794556 |
| FH | Entropy t=5 | Training_Durations:Training_Duration | Fold_3 | 44.06750702857971 | 39.04016089439392 | -5.027346134185791 |
| FH | Entropy t=5 | Training_Durations:Training_Duration | Fold_4 | 16.402400016784668 | 81.47686076164246 | 65.07446074485779 |
| FH | Entropy t=0.1 | brier_scores:Mean | Fold_0 | 0.0802918036648369 | 0.08021749152023172 | -7.431214460518198e-05 |
| FH | Entropy t=0.1 | brier_scores:Mean | Fold_1 | 0.07442828740384191 | 0.08039805010087019 | 0.005969762697028272 |
| FH | Entropy t=0.1 | brier_scores:Mean | Fold_2 | 0.0857511340848224 | 0.08200267058120762 | -0.0037484635036147823 |
| FH | Entropy t=0.1 | brier_scores:Mean | Fold_3 | 0.08465690925847852 | 0.08105606945762389 | -0.003600839800854627 |
| FH | Entropy t=0.1 | brier_scores:Mean | Fold_4 | 0.08717698702264359 | 0.08038077728384428 | -0.006796209738799311 |
| FH | Entropy t=0.1 | brier_scores:Std | Fold_0 | 0.04743229422091182 | 0.04723774829246015 | -0.000194545928451674 |
| FH | Entropy t=0.1 | brier_scores:Std | Fold_1 | 0.04127979897407757 | 0.047049077940512676 | 0.005769278966435108 |
| FH | Entropy t=0.1 | brier_scores:Std | Fold_2 | 0.04202911678039811 | 0.04041493871795665 | -0.0016141780624414626 |
| FH | Entropy t=0.1 | brier_scores:Std | Fold_3 | 0.04449640115383544 | 0.04202405402322118 | -0.002472347130614262 |
| FH | Entropy t=0.1 | brier_scores:Std | Fold_4 | 0.04796476318993027 | 0.045236108887529956 | -0.002728654302400317 |
| FH | Entropy t=0.5 | brier_scores:Mean | Fold_0 | 0.06751428640671978 | 0.06692464156986222 | -0.0005896448368575558 |
| FH | Entropy t=0.5 | brier_scores:Mean | Fold_1 | 0.07351536585128515 | 0.07255562113536075 | -0.0009597447159244016 |
| FH | Entropy t=0.5 | brier_scores:Mean | Fold_2 | 0.0829000618592457 | 0.07748625725095548 | -0.005413804608290218 |
| FH | Entropy t=0.5 | brier_scores:Mean | Fold_3 | 0.07378421389005674 | 0.07144079623061116 | -0.002343417659445582 |
| FH | Entropy t=0.5 | brier_scores:Mean | Fold_4 | 0.07798413381358704 | 0.07034213560180942 | -0.00764199821177762 |
| FH | Entropy t=0.5 | brier_scores:Std | Fold_0 | 0.037418169534890834 | 0.03647755491962747 | -0.0009406146152633674 |
| FH | Entropy t=0.5 | brier_scores:Std | Fold_1 | 0.039562458839695606 | 0.04060050890971708 | 0.0010380500700214734 |
| FH | Entropy t=0.5 | brier_scores:Std | Fold_2 | 0.04032454317912555 | 0.03632783426710429 | -0.003996708912021259 |
| FH | Entropy t=0.5 | brier_scores:Std | Fold_3 | 0.03642738119030386 | 0.03455266140460681 | -0.001874719785697046 |
| FH | Entropy t=0.5 | brier_scores:Std | Fold_4 | 0.04312301275141295 | 0.037624578385807586 | -0.005498434365605362 |
| FH | Entropy t=10 | brier_scores:Mean | Fold_0 | 0.06754381271765303 | 0.0673221525143442 | -0.00022166020330882663 |
| FH | Entropy t=10 | brier_scores:Mean | Fold_1 | 0.07407307580739367 | 0.07056773968611398 | -0.0035053361212796924 |
| FH | Entropy t=10 | brier_scores:Mean | Fold_2 | 0.07807024250565896 | 0.07710691171107331 | -0.0009633307945856456 |
| FH | Entropy t=10 | brier_scores:Mean | Fold_3 | 0.07677259330618207 | 0.07425134496369222 | -0.0025212483424898458 |
| FH | Entropy t=10 | brier_scores:Mean | Fold_4 | 0.06993219152481858 | 0.0693993213290372 | -0.000532870195781382 |
| FH | Entropy t=10 | brier_scores:Std | Fold_0 | 0.037498111752001184 | 0.03691502069467337 | -0.000583091057327817 |
| FH | Entropy t=10 | brier_scores:Std | Fold_1 | 0.040317024954337186 | 0.038976365069561654 | -0.0013406598847755316 |
| FH | Entropy t=10 | brier_scores:Std | Fold_2 | 0.03690009055560581 | 0.03607347700177402 | -0.0008266135538317898 |
| FH | Entropy t=10 | brier_scores:Std | Fold_3 | 0.038581529608515255 | 0.03618882571405397 | -0.002392703894461286 |
| FH | Entropy t=10 | brier_scores:Std | Fold_4 | 0.03722215500766154 | 0.03688840945337595 | -0.00033374555428558605 |
| FH | Entropy t=1 | brier_scores:Mean | Fold_0 | 0.06766661764425304 | 0.06815631620747119 | 0.0004896985632181494 |
| FH | Entropy t=1 | brier_scores:Mean | Fold_1 | 0.07414405421736052 | 0.07301137944229978 | -0.001132674775060738 |
| FH | Entropy t=1 | brier_scores:Mean | Fold_2 | 0.07758041355916108 | 0.07727081742731211 | -0.0003095961318489715 |
| FH | Entropy t=1 | brier_scores:Mean | Fold_3 | 0.07547723822962044 | 0.07118435034838956 | -0.004292887881230875 |
| FH | Entropy t=1 | brier_scores:Mean | Fold_4 | 0.07050468560641689 | 0.06839082759784613 | -0.0021138580085707515 |
| FH | Entropy t=1 | brier_scores:Std | Fold_0 | 0.03758430107551237 | 0.037739295031122465 | 0.0001549939556100971 |
| FH | Entropy t=1 | brier_scores:Std | Fold_1 | 0.039970381820866124 | 0.041058572924222596 | 0.0010881911033564715 |
| FH | Entropy t=1 | brier_scores:Std | Fold_2 | 0.03659146703408074 | 0.03611316932427905 | -0.00047829770980169217 |
| FH | Entropy t=1 | brier_scores:Std | Fold_3 | 0.03764822036927298 | 0.03465800784410039 | -0.002990212525172592 |
| FH | Entropy t=1 | brier_scores:Std | Fold_4 | 0.0375056751509462 | 0.036037865537666934 | -0.0014678096132792681 |
| FH | Entropy t=5 | brier_scores:Mean | Fold_0 | 0.06751459133891244 | 0.06741329564758072 | -0.00010129569133171534 |
| FH | Entropy t=5 | brier_scores:Mean | Fold_1 | 0.07390032936990289 | 0.07051334926835408 | -0.003386980101548809 |
| FH | Entropy t=5 | brier_scores:Mean | Fold_2 | 0.07752518742727017 | 0.07712626021853405 | -0.000398927208736119 |
| FH | Entropy t=5 | brier_scores:Mean | Fold_3 | 0.07403313231132475 | 0.07420482285522682 | 0.00017169054390207827 |
| FH | Entropy t=5 | brier_scores:Mean | Fold_4 | 0.07320538710654653 | 0.06936234581242791 | -0.0038430412941186237 |
| FH | Entropy t=5 | brier_scores:Std | Fold_0 | 0.03750835648738975 | 0.03700725287192086 | -0.0005011036154688939 |
| FH | Entropy t=5 | brier_scores:Std | Fold_1 | 0.040260562915148436 | 0.038928565749206855 | -0.0013319971659415814 |
| FH | Entropy t=5 | brier_scores:Std | Fold_2 | 0.03639675641093002 | 0.03608081990489992 | -0.00031593650603010254 |
| FH | Entropy t=5 | brier_scores:Std | Fold_3 | 0.03601448917813836 | 0.036164295023903954 | 0.00014980584576559236 |
| FH | Entropy t=5 | brier_scores:Std | Fold_4 | 0.03898887082813909 | 0.03685247852144064 | -0.0021363923066984453 |

## Coverage notes

PBC Entropy t=0.1 IBS_Score: only 1/5 old and 2/5 new folds populated

PBC Entropy t=0.1 Mean: only 1/5 old and 2/5 new folds populated

PBC Entropy t=0.1 Std: only 1/5 old and 2/5 new folds populated

Missing old raw: C:\Users\micha\OneDrive\Documents\#Msc Data Science\Research_2026\Code\Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling\Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_30\brier_raw_fold_0.csv

Missing old raw: C:\Users\micha\OneDrive\Documents\#Msc Data Science\Research_2026\Code\Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling\Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_30\brier_raw_fold_1.csv

Missing old raw: C:\Users\micha\OneDrive\Documents\#Msc Data Science\Research_2026\Code\Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling\Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_30\brier_raw_fold_2.csv

Missing old raw: C:\Users\micha\OneDrive\Documents\#Msc Data Science\Research_2026\Code\Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling\Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_30\brier_raw_fold_3.csv

Missing old raw: C:\Users\micha\OneDrive\Documents\#Msc Data Science\Research_2026\Code\Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling\Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_30\brier_raw_fold_4.csv

PBC entropy t=0.1 has fold CSVs but neither old nor new pooled CSV.

Archived raw Brier folders with 1.0/5.0/10.0 aliases are separate historical outputs; exact current spelling is preferred, and they are not averaged.

## Interpretation of the differences

- Pooled and fold-level changes tell different stories. FULL mean fold IBS changes from 0.165930 to 0.162772 (synthetic), 0.117625 to 0.112406 (PBC), and 0.074804 to 0.074004 (FH). These are much smaller than the pooled IBS changes. The CSVs support reporting these differences, but not assigning their entire magnitude to a model improvement. Review old versus new pooling and evaluation code before making that claim.
- Synthetic SCC is competitive with FULL, even at 5% retention. Entropy tau=0.5 remains fast (31.72 versus FULL 68.86 seconds per fold), but no longer has the highest synthetic truth correlation. Tau=0.1 deteriorates strongly in both pooled and fold-level C-index.
- PBC SCC at 5% improves markedly, but still trails the new FULL baseline. Entropy tau=10 has the strongest pooled C-index, IBS and Brier among configurations with complete pooled outputs. Its duration is only about 5% below FULL; tau=5 is about 18% below FULL. Fast low-temperature runs are less accurate.
- FH NCC m=50 has the strongest pooled metrics but takes 87.73 seconds per fold versus FULL 27.61. Entropy tau=0.5 takes 19.59 seconds and has pooled metrics close to FULL. SCC at 20% takes 20.02 seconds and also remains close to FULL.
- Durations include convergence and run conditions, so they are not isolated per-epoch speed measurements. FH FULL's new fold_2 takes 66.52 seconds while the other four folds take 16.76–19.29 seconds; its mean is sensitive to that fold.
- The five-fold results are descriptive, not repeated-seed significance estimates. Small differences should not be presented as established superiority.

## Source files

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\FULL\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\FULL\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\FULL\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\FULL\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\FULL\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\FULL\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/brier_scores_cause_1.csv>)

- [Results\FULL\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/CIndex_scores_cause_1.csv>)

- [Results\FULL\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/IBS_scores_cause_1.csv>)

- [Results\FULL\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\FULL\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/Training_Durations_cause_1.csv>)

- [Results\FULL\Metrics\truth_comparison_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL/Metrics/truth_comparison_metrics_cause_1.csv>)

- [Results\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\FULL_FH\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/brier_scores_cause_1.csv>)

- [Results\FULL_FH\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/CIndex_scores_cause_1.csv>)

- [Results\FULL_FH\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/IBS_scores_cause_1.csv>)

- [Results\FULL_FH\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\FULL_FH\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_FH/Metrics/Training_Durations_cause_1.csv>)

- [Results\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\FULL_PBC\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/brier_scores_cause_1.csv>)

- [Results\FULL_PBC\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/CIndex_scores_cause_1.csv>)

- [Results\FULL_PBC\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/IBS_scores_cause_1.csv>)

- [Results\FULL_PBC\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\FULL_PBC\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/FULL_PBC/Metrics/Training_Durations_cause_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\NCC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\NCC\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_1test_old\Metrics\truth_comparison_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_1test_old/Metrics/truth_comparison_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_FH\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_FH/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_0.5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_10_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_10_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_1_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_1_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Brier_Raw_cause_1_Entropy_tau_5_compression_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Brier_Raw_cause_1_Entropy_tau_5_compression_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/brier_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/CIndex_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/IBS_scores_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_0.1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC\Metrics\Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC/Metrics/Training_Durations_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC_IND\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC_IND/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_0.5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC_IND\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC_IND/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_10_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC_IND\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC_IND/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_1_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\ENTROPY_PBC_IND\Metrics\pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/ENTROPY_PBC_IND/Metrics/pooled_oof_metrics_cause_1_Entropy_tau_5_compression_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/brier_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/CIndex_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/IBS_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/Training_Durations_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_1test_old\Metrics\truth_comparison_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_1test_old/Metrics/truth_comparison_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/brier_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/CIndex_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/IBS_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_FH\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_FH/Metrics/Training_Durations_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Brier_Raw_cause_1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Brier_Raw_cause_1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\brier_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/brier_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\CIndex_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/CIndex_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\IBS_scores_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/IBS_scores_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC\Metrics\Training_Durations_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC/Metrics/Training_Durations_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\FULL_PBC_IND\Metrics\pooled_oof_metrics_cause_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/FULL_PBC_IND/Metrics/pooled_oof_metrics_cause_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_1test_old\Metrics\truth_comparison_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_1test_old/Metrics/truth_comparison_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_FH\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_FH/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_10\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_10/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_100\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_100/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_20\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_20/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Brier_Raw_cause_1_NCC_ncontrols_50\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Brier_Raw_cause_1_NCC_ncontrols_50/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\brier_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/brier_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\CIndex_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/CIndex_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\IBS_scores_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/IBS_scores_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC\Metrics\Training_Durations_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC/Metrics/Training_Durations_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_10.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_100.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_20.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\NCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/NCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_NCC_ncontrols_50.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_1test_old\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_1test_old/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\OLD_RESULTS_FOLDER_WRONG_SCC_LOSS\SCC_PBC_IND\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/OLD_RESULTS_FOLDER_WRONG_SCC_LOSS/SCC_PBC_IND/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\SCC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\SCC\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC\Metrics\truth_comparison_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC/Metrics/truth_comparison_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\SCC_FH\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_FH\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_FH\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_FH\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_FH\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_FH\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_FH/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_0.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_1.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_2.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_3.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.05\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.05/brier_raw_fold_4.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_0.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_1.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_2.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_3.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.1\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.1/brier_raw_fold_4.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_0.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_1.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_2.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_3.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.2\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.2/brier_raw_fold_4.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_0.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_1.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_2.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_3.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.3\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.3/brier_raw_fold_4.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_0.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_0.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_1.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_2.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_3.csv>)

- [Results\SCC_PBC\Metrics\Brier_Raw_cause_1_SCC_subcohort_0.5\brier_raw_fold_4.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Brier_Raw_cause_1_SCC_subcohort_0.5/brier_raw_fold_4.csv>)

- [Results\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_PBC\Metrics\brier_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/brier_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_PBC\Metrics\CIndex_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/CIndex_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_PBC\Metrics\IBS_scores_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/IBS_scores_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_PBC\Metrics\pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/pooled_oof_metrics_cause_1_SCC_subcohort_0.5.csv>)

- [Results\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.05.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.05.csv>)

- [Results\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.1.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.1.csv>)

- [Results\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.2.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.2.csv>)

- [Results\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.3.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.3.csv>)

- [Results\SCC_PBC\Metrics\Training_Durations_cause_1_SCC_subcohort_0.5.csv](<C:/Users/micha/OneDrive/Documents/#Msc Data Science/Research_2026/Code/Fine-Gray-CRISP-NAM-Survival-Analysis-Using-Risk-Set-Sampling/Results/SCC_PBC/Metrics/Training_Durations_cause_1_SCC_subcohort_0.5.csv>)
