from clases import Animal
from clases import Aguila
from clases import Oso
from clases import Elefante



class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def agregarAnimal(self, animal):
        self.animals.append(animal)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
###########pruebas directas###################
""" zoologico1 = Zoo("Zoologico Buin")
zoologico2 = Zoo("Zoologico Alameda")
print(zoologico1.name)
oso1 = Oso("marron","Alfredo",12)
aguila1 = Aguila("12", "marcelo",8)
elefante1 = Elefante("Martin", 12, "Africano")
zoologico1.agregarAnimal(oso1)
zoologico1.agregarAnimal(aguila1)
zoologico1.print_all_info()
zoologico2.agregarAnimal(elefante1)
zoologico2.print_all_info()
oso1.alimentacion(10)
elefante1.alimentacion(20)
zoologico1.print_all_info()
zoologico2.print_all_info()
lista2 = []
lista2.append(zoologico1)
lista2.append(zoologico2)
for zoologico in lista2:
    print(zoologico.name) """
############################Pruebas interactivas######################
listazoo = []
def crearZoo():
    name = input("Ingrese Nombre: ")
    a = Zoo(name)
    listazoo.append(a)
    print(f" se ha creado el zoo de nombre {name}")
def crearAnimal():
    print("animales para crear: \n" )
    print("1.- Elefante\n")
    print("2.- Oso\n")
    print("3.- Aguila\n")
    p = int(input("que animal desea crear: "))
    if p == 1:
        r= input("Ingrese nombre del elefante: ")
        e= input("Ingrese edad del elefante: ")
        t = input("ingrese el tipo del elefante: ")
        a = Elefante(r,e,t)
        print("el elfante fue creado")
        print("elija un zoologico para asignar el elefante")
        for zoologico in listazoo:
            print(f"- {zoologico.name}")
        w = input("ingrese el nombre del zoologico: ")
        for zoologico in listazoo:
            if zoologico.name == w:
                zoologico.animals.append(a)
    elif p == 2:
        r= input("Ingrese el color del oso: ")
        e= input("Ingrese el nombre del oso: ")
        t = input("ingrese la edad del oso: ")
        a = Oso(r,e,t)
        print("el oso fue creado")
        print("elija un zoologico para asignar el oso")
        for zoologico in listazoo:
            print(f"- {zoologico.name}")
        w = input("ingrese el nombre del zoologico: ")
        for zoologico in listazoo:
            if zoologico.name == w:
                zoologico.animals.append(a)

    elif p == 3:
        r= input("Ingrese tamaño del aguila: ")
        e= input("Ingrese nombre del aguila: ")
        t = input("ingrese edad del aguila: ")
        a = Aguila(r,e,t)
        print("el aguila fue creado!!\n")
        print("elija un zoologico para asignar el aguila")
        for zoologico in listazoo:
            print(F"- {zoologico.name}")
        w = input("ingrese el nombre del zoologico: ")
        for zoologico in listazoo:
            if zoologico.name == w:
                zoologico.animals.append(a)
def alimentarAnimalesZoo():
    print("Elija un zoologico para alimentar animales")
    for zoologico in listazoo:
        print(f"- {zoologico.name}")
    w = input("ingrese el nombre del zoologico: ")
    j = int(input("ingrese la cantidad de Comida: "))
    for zoologico in listazoo:
        if zoologico.name == w:
            for animales in zoologico.animals:
                animales.alimentacion(j)
                print(f"los/las {animales.__class__.__name__}s fueron alimentados\n")
                """ if animales.__class__.__name__ == "Oso":
                   animales.alimentacion(j)
                elif animales.__class__.__name__ == "Aguila":
                     animales.alimentacion(j)
                elif animales.__class__.__name__ == "Elefante":
                    animales.alimentacion(j) """

def mostraranimalesZoo():
    print("lista de zoologicos: \n")
    for zoologico in listazoo:
        print(f"- {zoologico.name}")
    u = input("Ingrese nombre del zoologico: ")
    for zoologico in listazoo:
        if zoologico.name == u:
            zoologico.print_all_info()

op = 0

def menu():
    print ("Selecciona una opción")
    print ("\t1 - Crear Zoo")
    print ("\t2 - Crear Animal")
    print ("\t3 - Mostrar Animales en Zoo seleccionado")
    print ("\t4 - Alimentar animales por zoologico")
    print ("\t9 - Salir")


while True:
    
    menu()
    op = input("ingrese una opcion: ")
    if op == "1":
        crearZoo()
    elif op == "2":
        crearAnimal()
    elif op == "3":
        mostraranimalesZoo()
    elif op == "4":
        alimentarAnimalesZoo()
    elif op == "9":
        break
    else:
        print(" No haz ingresado una opcion correcta, pulsa una tecla para continuar")