def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    box = []
    # for item in brackets_row:
    #     if item == "(":
    #         box.append(item)
    #     else:
    #         if box:
    #             box.pop()
    #         else:
    #             box.append(item)
    #             break
    #
    # if len(box) == 0:
    #     return True
    # return False

    for item in brackets_row:
        if item == "(":
            box.append(item)
        elif item == ")" and len(box) > 0:
            box.pop()
        else:
            box.append(item)
            break

    if len(box) == 0:
        return True
    return False



if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
