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
#opções para o funcionário
opcoesf = ["1 - Consultar estoque", "2 - Atualizar estoque", "3 - Adicionar produto", "4 - Alterar preço do produto"]
rangelenitals = [naope, enaope, latifrios, elatifrios, carne, ecarne, feira, efeira, bucal, ebucal, banho, ebanho, cabelo, ecabelo, limpeza, elimpeza, uten, euten]

print("Funcionário: 1; Cliente: 2")
cod = int(input("Digite o código referente a sua função: "))
while True:
    if cod == 1:
        print("Funcionário, informe os dados necessários: ")
        matricula = int(input("Digite sua matrícula: "))
        if matricula < 10000 or matricula > 99999:
            print("Inválido.") 
            continue
        nome = input("Digite seu nome: ")
        dianasc = int(input("Digite o dia do seu nascimento: "))
        if dianasc < 1 or dianasc > 31:
            print("Inválido")
            continue
        mesnasc = int(input("Digite o mês do seu nascimento: "))
        if mesnasc < 1 or mesnasc > 12:
            print("Inválido:")
            continue
        elif (mesnasc == 2 and dianasc > 29) or (mesnasc == 4 and dianasc > 30) or (mesnasc == 6 and dianasc > 30) or (mesnasc == 9 and dianasc > 30) or (mesnasc == 11 and dianasc > 31):
            print("Inválido.")
            continue
        anonasc = int(input("Digite o ano do seu nascimento: "))
        if anonasc < 1960 or anonasc > 2006:
            print("Ano inválido/menor de idade.")
            continue
        cpf = int(input("Digite seu cpf: "))
        if cpf < 10000000000 or cpf > 99999999999:
            print("CPF inválido.")
            continue
        while True: 
            print("Usuário, por favor selecione a operação que deseja realizar: ")
            for i in range(len(opcoesf)):
                print(opcoesf)
                opcaosel = int(input("Selecione a opção: "))
                if opcaosel == 1:
                    print ("Mostrando o estoque: ")
                    for i in range(len(rangelenitals)):
                        print(f"{rangelenitals[i]}")
                if opcaosel == 2:
                    print ("Mostrando o estoque: ")
                    for i in range(len(rangelenitals)):
                        print(f"{rangelenitals[i]}")
                    print(secoes)
                    selecionarsecao = int(input("O produto que gostaria de atualizar o estoque pertence a qual seção? "))
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
