carrinho = []
valoraserpago = []
secoes = ["1 - Alimentos", "2 - Higiene", "3 - Casa", "4 - Menu"]
subsecoes = ["1 - Não perecíveis", "2 - Laticínios&Frios", "3 - Carnes", "4 - Feira", "5 - Higiene bucal", "6 - Banho", "7 - Cabelo", "8 - Limpeza", "9 - Utensílios domésticos"]
#alimentos
naope = ["1 - Feijão", "2 - Arroz", "3 - Açúcar", "4 - Sal", "5 - Farinha",]
latifrios = ["1 - Leite", "2 - Iogurte", "3 - Queijo"]
carne = ["1 - Bovina", "2 - Suína", "3 - Ave"]
feira = ["1 - Alface", "2 - Tomate", "3 - Cebola", "4 - Couve", "5 - Repolho"]
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
bucal = ["1 - Creme dental", "2 - Escova", "3 - Fio dental", "4 - Enxaguante bucal"]
banho = ["1 - Sabonete"]
cabelo = ["1 - Shampoo", "2 - Condicionador", "3 - Creme para pentear"]
#preços2
pbucal = [9.95, 3.99, 5.75, 12.95]
pbanho = [2.19]
pcabelo = [17.90, 19.90, 13.90]
#estoque2
ebucal = [10, 10, 10, 10]
ebanho = [10]
ecabelo = [10, 10, 10]
#casa
limpeza = ["1 - Detergente", "2 - Desinfetante", "3 - Sabão em pó", "4 - Água sanitária"]
uten = ["1 - Pano de chão", "2 - Rodo", "3 - Vassoura"]
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
#formas de pagamento:
fpagamento = ["1 - Dinheiro", "2 - Pix", "3 - Cartão"]
#opções para o funcionário
opcoesf = ["1 - Consultar estoque", "2 - Atualizar estoque", "3 - Adicionar produto", "4 - Alterar preço do produto"]
rangelenitals = [naope, enaope, latifrios, elatifrios, carne, ecarne, feira, efeira, bucal, ebucal, banho, ebanho, cabelo, ecabelo, limpeza, elimpeza, uten, euten]

print("Funcionário: 1; Cliente: 2")
cod = int(input("Digite o código referente a sua função: "))
while True:

    #funcionário

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
        
    while cod == 1:

        #selecionar opção; funcionário

        print("Funcionário, por favor selecione a operação que deseja realizar: ")
        print(opcoesf)
        opcaosel = int(input("Selecione a opção: "))

        #opção1

        if opcaosel == 1:
            print ("Mostrando o estoque: ")
            for i in range(len(rangelenitals)):
                print(f"{rangelenitals[i]}")
                continue

        #opção2

        if opcaosel == 2:
            print ("Mostrando o estoque para que o funcionário possa atualizá-lo: ")
            for i in range(len(rangelenitals)):
                print(f"{rangelenitals[i]}")
            print(subsecoes)
            atualizarproduto = int(input("O produto que gostaria de atualizar o estoque pertence a qual subseção:? "))

            if atualizarproduto == 1: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(naope))):
                    print(f"{naope[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                enaope[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(enaope)

            if atualizarproduto == 2: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(latifrios))):
                    print(f"{latifrios[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                elatifrios[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(elatifrios)

            if atualizarproduto == 3: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(carne))):
                    print(f"{carne[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                ecarne[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(ecarne)

            if atualizarproduto == 4: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(feira))):
                    print(f"{feira[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                efeira[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(efeira)

            if atualizarproduto == 5: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(bucal))):
                    print(f"{bucal[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                ebucal[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(ebucal)

            if atualizarproduto == 6: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(banho))):
                    print(f"{banho[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                ebanho[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(ebanho)

            if atualizarproduto == 7: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(cabelo))):
                    print(f"{cabelo[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                ecabelo[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(ecabelo)

            if atualizarproduto == 8: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(limpeza))):
                    print(f"{limpeza[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                elimpeza[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(elimpeza)

            if atualizarproduto == 9: 
                print("Mostrando produtos da subseção selecionada: ")
                for i in (range(len(uten))):
                    print(f"{uten[i]}")
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                nestoque = int(input("Qual é o estoque desse produto?"))
                euten[atualizando] = nestoque
                print("O estoque foi atualizado com sucesso:")
                print(euten)

        #opção3

        if opcaosel == 3:
            print(subsecoes)
            adicionarproduto = int(input("O produto que gostaria de adcionar pertence a qual subseção:? "))
            if adicionarproduto == 1: 
                print("Mostrando produtos da subseção selecionada: ")
                print(naope)
                numero = 2
                numero+= naope(range)
                nome = input("Qual é o nome do produto?: ")
                naope.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pnaope.append(preco)
                print(naope)
                print(pnaope)

            if adicionarproduto == 2: 
                print("Mostrando produtos da subseção selecionada: ")
                print(latifrios)
                numero = 2
                numero+= latifrios(range)
                nome = input("Qual é o nome do produto?: ")
                latifrios.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                platifrios.append(preco)
                print(latifrios)
                print(platifrios)

            if adicionarproduto == 3: 
                print("Mostrando produtos da subseção selecionada: ")
                print(carne)
                numero = 2
                numero+= carne(range)
                nome = input("Qual é o nome do produto?: ")
                carne.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pcarne.append(preco)
                print(carne)
                print(pcarne)
                
            if adicionarproduto == 4: 
                print("Mostrando produtos da subseção selecionada: ")
                print(feira)
                numero = 2
                numero+= feira(range)
                nome = input("Qual é o nome do produto?: ")
                feira.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pfeira.append(preco)
                print(feira)
                print(pfeira)

            if adicionarproduto == 5: 
                print("Mostrando produtos da subseção selecionada: ")
                print(bucal)
                numero = 2
                numero+= bucal(range)
                nome = input("Qual é o nome do produto?: ")
                bucal.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pbucal.append(preco)
                print(bucal)
                print(pbucal)

            if adicionarproduto == 6: 
                print("Mostrando produtos da subseção selecionada: ")
                print(banho)
                numero = 2
                numero+= banho(range)
                nome = input("Qual é o nome do produto?: ")
                banho.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pbanho.append(preco)
                print(banho)
                print(pbanho)

            if adicionarproduto == 7: 
                print("Mostrando produtos da subseção selecionada: ")
                print(cabelo)
                numero = 2
                numero+= cabelo(range)
                nome = input("Qual é o nome do produto?: ")
                cabelo.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                pcabelo.append(preco)
                print(cabelo)
                print(pcabelo)

            if adicionarproduto == 8: 
                print("Mostrando produtos da subseção selecionada: ")
                print(limpeza)
                numero = 2
                numero+= limpeza(range)
                nome = input("Qual é o nome do produto?: ")
                limpeza.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                plimpeza.append(preco)
                print(limpeza)
                print(plimpeza)

            if adicionarproduto == 9: 
                print("Mostrando produtos da subseção selecionada: ")
                print(uten)
                numero = 2
                numero+= uten(range)
                nome = input("Qual é o nome do produto?: ")
                uten.append(f"{numero} - {nome}")
                preco = float(input("Digite o preço desse produto: "))
                puten.append(preco)
                print(uten)
                print(puten)

        #opção4

        if opcaosel == 4:
            print(subsecoes)
            atualizarpreco = int(input("O produto que gostaria de atualizar o preço pertence a qual subseção:? "))

            if atualizarproduto == 1: 
                print("Mostrando produtos da subseção selecionada: ")
                print(naope)
                print(pnaope)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pnaope[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(naope)
                print(pnaope)

            if atualizarproduto == 2: 
                print("Mostrando produtos da subseção selecionada: ")
                print(latifrios)
                print(platifrios)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                platifrios[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(latifrios)
                print(platifrios)

            if atualizarproduto == 3: 
                print("Mostrando produtos da subseção selecionada: ")
                print(carne)
                print(pcarne)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pcarne[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(carne)
                print(pcarne)

            if atualizarproduto == 4: 
                print("Mostrando produtos da subseção selecionada: ")
                print(feira)
                print(pfeira)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pfeira[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(feira)
                print(pfeira)

            if atualizarproduto == 5: 
                print("Mostrando produtos da subseção selecionada: ")
                print(bucal)
                print(pbucal)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pbucal[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(bucal)
                print(pbucal)

            if atualizarproduto == 6: 
                print("Mostrando produtos da subseção selecionada: ")
                print(banho)
                print(pbanho)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pbanho[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(banho)
                print(pbanho)

            if atualizarproduto == 7: 
                print("Mostrando produtos da subseção selecionada: ")
                print(cabelo)
                print(pcabelo)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                pcabelo[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(cabelo)
                print(pcabelo)

            if atualizarproduto == 8: 
                print("Mostrando produtos da subseção selecionada: ")
                print(limpeza)
                print(plimpeza)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                plimpeza[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(limpeza)
                print(plimpeza)

            if atualizarproduto == 9: 
                print("Mostrando produtos da subseção selecionada: ")
                print(uten)
                print(puten)
                atualizando = -1
                atualizando+= int(input("Digite o código referente ao produto que gostaria de atualizar: "))
                novop = int(input("Qual é o preço desse produto?"))
                puten[atualizando] = novop
                print("O preço foi atualizado com sucesso:")
                print(uten)
                print(puten)

    #cliente

    if cod == 2:
        print("Cliente, informe os dados necessários: ")
        nome = input("Digite seu nome: ")
        cpf = int(input("Digite seu cpf: "))
        if cpf < 10000000000 or cpf > 99999999999:
            print("CPF inválido.")
            continue
        
    while cod == 2:

        #ação:cliente

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
            print(menu)
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
                imposton = valoraserpago * 0.05
                impostoe = valoraserpago * 0.08
                impostom = valoraserpago * 0.12
                valoraserpagoci = (valoraserpago + imposton + impostoe + impostom)
                print("Sua compra foi finalizada.")
                print(f"Seu carrinho: {carrinho}")
                print(f"Valor a ser pago (com impostos): {valoraserpagoci}")
                print(fpagamento)
                pag = int(input("Cliente, por favor selecione a forma de pagamento: "))
                if pag == 1:
                    print("Método de pagamento selecionado: dinheiro")
                    valordado = float(input("Cliente, por favor insira o valor a ser pago:"))
                    if valordado < valoraserpago:
                        print("Valor insuficiente. Tente novamente.")
                        continue
                    if valordado > valoraserpago:
                        troco = valordado - valoraserpago
                        print(f"Troco: R${troco}")
                        print("Compra finalizada com sucesso!")
                        print(f"Nota fiscal: - Produtos: {carrinho}; - Preços: {valoraserpago}; - Impostos: Nacional: {imposton}; Estadual: {impostoe}; Municipal: {impostoe}; Forma de pagamento: Dinheiro:{valordado}; Troco: {troco}")
                        
                    if valordado == valoraserpago:
                        print("Compra finalizada com sucesso!")
                        print(f"Nota fiscal: - Produtos: {carrinho}; - Preços: {valoraserpago}; - Impostos: Nacional: {imposton}; Estadual: {impostoe}; Municipal: {impostoe}; Forma de pagamento: Dinheiro{valordado}")
                
            #operacao3
                
            if selecionarop == 3:
                print("Voltando ao início.")
                continue