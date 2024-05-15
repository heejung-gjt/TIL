def solution(order):
    answer = 0
    dic = [3, 6, 9]
    new_order = list(map(int, str(order)))
    
    for i in new_order:
        if i in dic:
            answer += 1

    return answer


def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')



def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))


def solution(order):
    return sum([str(order).count(n) for n in '369'])