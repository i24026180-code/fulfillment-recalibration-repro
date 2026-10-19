from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_release import validate

def test_frozen_aggregates():
    assert all(ok for name,ok in validate(verbose=False))

def test_core_reconstruction_config():
    from reproduce_olist_primary import ORIGINS, CLIP
    assert len(ORIGINS)==4
    assert CLIP==1e-7

def test_brier_contribution_identity():
    import numpy as np
    from reproduce_olist_primary import calc_scores
    y=np.array([0,0,1,1]);p=np.array([.1,.3,.7,.9])
    x=calc_scores(y,p)
    assert abs(x['OnTimeBrierContribution']+x['LateBrierContribution']-x['Brier'])<1e-14
