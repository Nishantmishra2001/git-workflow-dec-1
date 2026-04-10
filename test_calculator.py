import pytest

from calculator import add, subtract, multiply, div

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(4, 3) == 1

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(12, 3) == 4