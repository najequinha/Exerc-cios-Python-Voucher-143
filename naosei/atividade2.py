tarefa = []
descricao = []
status = []
menu = ["1 - Adicionar tarefa", "2 - Listar tarefas", "3 - Marcar tarefa como concluída", "4 - Remover tarefa", "5 - Sair"]
um = -1
d = {"Tarefa" : tarefa, "Descrição" : descricao, "Status" : status}
while True:
    print(menu)
    op = int(input("Qual ação gostaria de realizar: "))

    if op == 1:
        f = input("Digite a tarefa que gostaria de adicionar: ")
        b = input("Digite a descrição da tarefa: ")
        s = input("Digite o status da tarefa: ")
        cod = len(tarefa)
        cod+= 1
        tarefa.append(f"{cod} - {f}")
        descricao.append(b)
        status.append(s)
        print(f"Tarefas: {d}")
        continue
    elif op == 2:
        print("Listando tarefas:")
        print(d)
    elif op == 3:
        print(d)
        n = int(input("Qual o código da tarefa que gostaria de marcar como concluída? "))
        um+=n
        status[um] = "Concluída"
        print(f"Tarefas: {d}")
    elif op == 4:
        um += int(input("Digite o código da tarefa que gostaria de remover: "))
        del tarefa[um]
        del descricao[um]
        del status[um]
        print(f"Tarefas: {d}")
    elif op == 5:
        print("Saindo.")
        break
    else:
        print("Código inválido.") 
        continue