'''La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (barbijo,jabón o alcohol)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.'''

confirmacion = 's'

while confirmacion == 's':
    tipo = str(input("Ingrese tipo de producto (Barbijo - Jabon - Alcohol): "))

    while tipo != "Barbijo" and tipo != "Jabon" and tipo != "Alcohol":
        tipo = str(input("Ingrese tipo de producto (Barbijo - Jabon - Alcohol): "))

    precio = float(input("Ingrese precio: "))
    while precio < 100 or precio > 1000:
        precio = float(input("Ingrese precio (Entre 100 y 1000): "))

    cantidad = int(input("Ingrese cantidad de productos: "))
    while cantidad < 1:
        cantidad = int(input("Ingrese cantidad de productos: "))

    marca = str(input("Ingrese marca: "))
    fabricante = str(input("Ingrese fabricante: "))

    print("\nDatos de la compra realizada")
    print("Tipo de producto: ", tipo)
    print("Precio:", precio)
    print("Cantidad: ", cantidad)
    print("Marca: ",marca)
    print("Fabricante: ", fabricante)
    
    confirmacion = input("Desea hacer otra compra? (s/n): ")
    if confirmacion == 'n':
        break


print("Programa finalizado")