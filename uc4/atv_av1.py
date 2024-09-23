import random
numeros_sorteados = []
numeros_disp = list(range(1,76))
while len(numeros_disp)> 0:
    n_aleatorio = random.choice(numeros_disp)
    numeros_disp.remove(n_aleatorio)
    numeros_sorteados.append(n_aleatorio)
    print(f"Números sorteados: {numeros_sorteados}")
    op = input("Digite 1 para continuar e 2 para parar: ")
    if op == 1:
        print("Continuando")
        continue
    else:
        break