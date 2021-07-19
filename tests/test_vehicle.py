from app.vehicle.vehicles import car, motorcycle
from app.vehicle.vehiclefactory import VehicleFactory


def test_vehicle():
    vehicle = VehicleFactory.create_vehicle("car", "SG123")
    assert isinstance(vehicle, car.Car)
    assert not isinstance(vehicle, motorcycle.Motorcycle)
    assert vehicle.vehicle_type == "Car"
    assert vehicle.number == "SG123"
