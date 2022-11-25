import unittest
from math_operations import add, subtract


class Test_Math(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.as

    def test_subtract(self):
        self.assertEqual(subtract(2, 2), 0)


if __name__ == "__main__":
    unittest.main()