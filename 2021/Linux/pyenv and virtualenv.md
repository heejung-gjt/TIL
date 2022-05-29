### 우분투에 가상환경 설치하기
<br>

[👉 우분투 가상환경 설치시 발생했던 오류정리](https://github.com/heejung-gjt/TIL/blob/master/linux/%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BDerror.md)
<br>

#### ✔ Ubuntu 20.04.1 LTS에서 pyenv와 virtualenv설치

* * *

### 1.pyenv설치   
pyenv는 한 머신에 여러 버전의 파이썬을 설치할 수 있다. 필요에 따라 버전을 바꾸어가며 사용할 수 있게 해준다     

✔  pyenv를 설치하고 싶을 위치에 깃허브 저장소를 카피해준다.(보통 ~/.pyenv롤 설치를 해주는데 가장 최상단 root에 pyenv를 설치해준다)   

```bash
 $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
<br>

✔  .bashrc에서 pyenv 환경설정을 해준다
(__이때 우분투, zsh등 종류에 따라 다르니 찾아보자 !__)
```bash
vi ./bashrc

---bashrc---
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
------------

```
<br>

✔  그 뒤에 수정한 bashrc를 적용하기 위해서 
```source ~/.bashrc``` 명령어로 적용해주자  
```bash
$ source ~/.bashrc
```  
<br>

✔  그후 ```pyenv``` 명령어를 쳐서 설치가 잘되었는지 확인하자 (__잘 설치되지 않았다면 종료후 다시 켜서 해보자 !__)   
```bash
$ pyenv

----아래처럼 나오면 성공 !----
pyenv 1.2.22-26-g511756f0
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   activate    Activate virtual environment
   commands    List all available pyenv commands
   deactivate   Deactivate virtual environment
.
.
.
.

```
<br>

✔  원하는 python 버전을 list로 찾아서 설치해준다   

```bash
$ pyenv install --list # 원하는 버전 찾기
$ pyenv install 3.9.1  # python 설치
$ pyenv versions #현재 설치된 버전 보기
``` 
* * *

### 2. Virtualenv 설치
✔  python 설치가 끝났으면 virtualenv를 설치하여 가상환경을 만들어준다     
 virtualenv는 파이썬 환경을 격리해주는 툴이다. 즉, 파이썬 구동환경을 관리해주는데 가상환경을 이용하면 파이썬 버전을 세분화해서 여러 개별 환경으로 구분해 관리해준다      

✔  pyenv 설치할때처럼 clone 해준다
  ```bash
  git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

  ```
  <br>

✔  bashrc에서 환경설정을 추가해준다   
(잘 되지 않는다면 추가한 위치가 문제일 수도 있으니 이를 찾아보자 !)

```bash
vi ./bashrc

---bashrc---
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
------------
```
<br>

✔  source ~/.bashrc로 변경내용을 적용해준다
```bash
source ~/.bashrc
```
<br>

✔  그 후 가상환경을 생성해준다    
(__이때 오류가 발생한다면 종료했다가 다시 들어가보자!__)
```bash
pyenv virtualenv 3.9.1 <원하는 가상환경명>
```
<br>

✔  pyenv versions로 생성한 가상환경이 잘 생성되었는지 확인하자   

```bash
* system (set by /home/heejung/.pyenv/version)
  3.9.1
  3.9.1/envs/test
  test  # 생성한 가상환경
```

✔  접속이 잘 된다면 성공 !
```bash
pyenv activate test
```
<br>

✔  종료는 ```pyenv deactivate```