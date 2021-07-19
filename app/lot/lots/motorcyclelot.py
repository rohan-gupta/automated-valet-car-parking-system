from .lot import Lot


class MotorcycleLot(Lot):
    """Motorcycle lot class inheriting from base lot class."""

    def __init__(self, lot_type, number):
        # Calling the parent class constructor
        super().__init__(lot_type, number)
        self.parking_fee_rate = 1
