while True:
    total = 0
    nproduto = 1
    while True:
        produto = float(input(f"Produto {nproduto}: R$: "))
        if produto == 0:
            break
        else:
            total = total + produto
            nproduto = nproduto + 1
            
    print (f"O valor total é igual a {total}")
    pagamento = float(input("Insira o valor de pagamento: "))
    troco = pagamento - total
    print (f"Troco: {troco}")
