"""
klifs_utils
Utility functions to work with KLIFS data (local)

Complex coordinates.
"""

from bravado.client import SwaggerClient

from klifs_utils.util import _mol2_path, _mol2_file_to_dataframe
from klifs_utils.klifs_client import KLIFS_API_DEFINITIONS

KLIFS_CLIENT = SwaggerClient.from_url(KLIFS_API_DEFINITIONS, config={'validate_responses': False})


def mol2_to_dataframe(klifs_download_path, species, kinase_name, pdb_id, alt=None, chain=None):
    """
    Get complex structural data content (mol2 file) from local file.

    Parameters
    ----------
    klifs_download_path : pathlib.Path or str
        Path to folder where KLIFS_download folder lives.
    species : str
        Species.
    kinase_name : str
        Kinase name.
    pdb_id : str
        PDB ID.
    alt : str
        Alternate model ID.
    chain : str
        Chain ID.

    Returns
    -------
    pandas.DataFrame
        Complex structural data.
    """

    mol2_file = _mol2_path('complex', klifs_download_path, species, kinase_name, pdb_id, alt, chain)
    structure_df = _mol2_file_to_dataframe(mol2_file)

    return structure_df.df
