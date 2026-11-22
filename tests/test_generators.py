import pytest

from algo_lab.generators import (
    duplicates_generator,
    nearly_sorted_generator,
    random_generator,
    reverse_generator,
    sorted_generator,
)

generators = [
    lambda n: random_generator(n, 42),
    lambda n: sorted_generator(n),
    lambda n: reverse_generator(n),
    lambda n: duplicates_generator(n, 42),
    lambda n: nearly_sorted_generator(n, 42),
]


@pytest.mark.parametrize("generator", generators)
@pytest.mark.parametrize("n", [0, 1, 10, 100])
def test_generator_size(generator, n):
    result = generator(n)
    assert len(result) == n


@pytest.mark.parametrize("generator", generators)
def test_generator_empty(generator):
    result = generator(0)                                                                           
    assert result == []


@pytest.mark.parametrize("generator", generators)
@pytest.mark.parametrize("value", ["abc", 1.5, True, [1, 2]])
def test_generator_invalid_type(generator, value):
    with pytest.raises(TypeError):
        generator(value)


@pytest.mark.parametrize("generator", generators)
def test_generator_negative(generator):
    with pytest.raises(ValueError):
        generator(-5)


@pytest.mark.parametrize(
    "generator",
    [random_generator, duplicates_generator, nearly_sorted_generator]
)
@pytest.mark.parametrize("value", ["abc", 1.5, True, [1, 2]])
def test_generator_invalid_seed(generator, value):
    with pytest.raises(TypeError):
        generator(100, value)
    
    
def test_sorted_generator():
    assert sorted_generator(5) == [0, 1, 2, 3, 4]


def test_reverse_generator():
    assert reverse_generator(5) == [4, 3, 2, 1, 0]


def test_random_range():
    result = random_generator(100, 42)
    assert all(-10000 <= x <= 10000 for x in result)


def test_duplicates_range():
    result = duplicates_generator(100, 42)
    assert all(0 <= x <= 4 for x in result)


def test_nearly_sorted():
    result = nearly_sorted_generator(100, 42)
    assert sorted(result) == sorted_generator(100)
    count = sum(1 for i, value in enumerate(result) if i != value)
    assert count <= 10


@pytest.mark.parametrize(
    "generator",
    [random_generator, duplicates_generator, nearly_sorted_generator]
)
def test_same_seed(generator):
    assert generator(100, 42) == generator(100, 42)


@pytest.mark.parametrize(
    "generator",
    [random_generator, duplicates_generator, nearly_sorted_generator]
)
def test_different_seed(generator):
    assert generator(100, 42) != generator(100, 43)

