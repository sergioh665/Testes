import unittest
import Calculadora

class CalculadoraTest(unittest.TestCase): 
    
    def test_soma(self):
        self.assertEqual(Calculadora.Calculadora(2,2).soma(), 4)
        self.assertEqual(Calculadora.Calculadora(12,2).soma(), 14)
        self.assertEqual(Calculadora.Calculadora(5,4).soma(), 9)
        self.assertNotEqual(Calculadora.Calculadora(2,2).soma(), 5)
        self.assertNotEqual(Calculadora.Calculadora(12,2).soma(), 15)
        self.assertNotEqual(Calculadora.Calculadora(5,4).soma(), 10)
        self.assertEqual(Calculadora.Calculadora(5,2).soma(), 7)
        self.assertEqual(Calculadora.Calculadora(20,10).soma(), 30)
        self.assertEqual(Calculadora.Calculadora(50,25).soma(), 75)

    def test_subtracao(self): 
        self.assertEqual(2-2, 0)
        self.assertEqual(12-2, 10)
        self.assertEqual(5-4, 1) 
        self.assertNotEqual(2-2, 5)
        self.assertNotEqual(12-2, 15)
        self.assertNotEqual(5-4, 10)
        self.assertEqual(5-2, 3)
        self.assertEqual(20-10, 10)
        self.assertEqual(50-25, 25)
        self.assertNotEqual(5-2, 4)
        self.assertNotEqual(20-10, 9)
        self.assertNotEqual(50-25, 24)
                
    def test_multiplicacao(self):
        self.assertEqual(2*2, 4)
        self.assertEqual(2*12, 24)
        self.assertEqual(4*5, 20)
        self.assertNotEqual(2*2, 5)
        self.assertNotEqual(2*12, 15)
        self.assertNotEqual(4*5, 10)
        
    def test_divisao(self):
        self.assertEqual(2/2, 1)
        self.assertEqual(12/2, 6)
        self.assertEqual(5/5, 1)
        self.assertNotEqual(2/2, 5)
        self.assertNotEqual(12/2, 15)
        self.assertNotEqual(5/5, 10)
        self.assertEqual(10/2, 5)
        self.assertEqual(20/4, 5)
        self.assertEqual(50/5, 10)
        self.assertNotEqual(10/2, 4)
        self.assertNotEqual(20/4, 9)
        self.assertNotEqual(50/5, 24)
        
if __name__ == '__main__':
    unittest.main()