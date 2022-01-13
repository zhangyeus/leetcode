import unittest
import q1_two_sum

class q1_two_sum_test(unittest.TestCase):
    def test(self):
        ret = q1_two_sum.run([7,2,4,59,6], 65)    
        self.assertListEqual([3, 4], [3, 4])
        
if __name__ == '__main__':
    unittest.main()        