"""# test case for q1_two_sum"""

import unittest
import q1_two_sum

class Q1TwoSumTest(unittest.TestCase):
    def test(self):
        """test q1_two_sum"""
        ret = q1_two_sum.run([7, 2, 4, 59, 6], 65)  
        self.assertListEqual([3, 4], ret)

if __name__ == '__main__':
    unittest.main()
            