from collections import deque


def solution(numbers, k):
    queue = deque(numbers[::-1])

    for _ in range(k - 1):
        for _ in range(2):
            queue.appendleft(queue.pop())

    return queue.pop()


def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]


from collections import deque
def solution(numbers, k):
    array = deque(numbers)

    array.rotate(-(k-1)*2)

    return array[0]