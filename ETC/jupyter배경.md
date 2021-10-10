## jupyter notebook 기본 디렉토리 설정하기 + 배경색 변경

### 배경색 변경하기
```bash
$ pip install jupyterthemes
$ jt -l # 배경색 종류
$ jt -t onedork # 배경색 설정
```

이때 발생한 문제는 이전에 venv안에서 설치했던 jupyter notebook이 실행되서 실제 내가 필요한 디렉토리의 파일들을 볼 수 없었다

### 해결방법
jupyter의 설정 파일을 생성하여 기본 디렉토리를 설정해주었다
```python
$ jupyter-notebook --generate-config # 주피터 노트북 설정 파일 생성
$ ipython # 암호화된 비밀번호 생성하기 위해 ipython실행
$ from notebook.auth import security # 암호화된 비밀번호 생성
$ security.passwd()
Enter password:
Verify password:
Out[2]: '암호화된 비밀번호'
in[3]: exit()

$ cd Desktop # 디폴트 디렉토리로 설정할 폴더로 이동해서 디렉토리 주소를 복사한다
$ pwd 
$ cd ~/.jupyter # 주피터 노트북 설정 파일을 생성하면서 만들어진 .jupyter로 들어가서 설정파일을 수정한다
$ vi jupyter_notebook_config.py
```

<br>

```jupyter_notebook_config.py```    
나는 Desktop을 기본 default경로로 두어 어디서 jupyter를 열든 Desktop에서 열리게 설정해놓았다   
```python
# 필수
c = get_config()
c.JupyterApp.config_file_name = 'jupyter_notebook_config.py'

# 접속 허용 ip
c.NotebookApp.allow_origin = '*' # 접속 허용 ip로 *는 전체 허용을 의미한다.

# 서버 ip
# c.NotebookApp.ip = 'xxx.xx.xxx.xxx'

# 주피터 노트북 실행 시, 브라우저로 열지(True), url을 출력할지 정한다(False).
c.NotebookApp.open_browser = True

# 주피터 노트북 비밀번호
c.NotebookApp.password ='암호화된 비밀번호'

# 주피터 노트북 포트 설정
c.NotebookApp.port = 8888

# 주피터 노트북 홈 디렉토리 설정
c.NotebookApp.notebook_dir = '/home/heejung/Desktop/'
```
