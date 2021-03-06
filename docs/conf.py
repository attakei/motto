"""Configuration for documents.

This directory is premise to work on poetry environment of project.
"""
import motto


# Project information
project = "motto"
copyright = "2019, Kazuya Takei"
author = "Kazuya Takei"
release = motto.__version__

# General configuration
extensions = [
    "sphinx.ext.autodoc",
]
templates_path = ["_templates"]
language = "ja"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
