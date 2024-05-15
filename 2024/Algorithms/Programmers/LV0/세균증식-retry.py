### retry
"""
- 240506 [v]
"""

def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2

    return answer


def solution(n, t):
    answer = 2**t * n
    return answer