class Patient:
    def setId(self, id):
        self.Id = id

    def getId(self):
        return self.Id

    def setName(self, name):
        self.Name = name

    def getName(self):
        return self.Name

    def setSsn(self, ssn):
        self.Ssn = ssn

    def getSsn(self):
        return self.Ssn

p = Patient()
p.setId(123)
p.setName("Kartik")
p.setSsn("Car123")

print(p.getId(),p.getName(), p.getSsn())