import pytest


def test_multi(fixture1):
    print("test")

@pytest.fixture
def fixture1(fixture2):
    print("fixture1")


@pytest.fixture
def fixture2():
    print("fixture2")
