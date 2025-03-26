import amd


def amd_compare(cif1, cif2, k=10):
    dm = amd.compare(cif1, cif2, by='AMD', k=k)
    return dm


def pdd_compare(cif1, cif2, k=10):
    dm = amd.compare(cif1, cif2, by='PDD', k=k)
    return dm