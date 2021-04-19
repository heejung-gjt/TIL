## 멜론 100차트 순위 2021 01 ~ 스크래핑 후 csv 저장하기   

### 주의할점 
- 멜론은 html을 기준으로 스크래핑을 하기 위해선 import requests가 아닌 import urllib.request를 이용해야 한다    

Q. 왜 urllib.request인가? requests와 차이점은 무엇인가?    

- 멜론의 상태코드는 304가 출력된다.   따라서 API스크래핑에서 HTTP Get의 특별한 타입으로 요청 메시지에 다음 아래의 필드가 있다면 ```HTTP Conditional Get```으로 변경하자     
[304 상태코드 자세히 보기](http://wiki.gurubee.net/pages/viewpage.action?pageId=26739910)    

- If-Modified-Since   
- If-Unmodified-Since   
- If-Match   
- If-None-Match   
- If-Range header fields    

-> 대부분의 브라우저는 HTTP conditional request를 사용하여 자동 캐시 기능을 지원한다    

## 구현

- ### [api 스크래핑 이용해 01-03월 스크래핑]()   

- ### [json파일 생성후 csv파일로 변환]()    

- ### [DictWriter을 이용해 csv파일로 변환, 함수로 작성]()

## 연습 

- ### [csv파일 변환 연습]()