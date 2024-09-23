class Agendamento2:
    def __init__(self):
        self.agendamentos = []
    def Agendar(self, agendamento):
        self.agendamentos.append(agendamento)
        print(f"Agendamento feito com sucesso!\n{agendamento}")
    def __str__(self):
        return (f"{self.agendamentos}")
    def VisualizarAgendamentos(self):
        print("Mostrando agendamentos:")
        for i in self.agendamentos:
            print(i)
    def BuscarLivro(self, titulo):
        for lupa in self.livros:
            if lupa.titulo == titulo:
                return lupa
    def BuscarServico(self, servico):
        for lupa in self.agendamentos:
            if lupa.servico == servico:
                return lupa
    def Cancelar(self, servico):
        try:
            verdade = self.BuscarServico(servico)
            if verdade:
                self.agendamentos.remove(verdade)
                print(f"Agendamento cancelado com sucesso!")
                for i in self.agendamentos:
                    print(i)
        except Exception as e:
            print(e)