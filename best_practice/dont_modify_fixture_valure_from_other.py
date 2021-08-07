from copy import deepcopy

import pytest


@pytest.fixture
def alex():
    return {
        "name": "Alex",
        "team": "Green",
    }


@pytest.fixture
def bala(alex):
    alex["name"] = "Bala"
    return alex


@pytest.fixture
def carlos(alex):
    _carlos = deepcopy(alex)
    _carlos["name"] = "Carlos"
    return _carlos


def test_antipattern(alex, bala):
    assert alex == {"name": "Alex", "team": "Green"}
    assert bala == {"name": "Bala", "team": "Green"}


def test_pattern(alex, carlos):
    assert alex == {"name": "Alex", "team": "Green"}
    assert carlos == {"name": "Carlos", "team": "Green"}