class Programmer:
    def getname(self,n):
        self.name = n

    def setname(self):
        return self.name

    def getSalary(self, sal):
        self.salary = sal

    def setSalary(self):
        return self.salary

    def getTechnologies(self, techs):
        self.technologies = techs

    def setTechnologies(self):
        return self.technologies

p1 = Programmer()
p1.getname("Javes")
p1.getSalary(10000)
p1.getTechnologies(["Java", "Python", "Web Technology"])
print(p1.setname())
print(p1.setSalary())
print(p1.setTechnologies())

p2 = Programmer()
p2.getname('Poonam')
p2.getSalary(20000)
p2.getTechnologies(["C, c++, ruby"])
print(p2.setname())
print(p2.setSalary())
print(p2.setTechnologies())
