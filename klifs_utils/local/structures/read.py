"""
klifs_utils
Utility functions to work with KLIFS data

Read structure files from disc (locally).
"""

from pathlib import Path


def complex(klifs_download_path, species, kinase_name, pdb_id, alt=None, chain=None):
    """

    Parameters
    ----------
    klifs_download_path
    species
    kinase_name
    pdb_id
    alt
    chain

    Returns
    -------

    """

    mol2_path = _mol2_path(klifs_download_path, species, kinase_name, pdb_id, 'complex', alt, chain)
    structure = _read_with_biopandas(mol2_path)

    return structure


def protein(klifs_download_path, species, kinase_name, pdb_id, alt, chain):

    mol2_path = _mol2_path(klifs_download_path, species, kinase_name, pdb_id, 'protein', alt, chain)
    structure = _read_with_biopandas(mol2_path)

    return structure


def pocket(klifs_download_path, species, kinase_name, pdb_id, alt, chain):

    mol2_path = _mol2_path(klifs_download_path, species, kinase_name, pdb_id, 'pocket', alt, chain)
    structure = _read_with_biopandas(mol2_path)

    return structure


def ligand(klifs_download_path, species, kinase_name, pdb_id, alt, chain):

    mol2_path = _mol2_path(klifs_download_path, species, kinase_name, pdb_id, 'ligand', alt, chain)
    structure = _read_with_biopandas(mol2_path)

    return structure


def water(klifs_download_path, species, kinase_name, pdb_id, alt, chain):

    mol2_path = _mol2_path(klifs_download_path, species, kinase_name, pdb_id, 'water', alt, chain)
    structure = _read_with_biopandas(mol2_path)

    return structure


def _mol2_path(klifs_download_path, species, kinase_name, pdb_id, structure_type, alt=None, chain=None):

    klifs_download_path = Path(klifs_download_path)
    species = species.upper()
    structure_name = f'{pdb_id}_alt{alt}_chain{chain}'  # Add exceptions (if alt/chain None)

    return klifs_download_path / species / kinase_name / structure_name / f'{structure_type}.mol2'


def _read_with_biopandas(mol2_path):
    pass