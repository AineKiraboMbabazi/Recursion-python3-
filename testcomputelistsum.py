import unittest

from computelistsum import compute_sum


class testcomputesum(unittest.TestCase):
    @unittest.skip("work in progress")
    def test_input(self,list1):
        self.assertIsinstance(list1,list)

    def test_output(self):
        self.assertEqual(compute_sum([1,-2,-3,[4,6]]),6)
        self.assertEqual(compute_sum([1,2,3,[4,6]]),16)
        self.assertEqual(compute_sum([1,2,3]),6)


if __name__ == '__main__':
    unittest.main()


