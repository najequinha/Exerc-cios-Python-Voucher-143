a = float(input("Informe a população atual do local A: ")) 
b = float(input("Informe a população atual do local B: ")) 
a1 = float(input("Informe a taxa de crescimento da população A: ")) 
b1 = float(input("Informe a taxa de crescimento da população B: ")) 
contadora = 0
while a < b:
    a = ((a/100)*a1) + a
    b = ((b/100)*b1) + b
    contadora = contadora + 1
print (f"A população A vai se igualar ou ultrapassar a população B em {contadora} anos.")