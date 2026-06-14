# Maintaining this site with Codex

Use Codex as a careful editor and coding assistant, not as an unchecked publisher.

## Recommended workflow

1. Put this project in a private GitHub repository first.
2. Create a new branch for each change.
3. Ask Codex for small, reviewable changes.
4. Review the diff before accepting.
5. Build the site locally with `rmarkdown::render_site()`.
6. Check all pages in a browser.
7. Only then merge or publish.

## Good Codex prompts

### Audit the site

```text
Review this R Markdown portfolio site for outdated language, broken links, and confidential-information risks. Do not rewrite files yet. Give me a prioritized list of recommended changes.
```

### Update a page without over-editing

```text
Update work.Rmd to add a new public report. Keep the existing card format. Do not invent claims, do not add confidential details, and keep the tone concise and professional.
```

### Check for risky content

```text
Scan the repository for secrets, private data, local machine paths, .Rhistory content, GlobalData-owned code, or confidential client material. List anything risky and suggest removals.
```

### Improve Posit alignment

```text
Review index.Rmd, work.Rmd, and cases.Rmd for alignment with roles at Posit involving customer success, R/Shiny, Posit Connect, analytic workflow modernization, and client-facing technical delivery. Make suggestions only; do not modify files yet.
```

### Fix build errors

```text
Run the site build. If it fails, identify the smallest necessary change to fix the build. Do not change content unless required for the build.
```

## Guardrails for Codex

Tell Codex explicitly:

- Do not add employer-owned code.
- Do not create fake metrics or outcomes.
- Do not make confidential client work identifiable.
- Do not rewrite everything into generic marketing language.
- Preserve source `.Rmd` files as the source of truth.
- Keep edits small and diff-friendly.

## Suggested publishing options

- GitHub Pages for a simple static portfolio.
- Netlify if you want easy deploy previews.
- Posit Connect if you want to demonstrate familiarity with the Posit ecosystem, but only publish public-safe materials.

## Maintenance cadence

- Quarterly: check links and resume downloads.
- After every public report: add a card to `work.Rmd` and a link to `publications.Rmd`.
- Before every major application: tailor the homepage and case-study order to the job target.
