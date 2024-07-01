import math
def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if n < 0:
        raise ValueError ("Введите неотрицательное число")
    if not isinstance(n, int):
        raise TypeError("Введите целое число")
    if n == 1 or n == 0:
        return 1
    res = 1
    num = 1
    while num <= n:
        res  = res * num
        num += 1
    return res



