print ("Adição: +")
print ("Subtração: -")
print ("Multiplicação: *")
print ("Divisão: /")
operacao = input("Digite o símbolo da operação que deseja executar (+, -, *, /): ")
while operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/":
    print ("Adição: +")
    print ("Subtração: -")
    print ("Multiplicação: *")
    print ("Divisão: /")
    input("Digite o símbolo da operação que deseja executar(+, -, *, /): ")
else:
    if operacao == "+":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        conta = n1 + n2
        print (conta)
    if operacao == "-":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        conta = n1 - n2
        print (conta)
    if operacao == "*":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        conta = n1 * n2
        print (conta)
    if operacao == "/":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        conta = n1 / n2
        print (conta)