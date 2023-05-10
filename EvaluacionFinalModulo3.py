#para escribir comentarios en forma lineal se coloca gato adelante.
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes'] #cree una lista llamada nombres que contiene los nombres dados por el enunciado de la evaluacion.

magos = ['Harry Houdini', 'David Blaine', 'Teller'] #se crea una lista magos con algunos nombres que aparecen en la instruccion.
cientificos = ['Newton', 'Hawking', 'Einstein'] #se hace una lista cientificos con los nombres que aparecen en la instruccion.
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos] #Se utiliza una comprensión de lista para crear una nueva lista llamada otros que contiene los nombres de la lista nombres que no están en la lista magos ni en la lista cientificos.

def hacer_grandioso(): # defini una función llamada hacer_grandioso que no toma ningún argumento.
    for i in range(len(magos)): #Se inicia un bucle for que recorre los índices de la lista magos utilizando la función range()
        magos[i] = 'El gran ' + magos[i] #Se actualiza cada elemento de la lista magos en cada iteración, agregando el prefijo "El gran " al nombre del mago.

def imprimir_nombres(): #defini la función imprimir_nombres que no toma ningún argumento.
    for nombre in nombres: #Se inicia un bucle for que recorre cada elemento de la lista nombres.
        print(nombre) #Se imprime el nombre actual en cada iteración del bucle for de la función imprimir_nombres.

print("-----------------Inicio-----------------------") #separador linea de guiones para separar

print('Lista completa de nombres:') #Se imprime la cadena "Lista completa de nombres:".
imprimir_nombres() #Se llama a la función imprimir_nombres para imprimir todos los nombres de la lista nombres.
print()

hacer_grandioso() #Se llama a la función hacer_grandioso para modificar los nombres en la lista magos.

print("----------------------------------------------") #imprime linea como separador

print('Magos grandiosos:') #Se imprime la cadena  "magos grandiosos"
for mago in magos:#Se inicia un bucle for que recorre cada elemento de la lista magos.
    print(mago) #Se imprime el mago actual en cada iteración del bucle for.
print()

print("----------------------------------------------") #imprime linea como separador

print('Científicos:')#Se imprime la cadena "Científicos:".
for cientifico in cientificos: #Se inicia un bucle for que recorre cada elemento de la lista cientificos.
    print(cientifico) #Se imprime el científico
print()

print("----------------------------------------------") #imprime linea como separador

print('Otros:') #se imprime otros
for otro in otros:
    print(otro)

print("-----------------Fin-----------------------") #imprime linea para final