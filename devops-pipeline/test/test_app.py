import unittest
from src.app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        #self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 10)  # wrong on purpose

if __name__ == "__main__":
    unittest.main()
