def schitalka(N:int, k:int) -> int:
    people = [x for x in range(1, N+1)]

    while len(people) > 1:
        if k > len(people):
            B = k % len(people)
            people.pop(B-1)
        elif k <= len(people):
            people.pop(k-1)

    return people


if __name__ == "__main__":
    a = schitalka(5, 6)
    print(a)






