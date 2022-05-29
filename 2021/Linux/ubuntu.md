## window 재설치 또는 업데이트시 지워진 우분투 grud 복구하기

1. UEFI 지원하는 우분투 설치용 USB메모리를 준비해준다. (Ubuntu 설치용 usb 메모리를 만들어서 가지고 있는게 좋은듯 하다...[ubuntu 설치용 usb메모리 만들기](https://webnautes.tistory.com/1146))        

<br>

> GPT/MBR의 차이점은 ?      
> BIOS/UEFI 차이점은 ?
> 우분투 파티션 형식 확인해보기     

<br>

2. usb를 낀 채로 컴퓨터를 재부팅해준다. 재부팅할때 f2 연타로 눌러 바이오스 부팅순서로 들어가 준다. 여기서 ubuntu 설치용 usb로 부팅을 하기 위해 ```Boot Device Priority```를 변경해준다. 
```text
shift ^ 을 눌러 usb를 가장 위로 올려서 저장한다   
```

<br>

3. 컴퓨터 재부팅 되면서 우분투 Grud가 뜨는데 이때 첫번째 ubuntu를 눌러준다. 그 후 try ubuntu를 선택해 터미널을 켜준다. 터미널창에서 아래와 같은 명령어를 입력한다 
```bash
$ sudo add-apt-repository ppa:yannubuntu/boot-repair

$ sudo apt-get update

$ sudo apt-get install boot-repair

$ sudo boot-repair

```

__이때 boot-repair 설치를 위해 인터넷을 연결해준다 !__     

<br>

4. boot-repair가 실행되면 Recommended Repair를 선택한 후 yes를 선택해 넘어가면 프로그램이 자동으로 Grud를 복구해준다. 그 후 내 계정으로 우분투에 로그인 할 수 있게 된다!! 

