class Pessoa:
    nome = ""
    idade = 0
    endereco = ""
    def Nome(self):
        print (f"Nome: {self.nome}")
    def Idade(self):
        print (f"Idade: {self.idade}") 
    def End(self):
        print (f"Endereço: {self.endereco}")
    def detalhes(self):
        print (self.nome)
        print (self.idade)
        print (self.endereco)
pessoa1 = Pessoa()
while True:
    pessoa1.nome = (input("Insira o nome: "))
    pessoa1.idade = int(input("Insira a idade: "))
    pessoa1.endereco = (input("Insira o endereço: "))

    pessoa1.Nome()
    pessoa1.Idade()
    pessoa1.End()

    mudar = (input("Deseja alterar as suas informações(sim ou não)? ").capitalize())
    if mudar == "Sim":
        continue
    if mudar == "Não" or mudar == "Nao":
        print("Finalizado com sucesso.")
        break
    else:
        print("Não identificado. Reinicializando.")
        continue