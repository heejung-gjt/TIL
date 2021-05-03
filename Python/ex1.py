# import os
# import psutil, time

# start = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
# def square(n):
#   result = []
#   for i in range(n):
#     print('sleep')
#     time.sleep(1)
#     result.append(i**2)
#   return result

# result = square(9)
# end = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
# print("Memory Usage when program start: {}".format(start))
# print("Memory Usage when program end: {}".format(end))

# print()
# print()

# start = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
# def gen_square(n):
#   for num in range(n):
#     print('sleep')
#     time.sleep(1)
#     yield num**2

# result = gen_square(9900000) 
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# end = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
# print("Memory Usage when program start: {}".format(start))
# print("Memory Usage when program end: {}".format(end))
import time

def sleep_func(x):
  print("sleep...")
  time.sleep(1)
  return x
gen = (sleep_func(x) for x in range(5))
for i in gen:
  print(i)

# def sleep_func2(x):
#   print('sleep')
#   time.sleep(1)
#   yield x
# for i in range(5):
#   gen2 = sleep_func2(i)
#   print(next(gen2))

def sleep_func3(x):
  print('list sleep,,,')
  time.sleep(1)
  return x
gen3 = [sleep_func3(x) for x in range(5)]
for i in gen3:
  print(i)