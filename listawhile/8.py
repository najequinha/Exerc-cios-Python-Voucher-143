n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))
n5 = int(input("Digite um número: "))
numeros = [n1, n2, n3, n4, n5]
soma = (sum(numeros))
tamanho = (len(numeros))
media = soma/tamanho
print(f"A soma dos números é igual a {soma} e a média deles é igual a {media}.")