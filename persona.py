class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años ")
