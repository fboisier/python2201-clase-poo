class Vehiculo:
    def __init__(self, color, marca, modelo, pasajeros = 5):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.cantidadPasajeros = pasajeros
        
    def acelerar(self):
        raise NotImplementedError
        
    
    def frenar(self):
        print(f" El vehiculo está frenando {self.marca}")
        
    
    def virar(self):
        print(f" El vehiculo está virando {self.marca}")
        
    
    def encenderMotor(self):
        print(f" El vehiculo está encendiendo {self.marca}")
        
    def __str__(self):
        return f"El vehiculo de marca {self.marca} y color {self.color} tiene {self.cantidadPasajeros} capacidad de pasajeros"

    
class Auto(Vehiculo):
    def __init__(self, color, marca, modelo):
        super().__init__(color, marca, modelo)
        self.puertas = 5
    
    def acelerar(self):
        print(f" El auto esta acelerando {self.marca}") 

auto1 = Auto("Rojo", "TOYOTA", "YARIS")



class Camion(Vehiculo):
    def __init__(self, color, marca, modelo, pasajeros):
        super().__init__(color, marca, modelo, pasajeros)
        self.tara = 2000
        self.largo = 15
        self.eje = 3

    def acelerar(self):
        print(f" El camion esta acelerando {self.marca}") 

class Moto(Vehiculo):
    def __init__(self, color, marca, modelo):
        super().__init__(color, marca, modelo, 2)

    def encenderMotor(self):
        print("La moto enciende el motor con la pata.")

    def acelerar(self):
        print("La moto esta acelerando")


camion1 = Camion("Negro", "MB", "XX1",2)
moto1 = Moto("Azul", "Kawazaky", "S900")

print("A",auto1.__dict__)
print("C",camion1.__dict__)
print("M",moto1.__dict__)

auto1.acelerar()
camion1.acelerar()

camion1.encenderMotor()
auto1.encenderMotor()
moto1.encenderMotor()

moto1.acelerar()

class AutoMotora:
    def __init__(self):
        self.vehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def acelerarTodosLosVehiculos(self):
        for v in self.vehiculos:
            v.acelerar()
    

venta_autos = AutoMotora()
venta_autos.agregarVehiculo(camion1)
venta_autos.agregarVehiculo(auto1)
venta_autos.agregarVehiculo(moto1)

venta_autos.acelerarTodosLosVehiculos()