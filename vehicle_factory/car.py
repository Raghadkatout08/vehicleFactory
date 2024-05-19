from  vehicle_factory.factory import Factory 


class Car(Factory):
    car_count = 0 

    def __init__(self, model, fuel, color, doors=4):
        super().__init__(model, fuel) 

        self._number_of_wheels = 4 
        self._color = color 
        self.set_number_of_doors(doors)
        Car.car_count += 1
        
    def set_model(self, model):
        self._model = model


    def set_fuel_type(self, fuel):
        if fuel in ['electric', 'petrol', 'diesel']:
            self._fuel = fuel 
        else:
            raise ValueError("Fuel must be either 'electric', 'petrol', or 'diesel'.")
        
    def set_color(self, color):
        self._color = color 
    
    def set_number_of_doors(self, doors):
        if doors in [2, 4]:
            self._doors = doors
        else:
            raise ValueError("Number of doors must be either '2' or '4'.")
        
    def print_car_count(self):
        print(f"Number of cars created: {Car.car_count}")

    # def __str__(self):
    #     return (f"The type of your vehicle is: Car\nModel: {self._model}, fuelType: {self._fuel}, color: {self._color}, Number of doors: {self._doors}, Number of wheels: {self._number_of_wheels}")

    def __str__(self):
        return (f"Model: {self.get_attribute('model')}, "
                f"Fuel: {self.get_attribute('fuel')}, "
                f"Color: {self.get_attribute('color')}, "
                f"Doors: {self.get_attribute('doors')}, "
                f"Number of wheels: {self.get_attribute('number_of_wheels')}")