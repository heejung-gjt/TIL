### 진수변환

#### ⚡ 삽질기록

- sort와 sorted에 대한 정확한 개념이 부족함을 느껴 알고리즘을 풀때마다 노가다를 하는 상황이 생겼다..^^         

<br>

#### 📌 list.sort() 와 sorted()  
두개의 함수 모두 값의 정렬을 위한 함수이다.     

```sort()```      
sort()함수는 값을 정렬후 정렬된 값을 돌려주지 않아 변수에 넣어 쓸 수 없으며 리스트형에서만 동작한다.      
내림차순 정렬 : sort(reverse=True)
```python
lists = list.sort() # 불가능

lists = list.sort(reverse=True) # 내림차순 정렬
```
<br>

```sorted()```    
sorted()함수는 값을 정렬한 후 정렬된 값들을 돌려주기 때문에 변수에 넣어 값들을 활용할 수 있으며 이터러블한 자료형에서 동작한다     
내림차순 정렬 : sorted(reverse=True)
```python
lists = sorted(list) #가능

lists = sorted(list, reverse=True) # 내림차순 정렬
```
정렬한 값들의 자체를 정렬하여 출력하고 싶을땐 sort를 사용하자. 하지만 정렬한 값들을 다른 객체해 저장해 무언가를 해야한다면 sorted를 사용해주자
<br>

