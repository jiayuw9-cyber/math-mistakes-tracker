import random
from mistake_manager import load_mistakes 

def quiz_user(filename):
    mistakes = load_mistakes(filename)

    if len(mistakes) == 0:
        print("There are no mistakes to quiz.")
        return
    
# Random choose 10 mistakes
    num_questions = min(10, len(mistakes))
    selected = random.sample(mistakes, num_questions)
# split it into three parts
#just show the question
#make user print the answer 
# (I am not sure whether I can choose one word as a key word in the answer, and if it is match it is correct.)
#But if it is just numbers it should be match.
# Print the output.


#Also, if I have enough time, I can store the result of every times.(Or ten times?)
#Make a conclusion to as bar or scatter plot.