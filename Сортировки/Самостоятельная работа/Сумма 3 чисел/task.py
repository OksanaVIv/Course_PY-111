from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    support_set= []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = [nums[i], nums[j], nums[k]]
                    if set(trip) not in support_set:
                        support_set.append(set(trip))
                        result.append(trip)
    return result

if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))
