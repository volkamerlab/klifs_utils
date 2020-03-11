"""
klifs_utils
Utility functions to work with KLIFS data

Select a set of kinase groups, kinase families, kinase names, or kinase KLIFS IDs.
"""


def kinase_groups():
    """
    Get all kinase groups.

    Returns
    -------
    list of str
        Kinase group names.
    """

    pass


def kinase_families(kinase_group):
    """
    Get all kinase families for a kinase group.

    Parameters
    ----------
    kinase_group : str
        Kinase group name.

    Returns
    -------
    list of str
        Kinase family names.
    """

    pass


def kinase_names(kinase_group, kinase_family, species):
    """
    Get all kinase names for kinases belonging to a given kinase group, kinase family and/or species.

    Parameters
    ----------
    kinase_group : str
        Kinase group name.
    kinase_family : str
        Kinase family name.
    species : str
        Species name.

    Returns
    -------
    list of str
        Kinase names.
    """

    pass


def kinase_ids(kinase_group, kinase_family, kinase_name, species):
    """
    Get all KLIFS IDs for kinases belonging to a given kinase group, kinase family, species
    and/or with a given kinase name.

    Parameters
    ----------
    kinase_group : str
        Kinase group name.
    kinase_family : str
        Kinase family name.
    species : str
        Species name.
    kinase_name : str
        Kinase name.

    Returns
    -------
    list of int
        KLIFS kinase IDs.
    """

    pass
