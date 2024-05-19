from abc import ABC, abstractmethod

class Factory (ABC): 
    def __init__(self, model, fuel):
        self._model = model
        self.set_fuel_type(fuel)

    @abstractmethod
    def set_fuel_type(self, fuel):
        pass

    def get_attribute(self, attribute):
        return getattr(self, f"_{attribute}", None)

    def __str__(self):
        pass