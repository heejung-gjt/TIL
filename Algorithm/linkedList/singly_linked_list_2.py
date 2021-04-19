
class Node:
	def __init__(self, data, n=None):
		self.data = data  
		self.next = n  

class SingleLinkedList:
	def __init__(self):
		self.head = None
	
	def insert(self, value): 
		if self.head is None: 
			self.head = Node(value)
		else: 
			self.head = Node(value,self.head) 
	
	def printNode(self):
		if self.head is None:
			print('저장된 데이터 없음')
			return
		else:
			link = self.head

			while link: 
				print(link.data)
				link = link.next
			print()

	def deleteNode(self):
		if self.head is None:
			print('삭제할 데이터 없음')
			return
		else:
			self.head = self.head.next

	def searchNode(self, data):
		if self.head is None:
			print('저장된 데이터 없음')
			return
		else:
			link = self.head # 처음엔 head를 지정해준다
			index = 0 # 찾으려는 노드의 인덱스
			while link:
				if link.data == data:
					return index
				else:
					link = link.next
					index += 1