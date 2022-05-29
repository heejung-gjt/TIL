로컬에 존재하는 .env파일 서버로 복사해 붙여넣기 

```bash
$ scp -i ~/Downloads/neonews.pem ~/Desktop/github-upload/Neo-News/config/.env ubuntu@3.38.80.84:~/
```

<br>

.env파일 /srv ~ 폴더로 옮기기

```bash
$ mv .env /srv/Neo-News/config
```