def solution(my_string, s, e):
    a = list(my_string)
    b = a[s:e + 1]
    b.reverse()
    a[s:e + 1] = b
    return ''.join(a)



# sol1
#def solution(my_string, s, e):
#    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]