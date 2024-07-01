def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if n < 0:
        raise ValueError ("Введите неотрицательное число")
    if not isinstance(n, int):
        raise TypeError("Введите целое число")
    if n == 1 or n == 0:
        return 1
    return factorial_recursive(n-1) * n


