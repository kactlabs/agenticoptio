# Configuration file for the Sphinx documentation builder.
#
# This file configures Sphinx to generate comprehensive documentation
# for the AgenticOptio project, including both AgenticOptio and AgenticFlow
# packages with full API documentation, examples, and cross-references.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

# Add the project root to Python path for autodoc
sys.path.insert(0, os.path.abspath("../.."))
# Add source directories for both packages
sys.path.insert(0, os.path.abspath("../../src"))
sys.path.insert(0, os.path.abspath("../../source_one/src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AgenticOptio'
copyright = '2025, Raja CSP Raman / KactLabs'
author = 'Raja CSP Raman / KactLabs'
release = '0.1.1'
version = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",        # Automatic documentation from docstrings
    "sphinx.ext.napoleon",       # Support for Google/NumPy style docstrings
    "sphinx.ext.autosummary",    # Generate summary tables
    "sphinx.ext.viewcode",       # Add source code links
    "sphinx.ext.intersphinx",    # Link to other project docs
    "sphinx_autodoc_typehints",  # Better type hint rendering
    "myst_parser",               # Markdown support
]

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**/__pycache__',
    '**/test_*.py',
    '**/tests/**',
]

# -- Autodoc configuration --------------------------------------------------

# Generate autosummary stubs
autosummary_generate = True

autodoc_mock_imports = [
    "ollama",
]

# Default options for autodoc directives
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": "__init__",
    "exclude-members": "__weakref__",
}

# Type hints configuration
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# -- Napoleon configuration -------------------------------------------------

# Napoleon settings for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Intersphinx configuration ----------------------------------------------

# Links to external documentation
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    # 'openai': ('https://platform.openai.com/docs', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',

    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


# Custom sidebar
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# -- Options for LaTeX output -----------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',
    
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
    
    # Additional stuff for the LaTeX preamble.
    'preamble': '',
    
    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'AgenticOptio.tex', 'AgenticOptio Documentation',
     'Raja CSP Raman / KactLabs', 'manual'),
]

suppress_warnings = [
    "autodoc.import_object",
    "autodoc",
]

nitpicky = False