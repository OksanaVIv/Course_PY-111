from typing import List


def generate(num_rows: int) -> List[List[int]]:
    if not num_rows:
        return []

    p_table = [[0] * i for i in range(1, num_rows+1)]
    p_table[0] = [1]

    for i in range(1, num_rows):
        for j in range(i+1):
            if j-1 < 0:
                part2 = 0
            else:
                part2 = p_table[i-1][j-1]
            if j == i:
                part1 = 0
            else:
                part1 = p_table[i - 1][j]
            p_table[i][j] = part1 + part2
    return p_table


if __name__ == '__main__':
    print(generate(5))  # 7

