👉iterator(이터레이터)
list, set , dic와 같은 반복 가능한 객체를 말한다.   
이터레이터는 클래스에 __iter__, __next__, __getitem__메서드를 구현해야 한다
이터레이터를 쓰는 이유는 연속된 숫자가 아주 많을때는 메모리를 많이 사용하게 되므로 성능에 불리하다. 때문에 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을때 값을 만드는 방식을 사용한다. __iter__함수가 있는지 확인해보자 __iter__함수는 이터레이터 객체이며 그 안을 뜯어보면 __next__함수가 존재하는 것을 확인할 수 있다

👉 이터레이터 For문의 동작원리
이터러블 객체는 매직메서드 __iter__메서드를 가지고 있다. 해당 메서드로 이터레이터를 만들 수 있다
1. 먼저 해당 iterable객체의 __iter__()메소드를 호출하여 itetator객체를 얻어낸다
2. 이후 next()내장함수를 이용하여 반복을 수행한다(내부적으로 __next__()메소드를 호출한다 

👉 iterable과 iterator 비교
iterable이란 반복할 수 있는 객체로 string,list,tuple,dict,set는 이터러블 객체이다. iterator 객체는 __next__()메서드를 가지며 다음 순서의 item을 리턴한다. 
모든 iterator는 iterable이 될 수 있지만 모든 iterable은 iterator가 될 수 없다
예를 들어보자
```python
str1 = 'time is gold'
str1_list = str1.split(' ')
print(next(str1_list)) #TypeError: 'list' object is not an iterator

```

대신 모든 이터러블한 객체에 iter()메서드를 사용하면 iterator 객체를 만들 수 있다
```python
str_iter = iter(str1_list)
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
```
__iter__ : 이터레이터 객체를 리턴하는 메서드




👉generator(제너레이터)
제너레이터는 함수 안에서 yield라는 키워드만 사용하면 된다. 그래서 제너레이터는 이터레이터보다 훨씬 간단하게 작성할 수 있다

- 메모리 효율성 , 리스트는 데이터를 한번에 메모리에 적재하기 때문에 메모리 부족현상이 일어나 프로그램이 갑자기 죽을 수 있다. 제너레이터는 값에 데이터에 접근할때마다 메모리에 적재하기 때문에 큰 데이터를 다루는 경우 리스트보다 안정적이고 효율적이다

👉차이점
단순하게는 yield를 쓰냐 안쓰냐의 차이도 있지만 가장 큰 차이점은 이터레이터는 이터레이터는 모든 동작을 완료한 후 결과를 한번에 메모리에 적재시키지만 제너레이터는 각각의 yield에서 한번 실행 시킨 후 대기 상태에 들어가 결과를 반환한후 다음 코드를 진행하여 또다시 yield를 만날 경우 대기 상태에 들어가 결과를 반환하는 방식이다  

```python
def test_iter():
  start = 1
  x = iter(range(1,4))
  for i in x:
    print(i)
test_iter()
```

```python
def gen(count):
  start = 1
  while start <= count:
    yield start
    start += 1

for i in gen(3):
  print(i)
```

list객체의 각 요소는 이미 값이 정해져 있다
_list = [1,2,3]
0번인덱스 = 1
1번인덱스 = 2
2번인덱스 = 3

몇번째 어떤 요소가 있는지 손쉽게 확인할 수 있는 장점이 있지만 그 크기가 커질수록 메모리의 낭비가 심해진다는 단점이있다. 100만이 넘으면 100만개가 넘는 값을 모두 기억해야하기 때문에 메모리 낭비가 심하다

하지만 generator와 같은 lazy한 객체는 모든 요소를 저장하지 않고 처음에 주어야할 값, 그 다음부터 주어야 할값, 값을 언제까지 주어야 하는지에 대한 정보만 가지고 있다. 즉 모든 값을 메모리에 올려두지 않고 필요할때(호출할때)값을 평가해서 반환하는 방식이다. 
```python
def func1():
  for i in range(1,6):
    return i
foo1 = func1()
print(type(foo1))
print(foo1)
print(foo1)


def func2():
  for i in range(1,6):
    yield i
foo2 = func2()
print(type(foo2))
print(next(foo2))
print(next(foo2))
print(next(foo2))
print(next(foo2))
```