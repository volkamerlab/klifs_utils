"""
klifs_utils
Utility functions to work with KLIFS data (remote)

Structure coordinates.
"""

from bravado.client import SwaggerClient

from klifs_utils.util import mol2_text_to_dataframe, mol2_text_to_rdkit_mol

KLIFS_API_DEFINITIONS = "http://klifs.vu-compmedchem.nl/swagger/swagger.json"
KLIFS_CLIENT = SwaggerClient.from_url(KLIFS_API_DEFINITIONS, config={'validate_responses': False})


def structure(structure_id, structure_type):

    structure_types = 'complex protein pocket ligand water'.split()

    if structure_type not in structure_types:
        raise KeyError(f'Invalid structure type. Choose from {", ".join(structure_types)}.')

    mol2_text = _structure_text(structure_id, structure_type)

    if structure_type != 'ligand':
        return mol2_text_to_dataframe(mol2_text)
    else:
        return mol2_text_to_rdkit_mol(mol2_text)  # Possible? Or only from file?


def _structure_text(structure_id, structure_type):
    """
    Get structural data content (mol2 or pdb file) from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.
    structure_type : str
        Type of structure, i.e. complex, protein, pocket, or ligand.

    Returns
    -------
    str
        Structural data content (mol2 or pdb file) from KLIFS database.
    """

    structure_types = 'complex protein pocket ligand water'.split()

    if structure_type not in structure_types:
        raise KeyError(f'Invalid structure type. Choose from {", ".join(structure_types)}.')

    if structure_type == 'complex':
        return _complex_mol2_text(structure_id)
    elif structure_type == 'protein':
        return _protein_mol2_text(structure_id)
    elif structure_type == 'pocket':
        return _pocket_mol2_text(structure_id)
    elif structure_type == 'ligand':
        return _ligand_mol2_text(structure_id)


def _complex_mol2_text(structure_id):
    """
    Get structural data content (mol2 file) for complex from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Structural data content (mol2 file) for complex from KLIFS database.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_complex(
        structure_ID=structure_id
    ).response().result

    return result


def _protein_mol2_text(structure_id):
    """
    Get structural data content (mol2 file) for protein from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Structural data content (mol2 file) for protein from KLIFS database.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_protein(
        structure_ID=structure_id
    ).response().result

    return result


def _pocket_mol2_text(structure_id):
    """
    Get structural data content (mol2 file) for pocket from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Structural data content (mol2 file) for pocket from KLIFS database.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_pocket(
        structure_ID=structure_id
    ).response().result

    return result


def _ligand_mol2_text(structure_id):
    """
    Get structural data content (mol2 file) for ligand from KLIFS database as string (text).

    Parameters
    ----------
    structure_id : str
        KLIFS structure ID.

    Returns
    -------
    str
        Structural data content (mol2 file) for ligand from KLIFS database.
    """

    result = KLIFS_CLIENT.Structures.get_structure_get_ligand(
        structure_ID=structure_id
    ).response().result

    return result
