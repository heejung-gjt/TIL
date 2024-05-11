def solution(my_string, num1, num2):
    new_str = list(map(str, my_string))
    a = new_str[num1]
    b = new_str[num2]
    new_str[num1] = b
    new_str[num2] = a
    return ''.join(new_str)


def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)