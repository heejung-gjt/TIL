### 👉 Fork and Merge로 동료와 협업 - 실습으로 알아보기
<br>

```
PM
1. github에서 새로운 repo를 생성하고 내 컴에 clone 한다.
2. git flow init 후 develop에서 numguess.py를 만들고 add, commit, push
3. 팀원에게 알린다.
DEV
1. 알림 받은 후, 방문하여 fork 한다. fork한 나의 repo를 내 컴에 clone한다.
2. 팀장 repo에 방문하여 issue를 생성한다.
3. git flow init 후, dev -> feature/{MYFEATURE} 브랜칭 하여 작업한다.
   (commit 시 발급한 issue 번호 매기기)
4. feature finish 후 나의 develop으로 push 한다.
5. create pull request 하고 팀장에게 알린다.
PM
4. pull request를 리뷰한다.
5. 수정할 것을 지시한다.(DEV 6. 수정사항을 반영하여 다시 add,commit,push)
6. merge한다.
DEV 7. PM repo 업데이트 발생시 PM의 develop을 pull한다.
```

<br>

### PM

1. pm github에 ```fork-and-merge``` repo를 생성한 후 clone해준다 
```bash
$ git clone <url명>
```
<br>

2. git flow init으로  develop 브랜치를 생성한 후 해당 브랜치 내에서 numguess.py파일을 생성하여 add, commit을 해준다
```bash
$ git flow init

$ git branch #develop 생성되었는지 확인
* develop
  master

$ touch numguess.py
$ vi numguess.py # 팀원이 해야할 일 기록
$ git add numguess.py
$ git commit  
$ git push -u origin develop# master는 이미 remote와 로컬이 연결되어 있으므로 -u를 해주지 않아도 되지만 develop 브랜치는 생성된 후 처음 push를 하기 때문에    
```

3. 팀원에게 알린다    

<br>

### DEV

1. PM 의 git에 방문하여 해당 repo fork한 후 clone 해준다.    
``` 해당 repo로 이동 -> 오른쪽 상단에 fork click```  
```bash
$ git clone <fork한 dev의 url>
$ cd <clone명>
```
<br>

2. dev가 pm 의 repo에서 issue를 만든다


3. git flow init 후, dev -> feature/{MYFEATURE} 브랜칭 하여 작업한다.  
(commit 시 발급한 issue 번호 매기기)  

```bash
$ git flow init # develop 브랜치로 들어오면 pm이 작성한 numguess.py 가 있다
$ git flow feature start <feature/브랜치명>
$ vi numguess.py # 내용을 수정한다
$ git add numguess.py
$ git commit (commit 시 발급한 issue번호를 매겨준다) # solved: #n
```
<br>

4. feature finish 후 dev의 develop으로 push 한다.
```bash
$ git flow feature finish <feature/브랜치명>  # 기능 개발이 끝난 경우
$ git push origin develop
```
<br>

5. create pull request 하고 팀장에게 알린다.
pm의 repo로 돌아가 develop 브랜치에서 pull request를 눌러준다
<br>

6. 이때 conflict이 발생 할 수 있다. 이유는 이미 pm이 다른 내용을 merge했기 때문이다.   
다시 자신의 로컬로 돌아가 7번을 수행보자 ``` CONFLICT이 발생한다```
```bash
.
.
.
CONFLICT (content): Merge conflict in zero-to-number.py
Automatic merge failed; fix conflicts and then commit the result.
```
이제 다시 vi로 conflct 나는 파일로 들어가 변경해준다    
그 후 add , commit 을 차례대로 해준뒤 ```git push origin develop```으로 다시 push해주고 pull request해주면  끝 !
<br>

### PM

4. pull request를 리뷰한다.
5. 수정할 것을 지시한다. 
<br>

### DEV

6. 수정사항을 반영하여 다시 add,commit,push
```bash
$ vi numguess.py # 수정사항 변경
$ git add numguess.py
$ git commit
$ git push origin develop
```

### PM
6. ```merge 버튼을 눌러준다```

### DEV

7. PM repo 업데이트 발생시 PM의 develop을 pull한다.   

```bash
$ git remote -v # 자신의 remote인지 확인
$ git remote add pmorigin <pm의 url명>
$ git pull pmorigin develop # pm의 변경된 내용 pull
```

### PM

6. 자신의 로컬도 변경해준다
```
$ git pull origin develop
```