class IDiscount:
    """Interfaz para descuentos"""
    def apply(self, total: float):
        raise NotImplementedError
    
class NoDiscount(IDiscount):
    def apply(self, total: float):
        return total

class StudentDiscount(IDiscount):
    def apply(self, total: float):
        # 15% de descuento para estudiantes
        return total * 0.85

    