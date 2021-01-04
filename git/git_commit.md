### remote 서버 파일에는 수정이 없지만 로컬에서 수정된 파일 push 하기 

#### ⚡삽질 기록    

- 서버에서 작성한 readme.md 파일을 로컬에도 반영될 수 있게 로컬에서 서버를 pull 해준다   
- pull된 서버의 폴더를 로컬에서 열어 해당 폴더에 작성한 파일들을 옮겨준다    
- 로컬에서 git add와 git commit를 하여 서버에 반영해준다 
- 그럼 끝 ❗   

<br>

#### ❓하지만 아래의 어려움이 발생함
<br>

__1. 로컬에서 어떤 명령어를 먼저 쳐야되는지 굉장히 헷갈렸음__


__2. 어떤 폴더에서 add, commit, push등을 해야하는지 헷갈렸음__   

__3. 서버에 먼저 작성되어 있던 readme.md 파일이 commit할때마다 삭제됨__

<br>

#### 📌정리

가장 먼저 업로드 시키고 싶은 폴더에서 git을 생성해준다. 그 후 차례대로 
clone과 remote 명령어를 통해 github에 있는 어떤 폴더로 commit 할 건지 주소를 작성한다.
<br>

```cmder
C:\Users\dkfkf\Desktop\Django\Django_error
λ git init

λ git clone https://github.com/heejung-gjt/TIL.git
λ git remote add origin https://github.com/heejung-gjt/TIL.git
```
<br>
그 뒤 pull을 이용하여 서버에 있는 파일들을 로컬로 불러온다. 서버에 작성되어 있던 readme.md 파일은 나중에 같이 push 해준다. 그럼 리드미가 삭제될 이유는 없다.   
로컬에서 서버에서 불러온 폴더에 파일을 이동시킨다. 이때 주의하자 ! TIL폴더가 생성되었으니 TIL폴더로 옮겨준 후 TIL 안에서
commit등을 해준다.   

<br>

```cmder
λ git pull

λ ls
static.md  TIL/

C:\Users\dkfkf\Desktop\Django\Django_error\TIL (master -> origin)   
λ git add .

λ git commit -m "[#django01] static 파일 설정"

λ git push
```


<br>

그럼 서버에 이미 작성된 파일에 영향을 주지 않고 로컬에 있는 파일들을 서버에 업로드 할 수 있다    
생각보다 어렵지 않았지만 처음 공부했을때는 굉장히 헷갈렸다.. 진짜 날려먹은 readme만 몇개인가..

이상 오늘의 삽질이였다,,😂 그럼 git의 commit에 대해서 알아보자

<br>

### ⚡git의 commit