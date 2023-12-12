def solution(arr, n):
    answer = []

    if len(arr) % 2 == 0: # 짝수
        for i, j in enumerate(arr):
            if i % 2 != 0:
                j = j + n
            answer.append(j)

    else: # 홀수
        for i, j in enumerate(arr):
            if i % 2 == 0:
                j = j + n
            answer.append(j)

    return answer


# sol1
def solution(arr, n):
    if len(arr) % 2 == 0: # 짝수
        for i in range(1, len(arr), 2):
            arr[i] += n

    else: # 홀수
        for i in range(0, len(arr), 2):
            arr[i] += n

    return arr