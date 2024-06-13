from typing import List


def merge(left:list, right:list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort(container: List[int]) -> List[int]: # Сортировка будет вызываться столько раз, сколько всего эл-тов
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив

    Если без рекурсии, то надо исп-ть while


    """

    if len(container) <= 1:    # TODO реализуйте сортировку слиянием
        return container

    middle = len(container) // 2
    left = sort(container[:middle])
    right = sort(container[middle:])
    return merge(left, right)


if __name__ == "__main__":
    print(merge([3,5,5], [1,6]))
    print(sort([3, 5, 5, 1, 6]))
