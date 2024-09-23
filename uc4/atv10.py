class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    def Informacoes_do_aluno(self):
        self.nome = input("Insira seu nome: ")
        self.idade = int(input("Insira sua idade: "))
        self.peso = float(input("Insira seu peso: "))
        self.altura = float(input("Insira sua altura: "))
        self.altura = self.altura/100
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}m")
    def Obter_valor_mensalidade(self):
        if self.idade <= 18:
            self.mensalidade = (self.mensalidade * 0.8)
            print(f"Parabéns! Você acabou de ganhar 20% de desconto na sua mensalidade. Valor da sua mensalidade: {self.mensalidade}")
        else:
            print(f"Mensalidade: {self.mensalidade}")
    def Calcular_IMC(self):
        imc = (self.peso/(self.altura*self.altura))
        print(f"Seu imc é: {imc}")
aluno1 = Aluno_Academia("", "", "", "", 120)
aluno1.Informacoes_do_aluno()
aluno1.Obter_valor_mensalidade()
aluno1.Calcular_IMC()