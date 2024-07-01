from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком
    element_amount = len(container)
    while element_amount > 2:
        flag = 0
        for i in range(1, element_amount):
            if container[i] < container[i-1]:
                flag = 1
                container[i], container[i-1] = container[i-1], container[i]
        if flag == 0:
            return container
        element_amount -= 1
    return container


if __name__ == "__main__":
    arr = [1, 3, 0, 7, 4]
    print(sort(arr))

