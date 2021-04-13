def linear_search(L,x):
  i = 0
  while i < len(L) and L[i] != x:
    i += 1
  if i < len(L):
    return i
  else:
    return -1

answer = linear_search([3,6,4,7,8],8)
print(answer)
