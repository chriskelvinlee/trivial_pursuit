#!/usr/bin/env python
# encoding: utf-8
"""
output.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

def output(text, choices, correct, nltk_data, results, results_raw, answer,
        conf, cand, nltk_time, ai_time, de_time, outputCount, cache):
    url         = nltk_time[0]
    keyword_q   = nltk_time[1]
    keyword_a   = nltk_time[2]
    token_q     = nltk_time[3]
    token_url   = nltk_time[4]
    instances   = nltk_time[5]
    score1      = ai_time[0]
    score2      = ai_time[1]
    score3      = ai_time[2]
    score4      = ai_time[3]
    decide      = de_time
    nltk        = keyword_q+keyword_a+token_q+token_url
    ai          = url+instances+score1+score2+score3+score4+decide
    total       = nltk+ai
    # New Results
    if cache == False:   
        # write to cache
        f = open('cache/nltk{}.txt'.format(outputCount), 'w')
        print >>f, nltk_data[0]
        print >>f, nltk_data[1]
        print >>f, nltk_data[2] 
        print >>f, nltk_data[3]
        print >>f, nltk_data[4]
        print >>f, nltk_data[5]
        f.close()
        # Write to results
        f = open('results/query{}.txt'.format(outputCount), 'w')
    # Print results to cache
    else:
        f = open('reruns/query_re{}.txt'.format(outputCount), 'w')
        
    #Output files    
    print >>f, text
    print >>f, choices
    print >>f, choices[correct]
    if answer[0] == 1:
        print >>f, "Success!\n"
    else:
        print >>f, "Failurez :(\n"
    print >>f, "Index Order: 0,1,2,3,4"
    print >>f, "Correct:\t%d\t\t%d\t\t%d\t\t%d\t\t%d"  % (correct,correct,correct,correct,correct)
    print >>f, "Answer:\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d" % (answer[1],cand[0],cand[1],cand[2],cand[3])
    print >>f, "Confidence:\t%d\t\t%d\t\t%d\t\t%d\t\t%d"% (conf[4], conf[0], conf[1],conf[2],conf[3])
        
    print >>f, '\n#####'
    print >>f, "Total Time:\t\t%f"       % total
    print >>f, "NLTK Time:\t\t%f"        % nltk
    print >>f, "AI Time:\t\t%f"          % ai
    print >>f, "URL Time:\t\t%f"         % url
    print >>f, "Keyword (Q) Time:\t%f"   % keyword_q
    print >>f, "Keyword (A) Time:\t%f"   % keyword_a
    print >>f, "Tokens (Q) Time:\t%f"    % token_q
    print >>f, "Tokens (URL) Time:\t%f"    % token_url
    print >>f, "Map Instance Time:\t%f"    % instances
    print >>f, "Score1 Time:\t\t%f"   % score1
    print >>f, "Score2 Time:\t\t%f"   % score2
    print >>f, "Score3 Time:\t\t%f"   % score3
    print >>f, "Score4 Time:\t\t%f"   % score4
    print >>f, '#####\n'
    print >>f, 'raw results:'
    print >>f, results_raw
    print >>f, "\nscore_result1:\t%s"   % str(results[0]) 
    print >>f, "score_result2:\t%s"   % str(results[1])
    print >>f, "score_result3:\t%s"   % str(results[2])
    print >>f, "score_result4:\t%s"   % str(results[3])
    f.close()
    

