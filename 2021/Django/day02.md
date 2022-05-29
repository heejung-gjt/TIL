## models.py의 역할
장고는 SQL을 사용하지 않아도 파이썬으로 데이터베이스를 관리할 수 있는 ORM을 제공한다. 데이터가 많아지면 장고에서 제공해주는 것으로는 한계가 있다는 것을 알고있자.   



<br>

## views.py에서 html파일로 데이터 넘기기 
html에서는 딕셔너리의 key값으로 접근할 수 있다
```python
# views.py
context = {
  'data':data,
  'name':name
}
render(request, 'index.html',context)
```
```html
# index.html
<h1>{{ data }}</h1>
<h1>{{ name }}</h1>
```

<br>

## form태그를 이용해서 POST를 보낸다   
이때 주의해야 할 것이 있다   
- __action과 method의 작성__ : action의 역할은 request 데이터를 어떤 path에 있는 함수로 보낼지 결정하는 역할을 한다. 여기에선 result의 path에 request를 한다. 이때 method는 POST방식이므로 데이터를 보내는 요청을 한다    

- __ input에 있는 name__ : name의 역할은 views.py에서 해당 데이터를 찾을때 사용되는 네임이다. 데이터를 찾기위해서는 당연히 써주어야 한다    

- __csrf_token__ : 해당 토큰은 form에서 데이터를 요청할때 보안을 위해서 사용되어진다. 해당 내용을 써주지 않으면 error가 발생하기 때문에 잊지말고 꼭 써주도록 하자    
```HTML
<form action = "{% url 'result' %}" method = "POST">
{% csrf_token %}
<input name = "username">
<button type="submit">클릭</button>
```

<br>

## djagno 템플릿 문법
장고의 템플릿 언어는 강력함과 편리함 속 균형을 위해서 설계되었다. 장고 언어는 총 4가지의 기능을 제공해준다.    

- __변수__  
템플릿 변수는 views.py에서 해당 템플릿으로 객체를 전달해준다      
```.```은 변수의 속성에 접근할 때 사용한다   
```
{{ 변수 }}
{{ article.content }} : article객체를 html에서 객체의 속성인 content를 출력할 수 있도록 ```.```을 사용한다
``` 
- __필터__   
템플릿 필터는 변수의 값을 특정 형식으로 변환할때 사용한다. 변수 다음으로 ```|```를 넣은 후 적용하려는 필터를 명시한다         
```
{{ data|default:"none" }} # data가 비어있거나 없는경우 none을 출력해준다   

{{ article.content|length }} # content 값의 길이를 출력해준다
```
- __태그__     
템플릿 태그는 if,for문처럼 반복문을 통해 데이터를 제어할 수 있다. 20개가 넘는 템플릿 태그가 장고에 내장되어 있으므로 찾아보자      
아래와 같은 형식으로 탬플릿 태그를 쓸때는 반드시 닫아주어야 하는 태그들이 존재한다
```
{% if %}
{% end %}
{% endif %}
```
- __주석__      
html문서 상에 주석이 필요할때 사용한다   
```
{# 주석 #} # 한줄 주석

{% comment %}  # 여러줄 주석
{% endcomment %}
```

<br>

## CSS 사용하기

1. app안에 static 폴더를 만들어준다    
2. head에 link와 load static 추가해준다   
```html
<head>
{% load static %}
<link rel="stylesheet" herf="{% static 'home/css' %}">

```