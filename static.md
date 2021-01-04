### django static 설정해 css 사용하기 

⚡삽질 기록 


### 목차
   
✔ Installation

✔ MTV code pattern
   
✔ Practice
   
<br><br>

## [Installation](https://heejung-gjt.github.io/django-01)

### 가상환경 세팅하기

가상환경 세팅 전에 python 3.x 버전을 설치하여 환경변수에 등록해준다 ( 설치시 Add Python 3.x to PATH 클릭 )

패키지 간의 버전차이, 여러 충돌을 방지하기 위해 가상환경을 구축한다.
가상환경이 성공적으로 설정되면 터미널안에 (venv_django) 가 생성된다.
생성된 가상환경에서 django를 설치한다.
 

```bash
$ python -m venv venv_django   #venv_djanog 가상환경 설정
$ source venv_django/Scripts/activate  # 가상환경 실행
$ pip install django
```

### 프로젝트 생성

django 프로젝트는 하나의 프로젝트와 여러개의 app으로 구성된다. app안에는 model, view, template, url매핑등 여러가지 app들로 나누어서 구성하고 있다. app들을 여러개로 구성함으로써 개발 및 유지 보수를 효율적으로 할 수 있는 장점이 있다.   
<br>
django-admin 명령어를 통해서 프로젝트와 app을 생성한다. 생성된 app안에 templates 폴더를 만들어준다.

```bash
$ django-admin startproject community #community 프로젝트 생성
$ django-admin startapp user  #user 앱 생성
```

### 프로젝트 실행

만들어진 프로젝트를 runserver를 통해서 실행해준다.

```bash
$ python manage.py runserver
```
![runserver](https://user-images.githubusercontent.com/64240637/103471082-c2aa5580-4dbe-11eb-8a15-48de2b48b445.PNG)

위의 화면이 뜨면 제대로 install 된것 🙌
<br>

## [MTV code pattern](https://heejung-gjt.github.io/django-02)

### MTV 생성

django에서 MTV 패턴은 프로젝트 내에서 유저의 요청부터 응답까지 동작하는 방식에 대한 패턴이다. 
생성된 app 안에는 model과 view는 생성이 되어져 있다. template을 사용자가 따로 생성해야 하는데 보통 앱안에서 생성을 한다.

- Model 은 DB에 저장되는 데이터를 의미한다. models.py에서 생성되는 클래스는 DB의 구조로 생성되어진다. 데이터를 처리하는 로직을 가지고 있다   
- Template 은 사용자에게 보여지는 부분이다. 사용자가 직접 접근하는 html 등과 같은 페이지를 구성한다.   
- View 는 template에서 받은 request을 처리하고 받은 데이터를 로직으로 가공하여 reponse 해주는 역할을 한다. 


#### 1.Model 생성 ( user app 안에 있는 MTV )

📌  __django의 models.py 로직을 생성__   

```bash
$ class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='사용자명')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    class Meta:
        db_table = 'campus_user'
   
```
<br>

📌 __프로젝트에 생성되어져 있는 manage.py 를 통해 model에서 만들어진 로직으로 DB생성__   

```bash
$ python manage.py makemigratons
$ python manage.py migrate   #table 생성
```
📝 이때 생성한 프로젝트 내에 있는 settings.py 에서 INSTALLED_APPS 안에 user app을 넣어주어야 db가 생성된다.   

<br>

📌 __프로젝트내 db.sqlite3이 생성. 해당 db를 확인하기 위해서 [db browser for sqlite](https://sqlitebrowser.org/dl/)
다운받아 확인__   
<br>
### django static 설정해 css 사용하기 

#### ⚡삽질 기록    

- project에 static 폴더를 생성한다
- 생성한 폴더에 html의 스타일을 변경해줄 css 넣는다
- 넣은 css를 사용하기 위해서 settings.py에서  STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ] 를 작성한다
- 그 후 적용시킬 html 파일에 <link href="static/파일.style"> 작성해준다     
- 그럼 끝 ❗   

<br>

#### ❓하지만 아래의 오류가 발생함

static 폴더를 못찾는것 같았다. 아무리 구글링 해보아도 보통 settings.py만 변경시켜주는 내용이였다.
```bash
Not Found: /fcuser/register/static/bootstrap.min.css
[04/Jan/2021 22:35:50] "GET /fcuser/register/static/bootstrap.min.css HTTP/1.1" 404 2228
```
<br>

일단 내 django 파일에 있는 settings.py에는 아래의 코드들 처럼 os가 import되있는 상태가 아니였음     
<br>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # 보통 default값은 NAME': os.path.join(BASE_DIR, 'db.sqlite3') 인 듯 했다
    }
}
```
<br>

__다들 default값을 바꾸어준 것인가 ?__   
각설하고 그래서 settings.py에 os import 해준 뒤 아래 코드와 같이 작성해줌

```python
import os

STATIC_URL = '/static/' 
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
```
<br>

그 뒤 해당 HTML 파일로 돌아가 아래 코드 작성해줌

```html
<link rel ="stylesheet" href="static/bootstrap.min.css"> 
```
<br>

하지만 여전히 똑같은 문제가 발생함   
계속해서 구글링 한 결과 html에 static 파일을 삽입할때 href="{% static     %}" 처럼 작성하는 경우도 발견함    
위의 코드를 해석해보자면 __template 랜더링 과정에서 static이라는 이름의 메소드를 호출하면서 매개변수로 .css를 전달하여 해당 반환값을 찾을 수 있는 실제 경로가 된다__  ... 좀더 공부가 필요해보임    
<br>
아무튼 아래 코드처럼 바꾸어줌. 이때 {% load static %} 를 넣어주어야 static이 로드됨

```html
{% load static %}

<link rel="stylesheet" href="{% static 'bootstrap.min.css' %}" /> 
```
<br>

#### 📌정리

1. static 폴더를 만든 후 settings.py에 설정할때 import os를 넣어주자
2. template에서 파일을 삽입하는 방법은 여러개다. 그 중 나는 아래의 코드처럼 작성하였다
```html
{% load static %}

<link rel="stylesheet" href="{% static 'bootstrap.min.css' %}" /> 
```
이상 오늘의 삽질이였다,,😂 그럼 static 파일에 대해서 알아보자

<br>

### ⚡static 파일이란
