class Node:
	def __init__(self, data, n=None, p=None):
		self.data = data  # 저장된 데이터
		self.next = n  # 다음 노드를 가리키는 변수
		self.prev = p # 이전 노드를 가리키는 변수   

class DoublyLinkedList:
	def __init__(self):
		self.head = None #첫 생성시 내부에는 노드가 없으므로
		self.tail = None

	def insertBefore(self,data):
		if self.head is None:
			self.head = Node(data)
			self.tail = self.head
		else:
			self.head.prev = Node(data, n = self.head)
			self.head = self.head.prev
	
	def insertAfter(self,data):
		if self.tail is None:
			self.tail = Node(data)
			self.head = self.tail
		else:
			self.tail.next = Node(data, p = self.tail)
			self.tail = self.tail.next

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

double_link = DoublyLinkedList()
##테스트
double_link.insertBefore('1st')  # head삽입 테스트
double_link.insertBefore('2nd')  # head삽입 테스트
double_link.insertBefore('3rd')  # head삽입 테스트
double_link.insertAfter('B1st') # tail삽입 테스트
double_link.insertAfter('B3rd') # tail삽입 테스트
double_link.insertAfter('B2nd') # tail삽입 테스트
double_link.printNode()
print()
print()
print('head기준 데이터')
double_link.printNodeBefore()
print('tail기준 데이터')
double_link.printNodeAfter()
print('head기준 삭제 데이터')
double_link.deleteBefore()  # head로 삭제
double_link.printNodeBefore()
print('tail기준 삭제 데이터')
double_link.deleteAfter()  # tail로 삭제
double_link.printNodeBefore()
print('head기준 데이터 탐색')
result = double_link.searchBefore('B1st')
print(result)
print('tail기준 데이터 탐색')
result = double_link.searchAfter('2nd')
print(result)