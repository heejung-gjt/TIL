def solution(ineq, eq, n, m):
    if ineq == '<' and eq == '=':
        return 1 if n <= m else 0
    elif ineq == '>' and eq == '=':
        return 1 if n >= m else 0
    elif ineq == '<' and eq == '!':
        return 1 if n < m else 0
    elif ineq == '>' and eq == '!':
        return 1 if n > m else 0

    
# sol1
#def solution(ineq, eq, n, m):
#    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

# sol2
#def solution(ineq, eq, n, m):
#    answer = 0
#    if n > m and ineq ==">":
#        answer = 1
#    elif n < m and ineq == "<":
#        answer = 1
#    elif n == m and eq == "=":
#        answer = 1

    # return answer