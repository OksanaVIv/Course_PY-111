from typing import List


def majority_element(nums: List[int]) -> int:
    majority_element = None
    counter = 0

    for element in nums:
        if counter == 0:
            majority_element = element
            counter = 1
        elif element == majority_element:
            counter += 1
        else:
            counter -= 1

    return majority_element


if __name__ == "__main__":
    arr = [3, 1, 3, 0, 3, 3, 7, 4, 3]
    print(majority_element(arr))




