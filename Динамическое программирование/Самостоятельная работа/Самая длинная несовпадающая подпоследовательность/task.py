from typing import List


def is_subsequence(a: str, b: str) -> bool:
    for i in range(len(a)-1):
        indx = b.find(a[i])
        indx1 = b.find(a[i+1])
        if indx > indx1:
            return False
    return True

    element_amount = len(container)
    while element_amount > 2:
        flag = 0
        for i in range(1, element_amount):
            if container[i] < container[i-1]:
                flag = 1
                container[i], container[i-1] = container[i-1], container[i]
        if flag == 0:
            return container
        element_amount -= 1
    return container
def find_lus_length(strs: List[str]) -> int:
    len_strs = {}
    for i in strs:
        index = i
        value = len(i)
        len_strs.update({index: value})
    return max(len_strs.values())


if __name__ == '__main__':
    strs = ["aba","cdc","eae"]
    print(find_lus_length(strs))

