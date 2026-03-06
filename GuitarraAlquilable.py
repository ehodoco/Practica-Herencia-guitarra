from datetime import datetime
from Guitarra import Guitarra

class GuitarraAlquilable(Guitarra):
    def __init__(self, n_cuerdas:int, fecha_creacion: datetime, precio_base: float, marca: str, modelo: str, forma: str, fecha_alquilada:datetime, fecha_retorno: datetime):
        super().__init__(n_cuerdas, fecha_creacion, precio_base, marca, modelo, forma)
        self.fecha_alquilada = fecha_alquilada
        self.fecha_retorno = fecha_retorno

    def alquilar(fecha_alquilada, fecha_retorno):
        pass

    def cuota_alquiler(fecha_alquilada, fecha_retorno):
        pass
