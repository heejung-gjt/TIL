## 리스트에서 람다함수로 정렬하기 

#### ⚡삽질 기록    
알고리즘에서 정렬 문제를 풀때 2개의 값을 n번 받은뒤 key를 기준으로 정렬하거나 value를 기준으로 정렬하는 문제들이 꽤 많았다. 분명 sort나 sorted를 이용해서 쓰는 문제인데 어떤식으로 적용을 해야 할지 막막했다... 리스트 안에 있는 각 리스트들의 인덱스를 어떻게 구현하지..? 
정답은 꽤나 간단하다...ㅎㅎㅎ 알고나면 파이썬 정말 좋은 것 같다.. :-)

<br>

#### 📌 for과 lambda함수로 정렬문제 풀기
해당 문제는 ```백준의 11651 - 좌표 정렬하기2```의 문제이다.    
```text
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
```

n개의 입력값을 받고 n번 x,y좌표를 입력받아 y좌표가 증가하는 순 즉, 오름차순으로 정렬을 하고 만약 y좌표의 값이 똑같다면 x좌표를 기준으로 오름차순을 하는 문제이다.    

각각 for문과 lambda함수로 풀어보겠다    

```for문으로```

```python
n = int(input())
arr = []

for i in range(n):
    num1,num2 = map(int,input().split())
    arr.append([num2,num1])
sort_arr = sorted(arr)
for i in range(n):
    print(sort_arr[i][1],sort_arr[i][0])
```
<br>

```lambda함수로```   
n_arr의 배열에 리스트로 담은 x,y좌표를 담은 후 정렬을 시키는데 이때 lambda함수를 이용하여 
정렬시켜준다. x[1]즉 y좌표순으로 오름차순 정렬을 하다가 y좌표의 값이 같다면 x[0] 즉 x좌표를 
기준으로 오름차순 정렬을 한다. 람다함수가 알아서 적용시켜준다 . 단, 시간초과의 문제가 있는데 마지막 for문에서 ```for i in n_arr: print(i[0],i[1])```로 구현하면 시간초과가 난다,,, 왜인지는 좀 더 알아봐야겠다

```python
n = int(input())
n_arr = []
for i in range(n):
    x,y = map(int,input().split())
    n_arr.append([x,y])
n_arr.sort(key=lambda x:(x[1],x[0]))
for [i,j] in n_arr:
    print(i,j)
```

<br>

__람다함수 이용하면 간단하게 정렬가능__
```python
lists1 = [[1,2,3],[3,2,1],[2,1,3]]
lists2 = sorted(lists1, key=lambda num:(num[2],num[0]))

print(lists2)

# [[3, 2, 1], [1, 2, 3], [2, 1, 3]]
```
lists1의 인덱스값 2를 기준으로 정렬을 하다가 2의값이 같다면 인덱스 0을 기준으로 정렬이 되는 것을 볼 수 있다