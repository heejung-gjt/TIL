def binary_arr(L, x):
    answer = 0
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            answer = middle
            return answer
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
    if lower > upper:
        return -1
    # return answer

answer = binary_arr([1,4,6,8,10,23,45,65,78,99,100],78)
print(answer)