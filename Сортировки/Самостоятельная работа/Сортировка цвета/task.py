from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    # """
    # element_amount = len(nums)
    # while element_amount > 2:
    #     flag = 0
    #     for i in range(1, element_amount):
    #         if nums[i] < nums[i-1]:
    #             flag = 1
    #             nums[i], nums[i-1] = nums[i-1], nums[i]
    #     if flag == 0:
    #         return nums
    #     element_amount -= 1
    # return nums

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





if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    print(sort_сolors(arr))




    # low, mid, high = 0, 0, len(nums) - 1
    # while mid <= high:
    #     if nums[mid] == 0:
    #         nums[low], nums[mid] = nums[mid], nums[low]
    #         low += 1
    #         mid += 1
    #     elif nums[mid] == 1:
    #         mid += 1
    #     else:
    #         nums[mid], nums[high] = nums[high], nums[mid]
    #         high -= 1
    #
    # return nums