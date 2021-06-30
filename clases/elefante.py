if __name__ == '__main__':
    from animal import Animal
else:
    from clases import Animal
class Elefante(Animal):
    def __init__(self, name, edad,tipo, salud = 100, felicidad = 70):
        super().__init__(name, edad, salud, felicidad)
        self.tipo = tipo
    def alimentacion(self, cantidad):
        self.salud += round(cantidad * 0.12)
        self.nivelFelicidad += 10