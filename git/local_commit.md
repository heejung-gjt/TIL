## commit 했지만 contribution 그래프가 채워지지 않는 이유

### ⚡삽질 기록    

로컬로 commit을 한 모든 파일들이 contribution 그래프에 기록이 되지 않는걸 오늘 알았다..😂   
구글링을 해보니 .... 그래프가 채워지는 조건이 또 따로 있다고 한다   


### 📌정리

그래프가 채워지는 조건에 있는 이메일 !    
git을 pc에 설치하고 계정을 등록하게 되는데 이때 작성한 email과 github 계정에 있는 email이 같아야 한다   
그것도 모르고 열심히 커밋한 아이들이 전부 남지 않았다.. 그걸 이제야 깨닫다니ㅜㅜ    

- git에 등록된 email 보기       

```bash
git config user.email
```
<br>

- github에 등록된 email 보기   
 맨 오른쪽 위 상단 자신의 프로필 click -> settings 선택 -> Emails 선택    

<br>

- 등록된 email 변경하기   

```bash
git config --global user.email <동일한 email>
```

보통은 다들 email 등록 실수인듯 하다.. commit이 되지 않는 다른 이유들도 있으니 한번씩 찾아보길 !

