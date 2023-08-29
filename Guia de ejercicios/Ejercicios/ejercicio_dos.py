'''Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”'''

numero = int(input("Ingrese un numero del 1 al 8 para obtener informacion: "))
while numero < 1 or numero > 8: 
    numero = int(input("Ingrese un numero del 1 al 8 para obtener informacion: "))
    
    
if numero == 1:
    print('''¿Cuál es el sentido?
        \nSegún Guido van Rossum, el código es leído más
        veces que escrito, por lo que resulta importante
        escribir código que no sólo funcione, sino que
        además pueda ser leído con facilidad.''')
elif numero == 2:
    print('''Según Guido van Rossum, el código es leído más veces que escrito,
          por lo que resulta importante escribir código que no sólo funcione,
          sino que además pueda ser leído con facilidad.''')
    
elif numero == 2:
    print('''¿Que es PEP?
          \nPython Enhancement Proposal es un documento que proporciona 
          información a la comunidad de Python, o que describe una nueva característica.''')
        
elif numero == 3:
    print('''¿Que es PEP8?
          \nEs un conjunto de recomendaciones cuyo objetivo es ayudar a escribir 
          código más legible y abarca desde cómo nombrar variables,
          al número máximo de caracteres que una línea debe tener.''')
    
elif numero == 4:
    print('''Indentado
        \nPython no usa {} para designar bloques de código como otros lenguajes de programación,
        sino que usa bloques identados para indicar que un determinado bloque de código
        pertenece a porejemplo un if.''')

elif numero == 5:    
    print('''Tamaño Maximo de linea
          Se recomienda limitar el tamaño de cada línea a 79 caracteres,
          para evitar tener que hacer scroll a la derecha.''')

elif numero == 6:
    print('''Líneas en blanco
          \nEl uso de espacios en blanco mejora la legibilidad del código,
          y es por lo que la PEP8 indica dónde debemos usar espacios y dónde no.''')

elif numero == 7:
    print('''Comentarios
          \nCualquier comentario que contradiga el código es peor
          que ningún comentario.Si actualizamos el código, 
          se debe actualizar los comentarios para evitar crear inconsistencias''')

elif numero == 8:
        print('''Nombres
              \nFunciones: Uso de snake_case, letras en minúscula separadas por guión bajo:
              mi_funcion.Variables: Al igual que las funciones: 
              variable,mi_variable. Clases: Uso de CamelCase, usando mayúscula y sin barra baja:
              MiClase, ClaseDePrueba.''')