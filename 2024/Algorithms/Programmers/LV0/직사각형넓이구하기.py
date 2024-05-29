def solution(dots):
    dots.sort(key=lambda x: (x[0], x[1]))

    x = abs(dots[2][0] - dots[0][0])
    y = abs(dots[1][1] - dots[0][1])
    return x * y


'''
another
'''
def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    w = max(x) - min(x)
    h = max(y) - min(y)

    return w * h


def solution(dots):
    w = max(dots)[0] - min(dots)[0]
    y = max(dots)[1] - min(dots)[1]

    return w * y