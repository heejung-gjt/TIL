def solution(n, k):
    service_cnt = int(n // 10)
    return (n * 12000) + (k * 2000) - (service_cnt * 2000)


def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)