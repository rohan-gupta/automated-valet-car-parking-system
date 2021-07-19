from app.vehicle.vehicles import vehicle
from app.vehicle.vehiclefactory import VehicleFactory


def test_vehicle():
    car = VehicleFactory.create_vehicle("car", "SG123")
    motorcycle = VehicleFactory.create_vehicle("motorcycle", "SG789")
    assert isinstance(car, vehicle.Vehicle)
    assert isinstance(motorcycle, vehicle.Vehicle)
    assert car.vehicle_type == "Car"
    assert motorcycle.vehicle_type == "Motorcycle"
    assert car.number == "SG123"
    assert motorcycle.number == "SG789"
