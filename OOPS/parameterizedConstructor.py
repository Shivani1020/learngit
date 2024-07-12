class Course():

    def __init__(self, sub, ratings):
        self.name = sub
        self.ratings = ratings

    def average(self):
        numberofrating = len(self.ratings)
        avg = sum(self.ratings)/numberofrating
        print("Average rating for ",self.name, "is", avg)

c1 = Course("Java", [2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 =  Course("Python", [1,2,3,4])
print(c2.name)
print(c2.ratings)
c2.average()

