class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def addclinicaldata(self,clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, component, value):
        self.component = component
        self.value = value

p = Patient("Atul", 29)
c1 = Clinical("Heartrate", 80)
p.addclinicaldata(c1)

c2 = Clinical("BP","80/120")
p.addclinicaldata(c2)

print(p.name,p.age)
for eachClinical in p.clinical:
    print(eachClinical.component)
    print(eachClinical.value)

