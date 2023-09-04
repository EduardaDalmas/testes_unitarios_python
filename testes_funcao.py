import unittest
from funcao import dobrar_numero

class TesteDobroNumero(unittest.TestCase):

    def teste_numero_positivo(self):
        resultado = dobrar_numero(5)
        self.assertEqual(resultado, 10)

    def teste_numero_zero(self):
        resultado = dobrar_numero(0)
        self.assertEqual(resultado, 0)

    def teste_numero_negativo(self):
        resultado = dobrar_numero(-3)
        self.assertEqual(resultado, -6)

    def teste_numero_string(self):
        resultado = dobrar_numero('2')
        self.assertEqual(resultado, 4)

    def teste_numero_null(self):
        resultado = dobrar_numero(None)
        self.assertEqual(resultado, None)

if __name__ == '__main__':
    unittest.main()