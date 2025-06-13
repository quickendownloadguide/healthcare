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

# -- Custom meta tags for SEO ------------------------------------------------

def setup(app):
    app.add_config_value('html_context', {}, 'env')
    app.add_css_file('custom.css')
    app.add_meta_tags = lambda: [
        '<meta name="description" content="Login to your United Healthcare provider portal. Access secure tools, update provider data, view patient information, and manage claims.">',
        '<meta name="keywords" content="United Healthcare Provider Login, UHC Login, UnitedHealthcare Portal, Provider Account Access">',
        '<meta name="author" content="UnitedHealthcare">'
    ]
