while True:
    print("Adição = +; Substração = -; Multiplicação = *; Divisão = /")
    operacao = input("Digite o símbolo da operação que deseja realizar: ")
    if operacao == "+":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma = n1 + n2
            print (f"{n1} + {n2} = {soma}")
    elif operacao == "-":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma = n1 - n2
            print (f"{n1} - {n2} = {soma}")
    elif operacao == "*":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma = n1 * n2
            print (f"{n1} * {n2} = {soma}")
    elif operacao == "/":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma = n1 / n2
            print (f"{n1} / {n2} = {soma}")
    elif operacao != "+" or operacao != "-" or operacao != "*" or operacao != "/":
        print ("Operação inválida. Tente novamente.")

