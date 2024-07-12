class Student:
    def setId (self, id):
        self.Id = id

    def getId (self):
        return self.Id

    def setName(self, name):
        self.Name = name

    def getName(self):
        return self.Name

s = Student()
s.setId(101)
s.setName("Shakti")
print(s.getId())
print(s.getName())
