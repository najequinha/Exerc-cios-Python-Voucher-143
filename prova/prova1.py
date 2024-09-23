while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    if n1 < 1 or n2 < 1:
        print ("Número iválido. Tente novamente.")
    else:
        if (n1 == 10 and n2 == 10) or (n1 == 100 and n2 == 100) or (n1 == 1000 and n2 == 1000):
            print ("2")
        if n1 <=99 and n2 <=99:
            x1 = n2/10
            x1str = str(x1)
            d1 = x1str[0:1]
            u1 = x1str[2:3]
            d1int = int(d1)
            u1int = int(u1)
            x = n1/10
            xstr = str(x)
            d = xstr[0:1]
            u = xstr[2:3]
            dint = int(d)
            uint = int(u)
            soma = dint + uint + d1int + u1int
            print (f"{soma}")
        elif n1 <=999 and n2 <=999:
            x1 = n2/100
            x1str = str(x1)
            c1 = x1str[0:1]
            d1 = x1str[2:3]
            u1 = x1str[3:4]
            c1int = int(c1)
            d1int = int(d1)
            u1int = int(u1)
            x = n1/100
            xstr = str(x)
            c = xstr[0:1]
            d = xstr[2:3]
            u = xstr[3:4]
            cint = int(c)
            dint = int(d)
            uint = int(u)
            soma = c1int + d1int + u1int + cint + dint + uint
            print (f"{soma}")

    
