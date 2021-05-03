# def square(n):
#   for num in range(n):
#     yield num ** 2

# result = square(10)
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))

# for i in result:
#   print(i)

square = (x*x for x in range(9))
print(square)

for i in square:
  print(i) .