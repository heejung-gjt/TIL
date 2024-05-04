def solution(num_list):
    answer = 0
    odd = ''
    eval = ''
    for i, j in enumerate(num_list):
        if int(num_list[i]) % 2 == 0:
            odd += str(num_list[i])
        else:
            eval += str(num_list[i])
    return int(odd) + int(eval)