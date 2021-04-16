### 팀원과 git fork로 repo 공유하기   

1. 팀장이 repo를 판다. 
```bash
git clone <url...fork_space>
```

2. 로컬과 원격을 연결하기 위한 README.md같은 파일을 생성해준다
(main branch를 생성하고 싶다면 이부분은 좀 더 알아보자)    
```bash
fork_space$ touch README.md
fork_space$ git add README.md
fork_space$ git commit -m "docs: upload README.md"
fork_space$ git push origin master  
```

3. 팀원들이 팀장의 repo를 fork해준후 clone을 통해 원격에 폴더를 생성해준다
```bash
git clone <url...fork_space>
```

4. 생성된 repo에서 팀장의 브랜치에 접근하기 위해서 팀장 repo공간을 remote해준다
```bash
fork_space$ git remote add heejung(네임) master(팀장 브랜치 따라간다)
```

5. 자신의 로컬에 업로드 하고 싶으면
```bash
fork_space$ git push origin master
```

6. 팀장의 로컬에 업로드 하고 싶으면 
```bash
fork_space$ git push origin heejung master
```

7. 이때  push가 끝나면 자신의 fork한 repo에서 pull request를 해준다. create request눌러주기. 이때 팀장의 repo에 있는 내용이 수정되기 때문에 __다른 팀원들은 git pull heejung master 을 통해 변경된 내용을 자신의 원격 폴더에 가져와야 한다__       

8. 팀장이 merge하고 자신의 폴더에서 pull을 해주면 변경된 내용으로 업로드 된다
