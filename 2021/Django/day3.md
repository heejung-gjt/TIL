## foreign key(1:N)
외래키는 테이블의 필드 중에서 테이블의 행과 식별할 수 있는 키를 의미힌다
외래키는 테이블과 테이블을 연결하기 위해 사용되는 키이다. 테이블을 여러개로 나누어 foregin key로 연결하여 보다 효율적인 테이블을 구성할 수 있다     

- related_name : 개체 관계에 사용할 이름으로 models.py에서 관계를 정의할때 사용될 이름이며 템플릿에서 테이블의 속성에 접근할때 사용된다   

- on_delete : 개체가 삭제될때 함께 수행될 동작으로 외래키가 바라보는 테이블의 값이 삭제될때 수행할 방법을 지정한다.     
```
1. models.CASCADE : 외래키를 포함하는 행도 함께 삭제된다 (주로사용됨)
2. models.PROTECT : 해당 요소가 함께 삭제되지 않도록 오류 발생시킨다   
3. models.SET_NULL : 외래키 값을 NULL값으로 변경시킨다
```

- 접근 방법
N인 쪽에서는 관계되어 있는 모델이 1이기 때문에 바로 접근이 가능하지만 1인쪽에서 관계되어 있는 N에 접근하기 위해서는 set을 통해서 접근할 수 있다   

<br>

## Model Manger (views.py에서 생성한 models.py데이터 가져오기)   
이를 통해 해당 모델 클래스의 db 데이터를 추가, 조회, 수정, 삭제가 가능하다    

- models.objects.all()    
특정 모델의 전체 데이터를 조회한다    
```python
def home(request):
  class_object = MyClass.objects.all()

  return render(request, 'home.html',{'class_object':class_object})
```
- models.objdects.get(pk=1)   
특정 데이터만 조회하는 함수로 주로 유일한 값을 조회할때 사용한다    
```python
object = MyClass.objects.get(pk=1) # pk=1인 데이터를 반환한다. 이때 해당 데이터를 찾지 못하면 에러가 발생하기 때문에 에러처리를 해주어야 한다 

def home(request):
  try: 
    class_object = MyClass.objects.get(pk=1)
  except:
    class_object = None

  return render(request, 'home.html',{'class_object':class_object })
```
- models.objects.filter(class_num=2)     
특정 데이터만 조회하는 함수로 주로 여러개의 값을 조회할때 사용한다    
```python
filter 함수는 객체의 배열을 리턴한다. get의 에러처리가 번거롭다면 filter() ~ first()로 접근하는 방법도 존재한다

def home(request):
  class_object = MyClass.objects.filter(pk=1).first()
  return render(request, 'home.html',{'class_object':class_object })
```