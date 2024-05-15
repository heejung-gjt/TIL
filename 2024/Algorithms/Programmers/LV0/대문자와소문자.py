def solution(my_string):
    new_string = ''
    for i in my_string:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        new_string += i
        
    return new_string


def solution(my_string):
    return my_string.swapcase()


def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
