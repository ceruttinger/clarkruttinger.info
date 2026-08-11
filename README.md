# Clark Ruttinger — Quarto consulting website

This is the Quarto rebuild of `clarkruttinger.info`, repositioned from a professional portfolio toward an independent analytics consulting practice.

## Site structure

- `index.qmd` — consulting homepage
- `services.qmd` — five service practices + full 12-capability list
- `work.qmd` — representative case studies and public examples
- `about.qmd` — consulting biography and working approach
- `insights.qmd` — publications, reports, and public research
- `contact.qmd` — contact / project inquiry page
- `resume.qmd` — existing professional resume, available from About but not the main navigation
- `cases.qmd`, `projects.qmd`, `publications.qmd`, `presentations.qmd` — compatibility pages so old URLs do not become immediate 404s
- `_quarto.yml` — site navigation, output directory, footer, metadata
- `styles.css` — custom consulting-site design
- `person-schema.html` — updated JSON-LD structured data
- `CNAME` — custom domain for GitHub Pages
- `.nojekyll` — prevents GitHub Pages from applying Jekyll processing

## Render locally

From the project directory:

```bash
quarto preview
```

For a production build:

```bash
quarto render
```

The rendered site is written to `docs/`.

## GitHub Pages deployment

This project is configured for the simple GitHub Pages workflow where rendered files are committed in `docs/`.

1. Render with `quarto render`.
2. Commit the source files **and** the rendered `docs/` directory.
3. In GitHub repository **Settings → Pages**, set the source to the `main` branch and `/docs` folder.
4. Keep the existing custom-domain DNS settings. Quarto copies the root `CNAME` and `.nojekyll` files into the rendered site.

## Important migration note for existing static assets

Your old R Markdown site rendered directly into the repository root. If the current repository also contains static demo files that are not part of this package—especially the SNF benchmark demo, `projects/`, `downloads/`, or other generated HTML—copy the items you still want served into the Quarto project and make sure they are copied to `docs/` during rendering.

The cleanest options are:

- link to an independently hosted project site; or
- add the existing file/directory under `project: resources:` in `_quarto.yml` so Quarto copies it into `docs/`.

Do this **before** switching GitHub Pages from repository root to `/docs`, otherwise old root-only static files will no longer be part of the published site.

## Source images

The current headshot is included as `images/Ruttingerheadshot.jpg`. The prior RStudio/GitHub graphics were intentionally not used as primary branding because the new site presents a broader consulting practice rather than an R-specific portfolio.

## Sacred-geometry visual identity update

This version adds a restrained visual identity derived from the companion lecture *From Point to Flower*:

- `images/brand-emblem.png` — transparent geometry mark for the navbar and subtle page accents
- `images/favicon.png` — tighter crop for browser tabs
- `images/geometry-hero.webp` / `.jpg` — wide homepage hero background
- `styles.css` — navy/cyan/gold/violet palette, serif display headings, circumpunct micro-motifs, geometric watermarks, and the POINT → RELATION → SYSTEM → DECISION brand line

The intent is to use sacred geometry as a visual metaphor for structure, relationships, systems, and emergence—not to position the consulting practice as mystical or esoteric.
