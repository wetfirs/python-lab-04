import random

import pytest

from algo_lab.sorting import bubble_sort, merge_sort


@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([5], [5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
        ([-3, 5, -1, 0, -7], [-7, -3, -1, 0, 5]), 
        ([4, 4, 4, 4], [4, 4, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ]
)
def test_sort_correct(sort_func, data, expected):
    assert sort_func(data) == expected


@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_original_unchanged(sort_func):
    data = [5, 3, 1, 4, 2]
    original = data.copy()
    result = sort_func(data)
    assert data == original
    assert result is not data


@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
@pytest.mark.parametrize("value", ["123", 123, (3,1,2), [1, "2", 3], [1, 2.5, 3], [1, True, 3]])
def test_sort_invalid_input(sort_func, value):
    with pytest.raises(TypeError):
        sort_func(value)


@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_random(sort_func):
    rng = random.Random(42)
    for _ in range(10):
        data = [rng.randint(-100, 100) for _ in range(50)]
        result = sort_func(data)
        assert result == sorted(data)


