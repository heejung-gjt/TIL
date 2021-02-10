### 👉 Recursion (재귀함수)
__함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출이라고 한다__    
재귀호출은 알고리즘을 구현할때 매우 유용한 함수이다. 재귀호출이 사용되면 반드시 루프를 빠져나갈 조건이 있어야 한다.    
재귀함수는 같은 행위가 반복될때 사용된다(ex. 패토리얼, 피보나치, 누적합계 구하기...)
<br>

#### 재귀호출 사용해 hello() 생성하기
```python
def hello():
  print('Hello, World')
  hello()
hello()
```
#### 재귀호출 hello() 실행결과01 - RecursionError발생
재귀호출의 범위가 정해져 있기때문에 해당 문자열이 계속 출력되다가 범위를 초과하여 오류가 발생한 것이다.   
즉 , hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 RecursionError가 발생한다
```text
RecursionError Traceback (most recent call last)
<ipython-input-2-f4d5659d40d0> in <module>
      2     print('Hello, World')
      3     hello()
----> 4 hello()
<ipython-input-2-f4d5659d40d0> in hello()
      1 def hello():
      2     print('Hello, World')
----> 3     hello()
      4 hello()
... last 1 frames repeated, from the frame below ...
<ipython-input-2-f4d5659d40d0> in hello()
      1 def hello():
      2     print('Hello, World')
----> 3     hello()
      4 hello()
RecursionError: maximum recursion depth exceeded while calling a Python object
```
<br>

#### 재귀호출 hello() 재귀호출에 종료 조건 생성하기
```python
def hello(count):
    if count == 0:
        return
    
    print('hello,world')
    count-=1
    hello(count)
hello(5)
```
#### 재귀호출 hello() 실행결과01 - 정상적으로 출력
매개변수에 count를 파라미터로 지정하고 문장일 출력될때마다 count를 함수내에서 1씩 감소시켜준다. 감소시킨 count값을 다시hello의 매개변수에 알규먼트로 넣어 호출해준다. if문 조건으로 count값이 0이 될때 종료가 되는 것을 볼 수 있다
```text
hello(5)
hello,world
hello,world
hello,world
hello,world
hello,world
```
<br>

#### 🙌 재귀함수 이용한 실습

__1. Fibonacci Sequence (피보나치 수열)__   
첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두항의 합인 수열을 말한다.    
n의 수가 3보다 작으면 즉 0과 1인 경우 1을 반환해준다. 앞의 두항을 더해줄수 없기때문이다. 나머지는 앞의 두항을 더해준 값을
리턴해준다

```python:
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input())
print(fib(n))
```
<br>

__2. Factorial (팩토리얼)__   
0 이상의 정수 N을 받아서 N부터 (N-1)(N-2)...1까지 곱하는 문제이다.  
<br>

몇개의 수를 곱해줄 것인지 n으로 입력받는다. n=1인경우 1의 결과값을 반환하기때문에 return 1을 해준다. 나머지는 
n * fact(n-1)로 n!를 구현해준다. 
예) 5! -> 5 * 4 * 3 * 2 * 1     
5 * fact(5-1) -> fact(4)호출된다.    
4 * fact(4-1) -> fact(3)호출된다.    
3 * fact(3-1) -> fact(2)호출된다.   
2 * fact(2-1) -> fact(1)호출된다.    
fact(1) -> n의값 1이므로 return 1반환    
2 * fact(1) = 2반환    
3 * fact(2) = 6반환    
4 * fact(3) = 24반환    
5 * fact(4) = 120반환    

```python:
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
n = int(input())
print(fact(n))
```
