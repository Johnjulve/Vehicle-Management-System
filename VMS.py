from abc import abstractmethod
class Vehicle:
    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def honk(self):
        pass

class CarOptions:
    def __init__(self):
        self.mileage = 0

    def Travel(self, distance: int):
        print(f"Your Car has traveled {distance} km")
        self.mileage += distance
    
    def CarDetails(self, make, model, year):
        print(f"""
              Car Name: {make}
              Model Name: {model}
              Year: {year}
              Mileage: {self.mileage}
              """)

    def carUpdate(self, model):
        if self.mileage >= 10000:
            print(f"Your Car {model} needs maintenance")
        elif self.mileage >= 1000:
            print(f"Your Car {model} still has low mileage")
        else:
            print(f"Your Car {model} doesn't need maintenance")
    
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.options = CarOptions()

    def accelerate(self):
        distance = int(input("How many KM do you want to travel: "))
        print("Car is accelerating...")
        self.options.Travel(distance)
        

    def brake(self):
        print("Car is braking...")

    def honk(self):
        print("Car is honking...")
        
class Sedan(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.options = CarOptions()

    def accelerate(self):
        distance = int(input("How many KM do you want to travel: "))
        print("Sedan is accelerating...")
        self.options.Travel(distance)
        

    def brake(self):
        print("Sedan is braking...")

    def honk(self):
        print("Sedan is honking...")

class SUV(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.options = CarOptions()

    def accelerate(self):
        distance = int(input("How many KM do you want to travel: "))
        print("SUV is accelerating...")
        self.options.Travel(distance)

    def brake(self):
        print("SUV is braking...")

    def honk(self):
        print("SUV is honking...")

