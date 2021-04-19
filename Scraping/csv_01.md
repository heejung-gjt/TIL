## csv 변환
파이썬에는 csv 파일을 읽고쓰기 위한 csv 모듈이 존재한다.    

### csv 파일쓰기
csv파일을 생성하고 작성할 수 있다. list에 있는 데이터를 csv로 변환하거나 dict에 있는 데이터를 csv로 변환할 수 있다     

```dict -> csv```   
- writer()   
writer()을 사용하면 사전 항목이 하나만 있기 때문에 csv파일의 레이아웃에는 첫번째 열에 모든 키가 포함되고 값은 두번째 열에 있다. csv파일에 여러 사전을 삽입하고 싶다면 DictWriter()을 사용하자    

- DictWriter()    
첫번째 행에는 키 레이블이 포함되어야하고 결과행에는 각 사전 항목의 값이 포함된다. 가장 먼저 동일한 키 값을 가진 사전 배열을 선언한다. 그 뒤 DictWriter()을 사용하여 f 파일에 fieldnames는 사전에 지정해둔 field로 이름을 지정해주면 지정한 fieldnames의 순서대로 저장된다. 헤더를 추가하기위해 writerheader()를 먼저 호출한다. 이 후 writerrows를 사용하여 데이터를 csv에 넣어준다

```python
import csv


field = ['date','title','writer']  

sample_dict = [
  {'date':202102,'title':'a','writer':'a1234'},
  {'date':202103,'title':'b','writer':'bcdee'},
  {'date':202104,'title':'c','writer':'ljgor'}
]

def dict_writer_csv_dict(filepath): #DictWriter사용
  with open(filepath, 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    writer.writerows(sample_dict)

def writer_csv_dict(filepath): #writer사용
  with open(filepath, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    for dict in sample_dict:
      for k,v in dict.items():
        writer.writerow([k,v])
dict_writer_csv_dict('./sample_dict.csv')
writer_csv_dict('./sample_dict2.csv')
```

### csv 파일읽기
쓰기와 동일하게 reader() 혹은 DicReader()를 사용하여 각 필드를 읽을 수 있다   

- reader()로 생성된 객체를 for문으로 읽어오면 각 줄(row)을 읽어올 수 있다   
- 다시 row를 반복문으로 읽어오면 각 필드를 얻을 수 있다    
- 2개의 중첩된 for문으로 모든 필드를 가져올 수 있다    
- DictReader()의 경우 filednames를 통해 헤더를 순서대로 읽어올 수 있다. 먼저 읽어온 헤더를 순서대로 출력해주고 그 이후에 Reader()와 동일하게 For문으로 각 줄을 읽어온다. 이때 reader()와는 다르게 Row에는 dict타입이 저장되어 있기때문에 []연산자를 통해 접근하면 순차적으로 가져올 수 있다    


```python
def read_csv_dict(filepath):
  with open(filepath,'r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    for field in fields:
      print('{:>15}'.format(field), end='')
    print()
    for row in reader:
      for field in fields:
        print('{:>15}'.format(row[field]),end='')
      print()
read_csv_dict('./sample_dict.csv')

'''
  date          title         writer
202102              a          a1234
202103              b          bcdee
202104              c          ljgor
'''
```