def solution(sides):
    sides.sort()
    return 2 if (sides.pop() - sum(sides)) >= 0 else 1


def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2