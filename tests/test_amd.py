from pathlib import Path

import pandas as pd
import pytest

from diffpy.similarity.metrics.amd import amd_compare, pdd_compare

# get cif files for tests
curr_path = Path().absolute()
cif1 = curr_path / "tests" / "test_data" / "mp-390.cif"
cif2 = curr_path / "tests" / "test_data" / "mp-458.cif"
dm_amd = pd.read_pickle(curr_path / "tests" / "test_data" / "dm_amd.pkl")
dm_pdd = pd.read_pickle(curr_path / "tests" / "test_data" / "dm_pdd.pkl")

# set up input and output for tests
# for each case: (input1, input2, expected_output)
amd_test_datasets = [
    # test identical cif files
    (cif1, cif1, 0.0),
    # test different cif files
    (cif1, cif2, 0.5725326132426836),
    # test generate a distance matrix from two lists
    ([cif1, cif2], [cif1, cif2], dm_amd),
]


@pytest.mark.parametrize("input1, input2, expected_output", amd_test_datasets)
def test_amd_compare(input1, input2, expected_output):
    """Test the amd_compare function."""
    result = amd_compare(input1, input2, k=100)
    if isinstance(input1, list) or isinstance(input2, list):
        # check if two dataframes are equal
        assert result.equals(expected_output)
    else:
        # check if two floats are equal
        assert result == expected_output


# for each case: (input1, input2, expected_output)
pdd_test_datasets = [
    # test identical cif files
    (cif1, cif1, 0.0),
    # test different cif files
    (cif1, cif2, 0.6675364987310654),
    # test generate a distance matrix from two lists
    ([cif1, cif2], [cif1, cif2], dm_pdd),
]


@pytest.mark.parametrize("input1, input2, expected_output", pdd_test_datasets)
def test_pdd_compare(input1, input2, expected_output):
    """Test the pdd_compare function."""
    result = pdd_compare(input1, input2, k=100)
    if isinstance(input1, list) or isinstance(input2, list):
        # check if two dataframes are equal
        assert result.equals(expected_output)
    else:
        # check if two floats are equal
        assert result == expected_output
