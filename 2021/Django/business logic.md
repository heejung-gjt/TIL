## Django 비즈니스 로직 분리하는 방법

보통 비즈니스 로직, 즉 데이터를 가공하여 관리하는 것을 view단에서 하게 된다. 간단한 기능과 중복사용이 없다면 view에서 작성해도 괜찮다. __하지만__ 기능이 많아지고 중복 사용이 있을 경우에는 view에 넣는것은 코드의 가독성과 유지보수 면에서 적합하지 않다. view에서 관리하지 않고 로직을 관리할 수 있는 방법으로 4가지가 있다.     

<br>

> 1. Views/Forms/Serializers    
> 2. Fat Models   
> 3. Services   
> 4. QuerySets/Manager    

<br>

이중에서 fat models와 services의 방식으로 분리할 예정이기 때문에 일단 이 2가지를 정리할 것이다.    

<br>

### 1. Fat Models
데이터 관련 코드를 model에 넣어 캡슐화 하는 방식이다. 이 방식은 장고에서 권장하는 방향이다.      


### 2. Service Layer
모델과 뷰 사이에 비즈니스 로직을 담당하는 개념을 추가하는 것을 의미한다. 데이터베이스가 변경되는 로직은 service layer에 작성한다(ex- create, filter, get....)    


