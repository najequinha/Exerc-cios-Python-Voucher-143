class Filme:
    def __init__(self, nome, duracao, status):
        self.nome = nome
        self.duracao = duracao
        self.status = status
    def Atributos(self):
        self.nome = input("Nome: ")
        self.duracao = int(input("Duração (em minutos): "))
        self.status = 0
    def Play(self):
        if self.status == 0:
            self.status = 1
            print ("Play")
        else:
            self.status = 1
            print ("Filme já em reprodução")
class Ação(Filme):
    def __init__(self, nome, duracao, status):
        super().__init__(nome, duracao, status)
    def som(self):
        print("BOOM!!!!")
class Drama(Filme):
    def __init__(self, nome, duracao, status):
        super().__init__(nome, duracao, status)
    def som(self):
        print("*choro*")
class Suspense(Filme):
    def __init__(self, nome, duracao, status):
        super().__init__(nome, duracao, status)
    def som(self):
        print("*medo*")
filme1 = Filme("", 0, 0)
filme1.Atributos()
filme1.Play()
filme_acao = Ação("", 0, 0)
filme_acao.som()    
filme_drama = Drama("", 0, 0)
filme_drama.som()
filme_suspense = Suspense("", 0, 0)
filme_suspense.som()    