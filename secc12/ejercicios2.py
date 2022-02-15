# Ejercicio 1 #
# Multiplicar dos números sin usar el símbolo de la multiplicación

# n1 = int(input('Ingrese el primer número: '))
# n2 = int(input('Ingrese el primer número: '))

# n1 = 4
# n2 = 8
# resultado = 0

# for i in range(n2):
#     resultado += n1

# print(resultado)


# Ejercicio 2 #
# Ingresar un nombre y apellido y escribirlo al revés

# nombre = 'Chanchito'
# apellido = 'Feliz'

# nombre_completo = nombre + ' ' + apellido

# # Forma 1
# for i in range(len(nombre_completo) - 1, -1, -1):
#     print(nombre_completo[i], end = '')

# # Forma 2
# # Operación de slice:
# print(nombre_completo[::-1])


# Ejercicio 3 #
# Encontrar una función que encuentre el menor elemento de una lista

# lista = [1, 2, 55, -24, -13, 23]

# def menor_valor(lista):
#     menor = lista[0]
#     # for i in range(1, len(lista)):
#     #     if menor >= lista[i]:
#     #         menor = lista[i]
#     for x in lista:
#         if menor >= x:
#             menor = x
#     return menor

# def menor_valor_sv(lista):
#     menor = 'init'
#     for x in lista:
#         if menor == 'init':
#             menor = x
#         else:
#             menor = x if x < menor else menor
#     return menor

# print(menor_valor(lista))
# print(menor_valor_sv(lista))


# Ejercicio 3 #
