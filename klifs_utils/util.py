"""
klifs_utils
Utility functions to work with KLIFS data

General utility functions
"""

from pathlib import Path

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


def _mol2_path(structure_type, klifs_download_path, species, kinase_name, pdb_id, alt, chain):
    """
    Get mol2 file path.

    Parameters
    ----------
    structure_type : str
        Structure type, i.e. complex, protein, pocket, ligand, or water.
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

    Raises
    ------
    ValueError
        If structure type invalid.
    FileNotFoundError
        If file path does not exist.


    Returns
    -------
    pathlib.Path
        Path to mol2 path.
    """

    structure_types = 'complex protein pocket ligand water'.split()

    if structure_type not in structure_types:
        raise ValueError(f'Invalid structure type {structure_type}. Choose from {",".join(structure_types)}.')

    klifs_download_path = Path(klifs_download_path)
    species = species.upper()

    if alt and chain:
        structure_name = f'{pdb_id}_alt{alt}_chain{chain}'
    elif alt and not chain:
        structure_name = f'{pdb_id}_alt{alt}'
    elif not alt and chain:
        structure_name = f'{pdb_id}_chain{chain}'
    else:
        structure_name = f'{pdb_id}'

    mol2_path = klifs_download_path / species / kinase_name / structure_name / f'{structure_type}.mol2'

    if not mol2_path.exists():
        raise FileNotFoundError(f'File not found: {mol2_path}.')

    return mol2_path


def _mol2_file_to_dataframe(mol2_file):
    """
    Get structural data from mol2 file.

    Parameters
    ----------
    mol2_file : pathlib.Path or str
       Path to mol2 file.

    Returns
    -------
    pandas.DataFrame
        Structural data.
    """

    mol2_file = Path(mol2_file)

    pmol = PandasMol2()

    try:
        mol2_df = pmol.read_mol2(
            str(mol2_file),
            columns={
                0: ('atom_id', int),
                1: ('atom_name', str),
                2: ('x', float),
                3: ('y', float),
                4: ('z', float),
                5: ('atom_type', str),
                6: ('subst_id', int),
                7: ('subst_name', str),
                8: ('charge', float),
                9: ('backbone', str)
            }
        )

    except ValueError:
        mol2_df = pmol.read_mol2(
            str(mol2_file)
        )

    return mol2_df


def _mol2_file_to_rdkit_mol(mol2_file):
    """
    Get structural data from mol2 file.

    Parameters
    ----------
    mol2_file : pathlib.Path or str
       Path to mol2 file.

    Returns
    -------
    rdkit.Chem.rdchem.Mol
        Molecule.
    """

    mol = Chem.MolFromMol2File(mol2_file)

    return mol


def _mol2_text_to_dataframe(mol2_text):
    """
    Get structural data from mol2 text.

    Parameters
    ----------
    mol2_text : str
       Mol2 file content from KLIFS database.

    Returns
    -------
    pandas.DataFrame
        Structural data.
    """

    pmol = PandasMol2()

    try:
        mol2_df = pmol._construct_df(
            mol2_text.splitlines(True),
            col_names=[
                'atom_id', 'atom_name', 'x', 'y', 'z', 'atom_type', 'subst_id', 'subst_name', 'charge', 'backbone'
            ],
            col_types=[
                int, str, float, float, float, str, int, str, float, str
            ]
        )
    except ValueError:
        mol2_df = pmol._construct_df(
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
    Get structural data from mol2 text.

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
    Get structural data from pdb text.

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
