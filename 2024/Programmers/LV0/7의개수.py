def solution(array):
    cnt = 0
    for i in array:
        cnt += str(i).count('7')


    return cnt


def solution(array):
    return sum(map(lambda x: str(x).count('7'), array))



def solution(array):
    return str(array).count('7')