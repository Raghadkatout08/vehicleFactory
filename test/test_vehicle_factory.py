import pytest
from vehicle_factory.car import Car
from vehicle_factory.motorcycle import Motorcycle


@pytest.fixture
def new_car():
    return Car(model="Toyota Camry", fuel="petrol", color="Blue", doors=4)

@pytest.fixture
def new_motorcycle():
    return Motorcycle(model="Honda", fuel="electric")

def test_car_creation(new_car):
    car = new_car
    assert car.get_attribute("model") == "Toyota Camry"
    assert car.get_attribute("fuel") == "petrol"
    assert car.get_attribute("color") == "Blue"
    assert car.get_attribute("doors") == 4

def test_motorcycle_creation(new_motorcycle):
    motorcycle = new_motorcycle
    assert motorcycle.get_attribute("model") == "Honda"
    assert motorcycle.get_attribute("fuel") == "electric"
    assert motorcycle.get_attribute("wheels") == 2
    motorcycle.print_motorcycle_count() 
def test_car_color_change(new_car):
    car = new_car
    car.set_color("Green")
    assert car.get_attribute("color") == "Green"

def test_car_door_change(new_car):
    car = new_car
    car.set_number_of_doors(2)
    assert car.get_attribute("doors") == 2
