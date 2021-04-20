## django란
장고는 서버역할을 할 수 있는 웹 프레임워크(웹 개발을 하기 위한 도구들을 미리 갖춘 것)로 python 기반 웹 프레임워크이다      

## django 장점
- 파이썬 기반 웹 프레임워크로 파이썬에서 가능한 모든 동작이 가능하다   
- 다양하고 강력한 라이브러리가 존재한다   
- 장고의 보안은 매우 안전하다     
- 기본적으로 admin이 제공된다     

## django 가상환경 설정
가상환경을 만들어 django 프로젝트를 진행한다. 가상환경은 꼭 필요하다. 서로 다른 버전에서 프로젝트를 진행할 수 있기 때문에 가상화경을 세팅하여 사용하자
```bash
mkdir django_project
cd django_project
virtualenv venv
source venv/bin/activate
pip install django
```

## django 프로젝트 설치
config라는 폴더가 생긴다. config 폴더에는 프로젝트의 세팅 및 기본 구조가 담긴다. 뒤에 .을 붙여주어야 폴더로 생성이 된다
```bash
django-admin startproject config .
```
이후 프로젝트에서 사용할 앱을 생성한다. 이때 생성한 앱은 settings.py에 INSTALLED_APPS에 등록해주어야 한다
```bash
python manage.py startapp firstapp
```
manage.py를 실행하여 django서버를 실행시킨다.이때 manage.py가 있는 곳에서 실행해야 한다. 
```bash
python manage.py runserver
```

## 장고의 전체적인 흐름
![django](https://user-images.githubusercontent.com/64240637/115385635-517a9b00-a213-11eb-8593-285a46e84955.png)

1. 장고에서 웹서비스를 제공할때 가장먼저 필요한 데이터가 존재하는지 urls.py에서 찾아서 확인한다. 이때 정의된 url에 해당하는 views.py를 호출해준다   

2. 존재할 경우 해당 데이터를 가지고 있는 view에서 필요한 데이터를 model에서 가져와 로직을 작성하여 적절하게 가공하고 템플릿에 전달하는 역할을 한다    

3. 템플릿은 정보들을 보여주기 위해 html을 만들어두고 response로 주면서 사용할 수 있는 파일이다. 장고만의 템플릿 문법을 사용한다   

4. view에서 필요한 데이터를 models.py에서 찾는데 단순히 데이터베이스라고 생각해도 된다. models.py은 데이터베이스에 저장되는 데이터를 표현한다    

## views.py에서 요청을 처리하는 방식에 대한 실습
실습과정 : 해당 endpoint로 들어올때 해당하는 말을 보여주는 페이지를 만든다.urls.py에서 /로 들어왔을때 hello world 라는 문장이 나올 수 있도록 한다 

가장 먼저 urls.py에 요청이 들어오기 때문에 urls.py에서 /와 연결할 views.py를 작성해준다. 생성한 firstapp에 있는 views를 연결하므로 해당 app의 views를 import하여 사용한다. views에 index라는 함수를 실행한다
```python
# urls.py
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

urls.py에서 index를 요청하였기 때문에 views에서 응답하는 index함수를 작성한다
```python
#firstapp/views.py
from django.http import HttpResponse

def index(request):
  return HttpResponse('hello world')
```
이후 서버를 실행시키면 templates를 사용하지 않고도 화면에 데이터를 출력할 수 있다