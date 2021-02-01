### 📌 List Comprehension
<br>

리스트 컴프리헨션은 반복되거나 특정한 조건을 만족하는 리스트를 쉽게 만들어 내기 위한 방법이다    
다음은 기본적인 구조이다. 결과 값을 가장 먼저 작성하고 for 다음으로 조건을 작성해준다. in 다음에는 반복가능한 개체가 출력된다 
```python
<result> for <element> in <iterable>
``` 
<br>

#### 아래 코드를 컴프리헨션을 이용해 바꾸어보자.

 ```python
 """
 코드설명 
 numbers list안에 들어가 있는 정수를 차례대로 꺼내어 새로운 리스트인 new_numbers에 삽입하는 코드이다
 """

 numbers == [1,2,3,4,5]
 new_numbers = []

 for i in numbers:
    new_numbers.append(i*2)
print(new_numbers)
 ```
 <br>

#### 👉 리스트 컴프리헨션을 이용   
확실히 코드가 간결해진것을 볼 수 있다


 ```python
 numbers = [1,2,3,4,5]
 new_numbers = [item*2 for item in numbers]
 print(new_numbers)
 ```
 <br>

 리스트 컴프리헨션에는 조건문도 들어갈 수 있다. 조건문이 들어가 있는 아래 코드를 컴프리헨션을 이용해 바꾸어보자

 #### 1. if문이 하나 있는 경우

  ```python
  """
 코드설명 
 numbers list안에 들어가 있는 정수를 차례대로 꺼내어 제곱한뒤 새로운 리스트인 new_numbers에 삽입한다. 
 """
numbers = [1,2,3,4,5]
new_numbers = []

for i in numbers:
    new_numbers.append(i*2)
print(new_numbers)
 ```
 <br>

 #### 👉 리스트 컴프리헨션을 이용    
 if문 하나가 쓰일 경우 if문을 코드의 맨 마지막에 작성한다

 ```python
numbers = [1,2,3,4,5]
new_numbers = [item**2 for item in numbers if item%2==0]
new_numbers
 ```
<br>

 #### 2. if문과 else문이 있는 경우
 ```python
  """
 코드설명 
 numbers list안에 들어가 있는 정수를 차례대로 꺼내어 새로운 리스트인 new_numbers에 삽입한다. 이때 numbers안에 있는 짝수의 경우엔 제곱으로 출력하는 코드이다
 """

 numbers = [1,2,3,4,5]
 new_numbers = []

 for i in numbers:
    if i%2 == 0:
        new_numbers.append(i**2)
    else:
        new_numbers.append(i)
print(new_numbers)
 ```
 <br>

 #### 👉 리스트 컴프리헨션을 이용   
 if문과 else문이 동시에 쓰일 경우 아래와 같은 형식으로 쓰인다.    
 [<if의 결과값> if <조건문> else <else의결과값> for <for문>]

 ```python
numbers = [1,2,3,4,5]
new_numbers = [i**2 if i%2==0 else i for i in numbers]
 print(new_numbers)
 ```
 <br>

 #### 3. if-elif-else문이 동시에 쓰일 경우 
```python
"""
코드설명 
fizzbuzz 문제. 15의 배수인경우, fizzbuzz출력, 3의 배수인경우 fizz 출력, 5의 배수인경우 buzz를 출력하고, 나머지는 해당 값을 출력하는 코드이다
"""
numbers = [i for i in range(1,100+1)] # 꿀팁 ! 컴프리헨션 이용해  1~100사이의 값 차례대로 출력하기
fizzbuzz_list=[]

for i in numbers:
    if i %15 ==0:
        fizzbuzz_list.append('fizzbuzz')
    elif i % 3 == 0:
        fizzbuzz_list.append('fizz')
    elif i % 5 == 0:
        fizzbuzz_list.append('buzz')
    else:
        fizzbuzz_list.append(i)
print(fizzbuzz_list)    

 ```
 <br>

 #### 👉 리스트 컴프리헨션을 이용   
 코드가 훨씬 단축되는 것을 볼 수 있다
```python
numbers = [i for i in range(1,100+1)]

fizzbuzz_list = ['fizzbuzz' if i%15=0 else 'fizz' if i%3==0 else 'buzz' if i%5==0 else i for i in numbers ]
```

<br>

### 📌 dictionary Comprehension

#### 1. 딕셔너리 컴프리헨션 - if문이 하나 있는 경우

```python
"""
코드설명
 글자수가 6자리 이상인것만 가지고 오는 코드
"""
 fruits = {'a':'apple','b':'banana','c':'coconut','d':'durian'}
six_fruits={}

for k,v in fruits.items():
    if len(v) >= 6:  #value의 값이 6보다 큰경우 딕셔너리에 넣어준다
        six_fruits[k]=v
print(six_fruits)
 ```
 <br>

 #### 👉 딕셔너리 컴프리헨션을 이용    
리스트 컴프리헨션과 비슷한 형식이다
 ```python
 fruits = {'a':'apple','b':'banana','c':'coconut','d':'durian'}
six_fruits={k:v for k, v in fruits.items() if len(v) >= 6}
 ```
<br>

 #### 2. if문과 else문이 있는 경우
 ```python
  """
 코드설명 
number_dict에 있는 딕셔너리 value값 중 3보다 작은값은 v**2 값을 출력하고 나머지는 v-1의 값을 출력하는 코드이다
 """
number_dict = {'pi':3.1415,'e':2.71828,'year':2021, 'month':2, 'day':1}
new_number_dict = {}
for k,v in number_dict.items():
    if v < 3:
        new_number_dict[k] = v**2
    else:
        new_number_dict[k] = v-1
new_number_dict
 ```
 <br>

 #### 👉 딕셔너리 컴프리헨션을 이용   
앞에서부터 해석을 해보면 ```key값과 v의제곱값을 출력한다. 만약 v가 3보다 작다면 또는 v-1을 출력한다. number_dict안에 있는 이터러블한 값들을 반복하면서 ```
 ```python
number_dict = {'pi':3.1415,'e':2.71828,'year':2021, 'month':2, 'day':1}
new_number_dict = {k:v**2 if v<3 else v-1 for k,v in number_dict.items()}
new_number_dict
 ```
 <br>

 #### 3. if-elif-else문이 동시에 쓰일 경우 
```python
"""
코드설명 
fizzbuzz 문제. 15의 배수인경우, fizzbuzz출력, 3의 배수인경우 fizz 출력, 5의 배수인경우 buzz를 출력하고, 나머지는 해당 값을 출력하는 코드이다
"""
numbers = [i for i in range(1,100+1)] # 꿀팁 ! 컴프리헨션 이용해  1~100사이의 값 차례대로 출력하기
fizzbuzz_list=[]

for i in numbers:
    if i %15 ==0:
        fizzbuzz_list.append('fizzbuzz')
    elif i % 3 == 0:
        fizzbuzz_list.append('fizz')
    elif i % 5 == 0:
        fizzbuzz_list.append('buzz')
    else:
        fizzbuzz_list.append(i)
print(fizzbuzz_list)    

 ```
 <br>

 #### 👉 리스트 컴프리헨션을 이용   
 코드가 훨씬 단축되는 것을 볼 수 있다
```python
numbers = [i for i in range(1,100+1)]

fizzbuzz_list = ['fizzbuzz' if i%15=0 else 'fizz' if i%3==0 else 'buzz' if i%5==0 else i for i in numbers ]
```
