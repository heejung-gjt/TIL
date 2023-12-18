def solution(n):
    r = 0
    if n % 2 == 0:  # 짝수
        for i in range(2, n + 1, 2):
            r += (i * i)

    else:
        for i in range(1, n + 1, 2):
            r += i
    return r


# sol 1
# return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)