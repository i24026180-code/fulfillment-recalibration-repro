#!/usr/bin/env python3
"""Validate public aggregate identities, score differences and immutable Figure 1.
This is not re-estimation of intervals or validation of the original training.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

def validate(root: Path) -> dict:
    ev=root/'evidence';m=pd.read_csv(ev/'e17/metrics.csv');pairs=pd.read_csv(ev/'e17/paired_intervals.csv');checks=0
    if m.duplicated(['Backbone','Origin','Method']).any():raise AssertionError('Duplicate model-context metrics.')
    def close(a,b):
        nonlocal checks
        if not np.isclose(a,b,atol=1e-11,rtol=1e-9):raise AssertionError(f'Numerical mismatch: {a} vs {b}')
        checks+=1
    for _,x in m.iterrows():
        close(x.Brier,x.OnTimeBrierContribution+x.LateBrierContribution)
        close(x.ActualRate,x.Positives/x.N)
    decision=pd.read_csv(ev/'e17/decision_metrics.csv')
    for _,r in pairs.iterrows():
        mm=decision if r.Metric=='ValueCoverage5' else m
        aa=mm[(mm.Backbone==r.Backbone)&(mm.Origin==r.Origin)&(mm.Method==r.A)]
        bb=mm[(mm.Backbone==r.Backbone)&(mm.Origin==r.Origin)&(mm.Method==r.B)]
        if len(aa)!=1 or len(bb)!=1:raise AssertionError('Missing pair endpoint.')
        close(r.Delta,aa.iloc[0][r.Metric]-bb.iloc[0][r.Metric])
        if r.CI_low>r.CI_high:raise AssertionError('Reversed confidence interval.')
    u=pd.read_csv(ev/'e17/unknown_outcome_bounds.csv')
    for _,r in u.iterrows():
        close(r.N,r.Known+r.Unknown)
        if r.BrierLower>r.BrierUpper:raise AssertionError('Reversed unknown-label bound.')
    raw=m[(m.Backbone=='Core')&(m.Method=='Raw')]
    if int(raw.N.sum())!=45805:raise AssertionError('Unexpected primary sample size.')
    fig=root/'figures/figure1_framework.pdf'
    h=None
    if fig.exists():
        h=hashlib.sha256(fig.read_bytes()).hexdigest()
        if h!='fa896fd874ef3824395cfa1c658f829accc76e866c93f4ca3f693a835a71fcd9':raise AssertionError('Figure 1 changed from previous integrated source.')
    manifest=root/'evidence_manifest.json'
    count=0
    if manifest.exists():
        for item in json.loads(manifest.read_text()):
            p=root/item['path']
            if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise AssertionError('Evidence hash mismatch: '+item['path'])
            count+=1
    return {'passed':True,'arithmetic_checks':checks,'metric_rows':len(m),'paired_rows':len(pairs),'unknown_bound_rows':len(u),'primary_evaluation_orders':int(raw.N.sum()),'evidence_files_checked':count,'figure1_sha256':h,'scope':'Aggregate reconstruction only; frozen intervals checked arithmetically, not recomputed'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=ROOT);ap.add_argument('--out',type=Path);a=ap.parse_args()
    r=validate(a.root)
    if a.out:a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(r,indent=2))
    print(json.dumps(r,indent=2))
if __name__=='__main__':main()
