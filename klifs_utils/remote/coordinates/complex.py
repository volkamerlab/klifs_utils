"""
klifs_utils
Utility functions to work with KLIFS data (remote)

Complex coordinates.
"""

from klifs_utils.util import _mol2_text_to_dataframe, _pdb_text_to_dataframe
from klifs_utils.klifs_client import KLIFS_CLIENT


def mol2_to_dataframe(structure_id):
    """
    Get complex structural data content (mol2 file) from KLIFS database.

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    pandas.DataFrame
        Complex structural data.
    """

    mol2_text = _complex_mol2_text(structure_id)
    structure_df = _mol2_text_to_dataframe(mol2_text)

    return structure_df


def pdb_to_dataframe(structure_id):
    """
    Get complex structural data content (pdb file) from KLIFS database.

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    pandas.DataFrame
        Complex structural data.
    """

    mol2_text = _complex_pdb_text(structure_id)
    structure_df = _pdb_text_to_dataframe(mol2_text)

    return structure_df


def _complex_mol2_text(structure_id):
    """
    Get complex structural data content (mol2 file) from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Complex structural data.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_complex(
        structure_ID=structure_id
    ).response().result

    return result


def _complex_pdb_text(structure_id):
    """
    Get complex structural data content (pdb file) from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Complex structural data.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_pdb_complex(
        structure_ID=structure_id
    ).response().result

    return result
