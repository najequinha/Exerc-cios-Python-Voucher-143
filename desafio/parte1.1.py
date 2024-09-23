carrinho = []
valoraserpago = []
secoes = ["1 - Alimentos", "2 - Higiene", "3 - Casa", "4 - Menu"]
#alimentos
naope = ["1 - Feijão: R$3,99", "2 - Arroz: R$14,99", "3 - Açúcar: R$5,99", "4 - Sal: R$2,99", "5 - Farinha: R$3,65", "6 - Menu"]
latifrios = ["1 - Leite: R$3,99", "2 - Iogurte: R$2,99", "3 - Queijo: R$4,95", "4 - Menu"]
carne = ["1 - Bovina: R$21,90", "2 - Suína: R$12,75", "3 - Ave: R$11,99", "4 - Menu"]
feira = ["1 - Alface: R$2,49", "2 - Tomate: R$3,99", "3 - Cebola: R$1,98", "4 - Couve: R$2,25", "5 - Repolho: R$2,65", "6 - Menu"]
#preços1
pnaope = [3.99, 14.99, 5.99, 2.99, 3.65,]
platifrios = [3.99, 2.99, 4.95]
pcarne = [21.90, 12.75, 11.99]
pfeira = [2.49, 3.99, 1.98, 2.25, 2.65]
#estoque1
enaope = [10, 10, 10, 10, 10]
elatifrios = [10, 10, 10]
ecarne = [10, 10, 10]
efeira = [10, 10, 10, 10, 10]
#higiene
bucal = ["1 - Creme dental: R$9,95", "2 - Escova: R$3,99", "3 - Fio dental: R$5,75", "4 - Enxaguante bucal: R$12,95", "5 - Menu"]
banho = ["1 - Sabonete: R$2,19", "2 - Menu"]
cabelo = ["1 - Shampoo: R$17,90", "2 - Condicionador: R$19,90", "3 - Creme para pentear: R$13,90", "4 - Menu"]
#preços2
pbucal = [9.95, 3.99, 5.75, 12.95]
pbanho = [2.19]
pcabelo = [17.90, 19.90, 13.90]
#estoque2
ebucal = [10, 10, 10, 10]
ebanho = [10]
ecabelo = [10, 10, 10]
#casa
limpeza = ["1 - Detergente: R$2,99", "2 - Desinfetante: R$7,49", "3 - Sabão em pó: R$9,99", "4 - Água sanitária: R$4,65", "5 - Menu"]
uten = ["1 - Pano de chão: R$3,99", "2 - Rodo: R$12,99", "3 - Vassoura: R$14,99", "4 - Menu"]
#preços3
plimpeza = [2.99, 7.49, 9.99, 4.65]
puten = [3.99, 12.99, 14.99]
#estoque3
elimpeza = [10, 10, 10, 10]
euten = [10, 10, 10]
#menu
menu = ["1 - Excluir item do carrinho", "2 - Finalizar compra", "3 - Voltar ao início"]
#
alimento = ["1 - Não perecíveis", "2 - Laticínios&Frios", "3 - Carnes", "4 - Feira", "5 - Menu"]
higiene = ["1 - Higiene bucal", "2 - Banho", "3 - Cabelo", "4 - Menu"]
casa = ["1 - Limpeza", "2 - Utensílios domésticos", "3 - Menu"]

#selecionar função

print("Funcionário: 1; Cliente: 2")
cod = int(input("Digite o código referente a sua função: "))
if cod == 1:
    print("Funcionário, informe os dados necessários: ")
    matricula = int(input("Digite sua matrícula: "))
    nome = input("Digite seu nome: ")
    dianasc = int(input("Digite o dia do seu nascimento: "))
    mesnasc = int(input("Digite o mês do seu nascimento: "))
    anonasc = int(input("Digite o ano do seu nascimento: "))
    cpf = int(input("Digite seu cpf: "))
elif cod == 2:
    print("Cliente, informe os dados necessários: ")
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu cpf: "))
while True:
    print("Mostrando seções:")
    for i in (range(len(secoes))):
        print(f"{secoes[i]}")
    selecionarsecao = int(input("Digite o código referente a seção a qual gostaria de navegar: "))
    #secao:alimentos

    if selecionarsecao == 1:
        print("Seção atual: Alimentos")
        for i in (range(len(alimento))):
            print(f"{alimento[i]}")
        selecionarsub = int(input("Digite o código referente a subseção a qual gostaria de navegar: "))

        #naopereciveis

        if selecionarsub == 1:
            print("Mostrando produtos")
            for i in (range(len(naope))):
                print(f"{naope[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pnaope[selecionarproduto])
            carrinho.append(naope[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
        #laticiniosefrios

        if selecionarsub == 2:
            print("Mostrando produtos")
            for i in (range(len(latifrios))):
                print(f"{latifrios[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(platifrios[selecionarproduto])
            carrinho.append(latifrios[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue

        #carne

        if selecionarsub == 3:
            print("Mostrando produtos")
            for i in (range(len(carne))):
                print(f"{carne[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pcarne[selecionarproduto])
            carrinho.append(naope[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
        #feira

        if selecionarsub == 4:
            print("Mostrando produtos")
            for i in (range(len(feira))):
                print(f"{feira[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pfeira[selecionarproduto])
            carrinho.append(feira[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue

        #secao:higiene

        if selecionarsecao == 2:
            print("Seção atual: Higiene")
            for i in (range(len(higiene))):
                print(f"{higiene[i]}")
            selecionarsub = int(input("Digite o código referente a subseção a qual gostaria de navegar: "))


        #bucal

        if selecionarsub == 1:
            print("Mostrando produtos")
            for i in (range(len(bucal))):
                print(f"{bucal[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pbucal[selecionarproduto])
            carrinho.append(bucal[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
        #banho

        if selecionarsub == 2:
            print("Mostrando produtos")
            for i in (range(len(banho))):
                print(f"{banho[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pbanho[selecionarproduto])
            carrinho.append(banho[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
        #cabelo

        if selecionarsub == 3:
            print("Mostrando produtos")
            for i in (range(len(cabelo))):
                print(f"{cabelo[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(pcabelo[selecionarproduto])
            carrinho.append(cabelo[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
    #secao:casa

    if selecionarsecao == 3:
        print("Seção atual: Higiene")
        for i in (range(len(higiene))):
            print(f"{higiene[i]}")
        selecionarsub = int(input("Digite o código referente a subseção a qual gostaria de navegar: "))


        #limpeza

        if selecionarsub == 1:
            print("Mostrando produtos")
            for i in (range(len(limpeza))):
                print(f"{limpeza[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(plimpeza[selecionarproduto])
            carrinho.append(limpeza[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor total atual da compra: {sum(valoraserpago)}")
            continue
            
        #utensilios

        if selecionarsub == 2:
            print("Mostrando produtos")
            for i in (range(len(uten))):
                print(f"{uten[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            valoraserpago.append(puten[selecionarproduto])
            carrinho.append(uten[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            continue
            

    #secao:menu

    if selecionarsecao == 4:
        print("Selecione a operação que deseja executar: ")
        for i in (range(len(menu))):
            print(f"{menu[i]}")
            selecionarop = int(input("Digite o código referente a operação desejada: "))
            
        #operacao1 
            
        if selecionarop == 1:
            print("Excluir item do carrinho")
        for i in (range(len(carrinho))):
            print(f"{carrinho[i]}")
            eliminar = -1
            eliminar+= int(input("Digite o código referente ao produto que gostaria de eleminar do carrinho: "))
            del carrinho[eliminar]
            print(f"Seu carrinho: {carrinho}")
                
        #operacao2
            
        if selecionarop == 2:
            print("Sua compra foi finalizada.")
            print(f"Seu carrinho: {carrinho}")
            print(f"Valor a ser pago: {valoraserpago}")

        #operacao3
            
        if selecionarop == 3:
            print("Voltando ao início.")
#        else:
#            print("Inválido.")
