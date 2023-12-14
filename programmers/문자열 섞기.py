def solution(str1, str2):
    answer = ''
    for i, j in zip(str1, str2):
        answer += i  # res+=s1+s2
        answer += j
    return answer