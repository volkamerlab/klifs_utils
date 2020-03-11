"""
klifs_utils
Utility functions to work with KLIFS data
"""

# Add imports here
from .klifs_utils import *
from . import local
from . import remote
from .util import abc_idlist_to_dataframe
from .util import mol2_text_to_dataframe, mol2_file_to_dataframe
from .util import mol2_text_to_rdkit_mol, mol2_file_to_rdkit_mol

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
