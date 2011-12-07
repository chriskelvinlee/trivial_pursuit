from questions import *
from trivialpursuitfunctions import *
from scoring import *
from output import *
from determine import *

#What other options should test take in?
def runQuery( questions, scoringFunction):
    numberCorrect = 0
    currentCount = 0
    for question in questions:
        currentCount += 1
        print "*****"
        print "Processing Query %d of %d " % (currentCount, len(questions))
        
        # Read in question, choices, and correct answer
        text = question[0]
        choices = question[1]
        correct = question[2]
        outputCount = question[3]
        
        print "Processing NLTK..."
        # Parse urls, questions, answers and generate keywords
        raw = NLTK_parse(queryphrase=text, answers=choices)
        nltk_data = raw[0]          # array of size 6
        nltk_time = raw[1]          # array of size 6

        print "AI & Scoring..."
        # Get answer weight with scoring function(s)
        weights = score(choices, nltk_data, scoringFunction)
        results = weights[0]      # array of size 4
        ai_time = weights[1]        # array of size 4

        print "Determining Answer..."
        # Normalize to determine answer
        correctness = determineAnswer(results, choices, correct)
        answer  = correctness[0]
        conf    = correctness[1]
        de_time = correctness[2]

        # Save the results sys.out txt
        output(text, choices, correct, nltk_data, results, answer, conf,
            nltk_time, ai_time, de_time, outputCount)
        print "*****"
        
        # Print results live
        bld = text + ": "
        if answer[0] == 1:
            numberCorrect += 1
            bld += "Correct"
        else:
            bld += "Incorrect"
        print bld
        
    print str(numberCorrect) + "/" + str(len(questions))

runQuery( tp_Questions3, useAllScores)