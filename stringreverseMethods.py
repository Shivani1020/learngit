s = input("Enter the string: ")
print(s[::-1])

s1 = input("Enter the string: ")
size = len(s1)-1
result = ''
while size>=0:
    result += s1[size]
    size-=1
print("The reversed string is: ",result)

s3 = input("Enter the string: ")
print(''.join(reversed(s3)))