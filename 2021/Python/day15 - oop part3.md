## 목차    
✔ Inheritance   

✔ Override        
     
✔ IS-A : 상속       
    
✔ HAS-A : Composition(합성), Aggregation(통합)       
   

* * *

### 👉 Inheritance(상속)

<br>

__상속이란 부모 클래스의 속성을 자식 클래스가 물려받아 새로운 인스턴스를 생성하는 것이다.__    

상속을 이용하면 코드의 유지보수가 쉬워지고 중복코드가 작성되는 것을 방지할 수 있다        

예를 들면 SmartPhone 이라는 class가 있고 해당 클래스를 상속받은 iphone, galaxy 클래스를 만들 수 있으며, 
SmartPhone class에  메서드를 만들면  iphone, galaxy 클래스에서 SmartPhone class에 있는 속성과 메서드를 사용할 수 있다.    

##### SmartPone class (부모클래스).py
```python
class SmartPhone:
    def __init__(self, ap, os):
        self.ap = ap
        self.os = os
        print(f'ap : {ap}, os : {os}')
        
    def open_ai(self):
        print('welcome smartpone world')
        
```
<br>

##### IPhone class (자식클래스)
```python
class IPhone(SmartPhone):
    def __init__(self, ap, os, touch_id):
        # with class name
        SmartPhone.__init__(self, ap, os)
        self.touch_id = touch_id
        
    def open_ai(self): # override
        print('Hey, Siri!')
        
```
<br>

Galaxy class는 ```super()```을 사용하여 상속받았다.     

super()를 사용하여 기반 클래스(부모클래스)의 __init__ 메서드를 호출하였다. 
super()뒤에 .을 붙여서 메서드를 호출하는 방식이다 ```super().lnit__()```    

아래의 코드는 파생클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게
표시하였다. ```super(현재class, self).__init()```

##### Galaxy class (자식클래스)
```python
class Galaxy(SmartPhone):
    def __init__(self, ap, os, sam_pay):
        # with super()
        super(Galaxy, self).__init__(ap, os)
        self.sam_pay = sam_pay
        
    def open_ai(self):
        print('Hi, Bixby!')
        
```   
<br>

부모 클래스에 있는 ap와 os의 인스턴스 변수를 상속받기 위해 자식 클래스에서는
```SmartPhone.__init__(self,ap,os)```를 생성자 바로 아래에 작성해야 한다    

자식 클래스에서는 ap,os의 속성과 open_ai의 메서드를 모두 사용할 수 있음을 확인할 수 있다   
##### 각 class 인스턴스를 생성하여 실행
```python
smart_phone = SmartPhone('have','have')
smart_phone.open_ai()

iphone = IPhone('Siri','ios','touch_id')
iphone.open_ai()

galaxy = Galaxy('Bixby','android','sam_pay')
galaxy.open_ai()

"""
결과 :
ap : have, os : have
welcome smartpone world

ap : Siri, os : ios
Hey, Siri!

ap : Bixby, os : android
Hi, Bixby!
"""
```
<br>

### 👉 Override

__동일한 이름의 메서드를 삽입했을때 특정 클래스(부모클래스)의 메서드가
무시되고 다른 클래스(자식클래스)의 메서드가 호출되는 것을 말한다__    

부모와 자식에 같은 이름의 함수가 존재하면 자식의 함수가 우선이된다     
```python
class Parent:
    def over_ride(self):
        print('부모의 over_ride 메서드')
class Child(Parent):
    def over_ride(self):
        print('자식의 over_ride 메서드')
over = Child()
over.over_ride()

"""
결과 : 자식의 over_ride 메서드
"""
```
<br>

부모 클래스에 있는 over_ride 메서드도 호출되어 사용하기 위해서는 __super()__를
사용하면 된다
```python
class Parent:
    def over_ride(self):
        print('부모의 over_ride 메서드')
class Child(Parent):
    def over_ride(self):
        super().over_ride()
        print('자식의 over_ride 메서드')
over = Child()
over.over_ride()

"""
결과 : 

부모의 over_ride 메서드
자식의 over_ride 메서드
```

<br>

### 👉 IS-A : 상속
__IS-A는 ~은 ~의 한 종류다를 의미한다__     
     
__예를 들어 노트북은 컴퓨터의 한 종류다라는 문장은 관계가 성립하므로 Computer
클래스와 Laptop 클래스는 IS-A 관계이다__   
     
__IS-A의 관계가 아닐때 상속을 하면 클래스를 설계하는데 어려움이 있다__    

🙌 IS-A의 예를 들어보자    
노트북 클래스는 컴퓨터 클래스를 상속받아 컴퓨터 클래스의 모든 메서드와 변수를 가진다.   
즉 browse() 메서드나 work() 메서드를 정의하지 않아도 이미 사용할 수 있게 된다.
그 외에 다른 특성을 가지는 move 메서드를 생성하여 Laptop에서만 사용한다.  
```python
class Computer:
    def __init__(self,cpu,ram):
        self.CPU = cpu
        self.RAM = ram
    
    def browse(self):
        print('browse')
    
    def work(self):
        print('work')

class Laptop(Computer):
    
    def __init__(self,cpu,ram,battery):
        super().__init__(cpu,ram)
        self.battery = battery
    
    def move(self, to):
        print(f'move to {to}')

lap = Laptop('intel',16,'powerful')
lap.browse()
lap.work()
lap.move('office')

"""
결과 : 
browse
work
move to office
"""
```
<br>

### 👉 HAS-A : Composition(합성), Aggregation(통합)
__HAS-A 관계는 ~이 ~을 가진다 혹은 포함한다를 의미한다__    

🙌 예를 들어보자    
컴퓨터와 CPU, RAM의 관계를 보면 컴퓨터는 CPU와 RAM을 가지고 있으므로
HAS-A의 관계가 된다. 이때 컴퓨터01의 CPU를 CPU01이라고 했을때 컴퓨터01이 사라지면 CPU01도
함께 사라지는 것을 볼 수 있다. 컴퓨터가 CPU를 소유하고 있는 모양새로 둘은 강한
관계를 맺고 있다. 이러한 관계를 __Composition__이라고 한다         

아래의 코드를 보면 Computer 클래스는 인스턴스 변수 cpu를 가진다. 생성자에서 CPU객체를 생성하여
인스턴스 변수 cpu에 할당한다. 즉 Computer 객체가 생성될때 CPU 객체도 같이 만들어졌다가 Computer 객체가 사라질때
CPU 객체도 함께 사라진다
```python
class CPU:
    pass

class RAM:
    pass

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
```
<br>

🙌 예를 들어보자    
경찰관과 총의 관계를 보면 경찰은 총을 가지고 있기 때문에 HAS-A의 관계이다. 경찰은 총을 가지고 있을수도 있고
가지고 있지 않을 수도 있다. 경찰은 총을 언제든지 반납할 수 도 있다. 경찰이 존재해도 총이 없을수도 있고 있을수도 있는것처럼
둘의 객체는 생명주기를 함께 하지 않는 상대적으로 약한 관계이다. 이러한 관계를 __Aggregation__이라고 한다     
    
아래의 코드를 보면 Police 객체가 만들어질때 아직 Gun 객체를 가지고 있지 않는다. 이후 acquire_gun() 메서드를
통해 Gun 객체를 인스턴스 변수로 가지게 된다. 이는 HAS-A 관계이다. 또한 release_gun() 메서드를 통해 가지고 있던
총을 반납할 수도 있다. 이 두메서드를 이용하면 총을 가진 경찰과 가지고 있지 않은 경찰을 모두 표현할 수 있다
```python
class Gun:
    def __init__(self,kind):
        self.kind = kind
        
    def bang(self):
        print('bang bang')
        
class Police:
    def __init__(self):
        self.gun = None
        
    def acquire_gun(self, gun): # 총얻는다
        self.gun = gun
        
    def release_gun(self):  # 총 반납한다
        gun = self.gun
        self.gun = None
        return gun
    
    def shoot(self):  # 총 쏜다
        if self.gun:
            self.gun.bang()
        else:
            print('Unable to shoot')

p1 = Police()  # p1 경찰 인스턴스 생성
print('p1 shoots')
p1.shoot()  # p1은 gun 객체를 가지고 있지 않다
print('')

revolver = Gun('Revolver')  # revolver Gun 인스턴스 생성
p1.acquire_gun(revolver)  #p1이 revolver 획득

print('p1 shoots again')
p1.shoot() # p1이 revolver gun 획득함 , 총 있음
print('')

revolver = p1.release_gun()  # revolver 총 반납함
print('p1 shoots again')
p1.shoot()

"""
결과 :

p1 shoots
Unable to shoot

p1 shoots again
bang bang

p1 shoots again
Unable to shoot
"""
```
