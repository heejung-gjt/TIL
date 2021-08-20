
### jekyll에서 Django template 코드 작성하기

#### ⚡삽질 기록    

- Django html에서 템플릿을 확장하는 코드를 작성하여 넣었는데 Liquid Exception 에러가 발생하였다. {% load static %} 처럼 생긴 코드들에 대해서 오류가 발생한듯 하다. 찾아보니 jekyll이 ruby tag로 인식해서 오류가 발생한다고 한다.

```bash
  Liquid Exception: Liquid syntax error (line 20): Unknown tag 'load' in C:/blogmaker/_posts/Django/2021-01-09-django-0
5-template.md
             Error: Liquid syntax error (line 20): Unknown tag 'load'
             Error: Run jekyll build --trace for more information.
```
  
<br>

#### 📌해결방법

html코드를 {% raw %} ~{% endraw %} 안에다 작성하자 
```html
{% raw %} 
<html>
    <head>
        <!-- Required meta tags -->
        {% load static %}
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'bootstrap.min.css' %}" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    <body>
        <div class="container">
            {% block contents %}
            {% endblock %}
        </div>
        
    </body>
</html>
{% endraw %}

```
그럼 정상적으로 작동이 된다 !

