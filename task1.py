from abc import abstractmethod, ABC
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Vehicle:
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make = make
        self.model = model 
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено") 

class Motorcycle(Vehicle):
     def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")         

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass
    
    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "US")
    
    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU")

if __name__ == "__main__":
    us_vehicle_factory = USVehicleFactory()
    us_car = us_vehicle_factory.create_car("Toyota", "Corolla")
    us_motorcycle = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()

    us_vehicle_factory = EUVehicleFactory()
    us_car = us_vehicle_factory.create_car("Toyota", "Corolla")
    us_motorcycle = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()