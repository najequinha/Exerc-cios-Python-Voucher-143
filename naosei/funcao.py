numeros = [1, 2, 3, 4, 5, 6, 7, 9, 10]
par = []
impar = []
def verificacao(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
for i in numeros:
    if verificacao(i) == "Par":
        par.append(i)
    else:
        impar.append(i)
print(f"Números: {numeros}")
print(f"Pares: {par}")
print(f"Ímpares: {impar}")

