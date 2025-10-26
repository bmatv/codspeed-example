import pytest
import numpy as np

def sum_squares(arr):
    """Sum the squares of the numbers in an array."""
    return (np.asarray(arr)**2).sum()

# Your tests can also be benchmarks
@pytest.mark.benchmark
def test_sum_squares():
    assert sum_squares(range(1000)) == 332833500