'''Desafio 02
Diego Agustin Ostua Larramendia, 1D
'''
from os import system
from data_stark import lista_personajes

def stark_normalizar_datos(lista:list):
    """_summary_
        Normalizo/Convierto los datos correspondientes segun el valor encontrado de la lista que recibo por parametro
    Args:
        lista (list): recibo la lista de diccionario como parametro para normalizar sus datos
    """    
    bandera = False
    if len(lista) > 0:
        for diccionario in lista:
            for clave in diccionario.keys():
                if type(diccionario[clave]) != float and type(diccionario[clave]) != int:
                    if is_int(diccionario[clave]):
                        diccionario[clave] = int(diccionario[clave])
                        bandera = True
                    elif is_float(diccionario[clave]):
                        diccionario[clave] = float(diccionario[clave])
                        bandera = True
    else:
        print("ERROR, La lista esta vacia")
        
    if bandera:
        print("Datos Normalizados")


def obtener_nombre(heroe:dict):
    """_summary_
        Obtengo y devuelvo el nombre del heroe que recibe como parametro
    Args:
        heroe (dict): diccionario de un personaje en especifico
    Returns:
        str: el valor 'nombre' del heroe 
    """    
    nombre = heroe.get('nombre')                
    
    return nombre 

def imprimir_dato(string:str):
    """_summary_
        Recibo por parámetro un string y lo imprimo en la consola
    Args:
        string (str): tipo de dato string
    """    
    print(string)


def stark_imprimir_nombres_heroes(lista:list):
    """_summary_
        Recibo por parámetro la lista de héroes y la imprimo en la consola
    Args:
        lista (list): lista de diccionario
    """    
    if len(lista) > 0:    
        for personaje in lista:
            imprimir_dato(f"Nombre: {obtener_nombre(personaje)}")
    else:
        return -1

def obtener_nombre_y_dato(diccionario:dict, key:str):
    """_summary_
        Recibe por parámetro un diccionario (el cual representara a un héroe) y una key (string) la cual
        representa el dato que se desea obtener.
    Args:
        diccionario (dict)
        key (str)

    Returns:
        str: devuelvo tanto el nombre como el dato(key) recibido del diccionario que recibo por parametro
    """    
    if key in diccionario:
        nombre = obtener_nombre(diccionario)
        dato = diccionario.get(key)
    
    string_resultante = f"Nombre: {nombre:20s} | {key:>10}: {dato}"

    return string_resultante

def stark_imprimir_nombres_alturas(lista:list):
    """_summary_
        Recibe por parámetro la lista de héroes, e imprime sus nombres y alturas USANDO la función creada en el punto 2.
    Args:
        lista (list): lista de personajes
    Returns:
        int: -1 si la lista esta vacia
              1 si se pudo realizar
    """
    retorno = 0    
    if len(lista) > 0:
        for diccionario in lista:
            print(obtener_nombre_y_dato(diccionario,'altura'))
    else:
        retorno = -1
        
    return retorno
        

def calcular_max(lista:list, key:str):
    """_summary_
        Determinar cuál es el valor máximo de la lista que recibe por parametro
    Args:
        lista (list): lista que contiene los diccionarios
        key (str): clave de la cual se requiere conocer el maximo

    Returns:
        dict: diccionario con los datos del heroe junto con el dato mayor solicitado
    """    
    maximo = {}
    
    if len(lista) > 0:
        for diccionario in lista:
            if key in diccionario:
                valor = diccionario[key]
                if isinstance(valor,(int, float)):
                    if not maximo or valor > maximo[key]:
                        maximo = diccionario
                else:
                    print("Error, la clave ingresada no contiene un valor numerico")
                    break
    else:
        print("Error, la lista esta vacia")

    if maximo:
        return maximo


def calcular_min(lista:list, key:str):
    """_summary_
        Determinar cuál es el valor minimo de la lista que recibe por parametro
    Args:
        lista (list): lista que contiene los heroes
        key (str): clave de la cual se requiere conocer el minimo

    Returns:
        dict: diccionario con los datos del heroe junto con el dato mayor solicitado
    """    
    minimo = {}

    if len(lista) > 0:
        for diccionario in lista:
            if key in diccionario:
                valor = diccionario[key]
                if isinstance(valor,(int, float)):
                    if not minimo or valor < minimo[key]:
                        minimo = diccionario
                else:
                    print("Error, la clave ingresada no contiene un valor numerico")
                    break
    else:
        print("Error, la lista esta vacia")

    if minimo:
        return minimo

def calcular_max_min_dato(lista:list, calculo:str, key:str):
    """_summary_
        Recibe una lista, tipo de calculo, y una key para devolver el valor solitado
    Args:
        lista (list): lista que contiene los heroes
        calculo (str): filtro entre maximo y minimo segun se requiere
        key (str): clave de la cual se requiere conocer el minimo/maximo

    Returns:
        dict: heroe(segun maximo o minimo)
    """    
    if len(lista) > 0:
        calculo = calculo.lower()
        if calculo == 'maximo':
            maximo = calcular_max(lista,key)
            return maximo
        elif calculo == 'minimo':
            minimo = calcular_min(lista,key)
            return minimo
        else:
            print("Error, el tipo de calculo ingresado es incorrecto")
    else:
        print("Error, la lista esta vacia")
        

def stark_calcular_imprimir_heroe(lista:list, calculo:str, key:str):
    """_summary_
        Imprime Nombre del heroe y calcula el dato segun el criterio solicitado de la lista
    Args:
        lista (list): lista que contiene los heroes
        calculo (str): criterio maximo o minimo
        key (str): clave de la cual se requiere conocer el dato
    """    
    if len(lista) > 0:
        personaje = calcular_max_min_dato(lista,calculo,key)        
        
        if calculo == 'maximo':
            print(f"Mayor {key}: Nombre: {personaje['nombre']} | {key}: {personaje[key]}")
        elif calculo == 'minimo':
            print(f"Menor {key}: Nombre: {personaje['nombre']} | {key}: {personaje[key]}")
    else:
        print("Error, la lista esta vacia")
        return -1
        

def sumar_dato_heroe(lista:list, key:str):
    """_summary_
        Recibe como parámetro una lista un string que representara la key del dato que se requiere sumar
    Args:
        lista (list): lista que contiene los heroes
        key (str): clave de la cual se requiere conocer la suma de ese dato
    Returns:
        int/float: devuelvo la suma de los datos solicitados
    """    
    suma = 0
    
    if len(lista) > 0:
        clave_encontrada = False
        for personaje in lista:
            if type(personaje) == dict and personaje is not None:
                for dato in personaje:
                    if dato == key:
                        clave_encontrada = True
                        if type(personaje[dato]) == int or type(personaje[dato]) == float:
                            suma += personaje[dato]
        if not clave_encontrada:
            print("La clave ingresada no existe")
    else:
        print("Error, la lista esta vacia")
        
    return suma


def dividir(dividendo, divisor):
    """_summary_
        Recibe divisor y diviendo para realizar la operacion
    Args:
        dividendo (float)
        divisor (float)
    Returns:
        float: resultado de la division
    """    
    if divisor == 0:
        return 0
    else:
        division = dividendo / divisor
    
    return division


def calcular_promedio(lista:list, key:str):
    """_summary_
        Recibe como parámetro una lista y un string que representa el dato del héroe que se requiere calcular el promedio
    Args:
        lista (list): lista que contiene los heroes
        key (str): clave de la cual se requiere conocer el promedio de ese dato

    Returns:
        float: promedio solicitado
    """
    suma = sumar_dato_heroe(lista,key)
    promedio = dividir(suma,len(lista))
    
    return promedio
        
def stark_calcular_imprimir_promedio_altura(lista:list):
    """_summary_
        Determina la altura promedio de la lista recibida por parametro
    Args:
        lista (list): lista que contiene los heroes
    Returns:
        int: -1 en caso de la lista estar vacia
    """    
    if len(lista) > 0:
        altura_promedio = calcular_promedio(lista,'altura')
        if altura_promedio > 0:
            imprimir_dato(f"La altura promedio es: {round(altura_promedio, 2)}")
    else:
        print("Error, la lista esta vacia")  
        return -1
    

def validar_entero(numero_str:str):
    """_summary_
        Valida si una cadena de caracteres contiene únicamente dígitos
    Args:
        numero_str (str): numero formato string 
    Returns:
        bool: True en caso de ser entero
              False en caso de no serlo  
    """    
    if numero_str.isdigit():
        return True
    else:
        return False


def imprimir_menu():
    """_summary_
        Funcion encargada de imprimir el menu principal de opciones
    """    
    menu = ["1.Imprimir nombres heroes",
            "2.Imprimir nombres y alturas",
            "3.Calcular e imprimir max/min dato",
            "4.Calcular e imprimir promedio de altura",
            "5.Salir"]
    
    for i in range(len(menu)):
        imprimir_dato(menu[i])

'''Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
menú de opciones y le pedirá al usuario que ingrese el número de una de las
opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
funciones del ejercicio 6.1 y 6.2'''
def stark_menu_principal():
    """_summary_
        Imprime menú de opciones y pide al usuario ingresar una opcion correspondiente 
    Returns:
        int: Devuelvo la opcion ingresada o -1 en caso de ser incorrecta
    """    
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    if validar_entero(opcion):
        opcion = int(opcion)
        while opcion < 1 or opcion > 5:
                system('cls')
                imprimir_menu()
                opcion = input("Error,ingrese una opcion valida: ")
                if validar_entero(opcion):
                    opcion = int(opcion)
                else:
                    opcion = -1
        return opcion
    else:
        return -1
# --------------- Funciones Auxiliares ---------------
def is_int(numero_str):
    retorno = False

    if len(numero_str):
        if numero_str.isnumeric() or (numero_str[0] == "-" and numero_str[1:].isnumeric()):
            retorno = True
            
    return retorno

def is_float(numero_str):
    retorno = False
    cantidad_puntos = numero_str.count(".")

    if cantidad_puntos == 1:
        lista_flotante = numero_str.split(".")
        if is_int(lista_flotante[0]) and lista_flotante[1].isnumeric():
            retorno = True

    return retorno


# ------------------ BUCLE PRINCIPAL ------------------
def stark_marvel_app(lista:list):
        
    stark_normalizar_datos(lista)

    while True:
        opcion = stark_menu_principal()
    
        match opcion:
            
            case 1:
                stark_imprimir_nombres_heroes(lista)
            case 2:
                stark_imprimir_nombres_alturas(lista)
            case 3:
                stark_calcular_imprimir_heroe(lista,'minimo','altura')
            case 4:
                stark_calcular_imprimir_promedio_altura(lista)
            case 5:
                print("Programa Finalizado")
                break
        
        input("Presiona Enter para continuar...")
        system('cls')


#Llamada a funcion principal para la ejecucion del programa
stark_marvel_app(lista_personajes)