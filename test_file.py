import unittest
import os
from mistake_manager import add_mistake, load_data, view_mistakes

Test_file = "mistakes.txt"

class TestMathMistakeTracker(unittest.TestCase):
    def setUp(self):
        with open(Test_file,"r") as file:
            file.write("")
        self.tracker = MathMistakeTracker()

    def test_add_and_get_mistakes(self):
        self.tracker.add_mistake("Forgot to carry the one")
        self.tracker.add_mistake("Mixed up addition and multiplication")
        mistakes = self.tracker.get_mistakes()
        self.assertEqual(len(mistakes), 2)
        self.assertIn("Forgot to carry the one", mistakes)
        self.assertIn("Mixed up addition and multiplication", mistakes)
if __name__ == '__main__':    
    unittest.main()
