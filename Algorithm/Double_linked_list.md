## 이중연결리스트(Doubly Linked List)
이중연결리스트는 모든 노드가 이전노드와 다음 노드에 대한 정보를 모두 저장하고 있는 리스트이다

![이중연결](https://user-images.githubusercontent.com/64240637/115163380-c5b62100-a0e3-11eb-82f3-a320464ad608.png)

<br>

#### 이중 연결리스트 구조   

```[1] 구조```   
단일 연결 리스트는 단방향으로 밖에 삽입/삭제/조회를 못한다   
이중 연결 리스트는 노드에 변수 next로 다음노드를 변수 prev로 이전노드를 지정하여 이동할 수 있도록 한다. 또한 변수 head뿐만 아니라 변수 tail도 만들어 리스트의 앞과 뒤로 접근이 가능하도록 할 수 있다 

##### 코드 구현
```python
class Node:
	def __init__(self, data, n=None, p=None):
		self.data = data  # 저장된 데이터
		self.next = n  # 다음 노드를 가리키는 변수
		self.prev = p # 이전 노드를 가리키는 변수   

class DoublyLinkedList:
    def __init__(self):
        self.head = None #첫 생성시 내부에는 노드가 없으므로
        self.tail = None

double_link = DoublyLinkedList()
```

```[2] 삽입```    
이중 연결리스트의 삽입 방법은 2가지이다. head로 넣는 방법과 tail을 통해 넣는 방법이 있다. 상황에 따라 노드의 next와 prev 값을 다음노드와 이전노드로 지정해주면 된다      

가장먼저 ```저장된 노드가 없는 경우``` head와 tail 값은 None이다. 따라서 head에 넣든 tail에 넣든 결과는 같게 된다    

```저장된 노드가 있는 경우``` 기존에 있는 노드는 밀려나고 새로운 노드가 들어온다. 즉 새로운 노드의 next에 현재 head값을 저장하고 head에는 새로운 노드를 저장시킨다    
```head기준```` 
- 현재 head가 가리키는 기존 노드의 prev를 새로 생성하는 노드로 지정한다   
- 새로 생성한 노드의 next를 기존 노드로 지정한다    
- head를 새로 생성한 노드로 변경한다    

```tail기준```` 
- 현재 tail이 가리키는 기존 노드의 next를 새로 생성하는 노드로 지정한다   
- 새로 생성한 노드의 prev를 기존 노드로 지정한다    
- tail를 새로 생성한 노드로 변경한다

##### 코드 구현
```python

def insertBefore(self,data):
  if self.head is None:
    self.head = Node(data)
    self.tail = self.head
  else:
    self.head.prev = self.Node(data, n = self.head)
    self.head = self.head.prev

def insertAfter(self,data):
  if self.tail is None:
    self.tail = Node(data)
    self.head = self.tail
  else:
    self.tail.next = Node(data, p = self.tail )
    self.tail = self.tail.next
```

```[3] 출력```
단일 연결리스트와 동일하게 출력하면 된다. 
```저장된 노드가 없을때``` 없다라는 출력을 해주고 ```저장된 노드가 있을때``` 단일 연결리스트와 동일하게 출력해준다
##### 코드 구현
```python

def printNode(self):
  if self.head is None or self.tail is None:
    print('데이터 없음')
  else:
    link = self.head
    prev = self.tail
    while prev:
      print(link.data)
      print(prev.data)
      link = link.next
      prev = prev.prev

def printNodeBefore(self):
  if self.head is None:
    print('저장된 데이터 없음')
    return
  else:
    print('[리스트 구조]',end='\t')
    link = self.head

    while link:
      print(link.data,end=' ')
      link = link.next
    print()

def printNodeAfter(self):
  if self.tail is None:
    print('저장된 데이터 없음')
    return
  else:
    print('[리스트 구조]',end='\t')
    prev = self.tail

    while prev:
      print(prev.data,end=' ')
      prev = prev.prev
    print()
```

```[4] 삭제```
삭제 또한 head와 tail을 통해 삭제하는 방법이 있다

```저장된 노드가 없을 경우```는 제외시켜준다. ```저장된 노드가 있을 경우``` head를 통해 노드를 삭제할 경우 곧 head가 될 노드의 prev는 None으로 변경해주어야 한다    
```head기준```   
- 현재 head가 가리키는 노드의 next를 새로운 head로 지정    
- 새로운 head의 prev를 None으로 변경    
##### 코드 구현
```python

def deleteBefore(self):
  if self.head is None:
    print('삭제할 데이터 없음')
    return
  else:
    self.head = self.head.next
    self.head.prev = None
  
def deleteAfter(self):
  if self.tail is None:
    print('삭제할 데이터 없음')
    return
  else:
    self.tail = self.tail.prev
    self.tail.next = None
```

```[5] 탐색```
단일 연결 리스트와 동일하다. 단순히 head에서부터 탐색할지 tail에서부터 탐색할지가 나뉘는것 뿐이다. 이때 tail로 탐색해서 나온 인덱스는 초기값을 -1로 주고 진행할때마다 1씩 감소시켜 head로 구한 인덱스와 구분시켜 출력한다

```python

def searchBefore(self,data):
  if self.head is None:
    print('데이터 없음')
    return
  else:
    link = self.head
    index = 0
    while link:
      if link.data == data:
        return index
      else:
        link = link.next
        index += 1

def searchAfter(self,data):
  if self.tail is None:
    print('데이터 없음')
    return
  else:
    prev = self.tail
    index = 0
    while prev:
      if prev.data == data:
        return index
      else:
        prev = prev.prev
        index -= 1
```


<br>






