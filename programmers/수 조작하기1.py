def solution(n, control):
    condition = {'w': 1, 's': -1, 'd': 10, 'a': -10}

    for i in control:
        n += condition[i]
    return n

# sol1
#def solution(n, control):
#    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
#    return n + sum([key[c] for c in control])