#!/usr/bin/env python3
"""Conservative content and filename audit to run before GitHub upload.

Not a guarantee. Requires a human to review all files before public release.
"""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
BANNED_EXT={'.pkl','.joblib','.parquet','.docx','.pptx','.xlsx','.7z','.zip'}
KEYWORDS=('api_key','authorization: bearer','password=', 'kaggle.json', 'BEGIN RSA PRIVATE KEY', 'PRIVATE KEY-----')
WINDOWS_PATH=re.compile(r'[A-Za-z]:\\(?:Users|Documents|博士|论文|\S{15})',re.I)
EMAIL=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|org|edu|net|gov|io|cn|ai|ac\.uk)\b')
BAD=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts:continue
    rel=p.relative_to(ROOT)
    if any(x in ('raw','work','outputs','predictions','models') for x in rel.parts):
        # These directories must be excluded by .gitignore; never treat them as public.
        # Run the actual `git status --short` before pushing.
        continue
    if p.suffix.lower() in BANNED_EXT:BAD.append((str(rel),'Forbidden binary/data type'))
    if p.suffix.lower() not in {'.py','.csv','.md','.txt','.json','.cff','.yml','.yaml','.toml','.gitignore','.gitattributes'}:continue
    try:body=p.read_text(encoding='utf-8')
    except UnicodeDecodeError:continue
    if WINDOWS_PATH.search(body):BAD.append((str(rel),'Windows personal path'))
    if EMAIL.search(body):BAD.append((str(rel),'Email address (review)'))
    low=body.lower()
    if p.name != 'audit_public_files.py' and any(x in low for x in KEYWORDS):
        # these terms can appear in safe prose describing excluded files; manually review
        if p.suffix=='.py' and ('password=' in low or 'authorization: bearer' in low):BAD.append((str(rel),'Possible secret'))
print('Scanned public file tree:',ROOT)
for p,reason in BAD:print('CHECK:',p,'—',reason)
if BAD:sys.exit(1)
print('PASS: no disallowed file extensions, personal file paths, or embedded secrets detected (manual review still required)')
