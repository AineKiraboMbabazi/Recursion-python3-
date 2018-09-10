import unittest

from recursion.power import power

class testpower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,-1),pow(2,-1))
        self.assertEqual(power(5,-6),pow(5,-6))
        self.assertEqual(power(2,1),pow(2,1))
        self.assertEqual(power(2,3),pow(2,3))
        self.assertEqual(power(-5,-5),pow(-5,-5))
        self.assertEqual(power(-5.0,-5),pow(-5.0,-5.0))
        
    def test_input_integer_or_float(self):
        self.assertEqual(power('u',8),'invalid input')
if __name__ == '__main__':
    unittest.main()
    