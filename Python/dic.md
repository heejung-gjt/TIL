## 딕셔너리 value값으로 key값 구하기 

#### ⚡삽질 기록    

- key값으로 value값 구하는 건 알았지만 value값으로 key값 구하는건 모르고 있었다   
- for문의 반복문이 아직까지 헷갈린것도 한몫했다
- 리스트에서 불필요한 문자를 삭제하는 옵션 replace   
- 리스트안에 값을 넣는 옵션 append

<br>

#### 📌 value값으로 key값 구하기
<br>

[__1. items() 함수를 이용해주자__](https://heejung-gjt.github.io/python-DataStructure)
- values() value의 값만 뽑아낸다   
- keys()  key의 값만 뽑아낸다   
- items() 키-값 쌍을 한번에 뽑아낸다   
<br>

딕셔너리 table의 모든 쌍들에 있는 key와 value가 k와 v로 차례대로 for문을 반복한다.
만약 v와 k는 한 쌍이기 때문에 if문에서 value의 값이 조건을 만족하면 value와 대응하는 key값인 k를 출력하면 된다      
이를 이용해서 key값을 구 할 수 있다   
```python
table={"morning":2000, "afternoon":2500, "night":3000}

 for k, v in table.items(): 
  
  if v==2000:
    print(k) # 결과값 : 
    maxValue = v
      print(k)
```
<br>

__2. key값과 value의 값을 바꾸어 또다른 dic를 만들어준다__

<br>


#### 📌 replace와 append
<br>

__1. replace__ 
-  리스트에서 for문을 돌면서 각 문자열에 있는 특정 문자를 삭제하고 싶을때 replace 옵션을 사용해준다   
아래 코드처럼 삭제할 문자가 여러개면 replace().replace()로 연속해서 써주면 된다.   

```python
for text in texts:
  text = text.replace("%",'').replace("+",'')
```
<br>


#### 📌 append
<br>

__1. append__ 
-  새로운 list에 문자열을 넣고 싶을땐 append를 사용해준다

아래 코드처럼 삭제할 문자가 여러개면 replace().replace()로 연속해서 써주면 된다.   
__td_lists += text는 안된다는 것을 기억하고 있자__

```python
td_lists=[]

for text in texts:
  td_lists.append(text)
```
<br>

## 딕셔너리 key와 value를 이용한 정렬 
딕셔너리는 list와 마찬가지로 sorted함수를 이용해 정렬한다.   

__1.key를 이용한 정렬__     
sorted와 items()를 이용하여 정렬하게 되면 key를 기준으로 정렬이 되어진다   
```python
dict = {'c': 1, 'd':8, 'a':4 , 'b':2}
sort_dict = sorted(dict.items())

# [('a', 4), ('b', 2), ('c', 1), ('d', 8)]
```
내림차순 정렬은 ```sort_dict = sorted(dict.items(), reverse=True)``` reverse=True를 넣어주면 된다
<br>

__2.value를 이용한 정렬__   
sorted와 operator를 이용하여 정렬하게 되면 value를 기준으로 정렬이 되어진다   

```operator```   
operator.itemgetter()에서 0이나1을 넘기는거에 따라서 key로 정렬할것인지 value로 정렬할 것인지 정할 수 있다. 0을 주면 key로 정렬하게 되고 1을 주면 value로 정렬하게 된다. 
```python
import operator


dict = {'c': 1, 'd':8, 'a':4 , 'b':2}
sort_dict = sorted(dict.items(), key=operator.itemgetter(1))

# [('c', 1), ('b', 2), ('a', 4), ('d', 8)]
```

