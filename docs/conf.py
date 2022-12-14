"""Sphinx configuration."""
project = "Django Dataslice"
author = "Sergey Bershadsky"
copyright = "2022, Sergey Bershadsky"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
