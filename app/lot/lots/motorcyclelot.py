from .lot import Lot


class MotorcycleLot(Lot):
    def __init__(self, lot_type, number):
        super().__init__(lot_type, number)
        self.fee = 1.0
        self.allowed_vehicle_type = "Motorcycle"
