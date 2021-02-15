## *** 목차 ***
✔ class method             
     
✔ static method        
    
✔ Abstract Base class    

✔ Polymorphism    
        
   

* * *

### 👉 class method  

<br>

이에 앞서 클래스에 아무런 데코레이터가 없이 메서드가 선언되어지면 해당 메서드는 인스턴스 메서드로 첫번째 매개변수 self에 클래스의 인스턴스가 넘어오게 된다    

__클래스 메서드는 @classmethod 데코레이터를 사용해서 클래스 메서드로 정의를 한다. 이때 클래스 메서드는 첫번째
   매개변수에 cls를 지정해야 한다.__ 
```python
class Wallet:

    @classmethod
    def set_default(cls, amount):
        pass
```   
<br>

__클래스 메서드는 인스턴스 없이 호출할수 있고 메서드 안에서 클래스 속성, 클래스 메서드에 접근 할 때 사용한다__
```python
class Wallet:
    balance = 0
    name = 'Your wallet'
    
    def __init__(self, account):
        self.account = account
    
    @classmethod
    def set_default(cls, amount):
        while amount<1:
            print("You should deposit more than 1. Try again")
            amount = int(input('Enter value want to deposit: '))
        cls.balance = amount
        print('Set default value of balance to {}'.format(cls.balance))

w =  Wallet(0)
Wallet.set_default(10)  # Set default value of balance to 10
Wallet.balance  # 0
```
<br>

Wallet이라는 class를 만들어 클래스 속성 balance와 name을 만들어준다. 
```python
class Wallet:
    balance = 0
    name = 'Your wallet'
    
    def __init__(self, account):
        self.account = account
```        
<br>

다음으로 @classmethod를 붙여서 클래스 메서드를 만든다. 첫번째 매개변수가 cls인데 이곳에는 현재 클래스 Wallet이 들어온다.
따라서 클래스 속성에 접근하고 싶을때 cls.balance처럼 clas을 이용한다. 
```python
    @classmethod
    def set_default(cls, amount):
        while amount<1:
            print("You should deposit more than 1. Try again")
            amount = int(input('Enter value want to deposit: '))
        cls.balance = amount
        print('Set default value of balance to {}'.format(cls.balance))

w =  Wallet(0)
Wallet.set_default(10)  # Set default value of balance to 10
Wallet.balance  # 0
```
<br>

### 👉 static method

__static 메서드는 @staticmethod 데코레이터를 사용해서 스태틱 메서드로 정의를 한다. 이때 해당클래스는 매개변수에 self를 지정하지 않는다.__ 
```python
class Wallet:

    @staticmethod
    def print_wallet_static():
        print(Wallet.name)
```

__static메서드를 호출할때는 클래스에서 바로 메서드를 호출하면된다.__  Calc클래스에 정적메서드를 붙여 add와 mul메서드를 만들었다.  
해당 메서드를 호출하기 위해서는 ```클래스.메서드()```로 호출하면된다. 이때 정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없다. 그래서 보통
정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요없을때 사용한다    

여기서 만든 add,mul 메서드는 숫자 두개를 받아서 연산하는 과정일뿐 인스턴스 속성이 필요하지 않다
```python
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

결과 : 

30 
200

[reference-https://dojang.io/]
```
<br>

### 👉 Abstract Base class 
__추상클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해
사용한다__ 
  
추상클래스를 만들기 위해서는 ```from abc import *```를 임포트해야 한다.    
  
클래스의 괄호안에 (metaclass=ABCMeta)를 지정해야한다.      

메서드 작성시에는 위에 데코레이터 @abstractmethod를 붙여서 추상 메서드로 지정한다

```python
from abc import *

class AbstractClass(metaclass=ABCMeta):
    @abstractemthod
    def method_name(self):
        code...
```
<br>

예를 들어보자   
StudentBase라는 추상 class를 만들고 해당 클래스를 상속받는 학생 class를 만든다.
학생 class에서 추상메서드인 go_to_school을 구현하지 않아 아래의 코드는 에러가 발생한다. 추상클래스에서
정의한 메서드는 추상 클래스를 상속받은 클래스에서 모두 구현해야만 한다.
```python
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

 
james = Student()
james.study()

```
<br>

go_to_school() 메서드도 함께 구현한 학생 class
```python
from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
class Student(StudentBase):
    def study(self):
        print('공부하기')
 
    def go_to_school(self):
        print('학교가기')
 
james = Student()
james.study()
james.go_to_school()

"""
결과 :

공부하기
학교가기
"""
```
<br>

### 추상 메서드는 빈 메서드로 생성
추상 클래스는 인스턴스로 만들 수 없기 때문에 pass를 넣어서 빈 메서드로 만든다. 추상 클래스는
오로지 상속에만 사용되고 파생 클래스에서 반드시 구현해야 할 메서드를 정해 줄때 사용한다.   
<br>

### 👉 Polymorphism

__다형성은 자녀와 부모 클래스를 다룰때 중요한 개념이며 다양한 형태를 취하는 능력을 의미한다.   
파이썬의 다형성은 오버라이딩과 메서드 오버로딩을 사용하여 구현한다__    

같은 모양의 코드가 다른 동작을 하는 것을 말한다.    

다형성은 코드의 양을 줄이고 객체 타입을 하나의 타입으로 관리가 가능해 유지보수에 좋다.     

아래의 코드는 다형성의 예로 get_ap 메서드로 이름이 같지만 다른 동작이 출력되는 것을 볼 수 있다
```python 
class SmartPhone:
    def get_ap(self):
        print('Application Proccessor')

class IPhone(SmartPhone):
    def get_ap(self):
        print('A series')

class Galaxy(SmartPhone):
    def get_ap(self):
        print('Exynos')


iphone = IPhone()
iphone.get_ap()  # A series
galaxy = Galaxy()
galaxy.get_ap()  # Exynos


```