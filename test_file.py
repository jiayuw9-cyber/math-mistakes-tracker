import unittest
import os
from mistake_manager import add_mistake, load_data, view_mistakes

Test_file = "mistakes.txt"

class TestMathMistakeTracker(unittest.TestCase):
    def setUp(self):
        with open(Test_file,"w") as file:
            file.write("")
    
    def test_add_mistakes(self):
        add_mistake("","","", Test_file)
        data = load_data(Test_file)

        self.assertEqual(len(data), 1)

    def test_view_mistakes(self):
        add_mistake("","","", Test_file)
        data = view_mistakes(Test_file)

        self.assertEqual(len(data), 1)

        
if __name__ == '__main__':    
    unittest.main()
