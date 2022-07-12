# Creación de una clase:
class Dog:
    # Creación del constructor:
    def __init__(self, name):
        # Creación de un atributo:
        # self.name = name

        # --- Encapsulamiento ---
        # Encapsulamiento: Guardar, proteger o limitar el acceso de ciertos
        # atributos y/o propiedades en nuestros objetos
        self.__name = name

    # Creación de un método:
    def get_name(self):
        return "El nombre del perro es: " + self.__name


# --- Herencia ---
# Herencia: Una clase denominada "clase hija" tendrá los atributos y métodos
# de una clase denominada "clase padre"
# class clase_hija(clase_padre):
class Bulldog(Dog):
    # Elementos estáticos:
    max_height = 40

    # Utilizar constructor de la clase padre:
    # def __init__(self, atributo_clase_padre, atributo_clase_hijo):
    def __init__(self, name, pedigree, type):
        # Invocar al padre:
        # Nota: Si no se invoca al constructor padre, cuando se use
        # alguno de los métodos del padre saltará un error
        super().__init__(name)
        self.pedigree = pedigree
        self.type = type

    # --- Polimorfismo ----
    # Polimorfismo: Se puede modificar los métodos de la clase padre
    # para que realicen otras acciones

    # Sobreescribir un método:
    # def get_name(self):
    #     return "El perro es un Bulldog " + self.type

    # Reutilizar el método del padre:
    def get_name(self):
        return super().get_name() + ". Además, el perro es un Bulldog " + self.type

    # Método estático:
    @staticmethod
    def get_max_height():
        return "La máxima altura de un Bulldog es de " + str(Bulldog.max_height) + "cm"


class Service_dog:
    def __init__(self, role, years_of_service):
        self.role = role
        self.years_of_service = years_of_service

    # Parámetros opcionales
    def about_dog(self, info=""):
        return (
            info
            + "Rol: "
            + self.role
            + " - Años de servicio: "
            + str(self.years_of_service)
        )


# --- Multiherencia ---
# Multiherencia: Al igual que la herencia permite heredar atributos y métodos de la clase padre.
# Sin embargo, en este caso será de muchas clases. Cabe resaltar que esto es solo posible en Python
class Labrador(Dog, Service_dog):
    def __init__(self, name, role, years_of_service, color):
        Dog.__init__(self, name)
        Service_dog.__init__(self, role, years_of_service)
        self.__color = color


# Creación de un objeto:
dog1 = Dog("Spike")
print(dog1.get_name())

# Sin encapsulamiento:
# print(dog1.name)

# Creación de un objeto con Herencia:
bulldog1 = Bulldog("Rufus", True, "Inglés")
print(bulldog1.get_name())

# Elementos y métodos estáticos
# No se requiere crear un objeto para acceder a esos datos, debido a que
# es un atributo/método de la clase y no del objeto
print(Bulldog.max_height)
print(Bulldog.get_max_height())

labrador1 = Labrador("Chocolate", "Rescatista", 4, "Marrón")
print(labrador1.get_name())
print(labrador1.about_dog())
print(labrador1.about_dog("Rescates realizados: 80 - "))


# Referencia: https://www.youtube.com/watch?v=Z3XYBjQjZ9g
