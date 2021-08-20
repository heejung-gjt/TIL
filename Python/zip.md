## zip 함수
zip(*iterable)함수는 동일한 개수로 이루어진 반복 가능한 자료형을 묶어주는 역할을 하는 함수이다    

```python
list(zip([1,2,3],[4,5,6]))

# [(1,4),(2,5),(3,6)]
```

zip을 이용해서 딕셔너리를 만들 수도 있다
```python
number = [1,2,3,4]
name = ['son','han','park','kim']
dic = {}

for number, name in zip(number,name):
  dic[number] = name

# {1 : 'son' , 2 : 'han' , 3 : 'park' , 4 : 'kim'}
```

묶었던 데이터를 다시 해체할 수 도 있다. 이땐 zip()함수앞에 unpacking연산자를 붙여서 풀어준다
```python
number = [1,2,3]
letter = ['a','d','c']

zips = list(zip(number,letter))
print(zips) # [(1, 'a'), (2, 'd'), (3, 'c')]
 
num , let = zip(*zips)
print(num) # (1,2,3)
print(let) # ('a','b','c')
```