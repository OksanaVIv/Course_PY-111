def is_subsequence(s: str, t: str) -> bool:
    for i in range(len(s)-1):
        indx = t.find(s[i])
        indx1 = t.find(s[i+1])
        if indx > indx1:
            return False
    return True


if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    print(is_subsequence(s, t))