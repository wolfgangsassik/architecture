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
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Arc42 Demo Architecture'
copyright = '2024, Bosch Engineering GmbH'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  "sphinxcontrib.plantuml",
  "sphinxcontrib.confluencebuilder"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Options for Confluence output -------------------------------------------------

# https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/
# https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/configuration/

# https://inside-docupedia.bosch.com/confluence/display/HILFE/REST+API+Access
# https://inside-docupedia.bosch.com/confluence/plugins/servlet/restbrowser

# Use envvars to set sensitive values (API keys)

confluence_publish = False # Warning, setting this to true is not tested yet!!!
confluence_space_key = 'BEGCOGDSE'
confluence_parent_page = 'BEG Data Strategy - Engineering'
confluence_server_url = 'https://inside-docupedia.bosch.com/confluence/'
confluence_ask_user = True
confluence_ask_password = True
