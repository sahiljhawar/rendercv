import os
import sys

sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'myst_parser',
]
myst_enable_extensions = [
    "amsmath",
    "dollarmath",

]

mathjax3_config = {
    "tex2jax": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
    },
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

master_doc = os.getenv('SPHINX_MASTER_DOC')

