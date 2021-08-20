### list slicing
 
 리스트에서도 슬라이싱이 가능하다
 
 ```python
# a[start:stop:step]
a = [1, 2, 3, 4, 5, 6]

print(a[2:4]) # [3, 4]
print(a[1:]) # [2, 3, 4, 5, 6]
print(a[:1]) # [1]
print(a[:-1]) # [1, 2, 3, 4, 5]
print(a[-1:]) # [6]
print(a[::1]) # [1, 2, 3, 4, 5, 6]
print(a[::-1]) # [6, 5, 4, 3, 2, 1]
print(a[1::]) # [2, 3, 4, 5, 6]
 ```