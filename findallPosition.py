s = "Take up one idea and make that idea your life."\
    "Think and dream of that idea and leave every idea alone."
subs = "idea"
found = False
pos = -1
length = len(s)
while True:
    pos = s.find(subs, pos+1,length)
    if pos == -1:
        break
    print("Found the substring at position: ",pos)
    found = True
if found == False:
    print("Sub string not found")