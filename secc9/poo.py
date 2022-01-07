# La convención en todos los lenguajes de programación es escribir
# la primera letra en mayúscula

# El __init__ es su constructor y el self seria el this
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    # nombre = "Jose"
    # apellido = 'Garcia'

usuario = Usuario('Jose', 'Garcia')
usuario2 = Usuario('Lalo', 'Lecav')

print(usuario.nombre, usuario.apellido)

print(usuario2.nombre, usuario2.apellido)


