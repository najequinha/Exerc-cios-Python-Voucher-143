nome = str(input("Digite o seu nome: "))
if nome == nome[0:3]:
    print ("Inválido.")
else:
    print ("Válido.")
idade = int(input("Digite a sua idade: "))
if idade > 150 or idade < 0:
    print ("Inválido.")
else:
    print ("Válido.")
salario = float(input("Digite o seu salário: "))
if salario <=0:
    print ("Inválido.")
else:
    print ("Válido.")
sexo = str(input("Digite a letra referente ao seu sexo (f, m, o): ").upper ())
if sexo != "F" and sexo != "M" and sexo != "O":
    print ("Inválido.")
else:
    print ("Válido.")
estadocivil = str(input("Digite a letra referente ao seu estado civil (s, c, v, d): ").upper ())
if estadocivil != "S" and estadocivil != "C" and estadocivil != "V" and estadocivil != "D":
    print ("Inválido.")
else:
    print ("Válido.")

        
            