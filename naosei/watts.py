def tipos():
    print("0 - 12 watts")
    print("1 - 15 watts")
    print("2 - 18 watts")
    print("3 - 20 watts")
    print("4 - 22 watts")
watts = [12, 15, 18, 20, 22]
tipos()
tipo = int(input("Insira o tipo de cômodo: "))
t_ = watts[tipo]
print(t_)
largura = int(input("Insira a largura do cômodo: "))
comprimento = int(input("Insira o comprimento do cômodo: "))
def area(m, n):
   return m * n
area_ = area(largura, comprimento)
print(f"A área do cômodo é igual a: {area_}")
def mult(y, z):
    return y * z 
multiplicacao = mult(area_, t_)
def div(o, w):
    return o / w
divisao = div(multiplicacao, 60)
print(f"A quantidade de lâmpadas necessárias é igual a: {divisao}")

