pesototal = 0
alturatotal = 0
contadora = 0
maioraltura = 0
menorpeso = 99999999
menoraltura = 9999999
maiorpeso = 0
while True:
    codigo = int(input(f"Cliente, por favor insira seu código: "))
    if codigo > 0:
        
        contadora = contadora + 1
        altura = float(input("Digite a sua altura: "))
        peso = float(input("Digite o seu peso: "))
        if peso > maiorpeso:
            maiorpeso = peso
        
        if altura > maioraltura:
            maioraltura = altura
        
        if peso < menorpeso:
            menorpeso = peso
        
        if altura < menoraltura:
            menoraltura = altura
        pesototal = pesototal + peso
        alturatotal = alturatotal + altura
        mediaaltura = alturatotal / contadora
        mediapeso = pesototal / contadora
    else:
        break
print (f"O maior peso é igual a {maiorpeso}, já o menor é igual a {menorpeso}, e a maior altura é igual a {maioraltura}, já a menor altura é igual a {menoraltura}. A média de peso dos clientes da academia é igual a {mediapeso} e a média de altura é igual a {mediaaltura}.")    
    

