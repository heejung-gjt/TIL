## git branch로 checkout, merge 하기   -  branch생성 후 main의 변화가 없을때
<br>

#### git branch 명령어로 현재 존재 하는 branch와 위치하고 있는 branch를 볼 수 있다
```bash
git branch
```
<br>

#### main에 위치한 상황에서 python 파일을 하나 생성한 후 add,commit을 차례대로 해준다   
```bash
$ touch numguess.py
$ git add numguess.py
$ git commit (vi 편집기에서 작성)
```
<br>

main에 numguess.py 파일이 commit된 상태로 존재하는 것을 볼 수 있다. 해당 파일을 새로운 branch를 생성해 편집해보자   

#### 새로운 branch를 생성 한 후 해당 branch로 전환  
(git branch로 잘 전환되었는지 확인하자)
```python
$ git branch iteration  #브랜치 생성
$ git checkout iteration # 브랜치 전환
```
<br>

#### 해당 브랜치에서 numguess.py의 내용을 편집한 후 add, commit을 차례대로 해준다   
```bash
$ vi numguess.py
$ git add
$ git commit(vi 편집기에서 작성)
```
<br>

#### 수정된 numguess.py파일을 main과 병합하기 위해 merge 옵션을 사용한다. merge가 끝난 후에는 생성했던 branch를 지워주자 
```bash
$ git checkout main  # main으로 이동 후 병합
$ git merge numguess.py
$ git branch -D iteration
```
<br>

#### main에 있는 numguess.py를 확인해보면 iteration 브랜치에서 편집한 내용이 들어가 있는 것을 볼 수 있다   
<br>

위의 방법은 main에서 branch를 생성한 후 main의 내용에 변화가 없을때 merge할 수 있는 방법이다.    
branch를 만든 후에 main의 변화가 있을땐 merge하는 과정에서 conflict, 즉 충돌이 일어나게 된다   


<br>

## branch생성 후 main의 변화가 있을때 Conflict 해결하여 merge하기   
<br>

#### 새로운 branch를 생성한 후 해당 브랜치로 들어간다
```bash
$ git branch discard
$ git checkout discard

```
<br>

#### discrad 브랜치에서 numguess.py 파일을 수정한 후 add, commit을 해준다   
```bash
$ vi numguess.py
$ git add numguess.py
$ git commit
```
<br>

#### 그 뒤 충돌을 일부러 내기 위해 main으로 돌아와 merge전 numguess.py의 내용을 수정 후 add, commit을 해준다   
```bash
$ git checkout main
$ vi numguess.py
$ git add numguess.py
$ git commit
```
<br>

#### main에서 discard와 merge를 하면 충돌이 발생하게 된다
```bash
$ git merge discard

Auto-merging numguess.py
CONFLICT (content): Merge conflict in numguess.py
Automatic merge failed; fix conflicts and then commit the result.
```
<br>

#### numguess.py를 편집기를 통해 들어오면 아래와 같이 내용이 추가되어 있는 것을 볼 수 있다
```python
<<<<<<< HEAD
cnt = 5
while cnt != 0:
    num1 = random.randint(1,100)
    guess = int(input())
=======

while True:
    guess = int(input())
    if guess ==0:
        print('OK BYEBYE SEE YOU LATER.')
        break
    num1 = random.randint(1,100)
    print(f'ANSWER : {num1}')
    print(f'YOUR ANSWER : {guess}')

>>>>>>> discard

    if guess != num1:
        print('NOPE !')
        cnt -=1
print('GAME OVER')

```
<br>

```<<<<<< HEAD```       
< main에서 작성한 numgguess.py 내용 >   
```=========```   
```>>>>>>> discard```   
<branch discard에서 작성한 numguess.py 내용>      

병합을 위해서 위의 두가지의 코드를 적절히 조합하여 수정, 삭제 등 변경해주면된다. (단 ! 위의 코드에 생성되있는 ===, <<< 기호들은 지워준다)    
#### 적절히 수정한 후 저장 후  실행이 잘 되는지 확인한 후 (```python3 numguess.py```) add,commit을 해준다    

#### 만들었던 branch는 깔끔하게 지워준다
```bash
git branch -D discard
```
<br>

github에  들어가  insights -> network를 확인해보면 아래의 이미지처럼 branch가 병합된 것을 볼 수 있다   

![merge](https://user-images.githubusercontent.com/77425963/106344584-f3ae7500-62ed-11eb-9304-265a1194c5f5.png)