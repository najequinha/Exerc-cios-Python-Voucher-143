class Conta_Corrente:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero 
        self.saldo = saldo
    def nomeC(self):
        self.nome = (input("Digite o nome do cliente: ").upper())
        print(f"Nome: {self.nome}")
    def cpfC(self):
        self.cpf = int(input("Digite o CPF do cliente: "))
        print(f"CPF: {self.cpf}")
    def depositar(self):
        self.saldo+= float(input("Digite o valor que gostaria de depositar: "))
        print(f"Saldo atual: {self.saldo}")
    def sacar(self):
        valor = float(input("Digite o valor que gostaria de sacar: "))
        if self.saldo >= valor:
            self.saldo-=valor
            print(f"Transação aprovada! Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente. Operação cancelada.")
    def impSaldo(self):
        print(f"Imprimindo saldo: {self.saldo}")
conta1 = Conta_Corrente("Nome", "CPF", 0, 0)
conta1.nomeC()
conta1.cpfC()
conta1.depositar()
conta1.sacar()
conta1.impSaldo()
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