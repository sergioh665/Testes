import unittest
import ModDiv as mdv

class ModDivTest(unittest.TestCase):
    
    m = mdv.ModDiv()
    
    def test_mod(self):
        self.assertEqual(self.m.mod(5, 2), 1)
        self.assertEqual(self.m.mod(10, 3), 1)
        self.assertEqual(self.m.mod(15, 4), 3)
        self.assertEqual(self.m.mod(20, 5), 0)
        self.assertEqual(self.m.mod(25, 6), 1)
        self.assertEqual(self.m.mod(30, 7), 2)
        self.assertEqual(self.m.mod(35, 8), 3)
        self.assertEqual(self.m.mod(40, 9), 4)
        
        
    def test_div(self):
        self.assertEqual(self.m.div(5, 2), 2)
        self.assertEqual(self.m.div(10, 3), 3)
        self.assertEqual(self.m.div(15, 4), 3)
        self.assertEqual(self.m.div(20, 5), 4)
        self.assertEqual(self.m.div(25, 6), 4)
        self.assertEqual(self.m.div(30, 7), 4)
        self.assertEqual(self.m.div(35, 8), 4)
        self.assertEqual(self.m.div(40, 9), 4)        
        
if __name__ == '__main__':
    unittest.main()        