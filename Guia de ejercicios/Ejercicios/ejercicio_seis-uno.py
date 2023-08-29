'''Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.'''

# Programa sin usar listas

# Pedimos los datos de cada auto al usuario
# marca_uno = input("Ingrese la marca del primer auto: ")
# anio_uno = int(input("Ingrese el año del modelo del primer auto: "))
# precio_uno = float(input("Ingrese el precio del primer auto: "))

# marca_dos = input("Ingrese la marca del segundo auto: ")
# anio_dos = int(input("Ingrese el año del modelo del segundo auto: "))
# precio_dos = float(input("Ingrese el precio del segundo auto: "))

# marca_tres = input("Ingrese la marca del tercer auto: ")
# anio_tres = int(input("Ingrese el año del modelo del tercer auto: "))
# precio_tres = float(input("Ingrese el precio del tercer auto: "))

# # Mostramos los datos por pantalla
# print("Auto 1:")
# print("Marca:", marca_uno)
# print("Año del modelo:", anio_uno)
# print("Precio:", precio_uno)

# print("Auto 2:")
# print("Marca:", marca_dos)
# print("Año del modelo:", anio_dos)
# print("Precio:", precio_dos)

# print("Auto 3:")
# print("Marca:", marca_tres)
# print("Año del modelo:", anio_tres)
# print("Precio:", precio_tres)

#Programa usando listas

# Pedimos los datos de cada auto al usuario y los agregamos a una lista de diccionarios
autos = []
cantidad = 3

for i in range(cantidad):
    marca = input(f"Ingrese la marca del auto {i+1}: ")
    anio = int(input(f"Ingrese el año del modelo del auto {i+1}: "))
    precio = float(input(f"Ingrese el precio del auto {i+1}: "))

    auto = {"marca": marca, "anio": anio, "precio": precio}
    autos.append(auto)


for auto in autos:
    print(f"\nMarca: {auto['marca']}")
    print(f"Año del modelo: {auto['anio']}")
    print(f"Precio: {auto['precio']}\n")