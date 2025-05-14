# -*- coding: utf-8 -*-
import os

# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

copyright = "2025 Quantinuum"
author = "Quantinuum"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
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
    "sphinxcontrib.googleanalytics",
]

nitpicky = True

nitpick_ignore = {
    # nanobind signatures for arrays and JSON do not generate references
    ("py:class", "numpy.ndarray[dtype=complex128, shape=(*, *), order='F']"),
    ("py:class", "numpy.ndarray[dtype=complex128, shape=(2, 2), order='F']"),
    ("py:class", "numpy.ndarray[dtype=complex128, shape=(4, 4), order='F']"),
    ("py:class", "numpy.ndarray[dtype=complex128, shape=(8, 8), order='F']"),
    ("py:class", "numpy.ndarray[dtype=complex128, shape=(*), order='C']"),
    ("py:class", "JSON"),
    # numpy type aliases are documented as data rather than classes, so when 
    # used in signatures sphinx cannot find the cross-reference as it only 
    # looks for classes
    ("py:class", "numpy.typing.ArrayLike"),
    # similar for our own type aliases
    ("py:class", "pytket.utils.distribution.T0"),
    # some other packages it is difficult to link to
    ("py:class", "pathlib._local.Path"),
    ("py:class", "jinja2.nodes.Output"),
}

autodoc_type_aliases = {
    "npt.ArrayLike": "numpy.typing.ArrayLike",
}

autosectionlabel_prefix_document = True

myst_enable_extensions = [
    "dollarmath",
    "html_image",
    "attrs_inline",
    "colon_fence",
    "amsmath",
]

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#auto-generated-header-anchors
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
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
    "graphviz": ("https://graphviz.readthedocs.io/en/stable/", None),
    "qiskit": ("https://docs.quantum.ibm.com/api/qiskit/", None),
    "pytket": (pytketdoc_base + "api-docs/", None),
    "pytket-qiskit": (ext_url + "pytket-qiskit/", None),
    "pytket-quantinuum": (
        ext_url + "pytket-quantinuum/",
        None,
    ),
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
    "pytket-quest": (ext_url + "pytket-quest/", None),
}

coverage_modules = ["pytket"]
coverage_statistics_to_stdout = False
coverage_show_missing_items = True
coverage_ignore_classes = []
coverage_ignore_functions = ["add_wasm", "add_wasm_to_reg", "add_clexpr_from_logicexp"]
coverage_ignore_modules = ["pytket._tket.libtket", "pytket._tket.libtklog"]

# Bit of a hack to avoid executing cutensornet notebooks (needs GPUs)
# The pytket-azure examples will also not be executable
# -------------------------------------------------------------------

# Get the current working directory
current_directory = os.getcwd()

# Get the parent directory (absolute path)
parent_directory = os.path.dirname(current_directory)

repo_name = os.path.split(parent_directory)[1]

# Don't execute pytket-cutensornet + pytket-azure examples, execute everything else.
if repo_name in ("pytket-cutensornet", "pytket-azure"):
    nb_execution_mode = "off"
else:
    nb_execution_mode = "cache"
# -------------------------------------------------------------------

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
googleanalytics_id = "G-YPQ1FTGDL3"
