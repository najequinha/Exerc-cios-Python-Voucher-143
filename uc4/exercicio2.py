class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas, media):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = media
    def Atributos(self):
        self.matricula = int(input("Matrícula: "))
        self.nome = input("Nome: ")
        self.idade = int(input("Idade: "))
    def Notas_e_media(self):
        self.notas = []
        nota1 = float(input("Nota 1: "))
        self.notas.append(nota1)
        nota2 = float(input("Nota 2: "))
        self.notas.append(nota2)
        self.media = (nota1+nota2)/2
        print(f"Média: {self.media}")
    def Estudar(self):
        print("Vá estudar!")
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga = carga
        self.salario = salario
    def Atributos(self):
        self.matricula = int(input("Matrícula: "))
        self.nome = input("Nome: ")
        self.idade = int(input("Idade: "))
        self.formacao = input("Formação: ")
        self.disciplina = input("Disciplina: ")
        self.carga = int(input("Carga horária: "))
        self.salario = float(input("Salário: "))
    def Lecionar(self):
        print("Vá lecionar!")
aluno1 = Aluno(0, "", "", 0, 0)
aluno1.Atributos()
aluno1.Notas_e_media()
aluno1.Estudar()
professor1 = Professor(0, "", "", "", "", 0, 0)
professor1.Atributos()
professor1.Lecionar()