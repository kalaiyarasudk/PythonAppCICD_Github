from scr.math_operation import *

def test_addition():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0

def test_subtraction():
    assert subtract(2, 1) == 1
    assert subtract(1, 2) == -1
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0