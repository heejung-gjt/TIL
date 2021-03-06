### python 함수

-  매개변수(parameter)   
매개변수는 변수, 정의라고 부른다. 함수의 정의 부분에 나열되어 있는 변수로 func 함수에 있는 a와b를 파라미터, 즉 매개변수라고 부른다    

- 전달인자(argument)   
전달인자는 함수가 호출될때 제공되는 값들을 말한다. 실행이라고도 말하며 호출 할 때마다 값이 바뀔수 있다

```python
def func(a,b): # a 와 b == 파라미터 
    return a+b

result = func(10,20) # 10,20 == 알규먼트
```
<br>

### 이니셜라이저
이니셜라이저는 초기화를 뜻한다   

 아래의 코드에서 만약 사용자가 값을  입력하지 않는다면 (알규먼트가 없다면) 지정해둔 값, 즉 이니셜라이즈한 값을 추가해준다(파라미터에 이니셜라이즈를 추가할 수 있다)
```python
def ask_name(user_name='hee',status='Fool'):  # hee, Fool == 이니셜라이즈
    print(f'hi {user_name} {status}')

ask_name('heejung')

# 답 : hi heejung Fool 
# user_name은 사용자가 알규먼트를 입력하였기 때문에 파라미터로 전달 받았으며, status는 전달 받은것이 없기 때문에 이니셜라이즈 한 기본값  Fool이 출력된다 
```
<br>

### *args와 **kwargs

- args는 정해지지 않은 수의 파라미터를 받는다
- kwargs는 정해지지 않는 수의 키워드 파라미터를 받는다    
<br>

파라미터로 args 인자를 받는다. 사용자가 입력한 값의 수만큼 파라미터로 받는다. args는 튜플로 값이 출력된다.

```python
def print_(*args): #실제로 args 사용을 위해서는 *를 빼주자
    print(args, type(args)) #args 는 튜플로 받는다 . 리스트나 튜플은 비슷하므로 , 인덱스를 이용할 수 있다.
    for s in args:
        print(s, end=' ')
print_(1,2,3)

#답 : (1,2,3)<class 'tuple'>
      1,2,3
```
<br>

파라미터로 kwargs 인자를 받는다. 마찬가지로 사용자에게 여러개 값을 입력 받을 수 있다 . 이때 부가정보도 함께 보낼 수 있다. dic로 값을 출력할 수 있다

```python
def get_user_info(**kwargs): #부가 정보 알규먼트 지정 : 딕셔너리로 받아준다
    print(kwargs, type(kwargs))
    for k,v in kwargs.items(): #딕셔너리를 출력되므로 items()로 key와 value를 얻을 수 있다
    print('{}:{}'.format(k,v))
    print(kwargs['phone'])  #phone 넘버만 받고 싶다면

get_user_info(name='son',
             user_name='fdcmo',
             phone='0102808',
             locale='seoul')

"""
답 
{'name': 'son', 'user_name': 'fdcmo', 'phone': '0102808', 'locale': 'seoul'} <class 'dict'>
name:son
user_name:fdcmo
phone:0102808
locale:seoul
0102808
"""
```
파라미터 순서 : 디폴트알규먼트가 먼저 나오고 키워드 알규먼트가 나오기전에 이니셜라이즈 한 키워드 알규먼트가 나온다   
디폴트 알규먼트 -> 이니셜라이저 한 키워드 알규먼트 -> 키워드 알규먼트  