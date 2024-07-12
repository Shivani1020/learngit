##MAP

lst = [2,3,4,5]

result = list(map(lambda x : x**2,lst))
print(result)


## REDUCE

from functools import reduce

lst = [1,2,3,4,5,6]
result2 = reduce(lambda x,y:x*y,lst)
print(result2)
