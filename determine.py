#!/usr/bin/env python
# encoding: utf-8
"""
determine.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import time

def determineAnswer(results, choices, correct):
    determine_start_time = time.time()
    points = [0, 0, 0]
    finalConfidence = 0
    confidence = []
    candidateAnswers =[]
    
    # Loop through all score dict results
    for r in results:
        # If dict has 0 candidate answers
        if (r == {}):
            # Neutral score
            confidence.append(0)
            candidateAnswers.append(9)
        # Score set cannot be empty
        else:
            # Max and min values  
            highestChoice = ""
            a1 = min(r.values())
            z1 = max(r.values())
            if (a1 == 0):
                if val != a1 and val != z1:
                    ai = val
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
            
            # Find normalized min val
            a2 = min(r.values())
            z2 = max(r.values())
            
            # If dict has 3 candidate answers
            if len(r) == 3:
                # Multiplier of 1st vs 2nd
                for val in r.itervalues():
                    if val != a2 and val != z2:
                        finalConfidence += r[highestChoice]/val
                        confidence.append(r[highestChoice]/val)
            # If dict has 2 candidate answers
            elif len(r) == 2:
                finalConfidence += z2/a2
                confidence.append(z2/a2)
            # If dict has 1 candidate answers
            else:
                finalConfidence += 10 #Optimize
                confidence.append(10) #Optimize
                
                
    # Individual Confidence
    for i in xrange(0,4):
        # Correct add to neutral
        if (candidateAnswers[i] == correct):
            confidence[i] = 50 + confidence[i]
        # Incorrect subtract from neutral
        else:
            confidence[i] = 50 - confidence[i]
        # Bound below by zero    
        if confidence[i] < 0:
            confidence[i] = 0
        if confidence[i] > 99:
            confidence[i] = 99
        
  
    print candidateAnswers
    
    # FinalConfidence -> Normalize for plotting      
    answer_index = points.index(max(points))
    if answer_index == correct:
        finalConfidence = 50 + finalConfidence
    else:
        finalConfidence = 50 - finalConfidence
    # Bound below by zero 
    if finalConfidence < 0:
        finalConfidence = 0
          
    if finalConfidence > 99:
        finalConfidence = 99
    candidateAnswers.append(answer_index)  
    confidence.append(finalConfidence)
          
                
    determine_stop_time = time.time()
    de_time = (determine_stop_time - determine_start_time)
          
    # Return true if correct w/ confidence
    if answer_index == correct:
        return [[1, answer_index], confidence, candidateAnswers, de_time]
    else:
        return [[0, answer_index], confidence, candidateAnswers, de_time]