def solution(a, b):
    cnt = 0
    while a != 1:
        i, j = divmod(a, b)
        if not j:
            a = i
        else:
            a -= 1

        cnt += 1

    return cnt



print(solution(a=int(input()), b=int(input())))