'''Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
quiera (se limita a 1 perrito por ingreso), se les pide:
nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:

1. Generar un listado con todos los datos de los pacientes ordenados por edad.
2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por
nombre.
3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
impuesto por ingresos brutos e informarlo.
4. Informar el nombre y el peso del perro con más peso.'''

perros_mas_treintaKilos = []

while True:
    
    nombre = input("Ingrese nombre del paciente: ")
    
    precio = float(input("Ingrese el precio de la consulta (entre 500$ y 2500$): "))
    while precio < 500 or precio > 2500:
        precio = float(input("ERROR,Ingrese el precio de la consulta (entre 500$ y 2500$): "))
    
    raza = input("Ingrese raza (caniche,ovejero, siberiano): ")
    while raza != 'caniche' and raza != 'ovejero' and raza != 'siberiano':
        raza = input("ERROR, Ingrese raza (caniche,ovejero, siberiano): ")
    
    edad = int(input("Ingrese la edad del perro (entre 1 y 15): "))
    while edad < 1 or edad > 15:
         edad = int(input("ERROR,Ingrese la edad del perro (entre 1 y 15): "))
    
    
    confirmacion = input("Desea ingresar otro paciente? (s/n): ")
    confirmacion = confirmacion.lower()
    while confirmacion != 's' and confirmacion != 'n':
        confirmacion = input("Porfavor ingrese una opcion valida,desea ingresar otro paciente? (s/n): ")
        confirmacion = confirmacion.lower()
    if confirmacion == "n":
        break