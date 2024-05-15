from functools import reduce

def solution(n):
    answer = []
    n2 = n
    a = 2
    while True:

        if answer and reduce(lambda x,y: x*y, answer) == n:
            break

        if n2 % a == 0:
            answer.append(a)
            n2 = n2 // a

        else:
            a += 1

    return sorted(list(set(answer)))



def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n = n // d
            if d not in answer:
                answer.append(d)

        else:
            d += 1

    return answer