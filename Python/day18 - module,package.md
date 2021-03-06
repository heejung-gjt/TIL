### 👉 Module
모듈은 함수나 변수 또는 클래스를 모아 놓은 파일이다. 생성한 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있다.     
모듈은 간단한 기능을 담을때 사용한다.    
<br>

모듈 실습을 해보자.    

__✔ fibo.py에 함수 작성하여 main.py에서 실행(기본적인 구조)__     

fibo.py라는 파일과 main.py라는 파일을 만든다. fibo파일에는 fibo를 함수형식으로 나타낸 코드를 작성해준다.
main.py에서 fibo.py에 작성한 코드를 import시켜 실행시킨다. 이때 main.py파일은 fibo.py파일과 같은 폴더에 있어야 한다     
(실행은 항상 main.py에서 !)      

모듈을 사용할때는 import로 모듈을 가져온뒤 모듈명.모듈함수() 형식으로 사용한다    

##### fibo.py 
```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```
##### main.py
```python
import fibo

print(fibo.fibo(10))

# 결과 : 55

```
<br>

이때 모듈에서는 from import로 변수와 함수를 가져와 모듈명.모듈함수가 아닌 모듈함수만을 불러 사용할수 있다.
```fibo.py```파일은 위와 동일하다
##### main.py
```python
from fibo import fibo

print(fibo(10))

# 결과 : 55
```
<br>

__✔ hero.py파일에 class 작성하여 main.py에서 실행(모듈에 class 작성)__    

hero.py파일에 Hero라는 class를 작성하여 main.py에서 hero를 import하여 실행시킨다        

##### hero.py
```python
class Hero:
    def __init__(self,name,level):
        self.name = name
        self.level = level
    
    def intro(self):
        print(f'name : {self.name}')
        print(f'level : {self.level}')
```
##### main.py
```python
import hero

hulk = hero.Hero('hulk',4)
hulk.intro()

"""
결과 

name : hulk
level : 4
"""
```
<br>

마찬가지로 from import로 변수와 클래스를 가져와 모듈명.모듈클래스가 아닌 모듈클래스만을 불러 사용할수 있다.    
```hero.py```파일은 위와 동일하다
##### main.py
```python
from hero import Hero

hulk = Hero('hulk',4)
hulk.intro()

"""
결과

name : hulk
level : 4
"""
```
* * *
<br>

### 👉 package
패키지는  관련된 여러 모듈을 하나의 폴더로 묶는것이다. 실습을 통해 알아보자    
<br>

패키지로 사용할 project 폴더를 생성해서 해당 폴더에 fibo.py 파일과 hero.py파일을 넣어준다. 그럼 project라는 패키지 않에
fibo.py와 hero.py라는 두개의 모듈이 존재한다. 이렇게 만든 모듈을 main.py에서 불러와 사용해준다.     

project폴더를 생성한다         
" 이때 폴더안에 __init__.py를 넣어서 해당 폴더가 패키지라는 인식을 시켜주어야 하지만 python 3.3 이상부터는 
해당 파일이 없어도 패키지로 인식된다. 하지만 하위 버전에도 호환되도록 __init__.py 파일을 작성하는것을 권장한다 "
 

##### main.py
```python
import project.fibo
import project.hero

print(project.fibo.fibo(10))
hulk = project.hero.Hero('hulk',4)
hulk.intro()

"""
결과 

55
name : hulk
level : 4
"""
```
<br>

이때 마찬가지로 ```from import```를 사용하면 main.py에서 간단하게 사용이 가능하다    

##### main.py

```python
from project.fibo import fibo
from project.hero import Hero

print(fibo(10))
hulk = Hero('hulk',4)
hulk.intro()

"""
결과 

55
name : hulk
level : 4
"""
```