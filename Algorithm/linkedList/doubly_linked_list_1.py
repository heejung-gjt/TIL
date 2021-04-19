'''
value, next, 그리고 prev property를 지닌 Node 클래스를 구현한다.
Node를 이용하여 Doubly Linked List를 구현한다.
다음과 같은 리스트 ADT의 연산자를 구현해야 한다.
비어있는 리스트를 생성하는 생성자
리스트가 비어있는지 확인하는 연산자
리스트의 앞에 개체를 삽입(prepending)하는 연산자
리스트의 뒤에 개체를 삽입(appending)하는 연산자
리스트의 첫 머리(head)를 결정하는 연산자
주어진 인덱스에 해당하는 요소에 접근하는 연산자
주어진 인덱스에 새로운 요소를 삽입하는 연산자
주어진 인덱스에 해당하는 요소를 제거하는 연산자
'''

class Node:
  def __init__(self, value, next, prev):
    self.value = value
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    if self.head is None:
      return True
    else:
      return False

  def prepend(self,data):
    if self.head is None:
      self.head = Node(data,None,None)
      self.tail = self.head
    else:
      self.head.prev = Node(data,self.head,None)
      self.head = self.head.prev

  def append(self,data):
    if self.tail is None:
      self.tail = Node(data,None,None)
      self.head = self.tail
    else:
      self.tail.next = Node(data,None, self.tail)
      self.tail = self.tail.next

  def head(self,index):
    if self.head is None:
      return False
    
    link = self.head
    for _ in range(index):
      if link.next is None:
        return False
      link = link.next
    self.head = link
    self.head.prev = None
    return True

  def access(self, index):
    if self.head is None:
      return None

    link = self.head
    for _ in range(index):
      if link.next is None:
        return False
      link = link.next
    
    if link is None:
      return None
    else:
      return link.value
      
  def insert(self, index, value):
      if self.head is None and index > 0:
          return False

      if index == 0:
          self.prepend(value)
          return True
      
      curr = self.head
      for _ in range(index):
          if curr.next is None:
              return False
          curr = curr.next
      
      if curr is None:
          node = Node(value, None, self.tail)
          self.tail.next = node
          self.tail = node
      else:
          node = Node(value, curr, curr.prev)
          curr.prev.next = node
      return True

  def remove(self, index):
      if self.head is None:
          return False

      if index == 0:
          self.head = self.head.next
          if self.head is not None:
              self.head.prev = None
          return True
      
      curr = self.head
      for _ in range(index):
          if curr.next is None:
              return False
          curr = curr.next
      
      if curr is None:
          return False
      else:
          curr.prev.next = curr.next
          if curr.next is not None:
              curr.next.prev = curr.prev
          else:
              self.tail = curr.prev
          return True

  def print(self):
      if self.head is None:
          print('[]')
      else:
          curr = self.head
          print('[', end='')
          while curr.next is not None:
              print(curr.value, end=', ')
              curr = curr.next
          print(str(curr.value) + ']')


my_list = DoublyLinkedList()
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

my_list.head(10) #error나는 이유는 ?
my_list.print()