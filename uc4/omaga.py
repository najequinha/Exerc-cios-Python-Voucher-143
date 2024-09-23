import random
def numeros_de_uma_fileira(w, x, y, z):
    fileira = w
    qtd_n = x
    numeros_disp = list(range(y,z))
    numeros_da_cartela = []
    for i in range(qtd_n):
        n_aleatorio = random.choice(numeros_disp)
        numeros_disp.remove(n_aleatorio)
        numeros_da_cartela.append(n_aleatorio)
    print(numeros_da_cartela)
    return numeros_da_cartela
b = numeros_de_uma_fileira("B", 5, 1, 16)
i = numeros_de_uma_fileira("I", 5, 16, 31)
n = numeros_de_uma_fileira("N", 4, 31, 46)
g = numeros_de_uma_fileira("G", 5, 46, 61)
o = numeros_de_uma_fileira("G", 5, 61, 76)
