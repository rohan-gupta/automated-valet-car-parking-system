import time
import math
from abc import ABC, abstractmethod


class Lot(ABC):
    """Base lot class to be inherited from."""

    @abstractmethod
    def __init__(self, lot_type, number):
        """Abstract constructor to be extended in child class."""

        self.lot_type = str(lot_type)
        self.number = int(number)
        self.parking_fee_rate = None
        self.vehicle = None
        self.checkin = None
        self.checkout = None


    def add_vehicle(self, vehicle, timestamp):
        """Adds vehicle object to lot."""

        # Checking for compatible vehicle and lot type
        if vehicle.vehicle_type == self.lot_type:
            self.vehicle = vehicle
            self.checkin = int(timestamp)
        else:
            raise ValueError


    def remove_vehicle(self, timestamp):
        """Removes vehicle object from lot and calls the parking fee method."""

        vehicle = self.vehicle
        self.vehicle = None
        self.checkout = int(timestamp)
        parking_fee = self.calculate_parking_fee()
        return vehicle, parking_fee


    def calculate_parking_fee(self):
        """Calculates parking fee."""

        return self.parking_fee_rate * math.ceil((self.checkout - self.checkin)/3600)
