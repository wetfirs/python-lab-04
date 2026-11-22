def fibonacci_iter(n: int) -> int:
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("Число n должно быть неотрицательным")
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursion(n: int) -> int:
    if type(n) is not int:
        raise TypeError("n должно быть целым числом")
    if n < 0: 
        raise ValueError("Число n должно быть неотрицательным")
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
