def solution(num_list):
    res = 1
    for i in num_list:
        res *= i
    return 0 if res > (sum(num_list) * sum(num_list)) else 1


# sol1
#def solution(num_list):
#    s=sum(num_list)**2
#    m=eval('*'.join([str(n) for n in num_list]))
#    return 1 if s>m else 0