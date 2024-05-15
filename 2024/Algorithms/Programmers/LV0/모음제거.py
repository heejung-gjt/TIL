def solution(my_string):
    for i in my_string:
        if i in ['i', 'a', 'o', 'e', 'u']:
            my_string = my_string.replace(i, '')
    return my_string



def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])