from .lots import carlot, motorcyclelot


class LotFactory:
    """Factory class to intantiate vehicle objects."""
    
    @staticmethod
    def create_lot(lot_type, number):
        module_name = lot_type.lower() + "lot"
        class_name = lot_type.title() + "Lot"
        args = (lot_type, number)
        # Instantiate the class using args, obtained from module
        return getattr(globals()[module_name], class_name)(*args)
