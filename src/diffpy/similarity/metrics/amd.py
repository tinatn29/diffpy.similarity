import amd


def amd_compare(cif1, cif2, k=100):
    """
    Compare two CIF files or two lists fo CIF files using the AMD metric.
    Use cif1 = cif2 = cif_list = [cif_0, cif_1, ...]
    to compare all CIF files in cif_list.

    Parameters
    ----------
    cif1 : str
        Path to the first CIF file (or list of CIF files)
    cif2 : str
        Path to the second CIF file (or list of CIF files)
    k : int
        Number of nearest neighbors to consider.
        Default is 100.
    
    Returns
    -------
    dm : float or pandas.DataFrame
        If cif1 and cif2 are both strings, return the AMD distance value (float).
        If either cif1 or cif2 is a list, return a distance matrix of shape (len(cif1), len(cif2)).
        Each element represents the AMD distance between two structures from CIF files.
    """
    dm = amd.compare(cif1, cif2, by='AMD', k=k)
    if isinstance(cif1, list) or isinstance(cif2, list):
        # if at least one input is a list, return the distance matrix
        return dm
    else:
        return float(dm.iloc[0, 0])  # return the single distance value as a float


def pdd_compare(cif1, cif2, k=100):
    """
    Compare two CIF files or two lists fo CIF files using the PDD metric.
    Use cif1 = cif2 = cif_list = [cif_0, cif_1, ...]
    to compare all CIF files in cif_list.

    Parameters
    ----------
    cif1 : str
        Path to the first CIF file (or list of CIF files)
    cif2 : str
        Path to the second CIF file (or list of CIF files)
    k : int
        Number of nearest neighbors to consider.
        Default is 100.
    
    Returns
    -------
    dm : numpy.ndarray
        Distance matrix of shape (len(cif1), len(cif2)).
        Each element represents the PDD distance between two structures from CIF files.
    """
    dm = amd.compare(cif1, cif2, by='PDD', k=k)
    if isinstance(cif1, list) or isinstance(cif2, list):
        # if at least one input is a list, return the distance matrix
        return dm
    else:
        return float(dm.iloc[0, 0])  # return the single distance value as a float