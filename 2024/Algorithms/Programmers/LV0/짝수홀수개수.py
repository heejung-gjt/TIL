def solution(num_list):
    answer = []
    e = 0
    a = 0
    for i in num_list:
        if i % 2 == 0:
            e += 1
        else:
            a += 1
    return [e, a]



def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer