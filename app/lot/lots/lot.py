import time
from abc import ABC, abstractmethod


class Lot(ABC):
    @abstractmethod
    def __init__(self, lot_type, number):
        self.lot_type = str(lot_type)
        self.number = int(number)
        self.allowed_vehicle_type = None
        self.fee = None
        self.vehicle = None
        self.checkin = None
        self.checkout = None


    def add_vehicle(self, vehicle):
        if vehicle.vehicle_type == self.allowed_vehicle_type:
            self.vehicle = vehicle
            self.checkin = time.time()
        else:
            raise ValueError


    def remove_vehicle(self):
        vehicle = self.vehicle
        self.vehicle = None
        self.checkout = time.time()
        return vehicle

