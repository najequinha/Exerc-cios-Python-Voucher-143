cont = 0
while True:
    n = input("Digite um nome: ")
    cont+=1
    print (f"Tentativas: {cont}")
    if n == "Rafael" or n == "RAFAEL" or n == "rafael":
        print ("Nome correto")