x = 1
y = 2
z = 3
triangular = False
numero = int(input("Digite um número: "))
while (x*y*z) <= numero:
    if (x*y*z) == numero:
        triangular = True
        break
    
    x+= 1
    y+= 1
    z+= 1



if triangular == True:
    print ("O número é triangular.")
else:
    print ("O número não é triangular.")
