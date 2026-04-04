import unittest

class MathMistakeTracker:
    def __init__(self):
        self.mistakes = []

    def add_mistake(self, mistake):
        self.mistakes.append(mistake)

    def get_mistakes(self):
        return self.mistakes
class TestMathMistakeTracker(unittest.TestCase):
    def setUp(self):
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
