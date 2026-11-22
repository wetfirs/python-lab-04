import random


def random_generator(n: int, seed: int) -> list[int]:
    """Создаёт список из n случайных целых чисел от -10000 до 10000"""
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if type(seed) is not int:
        raise TypeError("seed должно быть целым числом")
    result = []
    rng = random.Random(seed)
    for i in range(n):
        result.append(rng.randint(-10000,10000))
    return result


def sorted_generator(n: int) -> list[int]:
    """Создаёт возрастающий список целых чисел от 0 до n - 1"""
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    result = list(range(n))
    return result


def reverse_generator(n: int) -> list[int]:
    """Создаёт убывающий список целых чисел от n - 1 до 0"""
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    result = list(range(n-1, -1, -1))
    return result


def duplicates_generator(n: int, seed: int) -> list[int]:
    """Создаёт список с большим количеством повторяющихся элементов"""
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if type(seed) is not int:
        raise TypeError("seed должно быть целым числом")
    result = []
    rng = random.Random(seed)
    for i in range(n):
        result.append(rng.randint(0,4))
    return result


def nearly_sorted_generator(n: int, seed: int) -> list[int]:
    """Создаёт почти отсортированный список целых чисел"""
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if type(seed) is not int:
        raise TypeError("seed должно быть целым числом")
    result = sorted_generator(n)
    if n <= 1:
        return result
    rng = random.Random(seed)
    swaps = max(1, n // 20)
    for _ in range(swaps):
        i = rng.randrange(n)
        j = rng.randrange(n)
        result[i], result[j] = result[j], result[i]
    return result

