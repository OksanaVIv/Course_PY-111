from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container


    min_val = min(container)
    max_val = max(container)
    # data = {key: 0 for key in range(min_val,max_val+1)}
    data = {key: [] for key in range(min_val, max_val + 1)}


    # TODO реализовать алгоритм сортировки подсч
    sorted_result = []

    for value in container:
        # if value in data:
        #     data[value] += 1
        data[value].append(value)
        # else:
        #     data[value] = 1

    # for key, value in data.items():
    #     for _ in range(value):
    #         sorted_result.append(key)
    for value in data.value():
       if value:
           sorted_result.extend(value)
        #     for _ in range(value):
        #         sorted_result.append(key)

    return sorted_result


if __name__ = "__main__"

