while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if usuario == senha:
        print("Senha inválida. Tente novamente.")
    else:
        print("Válido.")
        break