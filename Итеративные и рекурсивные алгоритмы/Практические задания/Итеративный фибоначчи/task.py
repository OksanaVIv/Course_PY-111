def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
      # TODO написать итеративный алгоритм чисел Фибоначчи
    if n < 0:
        raise ValueError ('Введите неотрицательное число')

    # list_ = [0,1]
    # a = 0
    # if n == 0:
    #     return 0;
    # if n == 1:
    #     return 1;
    # for _ in range (2, n+1):
    #     a = list_[0] + list_[1]
    #     list_[0], list_[1] = list_[1], a
    # return a

    a, b = 0, 1
    if n == 0:
        return a;
    if n == 1:
        return b;
    for _ in range (2, n+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    # assert fib_iterative(1) == 1
    # print(fib_iterative(1))
    # print(fib_iterative(0))
    print(fib_iterative(3))
