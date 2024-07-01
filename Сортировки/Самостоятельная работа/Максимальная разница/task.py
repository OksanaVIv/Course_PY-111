from typing import List


def maximum_gap(nums: List[int]) -> int:
    if not nums:
        return None


    nums.sort()
    res = 0

    for i in range(len(nums)-1):
        if res < nums[i+1] - nums[i]:
            res = nums[i+1] - nums[i]

    return  res



if __name__ == "__main__":
    nums = []
    print(maximum_gap(nums))



