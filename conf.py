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
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']

# -- HTML output -------------------------------------------------------------

html_theme = 'furo'
html_logo = 'logo.png'
html_favicon = 'favicon.ico'
html_title = "United Healthcare Provider Login – Secure Access Portal"
html_short_title = "UHC Provider Login"
html_show_sourcelink = False

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "footer_icons": [],  # This disables GitHub/footer icons
    "source_repository": None,
    "source_branch": None,
    "source_directory": None,
    'show_powered_by': False,
}

html_css_files = ['custom.css']
