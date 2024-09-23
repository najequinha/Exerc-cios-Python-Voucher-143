class Agendamento:
    def __init__(self, data, hora, servico, agendamentos, listadeservicos):
        self.data = data
        self.hora = hora
        self.servico = servico
        self.agendamentos = []
        self.listadeservicos = []
    def Agendar(self):
        agendamento = []
        self.data = input("Insira a data desejada: ")
        self.hora = input("Digite a hora desejada: ")
        self.servico = input("Determine o serviço: ")
        agendamento.append(self.data)
        agendamento.append(self.hora)
        agendamento.append(self.servico)
        self.agendamentos.append(agendamento)
        print(f"Agendamento feito com sucesso!\n{agendamento}")
    def ArmazenamentoDeAgendamentos(self):
        return self.agendamentos
    def Cancelar(self):
        self.VisualizarAgendamentos()
        # for i in self.agendamentos:
        #     print(i)
        qual = input("O agendamento de qual serviço gostaria de cancelar? ")
        for listas in self.agendamentos:
            for item in listas:
                if qual == item:
                    print(f"{listas} cancelado com sucesso!")
                    self.agendamentos.remove(listas)
    def __str__(self):
        return (f"{self.agendamentos}")
    def VisualizarAgendamentos(self):
        print("Mostrando agendamentos:")
        print(self.agendamentos)
    def Menu(self):
        print("1. Agendar atendimento\n2. Cancelar atendimento\n3. Visualizar agendamentos\n4. Sair ")
agendar = Agendamento("", "", "", "", "")
agendar.ArmazenamentoDeAgendamentos()
while True:
    try:
        agendar.Menu()
        op = int(input("Qual operação gostaria de realizar?: "))
        if op == 1:
            agendar.Agendar()
        elif op == 2:
            agendar.Cancelar()
        elif op == 3:
            agendar.VisualizarAgendamentos()
        elif op == 4:
            break
        else:
            continue
    except Exception as e:
        print(e)