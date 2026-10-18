from pathlib import Path
import csv, re, statistics, json, math

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'Results'
OLD = RESULTS / 'OLD_RESULTS_FOLDER_WRONG_SCC_LOSS'
OUT = ROOT / 'Documents' / 'results_comparison'
OUT.mkdir(parents=True, exist_ok=True)

def read(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def key(p):
    s = p.name
    s = re.sub(r'(?<=_)(\d+)\.0(?=_)', r'\1', s)
    return s

def label(p):
    s = p.name
    if 'ncontrols_' in s: return 'NCC m=' + re.search(r'ncontrols_([\d.]+)', s).group(1).removesuffix('.')
    if 'subcohort_' in s: return 'SCC a=' + re.search(r'subcohort_([\d.]+)', s).group(1).removesuffix('.')
    if 'tau_' in s: return 'Entropy t=' + re.search(r'tau_([\d.]+)_', s).group(1)
    return 'FULL'

def order(s):
    return (['FULL','NCC','SCC','Entropy'].index(s.split()[0]), float(s.split('=')[1]) if '=' in s else 0)

def delta(a,b,digits=4):
    a,b=float(a),float(b)
    return f'{a:.{digits}f} → {b:.{digits}f} ({b-a:+.{digits}f})'

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(map(str,r))+' |' for r in rows])

maps={
 'Synthetic': [('FULL_1test_old','FULL'),('NCC_1test_old','NCC'),('SCC_1test_old','SCC'),('ENTROPY_1test_old','ENTROPY')],
 'PBC': [(m+'_PBC',m+'_PBC') for m in ['FULL','NCC','SCC','ENTROPY']],
 'FH': [(m+'_FH',m+'_FH') for m in ['FULL','NCC','SCC','ENTROPY']],
}
report=['# Old versus new CSV results','All differences are new minus old. Values are descriptive run comparisons, not significance tests. Images were not inspected. Entropy retention is 0.1 throughout. Training duration is seconds per fold. Fold SD uses ddof=1 (sample SD), matching the recorded summary convention.','## Source selection','Synthetic old uses *_1test_old: FULL C-index 0.850110 and duration 58.1627 s match the thesis. PBC uses the archived non-IND folders: FULL 0.755646 matches the thesis. FH uses archived *_FH. Additional archived PBC_IND runs and FULL_1test are reported separately; Results/FullRisk is a separate baseline and is not silently substituted for Results/FULL.','Pooled Brier, fold-average Brier and integrated Brier (IBS) are separate metrics. Current pooled Brier is evaluated at the grid point nearest the median observed time. CSV summaries alone do not establish that old and new pooled evaluation protocols are identical. Changes include all run/pipeline differences, not an isolated estimate of the loss correction.']
summary={}; audit=[]; sources=[]; rawrows=[]; details=[]
for dataset,pairs in maps.items():
    entries={}; folds=[]; truth=[]
    for oldname,newname in pairs:
        od,nd=OLD/oldname/'Metrics',RESULTS/newname/'Metrics'
        oldfiles={key(p):p for p in od.glob('*.csv')}
        newfiles={key(p):p for p in nd.glob('*.csv')}
        assert len(oldfiles)==len(list(od.glob('*.csv')))
        for k in sorted(set(oldfiles)|set(newfiles)):
            op,np=oldfiles.get(k),newfiles.get(k)
            if not op or not np:
                audit.append(f'{dataset}: unmatched {op or np}');continue
            a,b=read(op),read(np)
            name=label(np); e=entries.setdefault(name,{'name':name})
            sources.extend([op,np])
            if k.startswith('pooled_'):
                e['old']={x:float(v) for x,v in a[0].items()};e['new']={x:float(v) for x,v in b[0].items()}
            elif 'Fold' in a[0]:
                aa={r['Fold']:r for r in a};bb={r['Fold']:r for r in b}
                cols=[x for x in a[0] if x!='Fold']
                for col in cols:
                    if any(not r[col] for r in a+b if r['Fold'].startswith('Fold_')):
                        na=sum(bool(r[col]) for r in a if r['Fold'].startswith('Fold_'))
                        nb=sum(bool(r[col]) for r in b if r['Fold'].startswith('Fold_'))
                        folds.append([name,k.split('_cause')[0]+':'+col,f'incomplete ({na}/5)',f'incomplete ({nb}/5)','not calculated'])
                        audit.append(f'{dataset} {name} {col}: only {na}/5 old and {nb}/5 new folds populated')
                        continue
                    av=[float(r[col]) for r in a if r['Fold'].startswith('Fold_')];bv=[float(r[col]) for r in b if r['Fold'].startswith('Fold_')]
                    am,bm=statistics.mean(av),statistics.mean(bv)
                    ast,bst=statistics.stdev(av),statistics.stdev(bv)
                    metric=k.split('_cause')[0]+':'+col
                    folds.append([name,metric,f'{am:.6f} ± {ast:.6f}',f'{bm:.6f} ± {bst:.6f}',f'{bm-am:+.6f}'])
                    if 'Training_Duration'==col: e['time']=[am,bm]
                    for f in sorted(set(aa)&set(bb)):
                        if f.startswith('Fold_'):details.append([dataset,name,metric,f,aa[f][col],bb[f][col],float(bb[f][col])-float(aa[f][col])])
                    if 'Mean' in aa and aa['Mean'][col] and abs(float(aa['Mean'][col])-am)>1e-8:audit.append(f'Summary mismatch {op} {col}')
                    if 'Mean' in bb and bb['Mean'][col] and abs(float(bb['Mean'][col])-bm)>1e-8:audit.append(f'Summary mismatch {np} {col}')
            elif k.startswith('truth_'):
                truth.append([name]+[delta(a[0][c],b[0][c]) for c in a[0]])
        # Raw Brier curves: match by numeric temperature, compare only equal time grids.
        oldraw={key(p.parent)+'/'+p.name:p for p in od.glob('Brier_Raw*/*.csv')}
        newraw={key(p.parent)+'/'+p.name:p for p in nd.glob('Brier_Raw*/*.csv')}
        # Historical aliases can map to the same numeric temperature. Prefer exact current directory spelling.
        for k,np in newraw.items():
            exact=od/np.parent.name/np.name
            op=exact if exact.exists() else oldraw.get(k)
            if not op:audit.append('Missing old raw: '+str(np));continue
            a,b=read(op),read(np); sources.extend([op,np])
            grid=len(a)==len(b) and all(abs(float(x['time'])-float(y['time']))<1e-9 for x,y in zip(a,b))
            if any(not x['brier_score'] for x in a+b):
                rawrows.append([dataset,label(np.parent),np.stem,len(a),len(b),'same' if grid else 'different','missing values','missing values','not calculated','not calculated'])
                continue
            av=[float(x['brier_score']) for x in a];bv=[float(x['brier_score']) for x in b]
            ds=[y-x for x,y in zip(av,bv)] if grid else []
            rawrows.append([dataset,label(np.parent),np.stem,len(a),len(b),'same' if grid else 'different',f'{statistics.mean(av):.6f}',f'{statistics.mean(bv):.6f}',f'{statistics.mean(ds):+.6f}' if grid else 'not aligned',f'{max(map(abs,ds)):.6f}' if grid else 'not aligned'])
    es=sorted(entries.values(),key=lambda e:order(e['name']));summary[dataset]=es
    report+=['## '+dataset,'### Pooled metrics and training duration',table(['Configuration','C-index old → new (delta)','IBS old → new (delta)','Brier old → new (delta)','Seconds/fold old → new (delta)'],[[e['name']]+([delta(e['old'][c],e['new'][c]) for c in ['pooled_c_index','pooled_ibs','pooled_brier']] if 'old' in e else ['missing pooled CSV']*3)+([delta(*e['time'],1)] if 'time' in e else ['missing']) for e in es]),'### Fold summaries','Mean ± SD across five folds. The Std column in the Brier source is within-fold variation across time; its mean and SD below are explicitly labelled separately.',table(['Configuration','Metric','Old mean ± SD','New mean ± SD','Mean delta'],sorted(folds,key=lambda r:(order(r[0]),r[1])))]
    if truth:report+=['### Synthetic truth correlations','Event 2 columns correlate the cause-1 model score with the event-2 generating predictor; they are not independent cause-2 model performance.',table(['Configuration','Pearson event 1','Spearman event 1','Pearson event 2','Spearman event 2'],sorted(truth,key=lambda r:order(r[0])))]

report+=['## Alternative archive comparisons','These are separate alternatives, not mixed into the primary comparisons. PBC_IND provenance must be verified before treating it as the same experimental cohort.']
for ds,pairs in [('PBC_IND',[(m+'_PBC_IND',m+'_PBC') for m in ['FULL','NCC','SCC','ENTROPY']]),('Synthetic alternate FULL',[('FULL_1test','FULL')])]:
    rows=[]
    for o,n in pairs:
        for op in (OLD/o/'Metrics').glob('pooled*.csv'):
            np=RESULTS/n/'Metrics'/op.name
            if not np.exists():continue
            a,b=read(op)[0],read(np)[0];sources.extend([op,np])
            rows.append([label(np)]+[delta(a[c],b[c]) for c in a])
    report += ['### '+ds,table(['Configuration','C-index old → new (delta)','IBS old → new (delta)','Brier old → new (delta)'],sorted(rows,key=lambda r:order(r[0])))]
report+=['## Raw Brier curve comparisons','No interpolation is performed. Differences are only calculated when all saved time points match. Each row covers every saved point in the corresponding fold CSV.',table(['Dataset','Configuration','Fold file','Old n','New n','Time grid','Old mean','New mean','Mean delta','Max absolute delta'],rawrows),'## Individual fold values','Matching fold labels do not prove identical patient membership. These are descriptive differences by stored label.',table(['Dataset','Configuration','Metric','Fold','Old','New','Delta'],details),'## Coverage notes']
report+=audit or ['No unmatched top-level CSVs or summary mean discrepancies in the primary mappings.']
report+=['PBC entropy t=0.1 has fold CSVs but neither old nor new pooled CSV.','Archived raw Brier folders with 1.0/5.0/10.0 aliases are separate historical outputs; exact current spelling is preferred, and they are not averaged.','## Source files']
report += [f'- [{p.relative_to(ROOT)}](<{p.as_posix()}>)' for p in sorted(set(sources))]
(OUT/'old_vs_new_results.md').write_text('\n\n'.join(report)+'\n',encoding='utf-8')
(OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
print('AUDIT',audit)
print('RAW GRID COUNTS',len(rawrows),sum(r[5]=='same' for r in rawrows))
print('REPORT',OUT/'old_vs_new_results.md')
