from vehicle_factory.car import Car
from vehicle_factory.motorcycle import Motorcycle

car1 = Car(model="Toyota Camry", fuel="petrol", color="Blue", doors=4)
car2 = Car(model="Toyota Corolla", fuel="diesel", color="Red", doors=2)
car3 = Car(model="Honda Civic", fuel="petrol", color="Black", doors=4)
car4 = Car(model="Ford Mustang", fuel="petrol", color="Yellow", doors=2)

motorcycle1 = Motorcycle(model="Harley Davidson", fuel="petrol")
motorcycle2 = Motorcycle(model="Yamaha YZF-R1", fuel="petrol")
motorcycle3 = Motorcycle(model="Kawasaki Ninja", fuel="petrol")
motorcycle4 = Motorcycle(model="Ducati Panigale V4", fuel="petrol")

print("\nCars:")
print("Car 1: " , car1)
print("Car 2: " , car2)
print("Car 3: " , car3)
print("Car 4: " , car4)

print("\nmotorcycles:")
print("Motorcycle 1: " , motorcycle1)
print("Motorcycle 2: " , motorcycle2)
print("Motorcycle 3: " , motorcycle3)
print("Motorcycle 4: " , motorcycle4)


print("Number of cars created:", Car.car_count)
print("Number of motorcycles created:", Motorcycle.motorcycle_count)
