nome = []
funcao = []
salario = []
contadora = 0
dic = {"Nome" : nome, "Função" : funcao, "Salário" : salario}
for i in range(4):
    contadora+=1
    print(f"Funcionário {contadora}, digite as seguintes informações: ") 
    n = input("Digite o nome: ")
    nome.append(n)
    f = input("Digite a função: ")
    funcao.append(f)
    s = float(input("Digite o salário: "))
    salario.append(s)
print(dic)
print(max(salario))
    