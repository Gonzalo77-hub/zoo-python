class Animal:
    def __init__(self, name, edad, salud, felicidad):
        self.nombre = name
        self.edad = edad
        self.salud = salud
        self.nivelFelicidad = felicidad
    
    def display_info(self):
        print(f"Animal: {self.__class__.__name__}, Nombre: {self.nombre}, Salud: {self.salud}, Felicidad: {self.nivelFelicidad}")
    
    def alimentacion(self):
        pass