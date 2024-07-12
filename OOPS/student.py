class Student:
    major = 'CSE'  #Declaring the static variable

    def __init__(self,name, rollno):
        self.name = name
        self.rollno= rollno

s1 = Student("Jack", 23)
s2 = Student("Alen", 24)
print(s1.name,s1.major, s1.rollno)
print(s2.name,s2.major,s2.rollno)
print(Student.major)