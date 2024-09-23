import random
class Sorteio_Bingo:
    def __init__(self, numeros_sorteados, numeros_disp, n_aleatorio, op):
        self.numeros_sorteados = numeros_sorteados
        self.numeros_disp = numeros_disp
        self.n_aleatorio = n_aleatorio
        self.op = op
    def Sortear_Numero(self):
        self.numeros_sorteados = []
        self.numeros_disp = list(range(1,76))
        while len(self.numeros_disp)> 0:
            self.n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(self.n_aleatorio)
            self.numeros_sorteados.append(self.n_aleatorio)
            print(f"Números sorteados: {self.numeros_sorteados}")
            self.op = int(input("Digite 1 para continuar e 2 para parar: "))
            if self.op == 2:
                break
            else:
                continue
inicio_sorteio = Sorteio_Bingo(0, 0, 0, 0)
inicio_sorteio.Sortear_Numero()