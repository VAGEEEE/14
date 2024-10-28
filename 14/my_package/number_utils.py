def factorial(n):
    """Обчислює факторіал числа."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
