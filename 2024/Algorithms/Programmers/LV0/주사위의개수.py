def solution(box, n):
    answer = 1
    for i in range(0, len(box)):
        answer *= (box[i] // n)

    return answer


def solution(box, n):
    x, y, z = box
    return x // n * y // n * z // n


def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n

    return answer