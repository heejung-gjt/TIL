##  Regular Expressions
정규 표현식은 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식언어이다. python은 re모듈로 정규표현식 사용이 가능한다  

<br>

### 👉 Meta Characters(메타문자)   
<br>

#### ✔ Dot(```.```) : 개행문자(\n)을 제외한 모든 문자를 의미한다
a와p사이엔 모든 문자와 매치된다

```python
a.pple  # a + 모든문자 + pple  
```
EX)
- a0ple
- adple    

* * *

#### ✔ Repetition(```*```) : 앞 문자의 반복을 의미한다
```*``` 앞에 있는 문자 p는 0개 ~무한대 반복이 가능하다
```python
ap*le   # 앞문자 p의 무한반복 가능
```

EX)    
- ale   
- aple   
- apppple    

* * *

#### ✔ Repetition(```+```) : 앞 문자의 반복을 의미한다
```+``` 앞에 있는 문자 p는 1개 ~무한대 반복이 가능하다
```python
ap+le   # 앞문자 p의 무한반복 가능, 하나 이상은 써야한다
```

EX)    
- aple   
- apple   
- apppppple    

* * *

#### ✔ Caret(```^```) : 정의한 문자열 패턴으로 시작함을 의미한다
```^``` 는 문자열의 처음을 의미한다
```python
^pen   # 문자열의 처음은 pen으로 시작되야 매치된다
```

EX)    
- penpineapple 
- pencil   

* * *

#### ✔ Dollar sign(```$```) : 정의한 문자열 패턴으로 끝남을 의미한다
```$``` 는 문자열의 처음을 의미한다
```python
pen$   # 문자열의 끝은 pen으로 끝나야 매치된다
```

EX)    
- applepen
- nicepen 

* * *

#### ✔ Question mark(```?```) : 앞 문자의 존재유무를 의미한다
```python
pen?cil   # 앞문자 n이 있는지 없는지 2가지에 매치된다
```

EX)    
- pencil
- pecil

* * *

#### ✔ Curly brackets(```{m,n}```)
반복횟수를 정의할때 사용한다. 중괄호 안의 숫자(m,n)은 반복횟수를 정의하며 , 정확히 일치할 경우 1개의 숫자를 , 범위를 정의할 경우 2개의 숫자를 사용한다. {3,}인 경우 반복 횟수는 3이상를 의미하고 {,3}인 경우 반복 회숫는 3이하를 의미한다     
__{m}__
```python
ba(na){2}  # ba + (na)반드시 2번 반복 == banana
```
__{m,n}__   
```python
ba(na){0,2}  # ba + (na)0~2회 반복 == ba, bana, banana
```
EX)    
- pencil
- pecil

* * *

#### ✔ Square brackets(```[]```)
문자 클래스를 의미한다. 대괄호 사이에 나열한 문자 중 하나의 값과 일치할 경우를 의미한다. 즉 " [] 사이의 문자들과 매치 " 라는 의미이다. 해당 문자 클래스와 함께 쓰이는 메타문자는 ```-```과 ```^```이다   
- ```-``` : 두 문자 사이의 범위를 뜻한다     
- ```^``` : 부정을 의미한다

__```-```__
```python
[A-Za-z]  # 대문자와 소문자 알파벳 전체 중 하나의 문자   
[a-g0-5]  # a,b,c,d,e,f,g 와 0,1,2,3,4,5 중 하나의 문자 
```
__```^```__   
```python
[^0-9]  # 숫자가 아닌 문자
[^A-Za-z]  # 알파벳이 아닌 모든 문자
```
EX)    
- [a,b,c] : a매치, before 매치
- [0-4]  : 43매치, 0934매치, 987매치X(0,1,2,4 중 매치되는 것이 없기 때문)
<br>

__자주 사용되는 문자 클래스__

- \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
- \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
- \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
- \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
* * *

#### ✔ Parentheses(```()```)
소괄호 안의 문자열의 그룹을 의미한다. 문자열 패턴의 반복을 검사하고 싶을 때 사용한다     
```python
(apple)+  # apple이 한개 이상 들어가야 매치된다 
```
EX)    
- penapple
- penappleappleapplepen

* * *

#### ✔ Vertical bar(```|```)
|의 좌우 중 하나의 값과 일치하는 경우를 의미한다   
```python
(apple|apqle)  # 두 문자열 중 하나와 일치해야 매치된다 
 
ap[q|p]le  # q또는 p 둘 중 하나의 값과 일치해야 매치된다
```
EX)    
- apple or apqle
- apqle or apple

* * *

#### ✔ Backslach(```\```)
정규표현식을 만들때 메타문자가 메타문자가 아닌 그 문자 그대로 사용하게 하기 위해 사용한다  
```python
https://www.google.co.kr  # . 이 메타문자로 인식 될 수 있다

=> https://www\.google\.co\.kr   # 앞에 \을 넣어 문자 그대로 사용 될 수 있게 한다
```
EX)    
- apple or apqle
- apqle or apple

* * *

#### ✔ match()
match는 문자열을 처음부터 정규식과 매치가 되는지 조사해주는 메서드이다

match 객체의 메서드   
- group() : 매치된 문자열을 돌려준다
- start() : 매치된 문자열의 시작 위치를 돌려준다   
- end() : 매치된 문자열의 끝 위치를 돌려준다   
- span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다
```python
import re

a = 'penpineapple'
b = 'applepen'

m = re.match('^pen', a)  # a문자열이 pen으로 시작하는지
n = re.match('^pen', b)  # b문자열이 pen으로 시작하는지

print(m)  # <re.Match object; span=(0, 3), match='pen'>, 0~2까지 pen으로 매치됨을 보여준다
print(n)  # None  매치되지 않으므로 none을 출력한다

m.group()  # pen
m.start()  # 0
m.end()    # 3
m.span()   #(0,3)
a[m.start():m.end()]   # pen
```
<br>

__match 실습예제__ 

```r'^.*(pen)$``` : 문자열이 pen으로 끝나고 앞에 시작은 모든 문자가 와도 되는데 문자의 개수는 0~무한개로 올 수 있다 
```python
a = 'penpineapple'
b = 'applepen'
c = 'pen'
m = re.match(r'^.*(pen)$', b)
m

"""
결과

a  # 매치되지 않는다, pen으로 문자가 끝나지 않기 때문이다

b  # <re.Match object; span=(0, 8), match='applepen'>

c  # <re.Match object; span=(0, 3), match='pen'>
"""
```
매치를 사용할때는 compile을 항상 먼저 해준다
```python
# Do compile first!!!

apples = ['a'+ 'p'*i +'le' for i in range(10)]
apple_finder = re.compile(r'^ap{2}le$')  #complie먼저 !

for item in apples:  # match되는 문자열 찾기
    m = apple_finder.match(item)
    print(item, m)
```

__re.group()__    
group()은 해당 그룹에 매칭된 문자열을 반환한다.
```python
>>> m = re.match('([0-9]+) ([0-9]+)', '1 5')
>>> m.group(1)    # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
'1'
```

<br>

#### gmail의 username 만드는 규칙 
username에 올 수 있는 문자열 지정 : alphabet, number, -, +
A-Z ,a-z, 0-9, -, + 의 문자열이 4개이상 32개 이하로 조합되서 username을 만드는 규칙이다
```python
r'[A-Za-z0-9\-\+]{4,32}@gmail\.com
```
<br>

#### ✔ findall()과 finditer()

1. findall()은 주어진 string 전체에서 pattern과 일치하는 것을 모두 찾아서 list로 반환한다     
```re.findall(r'패턴문자열','문자열')```   

```python
import re

result_list = re.findall(r"([A-Z]*)@([1-9]*)","SON@1234.&&")
print(result_list)

"""
결과 :

[('SON', '1234')]
"""
```
2.  finditer()은 findall()과 같은 기능을 하지만 결과물로 리스트를 반환하는 것이아니라 이터레이터를 반환하기 때문에 for 문을 사용해 원소값을 하나 하나 꺼내야한다    

```re.finditer(r'패턴문자열','문자열')```   

```python
import re

l_m = re.finditer(r'\d{3}-\d{4}-\d{4}', 'kwon 010-3333-4444 lee 010-5555-6666')
for m in l_m:
    print(m.group())   
"""
결과 :

010-3333-4444
010-5555-6666

```
3. re.I 옵션은 대소문자 구별없이 매치를 수행할때 사용한다
<br>

#### ✔ 조건이 있는 표현식    

#### 1.표현1(?=표현2) : 표현1 뒤에 문자열이 표현2와 매치되면 표현1 매치     
```EX) hi(?=friend) : hi 뒤에 문자열이 friend와 매치되면 매치```

##### ex)
```python
import re


string = input()
print(re.match('hi(?=friend)',string)) # hi 뒤에 friend 문자열이 있기때문에 hi가 매치된다

"""
결과 :

hifriend
<re.Match object; span=(0, 2), match='hi'>
"""
```
<br>

#### 2.표현1(?!표현2) : 표현1 뒤에 문자열이 표현2와 매치되지 않으면 표현1 매치     
```EX) hi(?!friend) : hi 뒤에 문자열이 friend와 매치되지 않으면 매치```

##### ex)
```python
import re


string = input()
print(re.match('hi(?!friend)',string)) # hi 뒤에 friend 문자열이 있기때문에 hi가 매치되지 않는다

"""
결과 :

hifriend
None
"""
```
<br>

#### 3.(?<=표현1)표현2 : 표현2앞의 문자열이 표현1과 매치되면 표현2 매치     
```EX) (?<=hi)friend : friend 앞에 hi가 있으면 friend를 매치```

##### ex)
```python
import re


string = input()
print(re.match('(?<=hi)(friend)',string)) 
```
<br>

#### 4.(?<!표현1)표현2 : 표현2 앞의 문자열이 표현1과 매치되지 않으면 표현2 매치     
```EX) (?<!hi)friend : friend 앞에 문자열이 hi와 매치되지 않으면 매치```

##### ex)
```python
import re


string = input()
print(re.match('(?<!hi)friend',string)) 

```
<br>

#### ✔ re.sub()
문자열을 바꿀 때는 sub 함수를 사용한다.```re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)```    

패턴, 바꿀 문자열, 문자열, 바꿀 횟수를 넣어준다. 여기서 바꿀 횟수를 넣으면 지정된 횟수만큼 바꾸어준다. 바꿀 횟수를 생략하면 찾은 문자열을 모두 바꾸어준다  
