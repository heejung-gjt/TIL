def solution(hp):
    li = [5, 3, 1]
    answer = 0
    index = 0
    while True:
        cnt = int(hp // li[index])
        answer += cnt
        hp -= (cnt * li[index])

        if hp == 0:
            break

        index += 1

    return answer


def solution(hp):
    answer = 0
    for i in [5, 3, 1]:
        d, hp = divmod(hp, i)
        answer += d

    return answer


def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)