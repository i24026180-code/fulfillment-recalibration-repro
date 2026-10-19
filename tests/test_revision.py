from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validate_revision',ROOT/'scripts/validate_revision.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def test_revision_aggregate():
    assert mod.validate(ROOT)['passed']
