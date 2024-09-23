class Funcionario:
    def __init__(self, nome, sobrenome, horas_t, valor_hora, valor_pago):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_t = horas_t
        self.valor_hora = valor_hora
        self.valor_pago = valor_pago
    def Nome(self):
        self.nome = (input("Digite seu nome: ").capitalize())
    def Sobrenome(self):
        self.sobrenome = (input("Digite seu sobrenome: ").capitalize())
    def Nome_Completo(self):
        print(f"{self.nome} {self.sobrenome}")
    def Horas_Trabalhadas(self):
        self.horas_t = int(input("Digite as horas trabalhadas: "))
        print(f"Horas trabalhadas: {self.horas_t}")
    def Valor_Hora(self):
        self.valor_hora = float(input("Digite o valor de cada hora: "))
        print(f"Horas trabalhadas: {self.horas_t}")
    def Adicionar_Horas(self):
        self.horas_t = int(input("Digite as horas a mais trabalhadas: "))
    def Valor_A_Ser_Pago(self):
        self.valor_pago = self.horas_t * self.valor_hora
        print(f"Valor: {self.valor_pago}")
    def Valor_A_Mais_A_Ser_Pago(self):
        self.valor_pago+= self.horas_t * self.valor_hora
        print(f"Valor: {self.valor_pago}")
funcionario1 = Funcionario("", "", 0, 0, 0)
funcionario1.Nome()
funcionario1.Sobrenome()
funcionario1.Nome_Completo()
funcionario1.Horas_Trabalhadas()
funcionario1.Valor_Hora()
funcionario1.Valor_A_Ser_Pago()
funcionario1.Adicionar_Horas()
funcionario1.Valor_A_Mais_A_Ser_Pago()