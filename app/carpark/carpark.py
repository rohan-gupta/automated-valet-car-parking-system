from app.vehicle.vehiclefactory import VehicleFactory
from app.lot.lotfactory import LotFactory


class CarPark:
    """Car park class that implements add/remove and fee calculation functionality."""
    
    def __init__(self):
        self.revenue = 0.0
        self.allowed_vehicle_type = ["Car", "Motorcycle"]
        self.lots = {}
        self.vehicles = {}


    def add_lot(self, lot_type):
        """Adds lot object and checks for allowed types."""

        if lot_type not in self.lots and lot_type in self.allowed_vehicle_type:
            self.lots[lot_type] = {}
        elif lot_type not in self.allowed_vehicle_type:
            raise ValueError("Lot type not allowed")
        # Try setting the lot number based on previous entries otherwise default to 1
        lot_number = max(self.lots[lot_type]) + 1 if self.lots[lot_type] else 1
        lot = LotFactory.create_lot(lot_type, lot_number)
        self.lots[lot_type][lot_number] = lot
        return self.lots
 

    def remove_lot(self, lot_type, lot_number):
        """Removes lot object for a given lot type and lot number.""" 

        if lot_type in self.lots and lot_number in self.lots[lot_type]:
            del self.lots[lot_type][lot_number]
        else:
            raise AttributeError("Lot type not found")
        return self.lots


    def get_vacant_lot(self, lot_type):
        """Returns smallest vacant lot number if available otherwise -1."""

        lot_numbers_vacant = []
        for lot_number, lot in self.lots[lot_type].items():
            if not self.lots[lot_type][lot_number].vehicle:
                lot_numbers_vacant.append(lot_number)
                break
        lot_number_vacant = min(lot_numbers_vacant) if lot_numbers_vacant else -1
        return lot_number_vacant


    def add_vehicle(self, vehicle_type, vehicle_number, timestamp):
        """Returns assigned lot number to vehicle otherwise 'Reject'."""
        
        if vehicle_number not in self.vehicles:
            vehicle = VehicleFactory.create_vehicle(vehicle_type, vehicle_number)
            lot_type = vehicle.vehicle_type
            lot_number_vacant = self.get_vacant_lot(lot_type)
            if lot_number_vacant != -1:
                self.lots[lot_type][lot_number_vacant].add_vehicle(vehicle, timestamp)
                self.vehicles[vehicle_number] = {"lot_type": lot_type, "lot_number": lot_number_vacant}
                status = "Accept", f"{lot_type}Lot{lot_number_vacant}"
            else:
                status = "Reject"
        else:
            status = "Reject"
        return status


    def remove_vehicle(self, vehicle_number, timestamp):
        """Returns freed lot number and parking fee otherwise raises error."""

        if vehicle_number in self.vehicles:
            lot_type, lot_number = self.vehicles[vehicle_number].values()
            vehicle, parking_lot_fee = self.lots[lot_type][lot_number].remove_vehicle(timestamp)
            self.revenue += parking_lot_fee
            status = f"{lot_type}Lot{lot_number}", parking_lot_fee
            return status
        else:
            raise AttributeError("Vehicle not found")
