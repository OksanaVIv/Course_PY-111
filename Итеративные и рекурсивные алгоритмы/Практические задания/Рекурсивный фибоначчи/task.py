def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """

    if n < 0:
        raise ValueError('Введите неотрицательное число')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

if __name__ == "__main__":
    # assert fib_iterative(1) == 1
    # print(fib_iterative(1))
    # print(fib_iterative(0))
    print(fib_recursive(3))


