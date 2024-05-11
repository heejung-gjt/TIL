def solution(num, k):
    answer = list(map(int, str(num)))
    if k not in answer:
        return -1
    return answer.index(k) + 1


def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1


def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
