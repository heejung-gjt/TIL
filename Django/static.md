
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
