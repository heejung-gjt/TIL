'''
# 구현 조건
- class와 array.array를 이용하여 Array List를 구현한다.
  - 데이터의 타입은 l(signed long)으로 한다.
  - array.array 객체의 메소드는 아래 메소드만을 사용한다.
    - arr[ind](인덱스로 접근), arr[ind:](슬라이싱)
- array.array의 용량(capacity)은 고정되어 있다고 가정한다.
  - 배열의 크기가 부족할 때 마다 2배 길이의 array.array를 새로 생성한다.
- 다음과 같은 리스트 ADT의 연산자를 구현해야 한다.
  - 비어있는 리스트를 생성하는 생성자
  - 리스트가 비어있는지 확인하는 연산자
  - 리스트의 앞에 개체를 삽입(prepending)하는 연산자
  - 리스트의 뒤에 개체를 삽입(appending)하는 연산자
  - 리스트의 첫 머리(head)를 결정하는 연산자
  - 주어진 인덱스에 해당하는 요소에 접근하는 연산자
  - 주어진 인덱스에 새로운 요소를 삽입하는 연산자
  - 주어진 인덱스에 해당하는 요소를 제거하는 연산자
'''
import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity # 용량
        self.length = 0 # 길이
        self.array = array.array('l', [0]*capacity) #배열 용량 추가
    
    def is_empty(self):
        return self.capacity == 0 # 배열 비워있는지 확인

    def prepend(self, value): # 리스트 앞에 요소 삽입
        if self.capacity == self.length: # 용량이 꽉차있는지 length와 비교 확인
            self.capacity *= 2 # 만약 꽉차있으면 용량 2배 늘리기
            new_array = array.array('l', [0]*self.capacity) #용량이 늘어난 만큼 배열 길이 증가시키기
            for i in range(self.length): # 배열길이만큼 for문 돌려 새로운 array[1]부터 array[0]~부터 삽입하기
                new_array[i + 1] = self.array[i]
            self.array = new_array # 새로운 array를 기존 Array에 넣어 업데이트
        else:
            for i in range(self.length - 1, -1, -1): # 만약 용량이 꽉차있지 않으면 1증가한 인덱스값부터 0전의 인덱스값까지 역으로 값 넣어주기
                self.array[i + 1] = self.array[i]

        self.array[0] = value # 비워있었던 Array[0]에 새로운 요소값 삽입
        self.length += 1 # 길이 늘어났기때문에 +=1해준다

    def append(self, value): 
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i] # 새로운 배열에 순차적으로 값 넣어주기
            self.array = new_array # 새로운 배열 기존의 array에 넣어 업데이트
        
        self.array[self.length] = value # array 길이를 인덱스로 즉 가장 마지막에 값 넣어주기
        self.length += 1 # 길이 늘어났기때문에 +=1해준다

    def set_head(self, index): # 리스트의 첫머리 결정 
        self.array = self.array[index:] # 리스트의 첫머리를 index로 지정하기 위해 array를 array[index:]부터 끝까지로 업데이트
        self.capacity = self.capacity - index #용량도 idex이전의 값을 뺀만큼 감소하기 때문에 빼준다
        self.length = self.length - index # 마찬가지로 길이도 감소하기 때문에 빼준다

    def access(self, index): #주어진 인덱스에 접근
        return self.array[index]
         
    #*****insert 이해 x*****
    def insert(self, index, value): # index에 새로운 값을 넣는다 
        if self.capacity == self.length: 
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(index - 1): # 0부터 index-1까지 순차적으로 새로운 배열에 넣는다
                new_array[i] = self.array[i]
            for i in range(index, self.length): 
                new_array[i + 1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.length += 1

    def remove(self, index): # index에 존재하는 요소값 삭제
        for i in range(index, self.length - 1):  # 삭제하기 위해서 index부터 length-1까지 순차적으로 index+1 부터 끝까지 새로운 배열에 업데이트 해준다
            self.array[i] = self.array[i + 1]    # 그럼 자연스럽게 [index]의 값은 삭제되어진다
        self.length -= 1 # 길이 감소하므로 -1해준다

    def print(self):
        print(self.array.tolist()[:self.length])
        
my_list = ArrayList(8)
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

my_list.set_head(10)
my_list.print()