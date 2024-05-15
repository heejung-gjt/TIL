def solution(numbers):
    answer = ''
    dic = {
        "one":'1', "two":'2',"three":'3',
        "four":'4', "five":'5', "six":'6',
        "seven":'7', "eight":'8', "nine":'9', "zero":'0', 
    }
    for k, v in dic.items():
        if k in numbers:
            numbers = numbers.replace(k, v)
    return int(numbers)




def solution(numbers):
    for n, e in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(e, str(n))

    return int(numbers)


