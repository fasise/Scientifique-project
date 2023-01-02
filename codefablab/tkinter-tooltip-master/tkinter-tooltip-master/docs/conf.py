# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# from tktooltip import __version__

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "tkinter-tooltip"
copyright = "2021-, Giannis Nikiteas"
author = "Giannis Nikiteas"

# The full version, including alpha/beta/rc tags
# release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxarg.ext",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.inheritance_diagram",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_sitemap",
]
# For sphinx_design in Markdown
myst_enable_extensions = ["colon_fence"]
suppress_warnings = ["myst.header"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = [".rst", ".md"]


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme = "furo"
html_title = "tkinter-tooltip"
# html_logo = "../assets/images/tooltip_logo.svg"
html_favicon = "../assets/images/tooltip_logo.svg"
html_baseurl = "https://gnikit.github.io/tkinter-tooltip/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["html_extra"]
# Default is {version}{lang}{link}
sitemap_url_scheme = "{link}"

display_toc = True
# autodoc_default_flags = ["members"]
autosummary_generate = True


intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10", None),
}

inheritance_graph_attrs = {
    "size": '"6.0, 8.0"',
    "fontsize": 32,
    "bgcolor": "transparent",
}
inheritance_node_attrs = {
    "color": "black",
    "fillcolor": "white",
    "style": '"filled,solid"',
}
inheritance_edge_attrs = {
    "penwidth": 1.2,
    "arrowsize": 0.8,
}
