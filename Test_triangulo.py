import unittest
import Triangule

class SimpleTest(unittest.TestCase):

    def test_Equilatero(self):
        result = Triangule.getTypeofTriangule(10,10,10)
        self.assertEqual(result, "Equilatero")
        
    def test_Isosceles(self):
        result = Triangule.getTypeofTriangule(10,40,10)
        self.assertEqual(result, "Isosceles")
        
    def test_Escaleno(self):
        result = Triangule.getTypeofTriangule(10,20,30)
        self.assertEqual(result, "Escaleno")
     
    def test_esTriangulo(self):
        result = Triangule.isTriangule(10,20,30)
        self.assertEqual(result, True) 

if __name__ == '__main__':
    unittest.main()