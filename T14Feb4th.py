#Task 14: Create a Class Car
from datetime import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.make} {self.model} ({self.year})")

    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.year

def main():
    my_car = Car("Toyota", "Corolla", 2018)
    my_car.display_info()
    age = my_car.calculate_age()
    print(f"Age of the car: {age} years")

if __name__ == "__main__":
    main()
