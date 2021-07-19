from .lot import Lot


class CarLot(Lot):
    def __init__(self, lot_type, number):
        super().__init__(lot_type, number)
        self.fee = 2.0
        self.allowed_vehicle_type = "Car"
