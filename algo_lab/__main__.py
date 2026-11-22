from .benchmark import run_benchmark, save_results


def main():
    """Запускает benchmark и сохраняет результаты в CSV-файл"""
    results = run_benchmark()
    save_results(results)

if __name__ == "__main__":
    main()