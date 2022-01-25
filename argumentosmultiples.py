def crear_persona(nombre, apellido, correo):
    print(f"{nombre} {apellido} {correo}")

def saludar(*args):
    # MIL COSAS
    crear_persona(*args)
    
saludar("Francisco", "Juan", "Felipe")

def saludar_2(nombre, *args, **kwargs):
    print(nombre, args, kwargs)

saludar_2("Francisco","Gato","Perro",43, apellido="Francisco", ciudad="Temuco")

