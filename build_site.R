# Build the R Markdown website.
# Run from the project root:
#   source("build_site.R")

if (!requireNamespace("rmarkdown", quietly = TRUE)) {
  install.packages("rmarkdown")
}

rmarkdown::render_site()
