class Node: 
  def __init__(self, data, next):
    self.data = data
    self.next = next

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self): # 리스트가 비어있는지 확인하는 연산자
    return self.head is None
    # if self.head ==None:
    #   return self.head
      
  def prepend(self, data): # 리스트의 앞에 개체를 삽입하는 연산자
    if self.head is None:
      self.head = Node(data, None)
    else:
      self.head = Node(data, self.head)

  def append(self, data): # 리스트의 뒤에 개체를 삽입하는 연산자
    if self.head is None:
      self.head = Node(data, self.head)
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = None(data, None)


  def set_head(self, index): # 리스트의 첫 머리를 결정하는 연산자
    curr = self.head
    for _ in range(index):
      if curr is None:
        return False
      curr = curr.next
    self.head = curr
    return True

  def access(self, index): # 주어진 인덱스에 해당하는 요소에 접근하는 연산자
    pass 

  def insert(self, index, data): # 주어진 인덱스에 새로운 요소를 삽입하는 연산자 
    pass

  def remove(self, index): # 주어진 인덱스에 새로운 요소를 
    pass

  def print(self):
    pass

# 특정 원소 참조(k번째)
# 리스트 순회
# 길이 얻어내기
# 원소삽입
# 원소삭제
# 두 리스트 합치기 


# class Node:
#   def  __init__(self,item):
#     self.data = item
#     self.next = None

# class LinkedList:
#   def __init__(self): # 비어있는 연결리스트 초기값 설정
#     self.nodeCount = 0 
#     self.head = None
#     self.tail = None

# # 특정 원소 참조하는 메서드 getAt
#   def getAt(self,pos): # 인자로 주어진 pos를 가지고 pos번째 노드를 뽑아서 뽑은 노드자체를 리턴해주는 메서드
#     if pos <= 0 or pos > self.nodeCount: # pos번째는 음수나 0이 될 수 없고 node의 개수보다 클 수 없다. 그런경우 None리턴
#       return None

#     i = 1
#     curr = self.head  # 연결리스트의 첫번째 노드를 가리킨다 
#     while i < pos: #i가 pos보다 작을동안 i를 1씩 증가시켜 curr.next를 curr에 대입한다
#       # 즉 pos-1번만큼 전진하면 그때 curr가 가리키고 있는 것이 내가 리턴하려는 pos번째 노드를 가리키게 된다
#       curr = curr.next 
#       i += 1

#     return curr

# # 리스트 순회 메서드 traverse
#   def traverse(self):
#     curr = self.head
#     answer = []
#     while curr != None:
#       answer.append(curr.data)
#       curr = curr.next
#       return answer

