word = input("Enter the word: ")
vowel = {'a', 'e', 'i', 'o', 'u'}
result = {}
for c in word:
    if c in vowel:
        result[c] = result.get(c, 0)+1
for k,v in result.items():
    print(k, "is present", v, " times")



# Only vowel count
str='python is cool'
d={}
#vowel='AEIOUaeiou'
for i in str:
    #if i in vowel:
    if i == 'a' or 'e' or 'i' or 'o' or 'u':
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
print(d)