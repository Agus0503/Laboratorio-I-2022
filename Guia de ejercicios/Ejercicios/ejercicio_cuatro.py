'''La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.

Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.

Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.'''


importe_total = 0
importe_total_bruto = 0
importe_con_descuento = 0

cantidad_tipo_vegetal = 0
cantidad_tipo_animal = 0
cantidad_tipo_mezcla = 0

vegetal_mas_caro = 0
animal_mas_caro = 0
mezcla_mas_caro = 0

peso_total = 0

for i in range(15):
    print("\nComience aqui debajo su compra")
    
    peso = float(input("Ingrese peso (entre 10 y 100 kilos): "))
    while peso < 10 or peso > 100:
        peso = float(input("Ingrese peso (entre 10 y 100 kilos): "))
    
    precio_por_kilo = float(input("Ingrese el precio por kilo (mayor a 0): "))
    while precio_por_kilo < 1:
        precio_por_kilo = float(input("Ingrese un precio mayor a 0: "))
        
    tipo = str(input("Ingrese tipo (vegetal, animal, mezcla): "))
    while tipo != "vegetal" and tipo != "animal" and tipo != "mezcla":
        tipo = str(input("Ingrese tipo (vegetal, animal, mezcla): "))
    
    importe_total = peso * precio_por_kilo
    importe_total_bruto += importe_total
    
    
    if tipo == "vegetal":
        cantidad_tipo_vegetal += peso
        if precio_por_kilo > vegetal_mas_caro:
            vegetal_mas_caro = precio_por_kilo
    elif tipo == "animal":
        cantidad_tipo_animal += peso
        if precio_por_kilo > animal_mas_caro:
            animal_mas_caro = precio_por_kilo
    elif tipo == "mezcla":
        cantidad_tipo_mezcla += peso
        if precio_por_kilo > mezcla_mas_caro:
            mezcla_mas_caro = precio_por_kilo
    
    #Actualizo el valor del peso total
    peso_total += peso
    
if peso_total > 100:
        importe_con_descuento = importe_total_bruto * 0.15
elif peso_total > 300:
    importe_con_descuento = importe_total_bruto * 0.25
    
print(f"El importe bruto total a pagar es: ${importe_total_bruto}")

if importe_con_descuento > 0:
    print(f"El importe con descuento es: ${importe_con_descuento}")

if vegetal_mas_caro > animal_mas_caro and vegetal_mas_caro > mezcla_mas_caro:
    print("El alimento mas caro es el vegetal")
elif animal_mas_caro > vegetal_mas_caro and animal_mas_caro > mezcla_mas_caro:
    print("El alimento mas caro es el animal")
elif mezcla_mas_caro > animal_mas_caro and mezcla_mas_caro > vegetal_mas_caro:
    print("El alimento mas caro es la mezcla")

print("El promedio de precio por kilo en total es: $", importe_total_bruto / peso_total)
