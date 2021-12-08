# Strings #

# Se puede usar tanto las comillas simples como las dobles

palabra = 'hola mundo' # string
oracion = 'hola mundo comilla doble'

entero = 20 # integer
con_decimales = 20.2 # float
complejo = 1j # es necesario utilizar una j al final de una variable de numero complejo

#print (palabra, oracion, entero, con_decimales, complejo)

# Listas #

#lista = [1, 2, 3] 
lista = ['Hola', 'Mundo', 'oink happy']

# Al imprimir una lista vacia solo se muestran los corchetes: []

# Para copiar una lista a otra:
lista2 = lista.copy()
# Para agregar un elemento a la lista:
lista.append(4)
# Para eliminar todos los elementos de la lista:
#lista.clear()

#print(lista, lista2)

# Para contar la cantidad de repeticiones de un elemento de la lista:
#print(lista2.count(3))
# Para contar los elementos de la lista:
#print(len(lista2))
largo_lista = len(lista)
#print(largo_lista)

# Para acceder a los elementos de la lista:
print(lista[0])
# Siempre se utilizan indices y no la posición del elemento


