from .benchmark import run_benchmark, save_results


def main():
    results = run_benchmark()
    save_results(results)

if __name__ == "__main__":
    main()