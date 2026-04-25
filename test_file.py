import unittest
import os
from mistake_manager import add_mistake, load_data, view_mistakes

test_file = "mistakes.txt"

class TestMathMistakeTracker(unittest.TestCase):
    def setup(self):
        with open(test_file,"w") as file:
            file.write("")
    
    def test_add_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = load_data(test_file)

        self.assertEqual(len(data), 1)

    #def test_load_mistakes(self):
    def test_load_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = load_data(test_file)

        self.assertEqual(data[0]["problem"], "1+1")
        self.assertEqual(data[0]["wrong"], "3")
        self.assertEqual(data[0]["correct"], "2")


    def test_view_mistakes(self):
        add_mistake("1+1","3","2", test_file)
        data = view_mistakes(test_file)

        self.assertEqual(len(data), 1)

        
if __name__ == '__main__':    
    unittest.main()
