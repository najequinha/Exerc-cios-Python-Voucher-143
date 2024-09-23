n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
numeros = [n1, n2]
maior = (max(numeros))
menor = (min(numeros))
intervalo = []
while menor<maior - 1:
    menor+=1
    intervalo.append(menor)
print(f"O intervalo compreendido entre os números {n1} e {n2} é composto pelos números {intervalo}.")
