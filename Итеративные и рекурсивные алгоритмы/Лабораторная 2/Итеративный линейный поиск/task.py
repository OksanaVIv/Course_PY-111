"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if len(arr) == 0:
        raise ValueError('Последовательность пуста')

    min_ = arr[0]
    for indx in range(1, len(arr)):
        if arr[indx] < min_:
            min_ = arr [indx]
    indx = 0
    while arr[indx] != min_:
        indx += 1
    return indx


