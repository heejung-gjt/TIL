import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)    
    
    return sum(list(map(lambda x: int(x), numbers)))



def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())