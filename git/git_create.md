## git에 작성 내용 업로드하기

#### 1. github페이지에서 새로운 repository를 생성한다    
- 여기서 만약 README.md를 생성했다면 4번-7번은 생략해준다   

<br>

#### 2. 로컬로 돌아와 저장할 폴더를 지정한 곳에 clone  해준다.  (클론 주소 :  github -> 생성한 repo -> code 클릭 -> https url을 복사 후 붙여넣기)
```bash
git clone <url주소>
```
<br>

#### 3. 해당 폴더에 github의  repo이름으로 폴더가 생성된다. (해당 로컬과 repo가 연결되었다)  
<br>

#### 4. README.md파일이 없다면 ```touch README.md```를 해준다
<br>

#### 5. git add 후 git commit을 해준다    
(이때 git commit -m ""은 삼가해준다. 직접 편집기 들어가 변경후 저장 선호)    
<br>

#### 6. main으로 branch를 연결해준다   
(만약 바로 push를 해준다면 master로 연결됨)
```bash 
git branch -M main
```
<br>

#### 7. 해당 내용을 main에 push해준다   
(처음 push를 해줄땐 -u를 써준다)
```bash
git push -u origin main 
```
<br>

### 8. github에서 확인해 잘 올라갔으면 끝 !