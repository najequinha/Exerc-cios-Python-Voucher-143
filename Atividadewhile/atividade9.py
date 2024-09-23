c1 = 0
c2 = 0
c3 = 0
c4 = 0
n = 0
b = 0
while True:
    voto = int(input("Inisira seu voto: "))
    if voto == 0:
        print(f"1: {c1}; 2: {c2}; 3: {c3}; 4: {c4}; 5: {n}; 6: {b}")
        break
    elif voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        n += 1
    elif voto == 6:
        b += 1
    else:
        print("Valor inválido.")