# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

copyright = "2024 Quantinuum"
author = "Quantinuum"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "enum_tools.autoenum",
    "sphinx.ext.autosectionlabel",
    "myst_nb",
]

autosectionlabel_prefix_document = True

myst_enable_extensions = ["dollarmath", "html_image", "attrs_inline"]

#https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#auto-generated-header-anchors
myst_heading_anchors = 3

html_theme_options = {}

html_theme = "furo"
templates_path = ["quantinuum-sphinx/_templates"]
html_static_path = ["quantinuum-sphinx/_static", "_static"]
html_favicon = "quantinuum-sphinx/_static/assets/quantinuum_favicon.svg"


pytketdoc_base = "https://docs.quantinuum.com/tket/"
ext_url = pytketdoc_base + "extensions/"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
    "qiskit": ("https://docs.quantum.ibm.com/api/qiskit", None),
    "pytket": (pytketdoc_base + "api-docs/", None),
    "pytket-qiskit": (ext_url + "pytket-qiskit/", None),
    "pytket-quantinuum": (ext_url + "pytket-quantinuum/", None,),
    "pytket-pennylane": (ext_url + "pytket-pennylane/", None),
    "pytket-qujax": (ext_url + "pytket-qujax/", None),
    "pytket-cirq": (ext_url + "pytket-cirq/", None),
    "pytket-braket": (ext_url + "pytket-braket/", None),
    "pytket-pyquil": (ext_url + "pytket-pyquil/", None),
    "pytket-pysimplex": (ext_url + "pytket-pysimplex/", None),
    "pytket-projectq": (ext_url + "pytket-projectq/", None),
    "pytket-qulacs": (ext_url + "pytket-qulacs/", None),
    "pytket-iqm": (ext_url + "pytket-iqm/", None),
    "pytket-stim": (ext_url + "pytket-stim/", None),
}


nb_execution_mode = "cache"

nb_execution_timeout = 120

nb_execution_excludepatterns = [
    "examples/backends/backends_example.ipynb",
    "examples/backends/qiskit_integration.ipynb",
    "examples/backends/comparing_simulators.ipynb",
    "examples/algorithms_and_protocols/expectation_value_example.ipynb",
    "examples/algorithms_and_protocols/pytket-qujax_heisenberg_vqe.ipynb",
    "examples/algorithms_and_protocols/pytket-qujax-classification.ipynb",
    "examples/algorithms_and_protocols/pytket-qujax_qaoa.ipynb",
    "examples/algorithms_and_protocols/ucc_vqe.ipynb",
    "examples/algorithms_and_protocols/entanglement_swapping.ipynb",
]

exclude_patterns = [
    "**/jupyter_execute",
    "jupyter_execute/*",
    ".jupyter_cache",
    "*.venv",
    "README.md",
    "**/README.md",
    ".jupyter_cache",
]

autodoc_member_order = "groupwise"
