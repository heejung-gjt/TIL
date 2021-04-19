'''
with open을 이용한 json파일 생성후 json파일 csv파일로 변환
'''
import urllib.request
import requests
import json,csv
from bs4 import BeautifulSoup


headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.melon.com/chart/month/index.htm',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': '"HTTP Conditional Get"',
}

infor_arr = []

for i in range(1,4):
  params = (
      ('classCd', 'GN0000'),
      ('moved', 'Y'),
      ('rankMonth', f'20210{i}'),
  ) 
  response = requests.get('https://www.melon.com/chart/month/index.htm', headers=headers, params=params)
  # print(response)
  soup = BeautifulSoup(response.text,'html.parser')

  table_list = soup.select_one('#frm > div > table > tbody')
  # table_body = table_list.select_one('#frm > div > table > tbody')
  table_50 = table_list.select('#lst50')
  table_100 = table_list.select('#lst100')
  table_arr = table_50 + table_100

  print(params[2][1])
  

  for music in table_arr:
    rank = music.select_one('div > span.rank').text
    title = music.select_one('td > div > div > div.ellipsis.rank01 > span > a').text
    music_infor = {
      'month': params[2][1],
      'rank': rank,
      'title': title
    }
    infor_arr.append(music_infor)
dict = {}
dict['infor_arr'] = infor_arr

import json,csv

file_path = './sample.json'

with open(file_path, "w", encoding='utf-8') as outfile:
  json.dump(dict, outfile, ensure_ascii=False)

data_file = open('data_file.csv','w')
csv_writer = csv.writer(data_file)

count = 0

for infor in infor_arr:
  print(infor)
  if count == 0:
    header = infor.keys()
    csv_writer.writerow(header)
    count += 1
  
  csv_writer.writerow(infor.values())

data_file.close()