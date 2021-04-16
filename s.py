number = [1,2,3]
letter = ['a','d','c']

zips = list(zip(number,letter))
print(zips)

num , let = zip(*zips)
print(num)
print(let)