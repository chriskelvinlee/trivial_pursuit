#!/usr/bin/env python
# encoding: utf-8
"""
weights.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

# base scores on frequency within documents Google returns, not just the two corpora?
def calculateQuestionKeywordWeight(keyword, weightedquestionkeywords):
    return (200 / (weightedquestionkeywords[keyword][0] + 1)) # optimize, can include part of speech, can include inverse frequency in our results

# base scores on frequency within documents Google returns, not just the two corpora?
def calculateAnswerKeywordWeight(answertoken, weightedanswerkeywords):
    return (200 / (weightedanswerkeywords[answertoken][0] + 1)) # optimize, can include part of speech, can include inverse frequency in our results

def calculateDistanceWeight(distance):
    return (50 / (distance + 1)) # optimize
    
    
def calculateInstanceScore(answertoken, keywords, distances, weightedquestionkeywords, weightedanswerkeywords, full):
    newscore = 0
    for keyword in keywords:
        if keyword in distances.keys():
            for distance in distances[keyword]:
                if full == True:
                    newscore += calculateQuestionKeywordWeight(keyword, weightedquestionkeywords) * 10 * calculateDistanceWeight(distance) # optimize
                else:
                    newscore += calculateQuestionKeywordWeight(keyword, weightedquestionkeywords) * calculateAnswerKeywordWeight(answertoken, weightedanswerkeywords) * calculateDistanceWeight(distance) # optimize
    return newscore