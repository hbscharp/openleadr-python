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
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'OpenLEADR'
copyright = '2020, OpenLEADR Contributors'
author = 'Stan Janssen'

# The full version, including alpha/beta/rc tags
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'VERSION')) as file:
    release = file.read().strip()

print(release)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.apidoc']

apidoc_module_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'openleadr')
apidoc_excluded_paths = [os.path.join(apidoc_module_dir, 'service'),
                         os.path.join(apidoc_module_dir, 'config.py')]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autoclass_content = 'both'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_logo = 'logo-tall.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    app.add_stylesheet('css/custom.css')  # may also be an URL
