from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """

    x = shape[0]
    y = shape[1]
    play_table = [None * y for i in range(x)]
    play_table[0][0] = 1
    step = play_table[0][0]
    i = 0
    j = 0
    for i <= x-1 and j <= y-1:
        play_table[i],[j] = min[i-]




    if step is not None:
        play_table[i+2][j-1] = step + 1

    path =
if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
