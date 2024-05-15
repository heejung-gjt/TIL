def solution(sides):
    answer = []
    max_num = max(sides)  # 2
    min_num = min(sides)  # 1

    for i in range(1, max_num + 1):
        if max_num < min_num + i:
            answer.append(i)
            
    for j in range(max_num + 1, sum(sides)):
        if sum(sides) > j:
            answer.append(j)
        
    return len(set(answer))
