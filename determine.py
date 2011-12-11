#!/usr/bin/env python
# encoding: utf-8
"""
determine.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.

text = question[0]
choices = question[1]
correct = question[2]
outputCount = question[3]
nltk_data = readCache(outputCount)
weights = score(choices, nltk_data, scoringFunction)
results = weights[0]      # array of size 4
ai_time = weights[1]      # array of size 4
results_raw = results
determineAnswer(results, choices, correct)

"""
import time
import random

def determineAnswer(results, choices, correct):
    determine_start_time = time.time()
    points = [0, 0, 0]
    finalConfidence = 0
    confidence = []
    candidateAnswers =[]
    
#########
## Permutations ##   
#   Catch all permutations of scores. Determine top candidate answer for
#   each scoring function, and return the relative normalized confidence.
#
#########
    
    # Loop through all score dict results
    for r in results:
        # If dict has 0 candidate answers
        if (r == {}):
            # Neutral score
            confidence.append(0)
            candidateAnswers.append(9)
        # If dict has 1, 2, or 3 candidate answers
        else:
            # Max and min values  
            highestChoice = ""
            a1 = min(r.values())
            z1 = max(r.values())
            # Returns sorted dict values 
            sortedpoo = sorted(r.values())
            # If all values are equal
            if (a1 == z1):
                candidateAnswers.append(9) # Neutral score
            # If 1st and 2nd largest values are equal
            elif len(r) == 3 and sortedpoo[1] == sortedpoo[2]:
                same_key = []
                for key, val in r.iteritems():
                    if val == sortedpoo[1]:
                        same_key.append(key)
                # Break tie to randomly choose between the two
                if random.random() > .5:
                    r[same_key[0]] = 1 + r[same_key[0]]
                    z1 = max(r.values())
                else:
                    r[same_key[1]] = 1 + r[same_key[1]]
                    z1 = max(r.values())
                "very bad inefficient code, duplicate from below"
                # If min is 0, use 2nd largest value as normalizing value
                if ( a1 == 0):
                    for val in r.itervalues():
                        if val != a1 and val != z1:
                            a1 = val
                # Iterate key and value through dict
                for key, val in r.iteritems():
                    # If value is max
                    if val == z1:   
                        # Go through all the candidate choices
                        for c in choices:
                            # if the max value matches the candidate choice            
                            if key == c:    
                                # Add point value                     
                                points[choices.index(c)] += 1   # Optimize
                                # Remember key 
                                highestChoice = key
                                # Remember this score unique score's candidate answer
                                candidateAnswers.append(choices.index(highestChoice))        
                    t = float(val)
                    if a1 != 0:
                        # Normalize
                        r[key] = t/a1 
            # For all other cases
            else:           
                # Iterate through dict
                for key, val in r.iteritems():
                    # If value is max
                    if val == z1:   
                        for c in choices:            
                            if key == c:    
                                # Add point value                     
                                points[choices.index(c)] += 1   # Optimize
                                # Remember key 
                                highestChoice = key
                                # This unique score's candidate answer
                                candidateAnswers.append(choices.index(highestChoice))        
                    t = float(val)
                    if a1 != 0:
                        # Normalize
                        r[key] = t/a1     
                        
#########
## Final Confidence Score ##   
#   Treat all edge case scenarios independently, and begin to aggregate
#   a final confidence score. 
#
#########
                        
                                
            # Find normalized min val
            a2 = min(r.values())
            z2 = max(r.values())
            sortedpoo2 = sorted(r.values())
            # If dict has 3 candidate answers
            if len(r) == 3:
                # If 2 score values are identical
                if sortedpoo2[0] == sortedpoo2[1] and sortedpoo2[1] != sortedpoo2[2]:
                    #finalConfidence += (r[highestChoice]+15)
                    confidence.append(r[highestChoice]+15)              # Optimize
                # If 3 score values are identical
                if sortedpoo2[0] == sortedpoo2[1] == sortedpoo2[2]:
                    confidence.append(0)
                # If all score values are unique
                else:               
                    # Multiplier of 1st vs 2nd
                    for val in r.itervalues():
                        if val != a2 and val != z2:
                            if val == 0:
                                val = 1
                            #finalConfidence += r[highestChoice]/val
                            confidence.append(r[highestChoice]/val)
            # If dict has 2 candidate answers
            elif len(r) == 2:
                if a2 == 0:
                    a2 = 1
                #finalConfidence += z2/a2
                confidence.append(z2/a2)                            #Optimize
            # If dict has 1 candidate answers
            elif len(r) == 1:
                #finalConfidence += 10 #Optimize
                confidence.append(10) #Optimize
    
    # Individual Confidence
    for i in xrange(0,4):
        # Correct add to neutral
        if (candidateAnswers[i] == correct):
            confidence[i] = 50 + confidence[i]      #Optimize
        # Incorrect subtract from neutral
        else:
            confidence[i] = 50 - confidence[i]      # Optimize
            
        # Bound below by zero    
        if confidence[i] < 0:
            confidence[i] = 0
        if confidence[i] > 99:
            confidence[i] = 99
        finalConfidence += confidence[i]        # Optimize


#########
## TODO ##   
#   Currently, we take the average of the confidence score after
#   each hae been penalized or rewarded for incorrect or correct answers.
#   We need to write a function that takes into consideration that if 3
#   are weakly confident but wrong, vs 1 score is strongly confident and
#   right (score4)
#
#########

    # Average of all scores
    finalConfidence = finalConfidence/4         # Optimize

        
    # FinalConfidence -> Normalize for plotting      
    answer_index = points.index(max(points))
    # If bad results, failed
    # if max(points) == min(points):
        # answer_index = 9
    
    """
    if answer_index == correct:
        finalConfidence += 50 + finalConfidence
    else:
        finalConfidence = 50 - finalConfidence
    """  
        
    # Bound below by zero 
    if finalConfidence < 0:
        finalConfidence = 0
          
    if finalConfidence > 99:
        finalConfidence = 99
        
    candidateAnswers.append(answer_index)  
    confidence.append(finalConfidence)
    print confidence
          
                
    determine_stop_time = time.time()
    de_time = (determine_stop_time - determine_start_time)
          
    # Return true if correct w/ confidence
    if answer_index == correct:
        return [[1, answer_index], confidence, candidateAnswers, de_time]
    else:
        return [[0, answer_index], confidence, candidateAnswers, de_time]
        

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]
