def solution(array, n):
    sorted(array)
    if len(array) == 1:
        return array[0]

    answer = array[0]
    for i in range(1, len(array)):
        if abs(answer - n) > abs(array[i] - n):
            answer = array[i]

        elif abs(answer - n) == abs(array[i] - n):
            answer = answer if (answer - n) < (array[i] - n) else array[i]

    return answer


def solution(array, n):
    array.sort(key=lambda x:(abs(x-n), x-n))
    return array[0]