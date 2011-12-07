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
    confidence = 0
    
    # Loop through all score dict results
    for r in results:
        # Score set cannot be empty
        if ( r != {}): 
              
            # Max and min values  
            highestChoice = ""
            a1 = min(r.values())
            z1 = max(r.values())
            if (a1 == 0):
                if val != a1 and val != z1:
                    ai = val
                    
            # Iterate through dict
            for key, val in r.iteritems():
                if val == z1:                    # If value is max
                    for c in choices:            
                        if key == c:                            # Max key is choice
                            points[choices.index(c)] += 1      # Add point value  
                            highestChoice = key          
                t = float(val)
                if a1 != 0:
                    r[key] = t/a1                           # Normalize             
            
            # Find normalized min val
            a2 = min(r.values())
            z2 = max(r.values())
            
            # Multiplier of 1st vs 2nd
            for val in r.itervalues():
                if val != a2 and val != z2:
                    confidence += r[highestChoice]/val
            if confidence == 0 or confidence > 99:
                confidence = 99
                
    determine_stop_time = time.time()
    de_time = (determine_stop_time - determine_start_time)
          
    # Return true if correct w/ confidence
    answer_index = points.index(max(points))
    if answer_index == correct:
        return [[1, answer_index], confidence, de_time]
    else:
        return [[0, answer_index], confidence, de_time]