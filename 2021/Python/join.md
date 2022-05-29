## join()
join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 주는데 이때 ''안에 구분자가 들어가 있으면 해당 구분자가 요소 하나하나를 구분하는 기호가 된다
> ''.join(리스트)
> '구분자'.join(리스트)

```python
a = ['a', 'b', 'c', 'd', 'f', 'g']
print(''.join(a)) # abcdfg
print(' '.join(a)) # a b c d f g
print(','.join((a))) # a,b,c,d,f,g
print('\n'.join(a)) 
"""
a
b
c
d
f
g
"""
```
### 정수형 list join하기
join을 쓸 때 리스트 안의 값이 int형일 경우 map을 통해 문자열 type으로 변경한 후에 사용해야 한다
```python
num_list = [1, 2, 3, 4, 5, 6, 7]
print(''.join(map(str, num_list))) # 1234567
```