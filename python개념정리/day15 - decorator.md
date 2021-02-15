### 👉 Decorator

function의 앞, 뒤로 해야 할 일이나 로깅 벤치마킹 등 다양한 용도로 쓰일 수 있다. 데이터 전처리 과정 또한 미리 정의해둔뒤 붙여서 사용할 수 있다.   

함수를 받아 명령을 추가하고 다시 함수의 형태로 반환해준다. 함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을때 사용한다.   

#### decorator 구조
```python
def decorator_name(func): #기능을 추가할 함수를 인자로 받는다
    def inner_function_name(*args, **kwargs):
        기존함수에 추가할 내용
        return func(*args, **kwargs)
    return inner_function_name
```
<br>

### 👉 데코레이터 실습01

my name is heejung의 내용이 나오기전에 hello라는 문장이 들어있는 wrapper함수를 먼저 호출해주고 introduce함수를 return해준다

```python
def introduce(name):
    print(f'My name is {name}!')  # *args, **kwargs는 관습적인 표현 ! 굳이 쓰지 않아도 된다

def decorator(func):
    def wrapper(name):
        print('hello')
        return func(name)
    return wrapper

decorator_hello = decorator(introduce)
decorator_hello('heejung')

"""
결과

hello
My name is heejung!
"""

```

__@decorator을 이용하여 실습01과 동일하게 나타낼 수 있다.__ @decorator == decorator_hello = decorator(introduce)의 역할과 동일하다  

```python
def decorator(func):
    def wrapper(name):
        print('hello')
        return func(name)
    return wrapper

@decorator
def introduce(name):
    print(f'my name is {name}!')

introduce('heejung')
"""
결과

hello
My name is heejung!
"""
```
<br>

### 👉 앞뒤로 원하는 값 추가 실습02
```python
import date
def date_time_decorator(func):
    def wrapper():
        print(str(datetime.datetime.now()))
        func()
        print(str(datetime.datetime.now()))
    return wrapper

@date_time_decorator
def login():
    print('heejung login')
login()

"""
결과 :

2021-02-15 22:25:39.986438
heejung login
2021-02-15 22:25:39.988109
"""
```
<br>

### 👉 @데코레이터 실습03
리커전 함수에 데코레이터 쓸때 반복을 없애주는 방법은 def fibo_rec위에
붙어있는 @time_checker를 떼어주고 따로 출력할때 ```time_checker(fibo_rec)(10)```으로 출력해주면 마지막 결과값만 볼 수 있다

```python
from time import time

def time_checker(func):
    def wrapper(seq):
        start_at = time()
        result = func(seq)
        end_at = time()
        print('execution time: {}sec'.format(end_at-start_at))
        return result

    return wrapper

@time_checker
def fibo_rec(num):
    if num < 2:
        return num
    else:
        return fibo_rec(num-2) + fibo_rec(num-1)

fibo_rec(10)

"""
결과
execution time: 2.384185791015625e-07sec
execution time: 4.76837158203125e-07sec
execution time: 0.0002911090850830078sec
execution time: 2.384185791015625e-07sec
execution time: 2.384185791015625e-07sec
execution time: 2.384185791015625e-07sec
execution time: 4.76837158203125e-05sec
execution time: 9.918212890625e-05sec
execution time: 0.0005664825439453125sec
execution time: 0.0sec
execution time: 2.384185791015625e-07sec
.
.
.

"""
```
<br>

### 👉 데코레이터 실습04    

Hi, {name}. You might be loved with {lang}" 이라는 문자열이 존재할 때, 이 문자열의 앞 뒤로 < h1 >,< em > 태그가 붙도록 하는 데코레이터를 생성해라    


```python
def em(func):
    def wrapper1(one,two):
        print('<em>',end=' ')
        func(one,two)
        print('</em>',end=' ')
    return wrapper1
    
def h1(func):
    def wrapper2(one,two):
        print('<h1>',end=' ')
        func(one,two)
        print('</h1>')
    return wrapper2

@h1
@em
def inner(name,lang):
    print(f'Hi {name}. You might be loved with {lang}',end=' ')
    
    
inner('heejung','pyton')
```
<br>

Advanced problem: Decorator 하나로 html 태그 이름을 지정할 수 있도록 위의 코드를 수정해보자

```python
진행중.....
```
<br>

### 👉 @memoize
메모이제이션은 이전에 계산한 값을 메모리에 저장하여 동일한 계산의 반복 수행을 제거해준다.   
(memoize 예 찾아보기.......)
```python
def memoize(func):
    memo = {}
    def wrapper(seq):
        if seq not in memo:            
            memo[seq] = func(seq)
        return memo[seq]
    return wrapper
    
@memoize
def fib_memo(num):
    if num<2:
        return num
    else:
        return fib_memo(num-1) + fib_memo(num-2)
```
<br>