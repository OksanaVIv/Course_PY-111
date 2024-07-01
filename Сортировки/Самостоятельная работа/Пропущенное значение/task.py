from typing import List


def missing_number(nums: List[int]) -> int:
    if not nums:
        return None

    for item in range(0, len(nums)+1):
        if item not in nums:
            return item


if __name__ == "__main__":
    a = [0,1,3]
    print(missing_number(a))

