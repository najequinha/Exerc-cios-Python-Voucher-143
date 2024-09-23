n = int(input("Digite o número o qual gostaria de verificar a tabuada: "))
tabuada = []
mult = 0
while (len(tabuada))<11:
    op = n * mult
    r = (f"{n} x {mult} = {op}")
    mult+=1
    tabuada.append(r)
print(tabuada)

