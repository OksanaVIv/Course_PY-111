from typing import List
import random
def partition (arr, low=0, high=None):

    if high is None:
        high = len(arr)-1

    pivot = arr[high]
    i = low - 1
    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """

    def _sort(container, low, high):
        if len(container) == 0 or len(container) == 1:
            return container
        if low < high:
             pivot_index = partition(container, low, high)
             _sort(container, low, pivot_index - 1)
             _sort(container, pivot_index + 1, high)# TODO реализовать алгоритм быстрой сортировки
    return _sort(container, 0, len(container)-1)



if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(4)]
    # print(partition(arr))
    # print(arr)
    a = sort(arr)
    print(a)
    # b = sorted(arr)
    # print(b)
