import unittest

from power import power

class testpower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,-1),0.5)
        self.assertEqual(power(5,-6),6.4e-05)
        self.assertEqual(power(2,1),2)
        self.assertEqual(power(2,3),8)
        

if __name__ == '__main__':
    unittest.main()
    