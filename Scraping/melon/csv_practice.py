'''
csv 읽기,쓰기 연습
'''
import csv


field = ['date','title','writer']  

sample_dict = [
  {'date':202102,'title':'a','writer':'a1234'},
  {'date':202103,'title':'b','writer':'bcdee'},
  {'date':202104,'title':'c','writer':'ljgor'}
]

def dict_writer_csv_dict(filepath):
  with open(filepath, 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    writer.writerows(sample_dict)

def writer_csv_dict(filepath):
  with open(filepath, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    for dict in sample_dict:
      for k,v in dict.items():
        writer.writerow([k,v])

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

dict_writer_csv_dict('./sample_dict.csv')
read_csv_dict('./sample_dict.csv')
# writer_csv_dict('./sample_dict2.csv')





