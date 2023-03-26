import unittest
from ..calc import is_normal

class TestCalc(unittest.TestCase):
    
    def test_solve_linear_equation(self):
        result1 = is_normal("7x-2=21")
        result2 = is_normal("2(4x + 3) + 6 =24 - 4x")
        
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

if __name__ == '__main__':
    unittest.main()