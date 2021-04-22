'''
배열로 구현한 환형 큐
'''
class CircularQueue:
	def __init__(self, n):
		self.maxCount = n # 큐의 크기
		self.data = [None] * n # 실제 데이터를 저장하려는 공간
		self.count = 0 # 현재 큐에 들어가있는 데이터 개수
		self.front = -1 
		self.rear = -1
	
	def size(self):
		return self.count
	
	def isEmpty(self):
		return self.count == 0
	
	def isFull(self):
		return self.count == self.maxCount
	
	def enqueue(self,x):
		if self.isFull():
			raise IndexError('큐 가득참')
		self.rear = len(self.data)
		self.data[self.rear] = x
		self.count += 1
	
	def dequeue(self):
		if self.isEmpty():
			raise IndexError('큐 비어있음')
		self.front = self.data[self.front+1]
		x = self.data[self.front]
		self.count -= 1
		return x
	
	def peek(self):
		if self.isEmpty():
			raise IndexError('큐 비어있음')
		return None