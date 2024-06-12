import pytest

from housing import Villa, StudentKot


@pytest.mark.parametrize("villa, sol", [
    (Villa("Halensebaan 9", 72, 3, 10), 3),
    (Villa("Kastelweg 54", 30, 1, 5), 1),
    (Villa("Geldenaaksebaan 255", 200, 3, 10), 6),
])
def test_maximum_occupants(villa, sol):
    assert villa.maximum_occupants == sol


@pytest.mark.parametrize("kot, sol", [
    (StudentKot("Naamsestraat 22", 30), 1),
    (StudentKot("Brusselsestraat 45", 40), 2),
    (StudentKot("Bondgenotenlaan 100", 80), 2),
])
def test_maximum_occupants_kot(kot, sol):
    assert kot.maximum_occupants == sol
