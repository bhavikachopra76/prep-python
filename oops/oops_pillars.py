from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.__engine_status = "OFF"
        self.brand = brand #Private attribute (encapsulation)
        self.__speed = 0 #Private attribute (encapsulation)

    @abstractmethod
    def start_engine(self):
        pass

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            print("Vehicle Accelerated")

    def get_speed(self):
        return self.__speed

    def _set_engine_status(self, status):
        self.__engine_status = status

    def get_status(self):
        print("\nBrand:", self.brand)
        print("Engine Status:", self.__engine_status)
        print("Speed:", self.__speed)

class Car(Vehicle): #single level Inheritance

    def start_engine(self):
        print("Car engine started with key ignition.")
        self._set_engine_status("ON")

class Bike(Vehicle): #Hierarchical inheritance
    def start_engine(self):
        print("\nBike engine started with key ignition.")
        self._set_engine_status("ON")

class ElectricCar(Car): #Multiple Level Inheritance
    @staticmethod
    def charge_battery():
        print("\nBattery charging... 🔋")

    def start_engine(self):
        print("\nElectric car engine started with push button")
        self._set_engine_status("ON")

class GPS:
    @staticmethod
    def enable_gps():
        print("GPS is enabled.")

class SmartCar(GPS, Car): #Multiple Inheritance
    @staticmethod
    def auto_drive():
        print("Autonomous driving mode activated.")

    def start_engine(self):
        print("\nSmart Car engine started with push button")
        self._set_engine_status("ON")

car1 = Car("BMW")
bike1 = Bike("Bullet")

vehicles = [Car("BMW"), Bike("Bullet")] #Runtime polymorphism

for v in vehicles:
    v.start_engine()


car1.accelerate(85)
car1.get_status()

bike1.get_status()

ev1 = ElectricCar("Tiago EV")
ev1.start_engine()
ev1.accelerate(50)
ev1.get_status()

sc1 = SmartCar("Elevate")
sc1.start_engine()
sc1.auto_drive()
sc1.enable_gps()







