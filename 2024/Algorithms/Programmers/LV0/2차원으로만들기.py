def solution(num_list, n):
    cnt = 0
    next_cnt = n
    answer = []

    while True:
        if next_cnt > len(num_list):
            break

        answer.append(num_list[cnt:next_cnt])
        cnt += n
        next_cnt += n

    return answer


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])