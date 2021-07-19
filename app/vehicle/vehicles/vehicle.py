from abc import ABC


class Vehicle(ABC):
    def __init__(self, vehicle_type, number):
        self.vehicle_type = vehicle_type.title()
        self.number = str(number)
 