## ✔ Git Undo 정리

- local에서 작업하고 있는 staging area나 working directory, commit 에서 작업하는 내용을 수정, 삭제 할 수 있는 내용이다.


## 📌git restore 명령어

#### working directory와 staging area에 있는 파일을 restore 명령어를 통해 각 내용을 초기화 할 수 있다


```bash
λ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   second_content.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sixth.txt

no changes added to commit (use "git add" and/or "git commit -a")

```
<br>

- git restore <파일이름> 을 이용하면 해당 파일이 있는 공간을 초기화 해준다.    
- 단지 작업하는 공간을 초기화하는 것이기 때문에 실제 해당 파일이 삭제되지는 않는다.

#### ✔변경된 내용이 working directory에 있을 경우  (Untracked file일 경우엔 적용x)

restore 명령어로 staging area에 있던 second_content.txt 파일이 초기화 되었다.   
__git restore <파일이름>__

```bash
λ git restore second_content.txt

C:\Users\dkfkf\Desktop\git\git-undo-직접 (master)
λ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sixth.txt

nothing added to commit but untracked files present (use "git add" to track)

```
- git restore . 는 전체를 초기화 해주는 명령어이다
<br>

#### ✔변경된 내용이 staging area에 있는 경우 (add한 경우)    

변경된 파일 2개가 staging area에 있는 것을 볼 수 있다. eight.txt파일을 working directory로 옮기기 위해 restore명령어를 사용한다 
__git restore --staged <파일이름>__ 

```bash
λ git status
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   eight.txt
        modified:   third_content.txt
        
λ git restore --staged eight.txt 

λ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   third_content.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        eight.txt
```
<br>
- git restore --staged 는 전체 add된 파일들을 working directory로 옮겨준다   
- git reset HEAD : 똑같은 역할을 한다   

#### ✔commit된 파일 초기화  
어떤 commit으로부터 파일을 초기화 할 건지 설정 할 수 있다

__git restore --source= <해쉬코드>__ 해당 해쉬코드를 가지고 있는 commit 파일을 초기화한다   
__git restore --source =HEAD~2__ HEAD에서 두번째 떨어진 곳으로 commit을 돌려준다

```bash
λ git status
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   eight.txt
        modified:   third_content.txt
        
λ git restore --staged eight.txt 

λ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   third_content.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        eight.txt
```