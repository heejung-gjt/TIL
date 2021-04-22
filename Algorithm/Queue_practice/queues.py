'''
리스트 이용하여 구현
'''

# class ArrayQueue: # 빈 큐 초기화
#   def __init__(self):
#     self.data = []

#   def size(self):
#     return len(self.data)

#   def isEmpty(self):
#     return self.size() == 0

#   def enqueue(self, data):
#     self.data.append(data)

#   def dequeue(self):
#     return self.data.pop(0)

#   def peek(self):
#     return self.data[0]

'''
배열 리스트로 구현
'''




import array


class LinearQueue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.front = 0
		self.rear = 0
		self.array = array.array('l', [0]*capacity)

	def put(self, value):
		if self.capacity == self.rear:
			return False
		else:
			self.array[self.rear] = value
			self.rear += 1 

	def get(self):
		if self.front == self.rear:
			return None
		value = self.array[self.front]
		self.front += 1
		return value

	def peek(self):
		if self.front == self.rear:
			return None
		value = self.array[self.front]
		return value

	def print(self):
		for i in range(self.front, self.rear - 1):
			print(self.array[i])
		print(self.array[self.rear - 1])
