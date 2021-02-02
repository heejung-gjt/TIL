
### 👉 file I/O

파일 입출력은 파일을 읽거나 쓸때 쓰는 방법이다. 주로(w, r, a) 3가지의 경우가 쓰인다 
```python
f = open('./<파일위치>','<모드>',encoding='utf-8')
```
<br>

#### w (쓰기모드) : 파일에 내용을 쓸때 사용한다   

```python
"""
numbers.txt파일이 없다면 생성된 후 hello가 쓰인다
"""
f = open('./numbers.txt','w',encoding='utf-8')
f.write('hello')
f.close()
``` 
 파일을 쓰거나 읽었을땐 항상 해당 파일을 닫아주는 close()를 함께 써주어야 한다
<br>

#### r (읽기모드) : 파일을 읽기만 할때 사용한다   
```python
"""
numbers.txt파일을 한줄을 읽어온다. 내용이 없으면 none을 반환한다
"""
f = open('./numbers.txt','r',encoding='utf-8')
text = f.readline()
print(text)
f.close()

# readline()으로 출력시 : hello
# readlines()으로 출력시 : ['hello']
```
읽기모드에선 readline()과 realines()함수를 사용한다 
readline()은 한 줄만을 읽어와서 변수에 담는다   
readlines()은 파일의 모든 라인을 읽어와 리스트로 리턴한다
<br>

#### a (추가모드) : 파일의 마지막에 새로운 내용을 추가 시킬때 사용한다   
```python
"""
numbers.txt파일 마지막에 '추가내용'이라는 내용이 추가된다
"""
f = open('./numbers.txt','a',encoding='utf-8')
    f.write('추가내용')
f.close()
```
<br>

#### with와 함께 쓰기
파일 입출력에서 파일을 open했다면 마직막에 close를 해주어야 한다. with를 사용하면 close를 해주지 않아도되는 편리함이 있다
```python
"""
with로 numbers.txt파일을 읽기 형식으로 열어 f라는 명칭으로 지정하였다. readline()함수를 사용하여 한줄을 출력한다 
"""
with open('./numbers.txt','r',encoding='utf-8') as f:
    print(f.readline())
```
<br>

#### ✔ 실습01

```python
"""
<쓰기모드>
numbers.txt파일에 hello라는 문자열을 10번 쓰이도록 작성하였다
"""
with open('./numbers.txt','w', encoding='utf-8') as f:
    for _ in range(10):
        f.write('hello\n')
----------------------------------------

"""
<읽기모드>
numbers.txt 파일의 내용을 읽기모드로 모든 줄의 내용을 출력하였다. readlines()로 읽었기 때문에 모든 내용은 리스트안에 담겨져 출력된다

출력결과 :
['hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n', 'hello\n']
"""
with open('./numbers.txt','r', encoding='utf-8') as f:
    print(f.readlines()) 
-----------------------------------------

"""
한줄에 한단어씩 출력하기 위해 for문을 사용하였고
개행문자를 없애기 위해 replace함수를 사용했다 

출력결과 :
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
"""
with open('./numbers.txt','r', encoding='utf-8') as f:
    text_list = f.readlines()
    for line in text_list:
        print(line.replace('\n',''))
-----------------------------------------

"""
<추가모드>
numbers.txt 파일 뒤에 1~10까지의 정수를 붙여 출력하였다

출력결과:
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
1
2
3
4
5
6
7
8
9
10
"""
numbers = [i for i in range(1,10+1)]
with open('./numbers.txt','a', encoding='utf-8') as f:
    for i in numbers:
        f.write(f'{i}\n') 

with open('./numbers.txt','r', encoding='utf-8') as f:
    for text in f.readlines():
        print(text.replace('\n',''))
```
<br>

#### ✔ 실습02
dictionary get 함수를 이용하여 글자수는 key값에 ,똑같은 글자수에 해당하는 값을 카운트한 값은  value값에 넣어 출력한다

1. 가장 먼저 파일을 읽어오는데 개행문자는 제거한 리스트형태로 가지고 온다
```python
with open('./a_word_list.txt','r', encoding='utf-8') as f:
    txt_list = f.readlines()
    a_word_list = [word.replace('\n','')for word in txt_list ]
a_word_list

"""
결과값
['aback',
 'abacus',
 'abandon',
 'abandoned',
 'abandonment',
 'abashed',
 'abate',
 'abbey',
 'abbr.',
 'abbreviate',
 'abbreviation',
 'ABC',
 .
 .
 ]
"""
```
<br>

2. 딕셔너리의 get함수를 이요하여 key를 이용해 value의 값을 불러온다. 이때 해당 값이 없다면 값을 지정해놓은 default값을 가져간다

```python
len_dict = {}
for word in a_word_list:
    len_dict[len(word)] = len_dict.get(len((word),0)+1  
# 해당 수가 존재한다면 존재하는 value값에 +1을 해주고 해당 수가 존재하지 않는다면 0을 반환하는데 +1을 해준다
"""
결과값
{5: 67,
 6: 80,
 7: 85,
 9: 89,
 11: 47,
 10: 86,
.
.
 }
"""
```
<br>

#### ✔ 실습03
dictionary setdefault 함수를 이용하여 글자수는 key값에 ,똑같은 글자수에 해당하는 단어는 value값에 리스트 형태로 넣어 출력한다

setdefault : 이 함수는 딕셔너리에 키-값 쌍을 추가해준다. ```setdefault(키, 기본값)```처럼 키와 기본값을 지정하여 값에 기본값을 저장 한 뒤 해당 값을 딕셔너리에 반환한다 
```python
"""
dict_ 빈 딕셔너리에  키-값쌍을 추가는데  키값에는 문자열의 길이를 추가하고 value값에는 빈문자열을 추가해준다. 이때 append를 사용하여  빈 리스트 형태인 value값에 key값에 저장한 문자열을 추가한다
"""
dict_ = {}
dict_setdefault(len('cat'),[]).append('cat')
# 결과값 : {3: ['cat']}
```
<br>

실습02 에 a_word_list 들어 있는 모든 문자들을 딕셔너리에 setdefault를 이용하여 실습03과 같이 실습해보자
```python
"""
a_word_list안에 들어있는 문자열을 하나씩 꺼내어 setdefault함수를 이용하여 key값과 value값을 출력해준다 

결과값:
{5: ['aback',
  'abate',
  'abbey',
  'abbr.',
  'amiss',
  'among'],
 6: ['abacus',
  'abduct',
  'abject',
  'ablaze',
  'amends',
  'amidst',
  'amoeba',
  'amoral',
  'amount',
  'ampere'],
 7: ['abandon',
  'abashed',
  'abdomen',
  .
  .
  
"""
filtered_dict={}
for word in a_word_list:
    filtered_dict.setdefault(len(word),[]).append(word)
filtered_dict
```