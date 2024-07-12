from abc import abstractmethod, ABC
class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("car is stoping")

    def display(self):
        print("Parent class display function")

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):                     # Overriding the display method
        print(self.cruiseControlEnabled)

    def drive(self):
        print("three series drive method")


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def display(self):
        print("Hey it is one of the demanded cars")
        super().display()

    def drive(self):
        print("five series drive method")

threeseries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeseries.cruiseControlEnabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
threeseries.drive()

threeseries.start()
threeseries.stop()
threeseries.display()

fiveseries = FiveSeries(False, "Rolls Royce", "5437", "2019")
print(fiveseries.parkingAssistEnabled, ",", fiveseries.make, ",", fiveseries.model, ",", fiveseries.year)
fiveseries.display()
