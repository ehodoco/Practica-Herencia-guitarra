from datetime import datetime

class Guitarra:

    impuesto_marca = {"Fender": 1.2, "BCRich": 1.3, "Gibson": 1.99, "Harley Benton": 1.01, "Jackson": 1.15, "MaxGuitar":10}

    def __init__(self, n_cuerdas:int, fecha_creacion: datetime, precio_base: float, marca: str, modelo: str, forma: str):
        self.n_cuerdas = n_cuerdas
        self.fecha_creacion = fecha_creacion
        self.precio_base = precio_base
        self.marca = marca
        self.modelo = modelo
        self.forma = forma