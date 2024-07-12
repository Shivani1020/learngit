l = [2,3,5,-2,5,3,1,19,23]
result = []
length = len(l)
for i in l:
  if i not in result:
    result.append(i)
print(result)