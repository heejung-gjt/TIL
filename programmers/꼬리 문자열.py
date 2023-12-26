def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer


# sol1
#def solution(str_list, ex):
#    filtered_list = [s for s in str_list if ex not in s]
#    return "".join(filtered_list)
