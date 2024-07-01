from typing import Union
from itertools import count
from math import factorial, sin


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """

    def item(n):
        return (-1)**n * x**(2*n+1) / factorial(2*n+1)

    result = 0
    n = 0
    element = x
    while abs(element) >= DELTA:
        element = item(n)
        result += element
        n += 1

    return result

# def sinx2(x: Union[int, float]) -> float:
#     """
#      Вычисление sin(x) с помощью разложения в ряд Тейлора как в примере Peek Solution
#      """
#     def item(n):
#         """ Подсчет очередного элемента бесконечного ряда Тейлора для sin(x)"""
#         return (pow(-1, n)) * (pow(x, 2*n+1)/factorial(2*n+1))
#
#     sum_ = 0
#     for i in count():
#         current_value = item(i)
#         sum_ += current_value
#
#         if abs(current_value) <= DELTA:
#             return sum_

print(sinx(1.55433))
print(sin(1.55433))
print(sinx2(1.55433))


# while element <= DELTA:
#     element = (-1)**n * x**(2*n+1) / factorial(2*n+1)
#     n += 1
#     result += element
# while True:
#     element = (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1)
#     if element < DELTA:
#         n += 1
#         result += element
#     else:
#         break
# return result



