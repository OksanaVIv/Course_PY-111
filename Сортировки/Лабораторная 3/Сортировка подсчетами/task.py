from typing import Sequence

       # TODO реализовать алгоритм сортировки подсчетами



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
    support_mass = {key: 0 for key in range(min_val, max_val + 1)}

    sorted_result = []

    for value in container:
        support_mass[value] += 1

    for value, quant in support_mass.items():
        if quant > 0:
            a = [value for _ in range(0, quant)]
            sorted_result.extend(a)

    return sorted_result


if __name__ == "__main__":
    arr = []
    print(sort(arr))





