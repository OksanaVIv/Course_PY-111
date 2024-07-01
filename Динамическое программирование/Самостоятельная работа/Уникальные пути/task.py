def unique_paths(m: int, n: int) -> int:
    field = [[0] * n for i in range(m)]
    field[0][0] = 1

    for i in range(1,n):
        field[0][i] = 1

    for i in range(1, m):
        field[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            field[i][j] = field[i-1][j] + field[i][j-1]
    return field[-1][-1]



if __name__ == '__main__':
    paths = unique_paths(3, 7)
    print(paths)