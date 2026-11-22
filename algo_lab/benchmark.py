import csv
import statistics
import time

from .generators import (
    duplicates_generator,
    nearly_sorted_generator,
    random_generator,
    reverse_generator,
    sorted_generator,
)
from .sorting import bubble_sort, merge_sort


def measure_sort(sort_function, data: list[int], repeats: int = 5) -> float:
    """Возвращает медианное время выполнения сортировки в секундах"""
    if type(repeats) is not int:
        raise TypeError("repeats должно быть целым числом")
    if repeats < 5:
        raise ValueError("Количество повторов должно быть не меньше 5")
    times = []
    for _ in range(repeats):
        copy_data = data.copy()
        start = time.perf_counter()
        sort_function(copy_data)
        end = time.perf_counter()
        elapsed = end - start
        times.append(elapsed)
    return statistics.median(times)

def run_benchmark():
    """Измеряет время работы сортировок на разных наборах данных"""
    sorts = {
        "bubble": bubble_sort,
        "merge": merge_sort
    }
    generators = {
        "random": lambda n, seed: random_generator(n, seed),
        "sorted": lambda n, seed: sorted_generator(n),
        "reverse": lambda n, seed: reverse_generator(n),
        "duplicates": lambda n, seed: duplicates_generator(n, seed),
        "nearly_sorted": lambda n, seed: nearly_sorted_generator(n, seed)
    }
    sizes_by_sort = {
    "bubble": [100, 1_000, 10_000],
    "merge": [10_000, 100_000, 1_000_000]
    }
    results = []
    for sort_name, sort_func in sorts.items():
        for size in sizes_by_sort[sort_name]:
            for generator_name, generator_func in generators.items():
                data = generator_func(size, 42)
                elapsed = measure_sort(sort_func, data)

                result = {
                    "size": size,
                    "generator": generator_name,
                    "sort": sort_name,
                    "time": elapsed,
                }
                results.append(result)
    return results

def save_results(results, filename="results.csv"):
    """Сохраняет результаты измерений в CSV-файл"""
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["size", "generator", "sort", "time"])
        writer.writeheader()
        writer.writerows(results)


