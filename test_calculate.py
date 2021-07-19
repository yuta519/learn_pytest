import pytest

import calculate


# base test function
def test_add():
    assert calculate.add(1, 2) == 3

# using decorator for parametered test
@pytest.mark.parametrize(('number', 'expected'), [
    (1, 3),
    (2, 4),
    (3, 5),
])
def test_add2(number: int, expected: int):
    assert calculate.add(number, 2) == expected

# def test_substraction():
#     assert calculate.substraction(3, 1) == 2
    