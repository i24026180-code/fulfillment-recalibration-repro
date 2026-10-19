# Before making this repository public

- [ ] Confirm every author/collaborator has approved release of research code and aggregate figures.
- [ ] Choose a code license (MIT/BSD/Apache-2.0 as appropriate) and add an actual `LICENSE` file; none is assigned here without owner approval.
- [ ] Replace placeholder `CITATION_TEMPLATE.cff` author/publication metadata.
- [ ] Verify dataset terms and all attributions independently; never upload raw Olist/LaDe/DataCo files as part of this code snapshot.
- [ ] Run `python scripts/audit_public_files.py` and read its report.
- [ ] Run `python scripts/validate_release.py`, `pytest -q`, and `python scripts/make_figures.py`.
- [ ] Test the raw pipeline on your exact downloaded data and record dependency versions + Brier discrepancies (do not silently overwrite frozen results).
- [ ] Decide public vs private repository visibility and whether article manuscript submission rules permit release at this stage.
- [ ] If paper is accepted, update title, DOI, author list, release tag, and archive a versioned record (optional Zenodo DOI).
