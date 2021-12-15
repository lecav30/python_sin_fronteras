# Input #
# Es la función utilizada para solicitar datos al usuario

dato = input('Ingrese dato: ')
print(dato)

lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

if lista.count(dato) > 0:
    print('El dato existe:', dato)
else:
    print('El dato no existe:', dato)
