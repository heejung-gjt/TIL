# def gen(count):
#   start = 1
#   while start <= count:
#     yield start
#     start += 1

# for i in gen(3):
#   # print(i)

# num = (x for x in [1,2,3,4,5])
# num2 = [x for x in [1,2,3,4,5]]

# print(type(num))
# print(type(num2))

# str1 = 'time is gold'
# str1_list = str1.split(' ')
# # print(next(str1_list)) #TypeError: 'list' object is not an iterator

# str_iter = iter(str1_list)
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))

# foo1 = [i for i in range(1,6)]
# print(type(foo1))

# def func1():
#   for i in range(1,6):
#     return i
# foo1 = func1()
# print(type(foo1))
# print(foo1)
# print(foo1)


# def func2():
#   for i in range(1,6):
#     yield i
# foo2 = func2()
# print(type(foo2))
# print(next(foo2))
# print(next(foo2))
# print(next(foo2))
# print(next(foo2))

# def endless_numbers(n):
#     num = 2
#     while num < n:
#         yield num
#         num = num + 2

# foo = endless_numbers(10)
# print(foo)
# print(next(foo))
# print(next(foo))

# _list = [1,2,3,4]
# print(dir(_list))
# print(next(_list))
# iter_list = _list.__iter__()
# print(type(iter_list))
# print(dir(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# for x in endless_numbers(30):
#   print(x)

# def list_number(n):
#   for i in n:
#     return i

# for x in list_number(30):
#   print(x)

# import time

# start = time.time()
# _list = []

# for i in range(20000000):
#   sum_ = 0
#   sum_ += i
# print(f'time {time.time() - start}')


# class Counter:
#     def __init__(self, stop):
#         self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
#         self.stop = stop    # 반복을 끝낼 숫자
 
#     def __iter__(self):
#         return self         # 현재 인스턴스를 반환
 
#     def __next__(self):
#         if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
#             r = self.current            # 반환할 숫자를 변수에 저장
#             self.current += 1  
#             return r                    # 숫자를 반환
#         else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
#             raise StopIteration   
#     def show(self):
#       print(self.current)      # 예외 발생
# start = time.time() 
# # counter = Counter(20000000)
# for i in Counter(200):
#   print(i,end='')
# print(f'time {time.time() - start}')
