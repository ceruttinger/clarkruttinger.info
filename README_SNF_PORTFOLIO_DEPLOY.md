# SNF benchmark demo portfolio deployment

This portfolio update adds a landing page for the Skilled Nursing Facility Strategic Benchmark Explorer and a Projects-page card that links to the demo dashboard.

## Files added or changed

- `snf-benchmark-demo.Rmd`
- `snf-benchmark-demo.html`
- `projects.Rmd`
- `projects.html`
- `style.css`
- `projects/snf-strategic-benchmark-demo/` placeholder folder

## Build the dashboard demo into this portfolio repo

Unzip the dashboard package `snf_hcris_dashboard_v0_37.zip`. From the dashboard project folder, run:

```r
Sys.setenv(PORTFOLIO_SITE_DIR = "/path/to/cv_v2")
Sys.setenv(SNF_DEMO_N = "10")
source("99_render_portfolio_demo_release.R")
```

This will:

1. Select about 10 diverse Utah SNF facilities.
2. Render the Explorer with only those facilities in the public selector.
3. Render client reports only for those facilities.
4. Copy the rendered dashboard into:

```text
cv_v2/projects/snf-strategic-benchmark-demo/
```

## Rebuild the portfolio site

From the portfolio repo root:

```r
source("build_site.R")
```

Then open:

```r
browseURL("snf-benchmark-demo.html")
browseURL("projects.html")
```

## Git deployment

After verifying locally:

```bash
git status
git add .
git commit -m "Add SNF strategic benchmark demo to portfolio"
git push
```

## Public caveat

The demo page includes a disclaimer because the facility reports use real public CMS cost-report data. Keep that caveat visible.
