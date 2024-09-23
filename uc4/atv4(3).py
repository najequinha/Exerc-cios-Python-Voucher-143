class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def enterN1(self):
        self.nota1 = float(input("Digite a primeira nota do aluno: "))
        print(f"Nota 1: {self.nota1}")
    def enterN2(self):
        self.nota2 = float(input("Digite a segunda nota do aluno: "))
        print(f"Nota 2: {self.nota2}")
    def enterN3(self):
        self.nota3 = float(input("Digite a terceira nota do aluno: "))
        print(f"Nota 3: {self.nota3}")
    def nomeA(self):
        self.nome = (input("Digite o nome do aluno: ").upper())
        print(f"Nome do aluno: {self.nome}")
    def mRA(self):
        self.ra = int(input("Digite a matrícula(RA) do aluno: "))
        print(f"RA: {self.ra}")
    def somaN(self):
        mediasimples = (self.nota1+self.nota2+self.nota3)/3
        if mediasimples >= 7:
            print(f"Média: {mediasimples} - APROVADO")
        elif mediasimples >= 5:
            print(f"Média: {mediasimples} - EXAME")
        else:
            print(f"Média: {mediasimples} - REPROVADO")
aluno1 = Aluno("Nome", "Ra", 0, 0, 0)
aluno1.nomeA()
aluno1.mRA()
aluno1.enterN1()
aluno1.enterN2()
aluno1.enterN3()
aluno1.somaN()