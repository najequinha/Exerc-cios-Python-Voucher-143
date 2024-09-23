a = float(80000) 
b = float(200000)
contadora = int(0)
while a < b:
    a = (a *0.03) + a
    b = (b * 0.015) + b
    contadora = contadora + 1
    
print (f"A população A vai se igualar ou ultrapassar a população B em {contadora} anos.")