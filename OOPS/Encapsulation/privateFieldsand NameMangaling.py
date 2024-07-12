class Student:
    def __init__(self):
        self.__id = 123         # Using __ makes the variables private
        self.__name = "John"

    def display(self):
        print(self.__id)
        print(self.__name)

s = Student()
print(s._Student__id);     # this method is called name Mangling
print(s._Student__name);