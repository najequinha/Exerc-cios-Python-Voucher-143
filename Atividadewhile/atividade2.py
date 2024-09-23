nome = input("Digite seu nome de usuário: ")
senha = input("Digite a sua senha: ")
while nome == senha:
    print ("Erro.")
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
else:
    print ("Tudo certo!")