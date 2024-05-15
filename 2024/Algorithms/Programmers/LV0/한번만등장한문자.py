def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))


def solution(s):
    filtered_chars = filter(lambda x: s.count(x) == 1, s)
    return ''.join(sorted(filtered_chars))


def solution(s):
    return ''.join(sorted([ch for ch in s if s.count(ch) == 1]))