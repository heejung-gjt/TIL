from re import sub
def solution(my_string):
    return sum(list(map(int, sub('[a-z A-Z]', '', my_string))))


def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])