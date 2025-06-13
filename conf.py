import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'United Healthcare Provider Login'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare, Inc.'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'  # clean, responsive theme
html_logo = 'logo.png'
html_favicon = 'favicon.ico'
html_title = "United Healthcare Provider Login – Secure Access Portal"
html_short_title = "UHC Provider Login"
html_show_sourcelink = False
html_static_path = ['_static']

# -- Theme options for furo --------------------------------------------------

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
}


