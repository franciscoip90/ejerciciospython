class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    
    def acelerar(self, incremento):
        self.velocidad +=incremento
        print(f"El {self.marca} {self.modelo} esta acelerando. velocidad actual: {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"el {self.marca} {self.modelo} esta frenando. velocidad actual: {self.velocidad} km/h")