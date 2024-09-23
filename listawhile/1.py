while True:
    nota = int(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.")
    else:
        print("Nota válida.")
        break