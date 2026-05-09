import unittest
import os
from mistake_manager import add_mistake, load_mistakes, view_mistakes

test_file = "test_mistakes.txt"

class TestMathMistakeTracker(unittest.TestCase):
    def setUp(self):    # I did setup instead of setUp, but it is not working, so I do the dubugging here using chatgpt.
        with open(test_file,"w") as file:
            file.write("")
    
    def test_add_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = load_mistakes(test_file)

        self.assertEqual(len(data), 1)

    #def test_load_mistakes(self):
    def test_load_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = load_mistakes(test_file)

        self.assertEqual(data[0][0], "1+1")
        self.assertEqual(data[0][1], "3")
        self.assertEqual(data[0][2], "2")


    def test_view_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = view_mistakes(test_file)

        self.assertEqual(len(data), 1)

        
if __name__ == '__main__':    
    unittest.main()
