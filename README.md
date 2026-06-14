# Clark Ruttinger Portfolio v2

This is a cleaned-up R Markdown website intended for current job applications and portfolio use.

## Pages

- `index.Rmd` — updated homepage and positioning
- `work.Rmd` — selected public work and older R/Shiny examples
- `cases.Rmd` — anonymized case studies, including confidential-client-safe descriptions
- `publications.Rmd` — selected peer-reviewed work and public reports
- `resume.Rmd` — current resume summary and downloadable resume files
- `presentations.Rmd` — presentation archive

## Build locally

From the project root:

```r
source("build_site.R")
```

or:

```r
rmarkdown::render_site()
```

The generated `.html` files are ignored by `.gitignore` in this v2 package. If you publish through GitHub Pages from static HTML, remove `*.html` and `site_libs/` from `.gitignore` or build into a deploy branch.

## What not to add

Do not add:

- GlobalData-owned source code
- proprietary client dashboards or screenshots
- private data
- credentials or API keys
- `.Rhistory`, `.Renviron`, `.RData`, or local machine paths

## Updating confidential work descriptions

Use the pattern:

> Problem type + your role + technical approach + outcome type

Avoid client names, private metrics, screenshots, code, internal architecture diagrams, or details that would identify confidential work.
