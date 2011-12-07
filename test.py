from questions import *
from trivialpursuitfunctions import *
from scoring import *
from output import *
from decide import *

#What other options should test take in?
def test( questions = tp_Questions, scoringFunction = useAllWeights ):
    numberCorrect = 0;
    for question in questions:
        # Read in question, choices, and correct answer
        text = question[0]
        choices = question[1]
        correct = question[2]
        
        # Parse urls, questions, answers and generate keywords
        raw = NLTK_parse( queryphrase=text, answers=choices )
        nltk_data = raw[0]          # array of size 6
        nltk_time = raw[1]          # array of size 6
        
        # Get answer weight with scoring function(s)
        weights = score(answers, nltk_data, scoringFunction)
        candidate = weights[0]      # array of size 4
        ai_time = weights[1]        # array of size 4
        
        # Determine correct results
        bld = text + ": "
        if getHighestResult(result, choices) == correct:
            numberCorrect += 1
            bld += "Correct"
        else:
            bld += "Incorrect"
        print bld
        
        # Output results        
    
    print str(numberCorrect) + "/" + str(len(questions))
    

def getHighestResult(result, choices):
    highestConfidence = 0
    highestChoice = ""
    for r in result:
        if result[r] > highestConfidence:
            highestChoice = r
            highestConfidence = result[r]
    
    index = 0
    for c in choices:
        if c == highestChoice:
            break
        index += 1
    return index
