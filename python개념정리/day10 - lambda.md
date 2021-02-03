## 👉 lambda 함수   

람다 함수는 함수를 보다 간편하게 작성해주며 사용된 후 버려지는 함수이다. __함수가 생성되는 곳에서만 필요하고__ 정의를 해서 쓰는 것이 아닌 필요한 곳에 사용 후 버려진다.

```python
def get_next_integer(i):
    return i+1
get_next_integer(10)

# 결과 11
```
다음 함수를 lambda를 이용하여 작성해본다
```python
 (lambda a:a+1)(10)  # 매개변수 a를 하나받고 a에 1을 더해서 값을 반환한다
 # 결과 11

 (lambda a,b a+b+1)(10,11)
 # 결과 22
```
<br>

### lambda함수 map()과 함께 쓰기
map은 두개의 인수를 가지고 있다    
```python
r = map(함수, 반복가능한 객체 (list, str, tuple))
```
<br>

### ✔ 실습01
정수 1-10 리스트의 각 값이  1씩 증가하는 코드

1.리스트컴프리헨션을 이용하여 작성
```python
number = [i for i in range(1,10+1) ]
number_list = [i+1 for i in number]
number_list

# 결과 :[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```
<br>

2.리스트컴프리헨션 + map()을 이용하여 작성

```python
def number_sum(a):
    return a+1

number = [i for i in range(1,10+1)]
list(map(number_sum, number))

# 결과 :[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```
<br>

3.lamda함수를 이용하여 작성
```python
number = [i for i in range(1,10+1)]
list(map(lambda a:a+1, number))

# 결과 :[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```
* * *

### ✔ 실습02
정수 1-10 리스트의 각 값이 제곱으로 증가하는 코드

1.for문과 함수를 이용하여 작성   

```python
def get_squared(num_list):
    result=[]
    for i in num_list:
        result.append(i**2)
    return result
numbers = [i for i in range(1,10+1)]
get_squared(numbers)
# 결과 :[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
<br>

2.map()을 이용하여 작성

```python
def get_squared(num_list):
    return num_list**2

numbers = [i for i in range(1,11)]
list(map(get_squared,numbers))

# 결과 :[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
<br>

3.lamda함수를 이용하여 작성
```python
numbers = [i for i in range(1,11)]
list(map(lambda a:a**2, numbers))

# 결과 :[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
