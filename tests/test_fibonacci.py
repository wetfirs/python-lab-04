import pytest

from algo_lab.fibonacci import fibonacci_iter, fibonacci_recursion


def test_fibonacci_iter():
    assert fibonacci_iter(0) == 0
    assert fibonacci_iter(1) == 1
    assert fibonacci_iter(2) == 1
    assert fibonacci_iter(6) == 8
    assert fibonacci_iter(10) == 55
    assert fibonacci_iter(20) == 6765


def test_fibonacci_recursion():
    assert fibonacci_recursion(0) == 0
    assert fibonacci_recursion(1) == 1
    assert fibonacci_recursion(2) == 1
    assert fibonacci_recursion(6) == 8
    assert fibonacci_recursion(10) == 55
    assert fibonacci_recursion(20) == 6765


def test_fibonacci_iter_negative():
    with pytest.raises(ValueError):
        fibonacci_iter(-5)


def test_fibonacci_recursion_negative():
    with pytest.raises(ValueError):
        fibonacci_recursion(-5)


@pytest.mark.parametrize("value", ["5", 3.5, True])
def test_fibonacci_iter_invalid_types(value):
    with pytest.raises(TypeError):
        fibonacci_iter(value)


@pytest.mark.parametrize("value", ["5", 3.5, True])
def test_fibonacci_recursion_invalid_types(value):
    with pytest.raises(TypeError):
        fibonacci_recursion(value)