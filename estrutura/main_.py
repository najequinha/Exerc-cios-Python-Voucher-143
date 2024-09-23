from agendamento import Agendamento
from agendamento2 import Agendamento2
def Menu():
    print("1. Agendar atendimento\n2. Cancelar atendimento\n3. Visualizar agendamentos\n4. Sair ")
agendamentos = Agendamento2()
while True:
    Menu()
    op = int(input("Qual operação gostaria de realizar?: "))
    if op == 1:
        try:
            nome = input("Cliente, insira seu nome: ")
            data = input("Selecione a data desejada: ")
            hora = input("Informe o horário: ")
            servico = input("Insira o serviço: ")
            agndmt = Agendamento(f"Nome: {nome}", f"Data: {data}", f"Hora: {hora}", f"Serviço: {servico}")
            agendamentos.Agendar(agndmt)
        except Exception as e:
            print(e)
    elif op == 2:
        try:
            servico = input("O agendamento de qual serviço gostaria de cancelar? ")
            agendamentos.Cancelar(f"Serviço: {servico}")
        except Exception as e:
            print(e)
    elif op == 3:
        agendamentos.VisualizarAgendamentos()
    elif op == 4:
        certeza = input("Tem certeza de que deseja sair?: ").capitalize()
        if certeza == "Sim":
            break
        else:
            continue
    else:
        continue
