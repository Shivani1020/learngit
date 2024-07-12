students = {'John': ['Python','DJango', 'DRF'],'bob':['Java','Spring'],'Jim':['JS','node','react']}
keys = students.keys()
for eachkey in keys:
    print("Courses taken by", eachkey, " are: ")
    for eachcourse in students[eachkey]:
        print(eachcourse)