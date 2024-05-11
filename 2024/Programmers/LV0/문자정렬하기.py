from re import sub


def solution(my_string):
    return sorted(list(map(int, sub('[^0-9]', '', my_string))))


def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])