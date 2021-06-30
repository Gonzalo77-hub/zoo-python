if __name__ == '__main__':
    from animal import Animal
else:
    from clases import Animal
class Oso(Animal):
    def __init__(self, color, name, edad, salud = 80, felicidad = 95):
        super().__init__(name, edad, salud, felicidad)
        self.colorPiel = color
    def alimentacion(self, cantidad):
        self.salud += round(cantidad * 0.15) 
        self.nivelFelicidad += 10
