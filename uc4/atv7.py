class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def Raio(self):
        self.raio = float(input("Insira o raio do círculo: "))
        print(f"Raio: {self.raio}")
    def Area(self):
        area = (3.14 * (self.raio ** 2))
        print(f"Área: {area}")
    def Circunferencia(self):
        circ = (2 * self.raio * 3.14)
        print(f"Circunferência: {circ}")
circulo1 = Circulo(0)
circulo1.Raio()
circulo1.Area()
circulo1.Circunferencia()