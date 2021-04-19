'''
01월부터 03까지의 순위와 title 스크래핑하기
- api 스크래핑 이용
- params로 01,02,03월의 정보 각각 스크래핑
'''
import urllib.request
import requests
from bs4 import BeautifulSoup


# hdr = { 'User-Agent' : 'Mozilla/5.0' }
# res = urllib.request.Request('https://www.melon.com/chart/month/index.htm',headers=hdr)
# html = urllib.request.urlopen(res).read()
# soup = BeautifulSoup(html,'html.parser')
# month = soup.select_one('#conts > div.calendar_prid > span').text

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

for i in range(1,4):
  params = (
      ('classCd', 'GN0000'),
      ('moved', 'Y'),
      ('rankMonth', f'20210{i}'),
  ) 
  print(params[2][1])
  response = requests.get('https://www.melon.com/chart/month/index.htm', headers=headers, params=params)
  # print(response)
  soup = BeautifulSoup(response.text,'html.parser')

  table_list = soup.select_one('#frm > div > table > tbody')
  table_50 = table_list.select('#lst50')
  table_100 = table_list.select('#lst100')
  table_arr = table_50 + table_100

  for music in table_arr:
    rank = music.select_one('div > span.rank').text
    title = music.select_one('td > div > div > div.ellipsis.rank01 > span > a').text
    print(rank, title)
  print()
  print()