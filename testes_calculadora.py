import unittest
from calculadora import Calculadora

class TestesCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def teste_somar(self):
        self.calculadora.somar(5)
        self.assertEqual(self.calculadora.resultado, 5)

    def teste_subtrair(self):
        self.calculadora.subtrair(3)
        self.assertEqual(self.calculadora.resultado, -3)
    
    def teste_multiplicar(self):
        self.calculadora.multiplicar(9)
        self.assertEqual(self.calculadora.resultado, 0)

    def teste_dividir(self):
        self.calculadora.dividir(7)
        self.assertEqual(self.calculadora.resultado, 0)

    def teste_combinacao(self):
        self.calculadora.somar(10)
        self.calculadora.subtrair(5)
        self.assertEqual(self.calculadora.resultado, 5)

if __name__ == '__main__':
    unittest.main()