def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(str(my_str[i:i+n]))
    return answer


def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]