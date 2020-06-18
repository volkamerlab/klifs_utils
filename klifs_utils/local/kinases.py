"""
klifs_utils
Utility functions to work with KLIFS data (local)

Kinase details.
"""


def kinase_groups(klifs_metadata):
    """
    Get all kinase groups.

    Returns
    -------
    list of str
        Kinase group names.
    """

    kinase_groups = klifs_metadata.groups.unique().tolist()

    return kinase_groups


def kinase_families(klifs_metadata, kinase_group=None):
    """
    Get all kinase families for a kinase group.

    Parameters
    ----------
    kinase_group : None or str
        Kinase group name (default is None, i.e. all kinase groups are selected).

    Returns
    -------
    list of str
        Kinase family names.
    """

    if kinase_group:
        klifs_metadata = klifs_metadata[klifs_metadata.groups == kinase_group]

    kinase_families = klifs_metadata.family.unique().tolist()

    return kinase_families


def kinase_names(klifs_metadata, kinase_group=None, kinase_family=None, species=None):
    """
    Get all kinase names for kinases belonging to a given kinase group, kinase family and/or species (default is None,
    i.e. get all kinase names). If multiple parameters are set, only kinases fullfilling all conditions are returned.

    Parameters
    ----------
    kinase_group : None or str
        Kinase group name (default is None, i.e. all kinase groups are selected).
    kinase_family : None or str
        Kinase family name (default is None, i.e. all kinase families are selected).
    species : None or str
        Species name (default is None, i.e. all species are selected).

    Returns
    -------
    pandas.DataFrame
        Kinase names with details.
    """

    return


def kinase_from_kinase_name(klifs_metadata, kinase_name, species=None):
    """
    Get all kinases (+details) by kinase name(s).

    Parameters
    ----------
    kinase_name : str
        Kinase name.
    species : None or str
        Species name (default is None, i.e. all species are selected).

    Returns
    -------
    pandas.DataFrame
        Kinase(s) details.
    """

    return


def kinase_from_kinase_ids(klifs_metadata, kinase_ids):
    """
    Get all kinases (+details) by KLIFS kinase ID(s).

    Parameters
    ----------
    kinase_ids : int or list of int
        KLIFS kinase ID(s).

    Returns
    -------
    pandas.DataFrame
        Kinase(s) details.
    """

    return