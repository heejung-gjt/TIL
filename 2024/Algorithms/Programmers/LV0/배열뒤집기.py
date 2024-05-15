def solution(num_list):
    return [num_list[i] for i in range(-1, -(len(num_list) + 1), -1)]



def solution(num_list):
    return num_list[::-1]


def solution(num_list):
    num_list.reverse()
    return num_list


print(solution([1,2,4,1,9]))

