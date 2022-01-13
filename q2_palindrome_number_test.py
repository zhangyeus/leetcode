"""test q2_palindrome_number"""

import unittest
import q2_palindrome_number

class Q2PalindromeTest(unittest.TestCase):
    def test(self):
        """
        # test palindrome number function
        """
        self.assertTrue(q2_palindrome_number.run(0))
        self.assertTrue(q2_palindrome_number.run(1331))
        self.assertTrue(q2_palindrome_number.run(2458542))
        self.assertFalse(q2_palindrome_number.run(-2458542))
        self.assertFalse(q2_palindrome_number.run(230))
        self.assertFalse(q2_palindrome_number.run(4357))
        self.assertFalse(q2_palindrome_number.run(1258542))        

if __name__ == '__main__':
    unittest.main()
    