from datetime import datetime
from Guitarra import Guitarra

class GuitarraAlquilable(Guitarra):
    def __init__(self, n_cuerdas:int, fecha_creacion: datetime, precio_base: float, marca: str, modelo: str, forma: str, fecha_venta: datetime, meses_garantia: int):
        super().__init__(n_cuerdas, fecha_creacion, precio_base, marca, modelo, forma)
        self.fecha_venta = fecha_venta
        self.meses_garantia = meses_garantia
        
    def vender():
        pass