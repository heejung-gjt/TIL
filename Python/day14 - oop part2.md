## 목차 
✔ 클래스 변수와 인스턴스변수    

✔ 클래스 변수의 버그    
     
✔ Call by object Reference    
    
✔ 정보은닉     
   
✔ 접근제어 지시자               

* * *

### 👉 클래스 변수와 인스턴스변수

<br>

클래스 변수는 class안에 있고 메서드 밖에 있는 곳에 위치하게 된다. 즉 accounts = 0 이 클래스 변수가 된다. 
인스턴스 변수는 self가 붙어있는 변수를 인스턴스 변수라고 한다. self.age변수를 인스턴스 변수라고 부른다.   
 
```python
class Wallet:
    accounts = 0
    def __init__(self,age):
        self.age = age
    def spend(self,money):
        Wallet.accounts += money 
```

<br>

__클래스 변수와 인스턴스 변수는 언제 사용이 되어질까?__    


2개의 인스턴스를 생성해보자__.생성된 인스턴스에 age의 정보가 각각 10과 25로 들어가 있다.    
 
즉 child와 adult는 인스턴스 변수인 age를 바인딩(가리키고)있다. 만약 child.counts를 호출하면 가장먼저 인스턴스의 네임스페이스에서 counts를 찾는다. 그 뒤 해당 변수가 
없다면 클래스 네임스페이스로 이동하여 찾고 해당 값이 반환되는 것을 알 수 있다.   

   
즉, __클래스 변수는 모든 인스턴스에 공유되기 때문에 공통으로 사용되어질 변수만 작성해야한다.__   
```python
class Wallet:
    accounts = 0
    def __init__(self,age):
        self.age = age
    def spend(self,money):
        Wallet.accounts += money 

child = Wallet(10)
adult = Wallet(25)

child.age # 10
adult.age # 25

child.accounts
```
<br>

### 👉 클래스 변수의 버그 
<br>

__인스턴스가 생성되어 값이 호출되어질때 메서드의 호출에 의해 클래스변수의 값이 변경되어지는 버그가 발생할 수 있다. 아래 코드를 보자 .__      

    
Hero라는 클래스를 만든후 IronMan의 인스턴스를 만들었다. IronMan.save_item('Fancy glasses)를 작성해
save_item 메서드를 호출하여 inventory 리스트에 값을 추가하였다. 확인해보면 Fancy glasses 값이 들어가 있는 것을 볼 수 있다.      


__이때 발생할 수 있는 문제점은 새로운 인스턴스의 save_item 사용에서 일어난다.__      


Hulk라는 인스턴스를 만들어 save_item('torn shirt')를 작성하여 해당 메서드를 호출하면 메서드에 있는 인스턴스 변수
inventory에 값이 저장되어진다. 그 후 값을 확인하면  ```['Fancy glasses', 'torn shirt']```가 출력되는 것을 볼 수 있다
즉, IronMan에서 넣었던 리스트안의 값이 함께 출력이 되는 버그가 발생한다                                                     
```python
class Hero: # class
    health = 100 # class variable
    inventory = []

    def __init__(self, name, weapon):
        self.name = name # instance variable
        self.weapon = weapon

    def attack(self): # instance method
        print("attack with {}".format(self.weapon))
    def save_item(self, item):
        self.inventory.append(item)

IronMan = Hero('Iron Man', 'Impulse Gun')
IronMan.save_item('Fancy glasses')
IronMan.inventory # 호출 : ['Fancy glasses']

Hulk = Hero('Hulk', 'Radioactive Fist')
Hulk.save_item('torn shirt')
Hulk.inventory  # 호출 : ['Fancy glasses', 'torn shirt']
```
<br>

그렇다면 뮤터블한 객체를 사용하는 올바른 방법은 무엇일까     


클래스 변수에 값을 선언하지 않고 init의 파라미터로 inventory를 지정해주어 사용해주면 위의 같은 버그가 해결되고
각각의 리스트만이 출력되는 것을 볼 수 있다
```python
class Hero: # class
    health = 100 # class variable

    def __init__(self, name, weapon, inventory):
        self.name = name # instance variable
        self.weapon = weapon
        self.inventory = []

    def attack(self): # instance method
        print("attack with {}".format(self.weapon))
    def save_item(self, item):
        self.inventory.append(item)
```
<br>

### 👉 Call by object Reference
<br>

__python의 함수인자 전달 방식은 call by object reference이다.__     


아래의 코드에서 name에 kim을 할당하였다. 이때 kim라는 값이 name이 가르키는 메모리
공간에 할당되는 것이 아닌 kim이라는 인스턴스의 주소 값을 name이 가르키게 된다. python은 변수라는 메모리 공간에 값을 직접
할당하지 않는다.  즉, 변수는 메모리 공간에 값을 직접 지정하지 않고 해당 값의 
인스턴스를 가르킨다.
```python
name = 'kim'
```
<br>

### 👉 정보은닉 
정보은닉이란 구현시 세부사항을 클래스 안에 감추어 데이터를 외부에서 마음대로 
변경하지 못하게 하는 것이다.    


접근제어자 : 접근제어자란 클래스와 클래스 멤버를 선언할때 사용하는 제어자이다. 정보은닉을 구현하기 위해 사용되어진다.    


#### 접근제어 지시자 3가지    
__public__    
default제어지시자이며 클랫의 외부에서 속성, 메서드에 접근이 가능하다.   


__protected__     
해당지시자는 변수명 앞에 _를 하나 붙이며, 부모 클래스에서는 public으로 사용되어지고 외부에서는 private으로 사용되어진다. 이때 실질적으로 접근을 제어하지 않고 사용자에게 경고 형태로만 제공해준다.         


__private__    
private 키워드로 선언한 메서드나 멤버는 클래스 안에서만 사용할 수 있고 객체를 통해서는 접근하거나 호출할 수없다.   
<br>

EX) 기본값 public인 경우 객체내부에 있는 변수 price의 값을 클래스 외부에서 바꿀 수 있다
```python
class SmartPhone:
    def __init__(self, price, sale):
        self.price = price
        self.sale = sale
        
sam_phone = SmartPhone(200000,'20%')
print(sam_phone.price)
sam_phone.price = 1000  # 객체내부에 있는 변수 price의 값을 바꿀 수 있다
print(sam_phone.price)

"""
답:
200000
1000
""" 
```
<br>

위의 경우를 막기 위하여 private 설정을 해준다. private으로 객체를 선언하였기때문에 외부에서 사용할 수 없다
```AttributeError```가 발생한다
```python
class SmartPhone:
    def __init__(self, price, sale):
        self.__price = price
        self.sale = sale
        
sam_phone = SmartPhone(200000,'20%')
print(sam_phone.__price)
sam_phone.__price = 1000  # 변경시 error
print(sam_phone.__price)

```
<br>

하지만 실제로 정보 은닉이 된 것은 아니다. __은닉변수명.__dict____를 통해 멤버변수를 확인할 수 있는데 정보 은닉이 되었던 변수가 보이게 된다. 즉 __dict__를 통해 유저가 마음만 먹으면 얼마든지 접근하여 변경할수 있다.    
```python
sam_phone.__dict__

"""
출력 : 
{'_price': 1000, 'sale': '20%'}
"""
```
__dict이용하여 price 가격 변경__   
```python
sam_phone.__dict__['_price'] = 300000
sam_phone._price  # 가격 변경되었다
