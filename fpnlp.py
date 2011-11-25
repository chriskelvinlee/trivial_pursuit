#!/usr/bin/env python

import nltk

from urllib import urlopen

from nltk.collocations import *

from nltk.corpus import stopwords

ignored_words = stopwords.words('english')

def findrange(number=0):
    return range(number)

def compute_score(queryphrase="", keywords=[], answers=[], urls=[], scorevalue=0, rangevalue=0, left=False, right=False):
    query = False
    keyword = False

    if answers == []:
        print "error, please enter answers"
        return 1

    if queryphrase == "" and keywords == []:
        print "error, please specify query or keywords"
        return 2
    elif queryphrase != "":
        query = True
    else:
        keyword = True

    if urls == []:
        print "error, please enter urls"
        return 3
    else:
        combinedtokens = []
        for url in urls:
            html = urlopen(url).read()
            raw = nltk.clean_html(html)
            combinedtokens += nltk.word_tokenize(raw)
        combinedtokens = [t for t in combinedtokens if len(t) > 1 and t.lower() not in ignored_words]
        # print(combinedtokens)
        querytokens = nltk.word_tokenize(queryphrase)
        # print(querytokens)

    # can support one word
    if query == True:
        length = len(querytokens)
        instances = []
        tokenrange = findrange(len(combinedtokens))
        for i in tokenrange:
            if combinedtokens[i : (i + length)] == querytokens:
                instances.append((i, (i + length)))
        # print(instances)
        relevanttokens = []
        for leftbound, rightbound in instances:
            if left == True:
                relevanttokens += combinedtokens[leftbound - rangevalue : leftbound]
            if right == True:
                relevanttokens += combinedtokens[rightbound : rightbound + rangevalue]
        # print(relevanttokens)
        relevanttokenrange = findrange(len(relevanttokens))
        scores = {}
        for answer in answers:
            answertokens = nltk.word_tokenize(answer)
            length = len(answertokens)
            for i in relevanttokenrange:
                if relevanttokens[i : (i + length)] == answertokens:
                    if answer not in scores.keys():
                        scores[answer] = scorevalue
                    else:
                        scores[answer] += scorevalue
        print scores
        return scores

    # only supports two keywords
    if keyword == True:
        instances = {}
        tokenrange = findrange(len(combinedtokens))
        for word in keywords:
            for i in tokenrange:
                if combinedtokens[i] == word:
                    if word not in instances.keys():
                        instances[word] = [i]
                    else:
                        instances[word].append(i)
        combinedinstances = []
        # right now only two keywords are supported
        if len(keywords) != 2:
            print "error, number of keywords must be two at this time, if using one word, use query"
            return 4
        elif len(keywords) == 2:
            for instanceone in instances[keywords[0]]:
                for instancetwo in instances[keywords[1]]:
                    if (instancetwo - instanceone) < 20 and (instanceone, instancetwo) not in combinedinstances:
                        combinedinstances.append((instanceone, instancetwo))
                    elif (instanceone - instancetwo) < 20 and (instancetwo, instanceone) not in combinedinstances:
                        combinedinstances.append((instancetwo, instanceone))
        # print(combinedinstances)
        relevanttokens = []
        for leftinstance, rightinstance in combinedinstances:
            relevanttokens += combinedtokens[leftinstance - rangevalue : rightinstance + rangevalue]
        # print(relevanttokens)
        relevanttokenrange = findrange(len(relevanttokens))
        scores = {}
        for answer in answers:
            answertokens = nltk.word_tokenize(answer)
            length = len(answertokens)
            for i in relevanttokenrange:
                if relevanttokens[i : (i + length)] == answertokens:
                    if answer not in scores.keys():
                        scores[answer] = scorevalue
                    else:
                        scores[answer] += scorevalue
        print scores
        return scores
    
# compute_score(queryphrase="Muslim Brotherhood", keywords=[], answers=["Egypt", "Africa"], urls=["http://www.nytimes.com/2011/11/23/world/middleeast/egypts-cabinet-offers-to-quit-as-activists-urge-wider-protests.html", "http://www.nytimes.com/2011/11/24/world/middleeast/egypt-protesters-and-police-clash-for-fifth-day.html"], scorevalue=1, rangevalue=5, left=True, right=True)

# Who assassinated Abraham Lincoln? Query: "assassinated Abraham Lincoln" in Google, word "assassination" in the results, left, right, large range of 100, gives John Wilkes Booth 13 and Mary Todd Lincoln 1

# compute_score(queryphrase="assassination", keywords=[], answers=["John Wilkes Booth", "Mary Todd Lincoln", "Stonewall Jackson", "Lee Harvey Oswald"], urls=["http://memory.loc.gov/ammem/alhtml/alrintr.html", "http://rogerjnorton.com/Lincoln75.html", "http://www.history.com/topics/abraham-lincoln-assassination"], scorevalue=1, rangevalue=200, left=True, right=True)

# When was the Treaty of Versailles signed? Query: question in Google, word "signed" in the results, left right, large range of 100, gives 1919 a score of 25 and 1914 a score of 9 / words "signed" and "Treaty" as keywords give 1919: 6 and 1914: 1

# compute_score(queryphrase="", keywords=["signed", "Treaty"], answers=["1919", "1939", "1914", "1815"], urls=["http://www.rpfuller.com/gcse/history/2.html", "http://www.historylearningsite.co.uk/treaty_of_versailles.htm", "http://www.firstworldwar.com/source/versailles.htm"], scorevalue=1, rangevalue=20, left=True, right=True)

# What king was overthrown during the French Revolution? entered into Google, used "overthrown" in our results ...had to adjust filter to consider short words...Louis XIV gets 1, Marie Antoinette gets 1, Louis XVI gets 5 (correctly!) / keywords "overthrown" and "King" give Louis XVI: 2

# compute_score(queryphrase="", keywords=["overthrown", "King"], answers=["Louis XIV", "Louis XVI", "Robespierre", "Marie Antoinette"], urls=["http://www.bbc.co.uk/history/historic_figures/louis_xvi.shtml", "http://faculty.ucc.edu/egh-damerow/french_revolution.htm", "http://chnm.gmu.edu/revolution/browse/glossary/"], scorevalue=1, rangevalue=20, left=True, right=True)

# What year did Zhou Enlai die? 1976 wins easily here

# compute_score(queryphrase="Zhou Enlai", keywords=[], answers=["1973", "1974", "1975", "1976"], urls=["http://www.britannica.com/EBchecked/topic/656977/Zhou-Enlai", "http://www.sjsu.edu/faculty/watkins/cultrev.htm", "http://www.answers.com/topic/zhou-enlai"], scorevalue=1, rangevalue=80, left=True, right=True)

# keyword generator, given a natural language question

# filter further to include more verbs, synonyms?

browntext = brown.words()
browndist = nltk.FreqDist(browntext)

reuterstext = reuters.words()
reutersdist = nltk.FreqDist(reuterstext)

text = nltk.word_tokenize("What king was overthrown during the French Revolution?")
tagged = nltk.pos_tag(text)
print(tagged)
print(tagged[0][0])
filtered = []
for pair in tagged:
    if pair[1] in ['JJ', 'N', 'NNP', 'VB', 'VBD', 'VBG', 'VBN']:
        filtered.append(pair[0])
# print(filtered)
filtereddist = {}
for word in filtered:
    filtereddist[word] = browndist[word] + reutersdist[word]
print(filtereddist)
sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
keywords = [sortedlist[0][0], sortedlist[1][0]]
print(keywords)

text = nltk.word_tokenize("When was the Treaty of Versailles signed?")
tagged = nltk.pos_tag(text)
print(tagged)
filtered = []
for pair in tagged:
    if pair[1] in ['JJ', 'N', 'NNP', 'VB', 'VBD', 'VBG', 'VBN']:
        filtered.append(pair[0])
# print(filtered)
filtereddist = {}
for word in filtered:
    filtereddist[word] = browndist[word] + reutersdist[word]
print(filtereddist)
sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
keywords = [sortedlist[0][0], sortedlist[1][0]]
print(keywords)

text = nltk.word_tokenize("When did Zhou Enlai die?")
tagged = nltk.pos_tag(text)
print(tagged)
filtered = []
for pair in tagged:
    if pair[1] in ['JJ', 'N', 'NNP', 'VB', 'VBD', 'VBG', 'VBN']:
        filtered.append(pair[0])
# print(filtered)
filtereddist = {}
for word in filtered:
    filtereddist[word] = browndist[word] + reutersdist[word]
print(filtereddist)
sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
keywords = [sortedlist[0][0], sortedlist[1][0]]
print(keywords)
