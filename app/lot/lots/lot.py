import time
import math
from abc import ABC, abstractmethod


class Lot(ABC):
    @abstractmethod
    def __init__(self, lot_type, number):
        self.lot_type = str(lot_type)
        self.number = int(number)
        self.parking_fee_rate = None
        self.vehicle = None
        self.checkin = None
        self.checkout = None


    def add_vehicle(self, vehicle, timestamp):
        if vehicle.vehicle_type == self.lot_type:
            self.vehicle = vehicle
            self.checkin = int(timestamp)
        else:
            raise ValueError


    def remove_vehicle(self, timestamp):
        vehicle = self.vehicle
        self.vehicle = None
        self.checkout = int(timestamp)
        parking_fee = self.parking_fee()
        return vehicle, parking_fee


    def parking_fee(self):
        return self.parking_fee_rate * math.ceil((self.checkout - self.checkin)/3600)
