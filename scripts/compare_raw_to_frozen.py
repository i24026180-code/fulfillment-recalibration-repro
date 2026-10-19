#!/usr/bin/env python3
"""Check a from-raw reproduction against frozen public S1 aggregate reference.

Example: python scripts/compare_raw_to_frozen.py --run outputs/olist_rebuild
"""
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--run',type=Path,required=True)
    ap.add_argument('--absolute-tolerance',type=float,default=1e-6)
    args=ap.parse_args()
    got=pd.read_csv(args.run/'summary.csv');expect=pd.read_csv(ROOT/'results/olist/window_s1.csv')
    # Frozen is extra in our public reconstruction, absent from E16-S1 reference.
    comparable=got[got.Method.isin(expect.Method.unique())]
    pair=comparable.merge(expect,left_on=['Origin','Method'],right_on=['Period','Method'],suffixes=('_run','_reference'),validate='one_to_one')
    if len(pair)!=len(comparable):raise AssertionError('Unmatched model/method rows')
    metrics=['Brier','LogLoss','AP','MeanPred']
    errs={m:float(np.max(np.abs(pair[f'{m}_run']-pair[f'{m}_reference']))) for m in metrics}
    print('reproduction comparison:',errs)
    if max(errs.values())>args.absolute_tolerance:raise SystemExit('FAIL: discrepancies exceed tolerance; compare data version and dependencies')
    ref=pd.read_csv(ROOT/'results/olist/window_s1_contrasts.csv')
    got2=pd.read_csv(args.run/'paired_brier.csv')
    got2=got2[got2.A.ne('Expanding')|got2.B.ne('Raw')]
    pairs=got2.merge(ref,on=['Origin','A','B'],suffixes=('_run','_reference'),validate='one_to_one')
    if len(got2)!=len(pairs):raise AssertionError('Unmatched window contrasts')
    for a,b in [('BrierDelta_run','BrierDelta_reference'),('CI_low','BrierCI_low'),('CI_high','BrierCI_high')]:
        d=float(np.max(np.abs(pairs[a]-pairs[b])))
        print(a,'max error',d)
        if d>args.absolute_tolerance:raise SystemExit('FAIL: paired interval discrepancy')
    print(f'PASS: {len(pair)} method rows and {len(pairs)} window contrasts reproduced.')

if __name__=='__main__':main()
