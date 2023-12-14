def solution(a, b):
    answer = f"{a}{b}" if int(f"{a}{b}") > int(f"{b}{a}") else f"{b}{a}"
    return int(answer)

# sol1
#return int(max(f"{a}{b}", f"{b}{a}"))