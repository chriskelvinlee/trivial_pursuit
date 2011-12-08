from questions import *
from trivialpursuitfunctions import *
from scoring import *
from output import *
from determine import *
from importcache import *

#What other options should test take in?
def runQuery( questions, scoringFunction, cache=False):
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
        
        if cache == False:
            print "Processing NLTK..."
            # Parse urls, questions, answers and generate keywords
            raw = NLTK_parse(queryphrase=text, answers=choices)
            nltk_data = raw[0]          # array of size 6
            nltk_time = raw[1]          # array of size 6
        else:
            print "Reading in NLTK cache..."
            nltk_data = readCache(outputCount)
            nltk_time = [0]*6


        print "AI & Scoring..."
        # Get answer weight with scoring function(s)
        weights = score(choices, nltk_data, scoringFunction)
        results = weights[0]      # array of size 4
        ai_time = weights[1]      # array of size 4
        results_raw = results

        print "Determining Answer..."
        # Normalize to determine answer
        correctness = determineAnswer(results, choices, correct)
        answer      = correctness[0]
        confidence  = correctness[1]
        candidate   = correctness[2]
        de_time     = correctness[3]

        # Save the results sys.out txt
        output(text, choices, correct, nltk_data, results, results_raw, answer, confidence, candidate, nltk_time, ai_time, de_time, outputCount, cache)
        
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

runQuery(tp_Questions0, useAllScores, cache=True)
runQuery(tp_Questions1, useAllScores, cache=True)
runQuery(tp_Questions2, useAllScores, cache=True)
runQuery(tp_Questions3, useAllScores, cache=True)
runQuery(tp_Questions4, useAllScores, cache=True)
runQuery(tp_Questions5, useAllScores, cache=True)
runQuery(tp_Questions6, useAllScores, cache=True)
runQuery(tp_Questions7, useAllScores, cache=True)
runQuery(tp_Questions8, useAllScores, cache=True)
runQuery(tp_Questions9, useAllScores, cache=True)
runQuery(tp_Questions10, useAllScores, cache=True)
runQuery(tp_Questions11, useAllScores, cache=True)



