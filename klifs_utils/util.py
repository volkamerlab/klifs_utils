"""
klifs_utils
Utility functions to work with KLIFS data

General utility functions
"""

from biopandas.mol2 import PandasMol2
from biopandas.pdb import PandasPdb
import pandas as pd
from rdkit import Chem


def _abc_idlist_to_dataframe(abc_idlist):
    """
    Transform ABC IDList object into DataFrame.

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


def _mol2_file_to_dataframe(mol2_file):
    """
    Get KLIFS structure coordinates from mol2 file.

    Parameters
    ----------
    mol2_file

    Returns
    -------

    """
    pass


def _mol2_file_to_rdkit_mol(mol2_file):
    """
    Get KLIFS structure coordinates from mol2 file.

    Parameters
    ----------
    mol2_file

    Returns
    -------

    """

    pass


def _mol2_text_to_dataframe(mol2_text):
    """
    Get KLIFS structure coordinates from mol2 text.

    Parameters
    ----------
    mol2_text : str
       Mol2 file content from KLIFS database.

    Returns
    -------
    pandas.DataFrame
        Structural data.
    """

    pmol2 = PandasMol2()

    try:
        mol2_df = pmol2._construct_df(
            mol2_text.splitlines(True),
            col_names=[
                'atom_id', 'atom_name', 'x', 'y', 'z', 'atom_type', 'subst_id', 'subst_name', 'charge', 'backbone'
            ],
            col_types=[
                int, str, float, float, float, str, int, str, float, str
            ]
        )
    except ValueError:
        mol2_df = pmol2._construct_df(
            mol2_text.splitlines(True),
            col_names=[
                'atom_id', 'atom_name', 'x', 'y', 'z', 'atom_type', 'subst_id', 'subst_name', 'charge'
            ],
            col_types=[
                int, str, float, float, float, str, int, str, float
            ]
        )

    return mol2_df


def _mol2_text_to_rdkit_mol(mol2_text):
    """
    Get KLIFS structure coordinates from mol2 text.

    Parameters
    ----------
    mol2_text : str
       Mol2 file content from KLIFS database.

    Returns
    -------
    rdkit.Chem.rdchem.Mol
        Molecule.
    """

    mol = Chem.MolFromMol2Block(mol2_text)

    return mol


def _pdb_text_to_dataframe(pdb_text):
    """
    Get KLIFS structure coordinates from pdb text.

    Parameters
    ----------
    pdb_text : str
       Pdb file content from KLIFS database.

    Returns
    -------
    dict of pandas.DataFrame
        Structural data
    """

    ppdb = PandasPdb()

    pdb_dict = ppdb._construct_df(
        pdb_text.splitlines(True)
    )

    print(f'Structural data keys: {pdb_dict.keys()}')

    return pdb_dict
