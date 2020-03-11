"""
klifs_utils
Utility functions to work with KLIFS data

Select a set of structures.
"""

from bravado.client import SwaggerClient

from klifs_utils.util import abc_idlist_to_dataframe

KLIFS_API_DEFINITIONS = "http://klifs.vu-compmedchem.nl/swagger/swagger.json"
KLIFS_CLIENT = SwaggerClient.from_url(KLIFS_API_DEFINITIONS, config={'validate_responses': False})


def structures_from_structure_id(structure_ids):
    """
    Get structure details from KLIFS structure ID.

    Parameters
    ----------
    structure_id : int or list of int

    Returns
    -------

    """

    if isinstance(structure_ids, int):
        structure_ids = [structure_ids]

    result = KLIFS_CLIENT.Structures.get_structure_list(structure_ID=structure_ids).response().result

    return abc_idlist_to_dataframe(result)


def structures_from_kinase_id(kinase_ids):

    if isinstance(kinase_ids, int):
        kinase_ids = [kinase_ids]

    result = KLIFS_CLIENT.Structures.get_structures_list(kinase_ID=kinase_ids).response().result

    return abc_idlist_to_dataframe(result)


def structures_from_pdb_id(pdb_ids):

    if isinstance(pdb_ids, str):
        pdb_ids = [pdb_ids]

    result = KLIFS_CLIENT.Structures.get_structures_pdb_list(pdb_codes=pdb_ids).response().result

    return abc_idlist_to_dataframe(result)
