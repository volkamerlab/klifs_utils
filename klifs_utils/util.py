"""
klifs_utils
Utility functions to work with KLIFS data

General utility functions
"""

from biopandas.mol2 import PandasMol2
import pandas as pd


def abc_idlist_to_dataframe(abc_idlist):
    """

    Parameters
    ----------
    abc_idlist : list of acb.IDList
        List of labeled list objects from abstract base classes module.

    Returns
    -------
    pandas.DataFrame
        Table with list labels as column names.
    """

    result = abc_idlist

    keys = list(result[0])

    results_dict = {key: [] for key in keys}

    for result in abc_idlist:
        for key in keys:
            results_dict[key].append(result[key])

    return pd.DataFrame(results_dict)


def mol2_file_to_dataframe(mol2_file):
    pass


def mol2_text_to_dataframe(mol2_text):
    """
    Get KLIFS residue names and IDs.

    Parameters
    ----------
    mol2_text : str
       Mol2 file content from KLIFS database.

    Returns
    -------
    pandas.DataFrame
        Table of mol2 file residue names and IDs.
    """

    ppdb = PandasMol2()

    mol2_df = ppdb._construct_df(
        mol2_text.splitlines(True),
        # TODO: Rename 'Residues' to 'subst_name'
        col_names=['atom_id', 'atom_name', 'x', 'y', 'z', 'atom_type', 'subst_id', 'subst_name', 'charge', 'backbone'],
        col_types=[int, str, float, float, float, str, int, str, float, str]

    )

    return mol2_df


def mol2_file_to_rdkit_mol(mol2_file):
    pass



def mol2_text_to_rdkit_mol(mol2_text):
    pass
