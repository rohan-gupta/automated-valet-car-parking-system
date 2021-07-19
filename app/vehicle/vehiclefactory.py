from .vehicles import car, motorcycle


class VehicleFactory:
    """Factory class to intantiate vehicle objects."""

    @staticmethod
    def create_vehicle(vehicle_type, number):
        module_name = vehicle_type.lower()
        class_name = vehicle_type.title()
        args = (vehicle_type, number)
        # Instantiate the class using args, obtained from module
        return getattr(globals()[module_name], class_name)(*args)
