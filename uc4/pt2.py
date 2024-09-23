import random
class Cartela_Bingo:
    def __init__(self, b=0, i=0, n=0, g=0, o=0, cartela=0, diagonale1d2=0, diagonale2d1=0, bh=0, ih=0, nh=0, gh=0, oh=0, todos_os_numeros=0, op=0):
        self.b = b
        self.i = i
        self.n = n
        self.g = g
        self.o = o
        self.cartela = cartela
        self.diagonale1d2 = diagonale1d2
        self.diagonale2d1 = diagonale2d1
        self.bh = bh
        self.ih = ih
        self.nh = nh
        self.gh = gh
        self.oh = oh
        self.todos_os_numeros = todos_os_numeros
        self.op = op
    def Gerar_Cartela(self):
        self.todos_os_numeros = []
        self.b = []
        numeros = list(range(1, 16))
        for i in range(5):
            n_sort = random.choice(numeros)
            self.b.append(n_sort)
            numeros.remove(n_sort)
            self.todos_os_numeros.append(n_sort)
        self.i = []
        numeros = list(range(16, 31))
        for i in range(5):
            n_sort = random.choice(numeros)
            self.i.append(n_sort)
            numeros.remove(n_sort)
            self.todos_os_numeros.append(n_sort)
        self.n = []
        numeros = list(range(31, 46))
        for i in range(4):
            n_sort = random.choice(numeros)
            self.n.append(n_sort)
            numeros.remove(n_sort)
            self.todos_os_numeros.append(n_sort)
        self.g = []
        numeros = list(range(46, 61))
        for i in range(5):
            n_sort = random.choice(numeros)
            self.g.append(n_sort)
            numeros.remove(n_sort)
            self.todos_os_numeros.append(n_sort)
        self.o = []
        numeros = list(range(61, 76))
        for i in range(5):
            n_sort = random.choice(numeros)
            self.o.append(n_sort)
            numeros.remove(n_sort)
            self.todos_os_numeros.append(n_sort)
        self.cartela = {"B" : self.b, "I" : self.i, "N" : self.n, "G" : self.g, "O" : self.o}
        print(self.cartela)
        self.bh = [self.b[0], self.i[0], self.n[0], self.g[0], self.o[0]]
        self.ih = [self.b[1], self.i[1], self.n[1], self.g[1], self.o[1]]
        self.nh = [self.b[2], self.i[2], self.g[2], self.o[2]]
        self.gh = [self.b[3], self.i[3], self.n[2], self.g[3], self.o[3]]
        self.oh = [self.b[4], self.i[4], self.n[3], self.g[4], self.o[4]]
        self.diagonale1d2 = [self.b[0], self.i[1], self.g[3], self.o[4]]
        self.diagonale2d1 = [self.b[4], self.i[3], self.g[1], self.o[0]]
    def MarcarNumero(self):
        while True:
            n_sort = int(input("Digite o número sorteado: "))
            for i in (self.b, self.i, self.n, self.g, self.o):
                for n in i:
                    if n == n_sort:
                        n = "x"
                        print(f"Número marcado!\n{self.cartela}")
            self.op = int(input("Digite 1 para continuar e 2 para parar: "))
            if self.op == 2:
                break
            else:
                continue
    def MarcarBingo(self):
        todas_as_linhas = [self.b, self.i, self.n, self.g, self.o, self.bh, self.ih, self.nh, self.gh, self.oh, self.diagonale1d2, self.diagonale2d1]
        for a in todas_as_linhas:
            if all(a):
                print("Bingo!")
cartela1 = Cartela_Bingo()
cartela1.Gerar_Cartela()
cartela1.MarcarNumero()
cartela1.MarcarBingo()
