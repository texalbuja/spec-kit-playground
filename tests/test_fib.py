import pytest

from src.fib import fib


def test_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1


def test_small_numbers():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3


def test_larger_number():
    assert fib(10) == 55


def test_negative_raises():
    with pytest.raises(ValueError):
        fib(-1)


def test_non_integer_raises():
    with pytest.raises(TypeError):
        fib(3.5)

