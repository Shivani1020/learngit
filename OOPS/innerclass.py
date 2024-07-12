class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self,number):
            self.number = number

        def start(self):
            print("Engine Started")

c = Car("BMW", 2017)
a = c.Engine(123)
print(a)
a.start()
print(a.number,":it is the car number")
print(c.make,c.year)