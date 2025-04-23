import pytest
from pathlib import Path
from diffpy.similarity.metrics.amd import amd_compare, pdd_compare


# get cif files for tests
curr_path = Path().absolute()
cif1 = curr_path / 'test_data' / 'mp-390.cif'
cif2 = curr_path / 'test_data' / 'mp-458.cif'

# set up input and output for tests
# for each case: (input1, input2, expected_output)
amd_test_datasets = [
    # test identical cif files
    (cif1, cif1, 0.0),
    # test different cif files
    (cif1, cif2, dm(cif1, cif2)),
    # test generate a distance matrix from two lists
    ([cif1, cif2], [cif1, cif2], dm)
]

pdd_test_datasets = [
    # test identical cif files
    (cif1, cif1, 0.0),
    # test different cif files
    (cif1, cif2, dm(cif1, cif2)),
    # test generate a distance matrix from two lists
    ([cif1, cif2], [cif1, cif2], dm)
]

@pytest.mark.parametrize("input1, input2, expected_output", amd_test_datasets)
def test_amd_compare(input1, input2, expected_output):
    """
    Test the amd_compare function.
    """
    result = amd_compare(input1, input2)
    assert result == expected_output

@pytest.mark.parametrize("input1, input2, expected_output", pdd_test_datasets)
def test_pdd_compare(input1, input2, expected_output):
    """
    Test the pdd_compare function.
    """
    result = pdd_compare(input1, input2)
    assert result == expected_output
