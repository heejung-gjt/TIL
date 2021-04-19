'''
멜론 21년기준 1 ~3월까지 1-100순위 스크래핑하기
'''
import urllib.request
import requests
import json,csv
from bs4 import BeautifulSoup


infor_arr = []

# 원하는 태그 추출해주는 함수
def tag_print(soup):
    table_list = soup.select_one('#frm > div > table > tbody')
    table_50 = table_list.select('#lst50')
    table_100 = table_list.select('#lst100')
    table_arr = table_50 + table_100    
    for music in table_arr:
      rank = music.select_one('div > span.rank').text
      title = music.select_one('td > div > div > div.ellipsis.rank01 > span > a').text
      music_infor = {
        'month': params[2][1],
        'rank': rank,
        'title': title
      }
      infor_arr.append(music_infor)

# csv변환해주는 함수
def writer_csv(file_path, infor):
  field = ['month','rank','title']
  with open(file_path, 'w',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=field)
    writer.writeheader()
    writer.writerows(infor)

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
    'If-None-Match': '"HTTP Conditional Get"', # 304 상태코드때문에 변경해줌
}

for i in range(1,4):
  params = (
      ('classCd', 'GN0000'),
      ('moved', 'Y'),
      ('rankMonth', f'20210{i}'),
  ) 
  # print(params[2][1])
  response = requests.get('https://www.melon.com/chart/month/index.htm', headers=headers, params=params)
  soup = BeautifulSoup(response.text,'html.parser')
  tag_print(soup)

writer_csv('./last_sample.csv',infor_arr)