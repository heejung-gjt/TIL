def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append((i, i//n))
    return len(answer)


def solution(n):
    answer =0  
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer


def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))