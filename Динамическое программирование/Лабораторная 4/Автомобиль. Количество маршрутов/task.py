from typing import List
import pprint

def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    if n <= 0 or m <= 0:
        raise ValueError("значение не может быть отрицательно или равно 0")

    table_route = [[0] * m for i in range(n)]
    table_route[0][0] = 1

    for i in range(1, n):
        table_route[i][0] = 1

    for j in range(1, m):
        table_route[0][j] = 1

    for i in range(1, n):
        for j in range (1, m):
            # if i == j:
            table_route[i][j] = table_route[i-1][j] + table_route[i][j-1] + table_route[i-1][j-1]

    return table_route


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7



