### git flow 이용하기 
<br>

#### ✔ installation

ubuntu 설치방법 (사용자 환경마다 설치 방법 다름)
<br>

```bash
sudo apt-get install git-flow
```
<br>

#### ✔ git flow init 은 새로운 기능의 개발을 develop 브랜치에서 시작하기 위한 명령어이다. 해당 명령어를 작성하면 develop라는 branch가 생성되며 해당 branch로 이동하게 된다.   
(몇몇 질문은 기본값으로 설정하자. enter를 쳐서 넘어가면 된다)

```bash
$ git flow init

Which branch should be used for bringing forth production releases?
   - main
Branch name for production releases: [main] 
Branch name for "next release" development: [develop] 

How to name your supporting branch prefixes?
Feature branches? [feature/] 
Bugfix branches? [bugfix/] 
.
.
.

$ git branch

* develop
  main
```
<br>

#### ✔ 새 기능의 개발을 시작하기 위해서 develop에 기반한 새 기능 브랜치를 생성하고 해당 브랜치로 전환한다   
```bash
$ git flow feature start <브랜치명>

$ git branch

develop
* feature/add-hint # 브랜치 생성됨
main
```
<br>

#### ✔ 해당 브랜치에서 numguess.py의 기능등을 수정한 후 add, commit을 차례대로 해준다
```bash
$ vi numguess.py
$ git add numguess.py
$ git commit
```
<br>

#### ✔ numguess.py의 기능 개발이 완료되었다면   
1. feature/add-hint 브랜치를  develop 브랜치에 병합한다    
2. 기능 브랜치를 feature/add-hint 브랜치를 삭제한다   
3. develop 브랜치로 전환한다     

아래의 명령어가 1~3번의 모든것을 수행한다
```bash
$ git flow feature finish add-hint

Switched to branch 'develop'
Updating cb25953..9eede5f
Fast-forward
 numguess.py | 9 ++++++---
 1 file changed, 6 insertions(+), 3 deletions(-)
Deleted branch feature/add-hint (was 9eede5f).

Summary of actions:
- The feature branch 'feature/add-hint' was merged into 'develop'
- Feature branch 'feature/add-hint' has been locally deleted
- You are now on branch 'develop'

$ git branch

* develop
  main
``` 
<br>

#### ✔ 수정한 numguess.py 를 출시하기 위해 릴리스를 시작한다.   
develop 브랜치로부터 release브랜치를 생성한다 
``` bash
$ git flow release start v.1.0.0.210130001

Switched to a new branch 'release/v.1.0.0.210130001'

Summary of actions:
- A new branch 'release/v.1.0.0.210130001' was created, based on 'develop'
- You are now on branch 'release/v.1.0.0.210130001'

Follow-up actions:
- Bump the version number now!
- Start committing last-minute fixes in preparing your release
- When done, run:
     git flow release finish 'v.1.0.0.210130001'
```
<br>

#### ✔ 릴리스를 완료해주면 된다. 이때 vi창이 3번 뜨게 된다.   
1. release브랜치를 main브랜치에 병합을 한다는 vi창  (저장)
2. 릴리스를 릴리스 이름으로 태그 (작성 후 저장)
3. 릴리스를 develop 브랜치로 재병합 (저장)

release 브랜치는 자동으로 삭제된다   
```bash
git flow release finish 'v.1.0.0.210130001'

# 첫번째 vi창
Merge branch 'release/v.1.0.0.210130001' into main
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
~              

# 두번째 vi창
#
# Write a message for tag:
#   v.1.0.0.210130001
# Lines starting with '#' will be ignored.
~         

# 세번째 vi창
Merge tag 'v.1.0.0.210130001' into develop

feat: numguess v1.0.0
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.

```
<br>

#### ✔ develop 브랜치와 main을 각각 push를 해서 리모트에 업로드 해준다

```bash
$ git push origin develop
$ git checkout main
$ git push origin main
```
<br>

 (파란선부터 시작) 아래의 이미지처럼 merge된 것을 볼 수 있다     

![merge](https://user-images.githubusercontent.com/77425963/106345983-f792c500-62f6-11eb-82e4-42891484c344.png)
<br>

### ⭐ 정리 

#### 명령어   
- feature : 특정 기능을 개발하거나 수정할때 사용하는 브랜치 (자동으로 생성, 삭제)
- release : 수정한 기능을 배포할때 사용하는 브랜치 (버전네이밍 짓는 방법 알아보기)   
- git flow feature start <branch-name> : 기능 개발 시작 
- git flow release start <branch-name> : 기능 배포 시작   
- git flow feature finish <branch-name> : 기능 개발 완료 (develop 에 feature 브랜치 병합후 feature 브랜치 삭제)   
- git flow release finish <version-name> : 기능 배포 완료 (main에 release 병합후 release 브랜치 삭제)   
- 프로젝트에 적용 : develop 와 main에 push 해준다   

<hotfix는 나중에 알아보자>  
 