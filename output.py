#!/usr/bin/env python
# encoding: utf-8
"""
output.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""


    f = open('query{ }.txt'.format(QUERYNUM), 'w')

    # write to file
    f = open(output, 'w')
    print >>f, queryphrase
    print >>f, keywords
    print >>f, weightedquestionkeywords        
    print >>f, weightedanswerkeywords
    print >>f, score_result1
    print >>f, score_result2
    print >>f, score_result3
    print >>f, score_result4
    print >>f, '\n#####'
    print >>f, "Total Time:\t\t%f"       % total
    print >>f, "NLTK Time:\t\t%f"        % (keyword_q+keyword_a+token_q+token_url)
    print >>f, "AI Time:\t\t%f"          % (url+instances+score1+score2+score3+score4)
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
    print >>f, '#####'
    f.close()