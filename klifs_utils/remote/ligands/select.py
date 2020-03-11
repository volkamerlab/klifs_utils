"""
klifs_utils
Utility functions to work with KLIFS data

Get ligand details.
"""

from bravado.client import SwaggerClient
import pandas as pd

from klifs_utils.util import abc_idlist_to_dataframe

KLIFS_API_DEFINITIONS = "http://klifs.vu-compmedchem.nl/swagger/swagger.json"
KLIFS_CLIENT = SwaggerClient.from_url(KLIFS_API_DEFINITIONS, config={'validate_responses': False})


def ligand_ids(kinase_ids):
    """
    Get ligand IDs and details from KLIFS kinase ID(s).

    Parameters
    ----------
    kinase_ids : int or list of int
        KLIFS kinase ID(s).

    Returns
    -------
    pandas.DataFrame
        Ligand(s) details.
    """

    if isinstance(kinase_ids, int):
        kinase_ids = [kinase_ids]

    results = []

    for kinase_id in kinase_ids:
        result = KLIFS_CLIENT.Ligands.get_ligands_list(kinase_ID=[kinase_id]).response().result
        result_df = abc_idlist_to_dataframe(result)
        result_df.insert(0, 'kinase_id', kinase_id, True)
        results.append(result_df)

    return pd.concat(results)


def structure_ids(ligand_ids):
    """
    Get structure IDs and details from KLIFS ligand ID(s).

    Parameters
    ----------
    ligand_ids : int or list of int
        KLIFS ligand ID(s).

    Returns
    -------
    pandas.DataFrame
        Structure(s) details.
    """

    if isinstance(ligand_ids, int):
        ligand_ids = [ligand_ids]

    results = []

    for ligand_id in ligand_ids:

        result = KLIFS_CLIENT.Ligands.get_ligands_list_structures(
            ligand_ID=[ligand_id]
        ).response().result
        result_df = abc_idlist_to_dataframe(result)
        result_df.insert(0, 'ligand_id', ligand_id, True)
        results.append(result_df)

    return pd.concat(results)
