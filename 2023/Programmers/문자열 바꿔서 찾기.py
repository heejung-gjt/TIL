def solution(myString, pat):
    answer = 0

    new_string = ''
    for char in myString:
        if char == 'A':
            new_string += 'B'
        elif char == 'B':
            new_string += 'A'
        else:
            new_string += char

    if pat in new_string:
        answer = 1

    return answer


# sol1
def solution(myString, pat):
    answer = 0

    myString = myString.replace('A', 'C').replace('B', 'A').replace('C', 'B')

    if pat in myString:
        answer = 1

    return answer


# sol2
def solution(myString, pat):
    answer = 0

    pat = pat.replace('A', 'C').replace('B', 'A').replace('C', 'B')

    if pat in myString:
        answer = 1

    return answer
