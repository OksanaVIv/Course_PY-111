from typing import Sequence
import random


def sort(arr:Sequence[int]) -> Sequence[int]:

    min_val = min(arr)
    max_val = max(arr)
    support_mass = {key: 0 for key in range(min_val, max_val + 1)}
    sorted_result = []

    for value in arr:
        support_mass[value] += 1

    for value, quant in support_mass.items():
        if quant > 0:
            a = [value for _ in range(0, quant)]
            sorted_result.extend(a)

    return sorted_result


if __name__ == "__main__":
    arr = [random.randint(13, 26) for _ in range(10 ** 6)]
    print(sort(arr))
