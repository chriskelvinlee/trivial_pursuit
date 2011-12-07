from questions import *
from trivialpursuitfunctions import *
from scoring import *

#What other options should test take in?
def test(questions = tp_Questions, scoringFunction = getSimpleAnswerPhraseScores):
    numberCorrect = 0;
    for question in questions:
        # Read in question, choices, and correct answer
        text = question[0]
        choices = question[1]
        correct = question[2]
        
        # Parse urls, questions, answers and generate keywords
        result = NLTK_parse(queryphrase=text, answers=choices)
        # Rank possible answers with scoring function(s)
        scores = score( ,scoringFunction = useAllWeights)
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
