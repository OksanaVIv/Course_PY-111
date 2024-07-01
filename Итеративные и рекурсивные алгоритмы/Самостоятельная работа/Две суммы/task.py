from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for idx1, value1 in enumerate(nums):
        for idx2, value2 in enumerate(nums):
            if value1 + value2 == target and idx1 != idx2:
                return [idx1, idx2]  # Сложность данного варианта 0(n^2)

    # 3, 5, 8, 0 , 4
    # # target = 4
    # # 4-3 = 1; 4-5 = -1; 4-8 = -4, 4-0 = 4; 4-4 = 0
    # # {1:0, -1:1, -4:2, 4:3, 0:4}


def two_sum_2(nums: List[int], target: int) -> List[int]:
    result_dict = {}
    for idx, value in enumerate(nums):
        result_dict[target - value] = idx

    for idx, value in enumerate(nums):
        if value in result_dict and result_dict[value] != idx:
            return result_dict[value], idx

    return result_dict


if __name__ == '__main__':
    print(two_sum_2([3, 5, 8, 0, 4], 4))
