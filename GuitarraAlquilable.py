from datetime import datetime, timedelta
from Guitarra import Guitarra

class GuitarraAlquilable(Guitarra):


    def __init__(self, n_cuerdas:int, fecha_creacion: datetime, precio_base: float, marca: str, modelo: str, forma: str, fecha_alquilada:datetime = None, fecha_retorno: datetime = None):
        super().__init__(n_cuerdas, fecha_creacion, precio_base, marca, modelo, forma)
        self.fecha_alquilada = fecha_alquilada
        self.fecha_retorno = fecha_retorno


    def disponible(self) -> bool:
        if datetime.today() < self.fecha_retorno:
            return False
        return True


    def alquilar(self, dias) -> tuple[float, datetime]:
        self.fecha_alquilada = datetime.today()
        cuota = self.cuota_diaria(dias)
        fecha_devolucion = self.fecha_alquilada + timedelta(days=dias)
        return (round(cuota, 2), fecha_devolucion)
    
    def cuota_diaria(self, dias) -> float:
        return (self.precio_base*self.impuesto_marca[self.marca]/dias)/4


if __name__ == "__main__":

    bcrich1 = GuitarraAlquilable(6, datetime(1999, 1, 1), 250, "BCRich", "Platinum Series", "Warlock")
    
    print(bcrich1.alquilar(184))