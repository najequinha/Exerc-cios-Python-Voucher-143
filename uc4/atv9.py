class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def Informacoes(self):
        self.ladoA = float(input("Digite o comprimento do lado A: "))
        print(f"Lado A: {self.ladoA}")
        self.ladoB = float(input("Digite o comprimento do lado B: "))
        print(f"Lado B: {self.ladoB}")
        self.ladoC = float(input("Digite o comprimento do lado C: "))
        print(f"Lado C: {self.ladoC}")
    def Calcular_Perimetro(self):
        perimetro = (self.ladoA + self.ladoB + self.ladoC)
        print(f"Perímetro: {perimetro}")
    def Maior_Lado(self):
        lados = [self.ladoA, self.ladoB, self.ladoC]
        maiorlado = max(lados)
        print(f"Maior lado: {maiorlado}")
triangulo1 = Triangulo(0, 0, 0)
triangulo1.Informacoes()
triangulo1.Calcular_Perimetro()
triangulo1.Maior_Lado()