from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """

    if len(seq) == 0:
        raise ValueError ("Последовательность пуста")

    left_border = 0;
    right_border = len(seq) - 1
    while left_border <= right_border:
        middle_index = left_border + (right_border - left_border) // 2
        middle_value = seq[middle_index]
        if middle_value == value:
            while 0 <= middle_index - 1 <= len(seq) and seq[middle_index - 1] == value:
                middle_index -= 1
            return middle_index
        if middle_value < value:
            left_border = middle_index + 1
        if middle_value > value:
            right_border = middle_index - 1
    raise ValueError ("Элемент не найден")

