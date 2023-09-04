class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def somar(self, numero):
        self.resultado += numero

    def subtrair(self, numero):
        self.resultado -= numero
    
    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        self.resultado /= numero