import random
class Cartela:
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        self.fileira = fileira
        self.qtd_n = qtd_n
        self.numeros_da_cartela = numeros_da_cartela
        self.numeros_disp = numeros_disp
    def numeros_de_uma_fileira(self):
        self.fileira = input("Fileira: ")
        self.qtd_n = int(input("Quantidade de números: "))
        self.numeros_disp = list(range(1,16))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
    def Numero_Sorteado(self):
        n_sort = int(input("Insira o número sorteado: "))
        for i in self.numeros_da_cartela:
            if n_sort == i:
                self.numeros_da_cartela.remove(i)
                print(self.numeros_da_cartela)
            else:
                continue
class FileiraB(Cartela):
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        super().__init__(fileira, qtd_n, numeros_da_cartela, numeros_disp)
    def numeros_de_uma_fileira(self):
        self.fileira = "B"
        self.qtd_n = 5
        self.numeros_disp = list(range(1,16))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
class FileiraI(Cartela):
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        super().__init__(fileira, qtd_n, numeros_da_cartela, numeros_disp)
    def numeros_de_uma_fileira(self):
        self.fileira = "I"
        self.qtd_n = 5
        self.numeros_disp = list(range(16, 31))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
class FileiraN(Cartela):
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        super().__init__(fileira, qtd_n, numeros_da_cartela, numeros_disp)
    def numeros_de_uma_fileira(self):
        self.fileira = "N"
        self.qtd_n = 4
        self.numeros_disp = list(range(31, 46))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
class FileiraG(Cartela):
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        super().__init__(fileira, qtd_n, numeros_da_cartela, numeros_disp)
    def numeros_de_uma_fileira(self):
        self.fileira = "G"
        self.qtd_n = 5
        self.numeros_disp = list(range(46, 61))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
class FileiraO(Cartela):
    def __init__(self, fileira, qtd_n, numeros_da_cartela, numeros_disp):
        super().__init__(fileira, qtd_n, numeros_da_cartela, numeros_disp)
    def numeros_de_uma_fileira(self):
        self.fileira = "O"
        self.qtd_n = 5
        self.numeros_disp = list(range(61, 76))
        self.numeros_da_cartela = []
        for i in range(self.qtd_n):
            n_aleatorio = random.choice(self.numeros_disp)
            self.numeros_disp.remove(n_aleatorio)
            self.numeros_da_cartela.append(n_aleatorio)
        print(self.numeros_da_cartela)
fileira_b1 = FileiraB("", 0, 0, 0)
fileira_i1 = FileiraI("", 0, 0, 0)
fileira_n1 = FileiraN("", 0, 0, 0)
fileira_g1 = FileiraG("", 0, 0, 0)
fileira_o1 = FileiraO("", 0, 0, 0)
print(f"Cartela:\nB: {fileira_b1.numeros_de_uma_fileira()}\nI: {fileira_i1.numeros_de_uma_fileira()}\nN: {fileira_n1.numeros_de_uma_fileira()}\nG: {fileira_g1.numeros_de_uma_fileira()}\nO: {fileira_o1.numeros_de_uma_fileira()}")