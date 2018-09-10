import unittest

from recursion.computelistsum import compute_sum


class Testcomputesum(unittest.TestCase):
    
    def test_output(self):
        self.assertEqual(compute_sum([1,-2,-3,[4,6]]),6)
        self.assertEqual(compute_sum([1,2,3,[4,6]]),16)
        
        self.assertEqual(compute_sum([1,2,3,4]), sum([1,2,3,4]))

    def test_input_is_list(self):
        self.assertEqual(compute_sum((1,2,3)), 'Invalid argument type. This should be a list')
        self.assertEqual(compute_sum('welcome'), 'Invalid argument type. This should be a list')

if __name__ == '__main__':
    unittest.main()


