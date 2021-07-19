import re
from app.lot.lots import lot
from app.lot.lotfactory import LotFactory
from app.vehicle.vehiclefactory import VehicleFactory
import pytest


def test_lot():
    car_lot = LotFactory.create_lot("CarLot", "1")
    car = VehicleFactory.create_vehicle("Car", "SG123")
    car_lot.add_vehicle(car)
    car_lot.remove_vehicle()
    assert isinstance(car_lot, lot.Lot)
    assert car_lot.lot_type == "CarLot"
    assert car_lot.number == 1
    assert car_lot.fee == 2.0
    assert re.match(r"\d+\.\d+", str(car_lot.checkin))
    assert re.match(r"\d+\.\d+", str(car_lot.checkout))


def test_lot_not_allowed_vehicle_type():
    car_lot = LotFactory.create_lot("CarLot", "1")
    motorcycle = VehicleFactory.create_vehicle("Motorcycle", "SG678")
    with pytest.raises(ValueError):
        car_lot.add_vehicle(motorcycle)