def solution(i, j, k):
    return sum(list(map(lambda x: str(x).count(f'{k}'), range(i, j + 1))))


def solution(i, j, k):
    return sum(map(lambda x: str(x).count(f'{k}'), range(i, j + 1)))


def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer


def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        answer += str(num).count(f'{k}')
    return answer


