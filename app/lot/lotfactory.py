from .lots import carlot, motorcyclelot


class LotFactory:
    @staticmethod
    def create_lot(lot_type, number):
        module_name = lot_type.lower()
        class_name = lot_type
        args = (lot_type, number)
        return getattr(globals()[module_name], class_name)(*args)
