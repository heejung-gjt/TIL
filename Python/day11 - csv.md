## 👉 csv와 json
<br>

### ✔ CSV 
csv는 csv 형식의ㅣ 표 형식 데이터를 읽고 쓰는 클래스를 구현한다.   
<br>

customer.csv가 파일객체이면 newline=''로 열려야 한다. csv 파일에서 읽은 각 행(row)은 문자열 리스트로 반환된다    
__reader__
```python
import csv

with open('./customers.csv', newline='') as customer_csv:
    customer = csv.reader(customer_csv)
    for row in customer:
        print(row)
"""
결과
['CustomerID', 'CustomerName', 'ContactName', 'Address', 'City', 'PostalCode', 'Country']
['1', 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany']
['2', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitución 2222', 'México D.F.', '05021', 'Mexico']
['3', 'Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312', 'México D.F.', '05023', 'Mexico']
.
.
"""        
```

### ✔ JSON

json은 다른 플랫폼으로 생성한 데이터를 전송하기 위해서 json 자료형태로 바꾸는 과정이다.   
전송하고 싶은 데이터를 dictionary 형태로 생성한 후 dump를 이용하여 자료를 인코딩 한다.   
받은 json 데이터를 python에서 사용하기 위해 load를 이용하여 자료를 디코딩한다.

- dump (dict -> str) python객체를 json 데이터로 쓰기    
- load (str -> dict) json 데이터를 python 객체로 읽기    
<br>

### 실습01    
(dump와 load이용해 dict 데이터 인코딩 디코딩하기)

<br>

__1.실습을 위해서 딕셔너리 형태의 data를 생성한다__   


```python
data = {'users':[
    {'name':'KD Hong', 'locale':'Seoul, KR'},
    {'name': 'John Doe', 'locale':'New York, US'},
    {'name': 'Jane Doe', 'locale':'London, UK'}
]}

"""
결과
{'users': [{'name': 'KD Hong', 'locale': 'Seoul, KR'}, {'name': 'John Doe', 'locale': 'New York, US'}, {'name': 'Jane Doe', 'locale': 'London, UK'}]} 
"""
```
<br>

__2.생성한 dict 자료를 json 데이터로 변경하기 위해 dump를 이용하여 users.json 파일에 작성한 dict자료를 넣는다__
```python
import json

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

"""
결과 : 새로운 json파일인 users.json이 생성된다   
{"users": [{"name": "KD Hong", "locale": "Seoul, KR"}, {"name": "John Doe", "locale": "New York, US"}, {"name": "Jane Doe", "locale": "London, UK"}]}
"""
```
<br>

__3.json 데이터를 load를 이용하여 python객체로 읽어온다__   
```python
with open('users.json','r',encoding='utf-8') as f:
    dse_data = json.load(f)

"""
결과
{'users': [{'name': 'KD Hong', 'locale': 'Seoul, KR'}, {'name': 'John Doe', 'locale': 'New York, US'}, {'name': 'Jane Doe', 'locale': 'London, UK'}]}
"""
```
<br>

### 실습02
(customer.csv파일을 인코딩하여 json 파일로 변환하기)
<br>

__1. csv파일 customer.csv파일을 읽기 형식으로 가지고 오는데  리스트 컴프리헨션을 이용하여 리스트 형태로 읽어온다__

```python
import csv

with open('./customers.csv','r',encoding='utf-8') as f"
    customer = csv.reader(f)
    customer_list = [i for i in customer]

"""
결과

-------------------customer.csv 파일-------------------
[['CustomerID',
  'CustomerName',
  'ContactName',
  'Address',
  'City',
  'PostalCode',
  'Country'],
 ['1',
  'Alfreds Futterkiste',
  'Maria Anders',
  'Obere Str. 57',
  'Berlin',
  '12209',
  'Germany'],
 ['2',
  'Ana Trujillo Emparedados y helados',
  'Ana Trujillo',
  'Avda. de la Constitución 2222',
  'México D.F.',
  '05021',
  'Mexico'],
 ['3',
  'Antonio Moreno Taquería',
  'Antonio Moreno',
  'Mataderos 2312',
  'México D.F.',
  '05023',
  'Mexico'],
  .
  .
]
"""
```
<br>

__2.읽어온 리스트 형태의 데이터에서 데이터 정보가 아닌 0번째 데이터를 제외한 모든 데이터를 딕셔너리 형태로 바꾼다__

```python
users = {'users':[]}  # customers 데이터를 담을 dict 정의

for row in customer list[1:]: # 데이터 정보가 아닌(column name) 0번째를 제외한 고객 데이터
    user_dict ={}  # 한명의 정보를 담을 dict 정의
    for index, key in enumerate(customer_list[0]):  # enumerate를 이용하여 column name을 이용해 index와 key를 생성한다
        user_dict[key] = row[index]  {column name} = 고객데이터
    users['users'].append(user_dict)  # 완성된 고객 데이터 dict 를  users['users']에 추가

with open('./customers.json', 'w', encoding='utf-8')as g:
    json.dump(users, g)  #customers.json 데이터 생성

"""
결과
새로운 customers.json 파일이 생성되고 json파일로 인코딩된 customer 데이터가 들어간다

-------------------customer.json 파일-------------------
"users": [{"CustomerID": "1", "CustomerName": "Alfreds Futterkiste", "ContactName": "Maria Anders", "Address": "Obere Str. 57", "City": "Berlin", "PostalCode": "12209", "Country": "Germany"}, {"CustomerID": "2", "CustomerName": "Ana Trujillo Emparedados y helados", "ContactName": "Ana Trujillo", "Address": "Avda. de la Constituci\u00f3n 2222", "City": "M\u00e9xico D.F.", "PostalCode": "05021", "Country": "Mexico"}, {"CustomerID": "3", "CustomerName": "Antonio Moreno Taquer\u00eda", "ContactName": "Antonio Moreno", "Address": "Mataderos 2312", "City": "M\u00e9xico D.F.", 
.
.

"""
```
for index, key in enumerate(customer_list[0]):    
        user_dict[key] = row[index]    
        
enumerate를 이용하여 column name을 이용해 index와 key를 생성한다 : column name 인 key값 CustomerID를 새로운 dict 인 user_dict의 키값으로 지정하고  이에 해당되는 index값 1을 이용해 고객의 데이터 리스트인 row, 즉 첫번째 리스트의 인덱스 1번에 있는 값 1을  value값으로 지정하여 고객 각각의 정보를 user_dict에 넣는다 

<br>

### 실습03
[👉 해당공공데이터 csv 파일 json 파일로 converting 하기](https://www.data.go.kr/data/15007386/fileData.do)

<br>

공공데이터포털 사이트에 있는 파이들은 대부분 cp949로 다운이 되어지므로 우분투에서 사용시
리눅스 시스템에서 파일 인코딩을 확인하고 utf-8로 바꾸어준다    

__파일 인코딩 확인 : file -bi <파일명>__   
__파일 인코딩 변환 : iconv -c -f <기존 인코딩명> -t <변경할 인코딩명> <파일명> > <새로 적용할 파일명>__   

<br>

__1.csv파일 리스트 형태로 열기__      
```python
import csv

with open('./aa.csv','r',encoding='utf-8') as f:
    people_num = csv.reader(f)
    people_list = [i for i in people_num]
people_list
"""
결과
[['구별',
  '동',
  '인구수_합계',
  '인구수_남',
  '인구수_여',
  '19세 이상_계',
  '19세 이상_남',
  '19세 이상_여',
  '65세 이상_계',
  '65세 이상_남자',
  '65세 이상_여자',
  '세대수',
  '재외국민'],
 ['수정구',
  '신흥1동         ',
  '13511',
  '7107',
  '6404',
  '12381',
  '6519',
  '5862',
  '2567',
  '1073',
  '1494',
  '7898',
  '9'],
  .
  .
"""
```
<br>

__2.해당 데이터 딕셔너리 형태로 변환하기__      
```python
import json

people = {'people':[]}

for i in people_list[1:]:
    people_dict={}
    
    for index, key in enumerate(people_list[0]):
        people_dict[key] = i[index]
    people['people'].append(people_dict)
    print(people)
with open('./people_num.json', 'w', encoding='cp949') as num:
    json.dump(people,num)
"""
결과
{'people': [{'구별': '수정구', '동': '신흥1동         ', '인구수_합계': '13511', '인구수_남': '7107', '인구수_여': '6404', '19세 이상_계': '12381', '19세 이상_남': '6519', '19세 이상_여': '5862', '65세 이상_계': '2567', '65세 이상_남자': '1073', '65세 이상_여자': '1494', '세대수': '7898', '재외국민': '9'}, {'구별': '수정구', '동': '신흥2동         ', '인구수_합계': '20239', '인구수_남': '9911', '인구수_여': '10328', '19세 이상_계': '17042', '19세 이상_남': '8328', '19세 이상_여': '8714', '65세 이상_계': '2686', '65세 이상_남자': '1277', '65세 이상_여자': '1409', '세대수': '7693', '재외국민': '22'}, {'구별': '수정구', '동': '신흥3동         ', '인구수_합계': '11309', '인구수_남': '5893', '인구수_여': '5416', '19세 이상_계': '10318', '19세 이상_남': '5377', '19세 이상_여': '4941', '65세 이상_계': '2020', '65세 이상_남자': '878', '65세 이상_여자': '1142', '세대수': '6450', '재외국민': '9'}, {'구별': '수정구', '동': '태평1동         ', '인구수_합계': '15566', '인구수_남': '7
.
.  
"""
```
<br>

__3. load로 json 가져오기__    
(구, 동, 인구수_남 데이터 가져오기)

```python
with open('people_num.json', 'r', encoding='utf-8') as f:
    des_data = json.load(f)
    for row in des_data['people']:
        print('구: {} 동: {} man: {}'.format(row['구별'],row['동'].strip(), row['인구수_남']))
"""
결과
구: 수정구 동: 신흥1동 man: 7107
구: 수정구 동: 신흥2동 man: 9911
구: 수정구 동: 신흥3동 man: 5893
구: 수정구 동: 태평1동 man: 7960
구: 수정구 동: 태평2동 man: 7853
구: 수정구 동: 태평3동 man: 6956
구: 수정구 동: 태평4동 man: 6830
구: 수정구 동: 수진1동 man: 6552
구: 수정구 동: 수진2동 man: 8125
구: 수정구 동: 단대동 man: 7843
구: 수정구 동: 산성동 man: 5179
구: 수정구 동: 양지동 man: 4932
구: 수정구 동: 복정동 man: 6107
구: 수정구 동: 위례동 man: 22343
구: 수정구 동: 신촌동 man: 2549
.
.
"""
```