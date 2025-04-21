# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "InvenTree Project"
copyright = "InvenTree contributors"
author = "Matthias Mair <code@mjmair.com>"
release = "0.1.0"
html_title = "InvenTree Project Documentation"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxext.opengraph",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["adr/template.md"]

ogp_site_url = "https://project.inventree.org/"
html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
    "announcement": "<em>In Beta</em> This is only in testing, not official yet!",
    "source_repository": "https://github.com/matmair/project",
    "source_branch": "main",
    "source_directory": "docs/",
}
