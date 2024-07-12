# Right Angled Triangle

num = int(input("Enter the row number for right angled triangle: "))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("* ",end="")
    print()
# second way
for i in range(1, num+1):
    print("* "*i)


# Pyramid
n = int(input("Enter the number of rows fo pyramid: "))
for i in range(1, n+1):
    print(" "*(n-i), end= "")
    print("* "*i)