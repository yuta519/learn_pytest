import pytest

import calculate

def test_add():
    assert calculate.add(1, 2) == 3
    assert calculate.add(2, 2) == 4
    assert calculate.add(3, 1) == 4

def test_substraction():
    assert calculate.substraction(3, 1) == 2
    assert calculate.substraction(1, 1) == 0 
    assert calculate.substraction(1, 2) == 0
    