from questions import *
from trivialpursuitfunctions import *

#What other options should test take in?
def test(questions = historyQuestions):
    numberCorrect = 0;
    for question in questions:
        text = question[0]
        choices = question[1]
        correct = question[2]
        result = compute_score(queryphrase=text, answers=choices)

        bld = text + ": "
        if getHighestResult(result, choices) == correct:
            numberCorrect += 1
            bld += "Correct"
        else:
            bld += "Incorrect"
        print bld
    print str(correct) + "/" + str(len(questions))

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
