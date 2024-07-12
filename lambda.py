l = lambda a,b: a+b
print("Sum of a and b is: ", l(20,30))



## Even or Odd filter
#li = [1,20,4,8,7,5]
di = {1:"as",2:"er",5:"er",6:"ed"}
result = list(filter(lambda x : x%2==0,di))
print(result)
for i in result:
    print(i)