"""
klifs_utils
Utility functions to work with KLIFS data
"""

# Add imports here
from .klifs_utils import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
