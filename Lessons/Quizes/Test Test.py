import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        result = main.game(5, 5)
        self.assertTrue(result)

    def test_input2(self):
        result = main.game(5, 2)
        self.assertFalse(result)

    def test_input3(self):
        result = main.game(5,11)
        self.assertFalse(result)
    
if __name__ == "__main__":
    unittest.main()