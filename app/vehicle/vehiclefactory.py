from .vehicles import car, motorcycle


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, number):
        module_name = vehicle_type.lower()
        class_name = vehicle_type.title()
        args = (vehicle_type, number)
        return getattr(globals()[module_name], class_name)(*args)
