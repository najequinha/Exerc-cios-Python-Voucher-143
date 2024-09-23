cont = 0
notas = []
for i in range(4):
    cont+=1
    n = float(input(f"Digite a nota {cont}: "))
    d = {"Notas" : notas}
    notas.append(n)
total = sum(notas)
media = total / cont
print(d)
print(f"Média: {media}")