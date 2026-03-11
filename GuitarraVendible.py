from datetime import datetime, timedelta
from Guitarra import Guitarra

class GuitarraVendible(Guitarra):
   
    def __init__(self, n_cuerdas:int, fecha_creacion: datetime, precio_base: float, marca: str, modelo: str, forma: str, dias_garantia: int, fecha_venta: datetime = None):
        super().__init__(n_cuerdas, fecha_creacion, precio_base, marca, modelo, forma)
        self.fecha_venta = fecha_venta
        self.dias_garantia = dias_garantia
    

    def disponible(self) -> bool:
        if self.fecha_venta != None:
            return False
        return True


    def precio_venta(self) -> float:
        return self.precio_base * self.impuesto_marca[self.marca]


    def vender(self) -> datetime:
        self.fecha_venta = datetime.today()
        fin_garantia = self.fecha_venta + timedelta(days=self.dias_garantia)
        return fin_garantia


if __name__ == "__main__":

    bcrich1 = GuitarraVendible(6, datetime(1999, 1, 1), 250, "BCRich", "Platinum Series", "Warlock", 184)
    
    print(bcrich1.vender())