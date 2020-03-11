"""
klifs_utils
Utility functions to work with KLIFS data

General utility functions
"""

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