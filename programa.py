from clases import BankAccount
from clases import User

def saludar():
    print("HOLA")

def despedir():
    print("CHAO")

while True:
    print("1 Decir Hola")
    print("2 Decir Chao")
    print("3 Salir")
    numero = int(input("Ingrese una opción: "))

    if numero == 1:
        saludar()
    
    if numero == 2:
        despedir()

    if numero == 3:
        break
