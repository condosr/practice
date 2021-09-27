import unittest
from practice import myFunc
#import practice
#import pytest
#print(myFunc(2))
class TestPractice(unittest.TestCase):
    
    def test_answer(self):
        self.assertEqual(myFunc(2), 4)

#test_answer()


if __name__ == "__main__":
    unittest.main