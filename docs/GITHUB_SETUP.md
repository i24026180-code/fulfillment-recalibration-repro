# Publish repository with your own GitHub account

**Suggested repository name:** `fulfillment-recalibration-repro`  
**Description:** `Reproducibility materials for temporal reliability of fulfillment-risk recalibration (Olist, DataCo, LaDe-P).`  
**Topics:** `probability-calibration`, `temporal-shift`, `ecommerce`, `logistics`, `reproducibility`, `ieee-access`

1. Complete [publication checklist](PUBLICATION_CHECKLIST.md), including license and author approval.
2. Unzip the distributed GitHub release locally. Enter the folder containing `README.md`, `scripts/`, `src/`, `results/`, and `figures/`.
3. Create an **empty** repository (do not generate a GitHub README) using your own GitHub account at https://github.com/new. Consider **Private** visibility until all coauthors approve.
4. Open Terminal/PowerShell in the extracted folder and run:

```bash
git init
git branch -M main
git add .
git status
git commit -m "Release reproduction materials v0.2.0"
git remote add origin https://github.com/YOUR_USERNAME/fulfillment-recalibration-repro.git
git push -u origin main
```

Replace `YOUR_USERNAME`. GitHub requires you to authenticate (browser, credential manager, or personal access token); **never put secrets in command lines or the repository**. Uploading a ZIP file itself into GitHub's web interface does NOT expand it into folders; unzip locally and push files.

5. In the GitHub repository, inspect `Actions` for the aggregate CI checks. Confirm that only public aggregate files are committed. Add the repo URL to the manuscript's Code Availability statement only after it is actually published.

If you prefer GitHub Desktop, choose File → Add local repository (create one if needed), then Publish repository and review visibility.
