#listas
pacientes = []
nomepaciente = []
cpf = []
idade = []
horario = []
cont = 0
range = -1
#login
while True:
    cod = int(input("Bem vindo(a)! Digite 1 para entrar como Paciente ou 2 para entrar como Médico: "))
    if cod == 1:
        print("Paciente, digite 1 para marcar uma nova consulta ou 2 para consultar seu histórico de consultas: ")
        op = int(input())
        if op == 1:
            cont+=1
            n = input("Paciente, digite seu nome: ")
            nomepaciente.append(n)
            c = int(input("Paciente, digite seu cpf: "))
            cpf.append(c)
            i = int(input("Paciente, digite sua idade: "))
            idade.append(i)
            h = input("Paciente, digite o horário de sua consulta: ")
            horario.append(h)
            d = {"Nome do paciente" : n, "CPF" : c, "Idade" : i, "Horário da consulta" : h}
            pacientes.append(f"{cont} - {d}")
            print("Consulta marcada com sucesso!")
            continue
        if op == 2:
            if (len(pacientes))>=1:
                print("Cliente, aqui está o seu histórico de consultas: ")
                print(pacientes)
                continue
            else:
                print("Seu histórico de consultas está vazio.")
                continue
        else:
            print("Erro!")
            continue
    if cod == 2:
        if (len(pacientes))>=1:
            print("Médico, aqui está a lista de pacientes: ")
            print(pacientes)
            atender = int(input("Qual é o código do paciente que gostaria de atender?: "))
            range+= atender
            del pacientes[range]
            print("Paciente atendido! Nova lista de espera: ")
            print(pacientes)
            continue
        if (len(pacientes))<1:
            print("Todos os pacientes foram atentidos! Volte depois.")
            continue
    else:
        print("Erro!")
        continue