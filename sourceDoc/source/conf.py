# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'iCook'
copyright = '2024, Eddy Terrasse'
author = 'Eddy Terrasse'

release = '0.1'
version = '1.1'




# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]




intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']




# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_logo  = 'Figures/logo64.png'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}
