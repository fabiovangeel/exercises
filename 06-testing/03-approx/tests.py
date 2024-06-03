import pytest
from mystatistics import average


@pytest.mark.parametrize("ns, expected", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([1, 2, 3, 4, 5, 6, 7], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8], 4.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ([0.1, 0.1, 0.1], 0.1),
])
def test_average(ns, expected):
    assert pytest.approx(average(ns)) == expected
