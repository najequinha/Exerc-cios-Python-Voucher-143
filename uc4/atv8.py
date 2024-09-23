class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    def Validar_Data(self):
        while True:
            self.dia = int(input("Insira o dia: "))
            if self.dia < 1 or self.dia > 31:
                print("Inválido")
                continue
            else:
                print(f"Dia: {self.dia}")
            self.mes = int(input("Insira o mês: "))
            if self.mes < 1 or self.mes > 12:
                print("Inválido:")
                continue
            if (self.mes == 2 and self.dia > 29) or (self.mes == 4 and self.dia > 30) or (self.mes == 6 and self.dia > 30) or (self.mes == 9 and self.dia > 30) or (self.mes == 11 and self.dia > 30):
                print("Inválido.")
                continue
            else:
                print(f"Mês: {self.mes}")
            self.ano = int(input("Insira o ano: "))
            if self.ano>2024:
                print("Inválido")
                continue
            else:
                print(f"Ano: {self.ano}")
                break
    def Anotacao(self):
        self.anotacao = input("Digite a anotação aqui: ")
        print(f"Anotação({self.dia}/{self.mes}/{self.ano}): {self.anotacao}")
anotacao1 = Agenda(0, 0, 0, "")
anotacao1.Validar_Data()
anotacao1.Anotacao()