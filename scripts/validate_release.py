#!/usr/bin/env python3
"""Verify frozen public aggregate evidence; no models are trained."""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'results/olist'


def validate(verbose=True):
    m=pd.read_csv(R/'four_origin_s1.csv').sort_values('Origin')
    c=pd.read_csv(R/'calendar_encoding_all_origins.csv')
    w=pd.read_csv(R/'window_s1.csv')
    d=pd.read_csv(R/'window_s1_contrasts.csv')
    loss=pd.read_csv(R/'brier_loss_decomposition_s1.csv')
    checks=[]
    def chk(condition,name):
        checks.append((name,bool(condition)))
        if not condition: raise AssertionError(name)
    chk(len(m)==4 and m.Origin.is_unique,'Four S1 origins')
    chk(m.N.sum()==45805,'Total evaluation observations 45,805')
    chk(len(c)==16,'Four origins by four encodings')
    chk((c.BrierCI_low<c.BrierCI_high).all(),'CI bounds ordered')
    chk(np.allclose(c.BrierDelta,c.ExpandingBrier-c.RawBrier,atol=2e-6),'Calendar contrast arithmetic')
    chk(np.allclose(m.BrierDelta,m.ExpandingBrier-m.RawBrier,atol=2e-6),'Main contrast arithmetic')
    chk(m.BrierDelta.lt(0).sum()==2 and m.BrierDelta.gt(0).sum()==2,'Two gains/two losses')
    chk(set(w.Method)=={'Raw','Expanding','Rolling60','Approval60'},'S1 E16 methods')
    chk(len(w)==16,'Four origin times four policies')
    for _,row in d.iterrows():
        x=w[(w.Period==row.Origin)&(w.Method==row.A)]
        y=w[(w.Period==row.Origin)&(w.Method==row.B)]
        chk(len(x)==len(y)==1 and abs(float(x.Brier.iloc[0]-y.Brier.iloc[0])-row.BrierDelta)<2e-6, f"Window {row.Origin} {row.Contrast}")
    chk(np.allclose(loss.OnTimeDelta+loss.LateDelta,loss.TotalDelta,atol=2e-6),'Loss contribution summation')
    chk(np.allclose(loss.sort_values('Origin').TotalDelta,m.BrierDelta,atol=2e-6),'Loss contributions equal main')
    chk(not any('order_id' in x for x in c.columns),'Aggregate tables exclude order_id')
    if verbose:
        print(f'PASS: {len(checks)} aggregate consistency checks')
        for _,x in m.iterrows(): print(x.Origin,'Brier Δ',f'{x.BrierDelta:+.6f}')
    return checks

if __name__=='__main__':
    try:validate()
    except Exception as e:
        print('FAIL:',e,file=sys.stderr);sys.exit(1)
