class Carro:
    cor = 'sem cor'
    marca = 'sem marca'
    modelo = 'sem modelo'
    ano = 2010
    km_rodados = 0
    motor = 0
    movimento = 0
    def detalhes(self):
        print (self.cor)
        print (self.marca)
        print (self.modelo)
        print (self.ano)
        print (self.km_rodados)
    def ligarMotor(self):
        if self.motor == 0:
            self.motor = 1
            print ("Motor ligado")
        else:
            self.motor = 1
            print ("Motor já ligado")
    def desligarMotor(self):
        self.motor = 0
        print ("Motor desligado")
    def andar(self):
        self.movimento = 1
        print ("Carro em movimento")
    def parar(self):
        self.movimento = 0
        print ("Carro parado")
carro1 = Carro()
carro1.cor = "Prata"
carro1.marca = "Fiat"
carro1.modelo = "Uno"
carro1.ano = 2010
carro1.km_rodados = 450
carro1.detalhes()
carro1.ligarMotor()
carro1.desligarMotor()
carro1.andar()
carro1.parar()
