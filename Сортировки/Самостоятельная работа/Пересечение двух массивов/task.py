from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    for item in set(nums1):
        if item in set(nums2):
            result.append(item)
    return result

if __name__ == "__main__":
    a = [1,2,2,1]
    b = [2,2]
    print(intersection(a, b))