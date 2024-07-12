lst = [var for var in range(1, 30) if var % 2 == 0]
print(lst)

lst1 = [var for var in range(2, 20, 2)]
print(lst1)

lst2 = [2, 3, 4, 5]
result = [i ** 3 for i in lst2]
print(result)

##Product of lists
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
'''z = []
for i in range(len(a)):
    z.append(a[i]*b[i])'''
z = [a[i] * b[i] for i in range(len(a))]
print(z)

x = [1, 2, 3, 4]
y = [8, 1, 2, 9]
'''result = []
for i in x:
    if i in y:
        result.append(i)'''
result = [i for i in x if i in y]
print(result)
