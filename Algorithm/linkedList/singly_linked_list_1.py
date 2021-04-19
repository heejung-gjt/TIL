'''
단방향 연결 리스트 (Singly Linked List)
value와 next property를 지닌 Node 클래스를 구현한다.
Node를 이용하여 Singly Linked List를 구현한다.
다음과 같은 리스트 ADT의 연산자를 구현해야 한다.
비어있는 리스트를 생성하는 생성자
리스트가 비어있는지 확인하는 연산자
리스트의 앞에 개체를 삽입(prepending)하는 연산자
리스트의 뒤에 개체를 삽입(appending)하는 연산자
리스트의 첫 머리(head)를 결정하는 연산자
주어진 인덱스에 해당하는 요소에 접근하는 연산자 access
주어진 인덱스에 새로운 요소를 삽입하는 연산자  insert
주어진 인덱스에 해당하는 요소를 제거하는 연산자  remove
'''
# 구조
class Node:
  def __init__(self, value, n = None):
    self.value = value
    self.next = n

class SinglyLinkedList:
  def __init__(self):
    self.head = None
  
  def is_empty(self):
    if self.head is None:
      return print('리스트 비어있음')
  
  def prepend(self,value):
    if self.head is None:
      self.head = Node(value)
    else:
      self.head = Node(value, self.head)

  def append(self,value):
    if self.head is None:
      self.head = Node(value)
    else:
      print(f'\n{value}값 데이터 뒤에 추가\n')
      link = self.head
      while link.next:
        link = link.next
      link.next = Node(value)

  def head(self,index):
    link = self.head
    for _ in range(index):
      if link is None:
        return False
      link = link.next
    self.head = link
    return True

  def access(self,value):
    if self.head is None:
      print('데이터 없음')
    else:
      index = 0
      link = self.head
      while link:
        if link.value == value:
          # print(f'{value} 데이터 {index}번째 존재함')
          return index
        else:
          index += 1
          link = link.next

  def insert(self, index, value):
    if self.head is None:
      return False
    link = self.head
    prev = None
    for _ in range(index):
      if link is None:
        return False
      prev = link
      link = link.next

    prev.next = Node(value, link)
    return True

  def remove(self,index):
    if index == 0:
      if self.head:
        self.head = self.head.next
        return True
      else:
        return False
    link = self.head
    prev = None
    for _ in range(index):
      if link is None:
        return False
      prev = link
      link = link.next

    if link is None:
      return False
    
    prev.next = link.next
    return True

  def print(self):
    if self.head is None:
      print('저장된 데이터 없음')
      return
    else:
      link = self.head
      while link:
        print(link.value,end=' ')
        link = link.next
      print()


my_list = SinglyLinkedList()
my_list.print()

for i in range(10):
    my_list.append(i + 1)

my_list.print()

for i in range(10):
    my_list.prepend(i + 1)

my_list.print()

value = my_list.access(3)
print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.head(10)
my_list.print()