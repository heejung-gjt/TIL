def solution(emergency):
    dic = {}
    answer = []
    for i, j in enumerate(sorted(emergency, reverse=True)):
        dic[j] = i + 1

    for i in emergency:
        answer.append(dic[i])
    return answer


def solution(emergency):
    answer = []
    a = {j: i+1 for i, j in enumerate(sorted(emergency, reverse=True))}

    for i in emergency:
        answer.append(a[i])
    return answer


"""
index쓰면 시간복잡도 더 커짐 (O(n**2))
"""
def solution(emergency):
    sort = sorted(emergency, reverse=True)
    return [sort.index(i) + 1 for i in emergency]