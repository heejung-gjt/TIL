"""
테스트케이스 58.3점
"""
def solution(score):
    avg_list = list(map(lambda x: (x[0] + x[1]) // 2, score))
    sort_score = sorted(avg_list, reverse=True)

    avg_str = ','.join(map(str, avg_list))
    for i, j in enumerate(sort_score):
        avg_str = avg_str.replace(f"{j}", f"{i + 1}")

    return list(map(int, avg_str.split(',')))



"""
풀이
"""
def solution(score):
    avg_list = list(map(lambda x: (x[0] + x[1]) / 2, score))
    sort_score = sorted(avg_list, reverse=True)
    new_dict = {}
    number = 1

    while sort_score:
        max_value = max(sort_score)
        
        if max_value not in new_dict:
            new_dict[max_value] = number

        number += 1
        sort_score.remove(max_value)
        
    answer = []
    for i in avg_list:
        answer.append(new_dict[i])
        
    return answer


"""
another
"""

# 의도가 비슷한 방식
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]


# 이해 안감
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
