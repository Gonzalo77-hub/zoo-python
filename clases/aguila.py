if __name__ == '__main__':
    from animal import Animal
else:
    from clases import Animal
class Aguila(Animal):
    def __init__(self, tam, name, edad, salud = 85, felicidad = 100):
        super().__init__(name, edad, salud, felicidad)
        self.tamaño = tam
    def alimentacion(self, cantidad):
        self.salud += round(cantidad * 0.26)
        self.nivelFelicidad += 12