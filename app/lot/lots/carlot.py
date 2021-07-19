from .lot import Lot


class CarLot(Lot):
    def __init__(self, lot_type, number):
        super().__init__(lot_type, number)
        self.parking_fee_rate = 2.0
