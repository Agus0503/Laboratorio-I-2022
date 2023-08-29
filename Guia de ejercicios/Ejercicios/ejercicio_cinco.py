'''Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento
de HR dispone de lista de justicieros pero solo tiene información detallada de algunos de
ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista
heroes_info se puedan listar los datos de cada héroe con el siguiente formato: (ver foto pdf)
TIP: Las habilidades están repetidas, buscá la manera de que en el resultado final no existan
duplicados, que usarías para eso?'''

heroes_info = [
{"Nombre" : "Super Girl", "ID" : 1, "Origen" : "Krypton", 
 "Habilidades" : ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
 "Identidad" : "Kara Zor-El"},
{"Nombre" : "Shazam", "ID" : 25, "Origen" : "Tierra",
 "Habilidades" : ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
 "Identidad" : "Billy Batson",},
{"Nombre" : "Power Girl", "ID" : 14, "Origen" : "Krypton",
 "Habilidades" : ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
 "Identidad" : "Karen Starr"},
{"Nombre" : "Wonder Woman", "ID" : 29, "Origen" : "Amazonia",
 "Habilidades" : ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
 "Identidad" : "Diana Prince"}
]

for key in heroes_info:
    nombre = key["Nombre"]
    Id = key["ID"]
    origen = key["Origen"]
    identidad = key["Identidad"]
    print(f"Id: {Id}, Nombre: {nombre} \nIdentidad: {identidad}, Origen: {origen}")
    
    habilidades_sin_repetir = set(key["Habilidades"]) #Creo un set de habilidades para descartar las habilidades repetidas
    habilidades = " " #Declaro variable para almacenar la habilidad recibida
    for habilidad in habilidades_sin_repetir: 
        habilidades += habilidad + " | " #"Guardo" la habilidad en la variable y concateno con "|" para el muestreo solicitado
    print(f"Habilidades: {habilidades} ") #Muestro las habilidades sin repetir y con el formato indicado
    print("----------------------------------\n")