from  vehicle_factory.factory import Factory 

class Motorcycle(Factory ):
    motorcycle_count = 0
    def __init__(self, model, fuel, wheels=2):
        super().__init__(model, fuel)
        self._wheels = wheels
        Motorcycle.motorcycle_count += 1 

    def set_model(self, model):
        self._model = model 

    def set_fuel_type(self, fuel):
        if fuel in ['electric', 'petrol', 'diesel']:
            self._fuel = fuel
        else:
            raise ValueError(f"Fuel must be either 'electric', 'petrol', or 'diesel'. Invalid fuel type: {fuel}")

    def print_motorcycle_count(self): 
        print(f"Number of motorcycles created: {Motorcycle.motorcycle_count}")

    # def __str__(self):
    #     return (f"The type of your vehicle is: Motorcycle\nModel: {self._model}, fuelType: {self._fuel}, Number of wheels: {self._wheels}")
    
    def __str__(self):
        return (f"Model: {self.get_attribute('model')}, "
            f"Fuel: {self.get_attribute('fuel')}, "
            f"Number of wheels: {self.get_attribute('wheels')}")

