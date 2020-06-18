"""
klifs_utils
Utility functions to work with KLIFS data (remote)

Ligand coordinates.
"""

from klifs_utils.util import _mol2_text_to_dataframe, _mol2_text_to_rdkit_mol
from klifs_utils.klifs_client import KLIFS_CLIENT


def mol2_to_dataframe(structure_id):
    """
    Get ligand structural data content (mol2 file) from KLIFS database.

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    pandas.DataFrame
        Ligand structural data.
    """

    mol2_text = _ligand_mol2_text(structure_id)
    structure_df = _mol2_text_to_dataframe(mol2_text)

    return structure_df


def mol2_to_rdkit_mol(structure_id, compute2d=True):
    """
    Get ligand structural data content (mol2 file) from KLIFS database.

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.
    compute2d : bool
        Compute 2D coordinates for ligand (default).

    Returns
    -------
    rdkit.Chem.rdchem.Mol
        Ligand structural data.
    """

    mol2_text = _ligand_mol2_text(structure_id)
    mol = _mol2_text_to_rdkit_mol(mol2_text, compute2d)

    return mol


def _ligand_mol2_text(structure_id):
    """
    Get ligand structural data content (mol2 file) from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Ligand structural data.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_ligand(
        structure_ID=structure_id
    ).response().result

    return result
