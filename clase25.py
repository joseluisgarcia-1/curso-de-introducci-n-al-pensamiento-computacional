import unittest

def suma(num_1, num_2):
    return abs(num_1 + num_2)

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 22
        num_2 = 6

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 28)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -17)
        #si coloco el 17, ya no arroja el error

if __name__ == '__main__':
    unittest.main()