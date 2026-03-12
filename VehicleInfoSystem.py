"""1) Problem: Vehicle Information System

Design a program using inheritance.

🔹 Base Class: Vehicle

Create a class Vehicle with the following attributes:

vehicle_id

brand

price

Methods:

display_vehicle()

Displays vehicle details.

🔹 Derived Class: Car (inherits from Vehicle)

Add the following additional attributes:

num_doors

fuel_type

Methods:

display_car_details()

Display all vehicle details along with car-specific information.

🔹 Tasks

Create at least 2 car objects.

Display their details.

Example Output
Vehicle ID: 201
Brand: Toyota
Price: 800000
Doors: 4
Fuel Type: Petrol
"""

class Vehicle:
    def __init__(self, vehicle_id: int, brand: str, price: float):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price

    def display_vehicle(self) -> None:
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")


class Car(Vehicle):
    def __init__(
        self,
        vehicle_id: int,
        brand: str,
        price: float,
        num_doors: int,
        fuel_type: str,
    ):
        super().__init__(vehicle_id, brand, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_car_details(self) -> None:
        # reuse base class display first
        self.display_vehicle()
        print(f"Doors: {self.num_doors}")
        print(f"Fuel Type: {self.fuel_type}")


# --- example usage --------------------------------------------------
def main() -> None:
    cars = [
        Car(201, "Toyota", 800000, 4, "Petrol"),
        Car(302, "Honda", 950000, 2, "Diesel"),
    ]

    for car in cars:
        car.display_car_details()
        print()


if __name__ == "__main__":
    main()
