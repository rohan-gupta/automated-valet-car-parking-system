import re
from app.lot.lots import lot
from app.lot.lotfactory import LotFactory
from app.vehicle.vehiclefactory import VehicleFactory
import pytest


def test_lot():
    car_lot = LotFactory.create_lot("Car", "1")
    car = VehicleFactory.create_vehicle("Car", "SG123")
    car_lot.add_vehicle(car, 100.100)
    vehicle, parking_fee = car_lot.remove_vehicle(110.100)
    assert isinstance(car_lot, lot.Lot)
    assert car_lot.lot_type == "Car"
    assert car_lot.number == 1
    assert car_lot.parking_fee_rate == 2
    assert parking_fee == 2


def test_lot_not_allowed_vehicle_type():
    car_lot = LotFactory.create_lot("Car", "1")
    motorcycle = VehicleFactory.create_vehicle("Motorcycle", "SG678")
    with pytest.raises(ValueError):
        car_lot.add_vehicle(motorcycle, 100)
