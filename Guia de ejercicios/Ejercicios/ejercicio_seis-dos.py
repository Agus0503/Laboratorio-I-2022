'''La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.'''

diccionario = []

while True:
    palabra = input("Ingrese una palabra en español: ")
    
    indice = -1
    for i in range(len(diccionario)):
        if diccionario[i][0] == palabra: # Verifico si la palabra ya existe en el diccionario
            indice = i
            break
        
    if indice != -1:
        print(f"La palabra '{palabra}' ya existe en el diccionario con índice {indice+1}")
    else:
        traduccion = input(f"Ingrese la traducción de '{palabra}' al inglés: ")
        diccionario.append([palabra, traduccion])
    
    confirmacion = input("Desea ingresar otra palabra? (s/n): ")
    while confirmacion != 's' and confirmacion != 'n':
        confirmacion = input("Porfavor ingrese una opcion valida,desea ingresar otra palabra? (s/n): ")
    # Si el usuario ingresa "s", se rompe el ciclo y se muestra el diccionario completo
    if confirmacion == "n":
        break

# Muestro el diccionario completo
print("\nDiccionario completo:")
for i in range(len(diccionario)):
    print(f"Esp:{diccionario[i][0]} -> Ing:{diccionario[i][1]}")


'''Cuando utilizo [i][0] o [i][1] hago referencia al indice con "i" y con subindice 0 accedo a palabra en español,
y con subindice 1 accedo a palabra en ingles, ya que el usar append, estoy agregando a la lista diccionario, "sublistas" de 2 elementos
siendo esos palabra en español[0] y palabra en ingles[1]'''