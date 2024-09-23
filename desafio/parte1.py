carrinho = []
secoes = ["Alimentos", "Higiene", "Casa"]
#alimentos
naope = ["Feijão", "Arroz", "Açúcar", "Sal", "Farinha"]
latifrios = ["Leite", "Iorgute", "Queijo"]
carne = ["Bovina", "Suína", "Ave"]
feira = ["Alface", "Tomate", "Cebola", "Couve", "Repolho", "Salsa", "Pepino", "Acelga"]
#higiene
bucal = ["Creme dental", "Escova", "Fio dental", "Enxaguante bucal"]
banho = ["Sabonete"]
cabelo = ["Shampoo", "Condicionador", "Creme para pentear"]
#casa
limpeza = ["Detergente", "Desinfetante", "Sabão em pó", "Água sanitária"]
uten = ["Pano de chão", "Rodo", "Vassoura"]
#
alimento = ["Não perecíveis", "Laticínios&Frios", "Carnes", "Feira"]
higiene = ["Higiene bucal", "Banho", "Cabelo"]
casa = ["Limpeza", "Utensílios domésticos"]
cod_a = 0
zero1 =0
zero2 = 0
for i in (range(len(secoes))):
    cod_a+=1
    print(f"{cod_a} - {secoes[i]}")
selecionarsecao = int(input("Digite o código referente a seção a qual gostaria de navegar: "))
while True:
    if selecionarsecao == 1:
        print("Seção atual: Alimentos")
        for i in (range(len(alimento))):
            zero1+=1
            print(f"{zero1} - {alimento[i]}")
        selecionarsub = int(input("Digite o código referente a subseção a qual gostaria de navegar: "))

        #naopereciveis

        if selecionarsub == 1:
            print("Mostrando produtos")
            for i in (range(len(naope))):
                zero2+=1
                print(f"{zero2} - {naope[i]}")
            selecionarproduto = -1
            selecionarproduto+= int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            carrinho.append(naope[selecionarproduto])
            print(f"Seu carrinho: {carrinho}")
            opcao = int(input("Digite 0 para finalizar a compra e 1 para voltar ao início e adicionar mais produtos ao carrinho: "))
            if opcao == 0:
                break

        #laticiniosefrios

        if selecionarsub == 2:
            print("Mostrando produtos")
            for i in (range(len(latifrios))):
                zero1 = 0
                zero1+=1
                print(f"{zero1} - {latifrios[i]}")
            selecionarproduto = int(input("Digite o código referente ao produto que gostaria de adicionar no carrinho: "))
            carrinho.append(selecionarproduto)
            print(f"Seu carrinho: {carrinho}")
            opcao = int(input("Digite 0 para finalizar a compra e 1 para voltar ao início e adicionar mais produtos ao carrinho: "))
            if opcao == 0:
                break