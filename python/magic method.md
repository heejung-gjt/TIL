### python 특수한 메서드(Magic Method)

#### 1. init
인스턴스를 생성하면 자동으로 실행되어지는 함수이다
  
#### 2. str
인스턴스 자체를 출력할때 형식을 지정하는 함수이다. 객체를 출력하면 __ __str__ __ 메서드를 호출한다. 아래 코드를 보면
생성된 subject자체를 출력해보면 __ __str__ __ 에서 지정한 return값이 출력되는것을 볼 수 있다
```python
class Subject():
    def __init__(self, title, date):
        self.title = title
        self.date = date
        
    def __str__(self):
        return f'과목: {self.title}, 날짜: {self.date}'

subject = Subject('coding', 210213)
print(subject)

# 출력 : 과목: coding, 날짜: 210213
```