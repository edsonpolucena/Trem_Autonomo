import unittest
from TremAutonomo import TremAutonomo

class TestTremAutonomo(unittest.TestCase):

    def setUp(self):
        self.trem = TremAutonomo()

    def test_movimento_direita(self):
        comandos = ["DIREITA", "DIREITA"]
        self.assertEqual(self.trem.mover(comandos), 2)

    def test_movimento_esquerda(self):
        comandos = ["ESQUERDA"]
        self.assertEqual(self.trem.mover(comandos), -1)

    def test_movimentos_consecutivos_invalidos(self):
        comandos = ["DIREITA"] * 21
        with self.assertRaises(ValueError):
            self.trem.mover(comandos)

    def test_movimentos_totais(self):
        comandos = ["DIREITA"] * 20 + ["ESQUERDA"] * 10 + ["DIREITA"] * 20  
        self.assertEqual(self.trem.mover(comandos), 30) 

    def test_comando_invalido(self):
        comandos = ["DIREITA", "PULAR"]
        with self.assertRaises(ValueError):
            self.trem.mover(comandos)

    def test_lista_vazia(self):
        comandos = []
        self.assertEqual(self.trem.mover(comandos), 0)

if __name__ == '__main__':
    unittest.main()
