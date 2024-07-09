import unittest
import Fatorial as ft

class FatorialTest(unittest.TestCase):

    f = ft.Fatorial()
    
    def test_fatorial(self):
        self.assertEqual(self.f.calcular(4), 24)
        self.assertEqual(self.f.calcular(5), 120)
        self.assertEqual(self.f.calcular(6), 720)
        self.assertEqual(self.f.calcular(7), 5040)
        self.assertEqual(self.f.calcular(8), 40320)
        self.assertEqual(self.f.calcular(9), 362880)
        self.assertEqual(self.f.calcular(10), 3628800)
        
        
if __name__ == '__main__':
    unittest.main()        