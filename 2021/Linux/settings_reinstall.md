```text
dpkg: unrecoverable fatal error, aborting:
 unknown system user 'redis' in statoverride file; the system user got removed
before the override, which is most probably a packaging bug, to recover you
can remove the override manually with dpkg-statoverride
E: Sub-process /usr/bin/dpkg returned an error code (2)
```

<br>

아래 파일 들어가 에러나는 패키지 삭제 (redis)
```bash
$ sudo vi /var/lib/dpkg/statoverride
```

<br>

아래와 같은 에러 주의, vim안에서 한줄 삭제 후 커서는 존재하는 문장 위로 올려 저장
```text
dpkg: unrecoverable fatal error, aborting:
 statoverride file contains empty line
E: Sub-process /usr/bin/dpkg returned an error code (2)
```
