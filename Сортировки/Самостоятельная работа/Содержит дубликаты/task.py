from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    print(set(nums))
    return len(nums) > len(set(nums))


    # if not nums:
    #     return None
    #
    # min_val = min(nums)
    # max_val = max(nums)
    # support_mass = {key: 0 for key in range(min_val, max_val + 1)}
    # result = []
    #
    # for value in nums:
    #     support_mass[value] += 1
    #
    # for value, quant in support_mass.items():
    #     if quant > 1:
    #         result.append(value)
    #
    # return result





if __name__ == "__main__":
    arr = [3,3,2]
    print(contains_duplicate(arr))