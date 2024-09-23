produtos = [1, 2]
carrinho = []
while True:
    print(f"Produtos: {produtos}")
    compra = (int(input("Selecione o produto que gostaria de adicionar ao seu carrinho ou digite qualquer outro número para finalizar a compra: ")))
    if compra== 1 or compra==2:
        carrinho.append(compra)
        print (f"Seu carrinho: {carrinho}")
    else:
        print("Compra finalizada.")
        break