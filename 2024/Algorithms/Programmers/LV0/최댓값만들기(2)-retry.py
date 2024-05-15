def solution(numbers):
    answer = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if answer is None:
                answer = numbers[i] * numbers[j]

            elif answer < numbers[i] * numbers[j]:
                answer = numbers[i] * numbers[j]
    return answer


def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
