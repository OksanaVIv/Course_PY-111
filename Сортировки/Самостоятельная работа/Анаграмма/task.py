def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for item in s:
        a = s.count(item)
        b = t.count(item)
        if a != b:
            return False
    return True

if __name__ == "__main__":
    a = ""
    b = ""
    print(is_anagram(a, b))