"""
큐사용 많이 함
"""
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in range(len(numbers) - 1):
            answer.append(numbers[i])
    else:
        sub_answer = []
        sub_answer.append(numbers[0])
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.extend(sub_answer)

    return answer


from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    if direction == 'right':
        queue.appendleft(queue.pop())
        return list(queue)
    queue.append(queue.popleft())
    return list(queue)


from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)

    return list(numbers)



def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
