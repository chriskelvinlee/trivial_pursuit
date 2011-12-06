import nltk
import urllib2
import re
from operator import itemgetter
from urllib import urlopen
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.corpus import reuters
from nltk.corpus import brown
from nltk.probability import *
from nltk.corpus import wordnet as wn
from googleResults import *

ignored_words = stopwords.words('english')

def getSimpleQuestionKeywords(query):
    browntext = brown.words()
    browndist = nltk.FreqDist(browntext)

    reuterstext = reuters.words()
    reutersdist = nltk.FreqDist(reuterstext)

    text = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(text)

    filteredparts = []
    for pair in tagged:
        if pair[1] in ['FW', 'JJ', 'JJR', 'JJS', 'JJT', 'N', 'NN', 'NNP', 'NNS', 'NP', 'NPS', 'NR', 'RB', 'RBR', 'RBT' 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'NUM', 'CD', 'OD']:
            filteredparts.append(pair[0])

    filtereddist = {}
    for word in filteredparts:
        frequency = browndist[word] + reutersdist[word]
        if frequency < 600:
            filtereddist[word] = frequency
    sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
    keywords = []
    for pair in sortedlist:
        keywords.append(pair[0])
    return keywords

# we want to add phrases here, add parts of speech distinctions
def getWeightedQuestionKeywords(query):
    browntext = brown.words()
    browndist = nltk.FreqDist(browntext)

    reuterstext = reuters.words()
    reutersdist = nltk.FreqDist(reuterstext)

    text = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(text)

    filteredparts = []
    for pair in tagged:
        if pair[1] in ['FW', 'JJ', 'JJR', 'JJS', 'JJT', 'N', 'NN', 'NNP', 'NNS', 'NP', 'NPS', 'NR', 'RB', 'RBR', 'RBT' 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'NUM', 'CD', 'OD']:
            filteredparts.append(pair)

    filtereddist = {}
    for pair in filteredparts:
        frequency = browndist[pair[0]] + reutersdist[pair[0]]
        if frequency < 600 or (pair[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] and (frequency < 1500)): # more types here?
            filtereddist[pair[0]] = (frequency, pair[1])
    return filtereddist # ensure there are at least a certain number of keywords? add stemming or synonyms? add phrases?

# we want to add phrases here, add parts of speech distinctions
def getAnswerKeywords(answers):
    browntext = brown.words()
    browndist = nltk.FreqDist(browntext)

    reuterstext = reuters.words()
    reutersdist = nltk.FreqDist(reuterstext)
    
    answerfrequencies = {}
    for answer in answers:
         answertokens = nltk.word_tokenize(answer)
         answertokens = [t for t in answertokens if len(t) > 2 and (t.lower() not in ignored_words)]
         tagged = nltk.pos_tag(answertokens)
         for pair in tagged:
             frequency = browndist[pair[0]] + reutersdist[pair[0]]
             answerfrequencies[pair[0]] = (frequency, pair[1])
    return answerfrequencies # add stemming or synonyms? add phrases?

def findrange(number=0):
    return range(number)

def getTokens(urls):
    combinedtokens = []
    for url in urls:
        html = urlopen(url).read()
        raw = nltk.clean_html(html)
        combinedtokens += nltk.word_tokenize(raw)
    # may need to adjust 2 value here depending on answer choices
    combinedtokens = [t for t in combinedtokens if len(t) > 2 and t.lower() not in ignored_words]
    return combinedtokens

def getInstances(keywords, combinedtokens):
    instances = {}
    tokenrange = findrange(len(combinedtokens))    
    for i in tokenrange:
        if combinedtokens[i] in keywords:
            if combinedtokens[i] not in instances.keys():
                instances[combinedtokens[i]] = [i]
            else:
                instances[combinedtokens[i]].append(i)
    return instances

# score by simply counting instances of answer phrases, without question keywords
def getSimpleAnswerPhraseScores(answers, combinedtokens):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        for i in tokenrange:
            newscore = 0
            if (combinedtokens[i : (i + len(answertokens))] == answertokens):
                newscore = 1
                if answer not in scores.keys():
                    scores[answer] = newscore
                else:
                    scores[answer] += newscore
    return scores

# score by simply counting instances of answer keywords, without question keywords
def getSimpleAnswerKeywordScores(answers, combinedtokens):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        # may need to adjust 2 value here depending on answer choices
        splitanswertokens = [t for t in answertokens if len(t) > 2 and (t.lower() not in ignored_words)]
        splitrange = findrange(len(splitanswertokens))
        for j in splitrange:
            for i in tokenrange:
                newscore = 0
                if combinedtokens[i] == splitanswertokens[j]:
                    newscore = 1
                    if answer not in scores.keys():
                        scores[answer] = newscore
                    else:
                        scores[answer] += newscore
    return scores

# score using question keywords and fixed weights
def getWeightedQuestionKeywordScores(answers, keywords, combinedtokens, instances, rangevalue):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        # may need to adjust 2 value here depending on answer choices
        splitanswertokens = [t for t in answertokens if len(t) > 2 and (t.lower() not in ignored_words)]
        splitrange = findrange(len(splitanswertokens))
        for j in splitrange:
            for i in tokenrange:
                newscore = 0
                if ((combinedtokens[i : (i + len(answertokens))] == answertokens) and (j == 0)):
                    newscore = 10 # optimize
                    for word in keywords:
                        if word in instances.keys():
                            for instance in instances[word]:
                                # optimize value of range here
                                if abs(i - instance) < rangevalue or abs((i + len(answertokens)) - instance) < rangevalue:
                                    newscore *= 2 # optimize
                    if answer not in scores.keys():
                        scores[answer] = newscore
                    else:
                        scores[answer] += newscore
                elif ((combinedtokens[i] == splitanswertokens[j]) and (combinedtokens[i] not in keywords)):
                    newscore = 1
                    for word in keywords:
                        if word in instances.keys():
                            for instance in instances[word]:
                                # optimize value of range here
                                if abs(i - instance) < rangevalue or abs(i - instance) < rangevalue:
                                    newscore *= 2 # optimize
                    if answer not in scores.keys():
                        scores[answer] = newscore
                    else:
                        scores[answer] += newscore
    return scores

# use function below to score, using question keywords and answer keywords
def getFunctionQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        # may need to adjust 2 value here depending on answer choices
        splitanswertokens = [t for t in answertokens if len(t) > 2 and (t.lower() not in ignored_words)]
        splitrange = findrange(len(splitanswertokens))
        for j in splitrange:
            for i in tokenrange:
                distances = {}
                if ((combinedtokens[i : (i + len(answertokens))] == answertokens) and (j == 0)):
                    for word in keywords:
                        if word in instances.keys():
                            for instance in instances[word]:
                                if word not in distances.keys():
                                    distances[word] = [min(abs(instance - i), abs(instance - (i + len(answertokens))))]
                                else:
                                    distances[word].append(min(abs(instance - i), abs(instance - (i + len(answertokens)))))
                    newscore = calculateInstanceScore(answer, keywords, distances, weightedquestionkeywords, weightedanswerkeywords, full=True)
                    if answer not in scores.keys():
                        scores[answer] = newscore
                    else:
                        scores[answer] += newscore
                elif ((combinedtokens[i] == splitanswertokens[j]) and (combinedtokens[i] not in keywords)):
                    for word in keywords:
                        if word in instances.keys():
                            for instance in instances[word]:
                                if word not in distances.keys():
                                    distances[word] = [abs(instance - i)]
                                else:
                                    distances[word].append(abs(instance - i))
                    newscore = calculateInstanceScore(splitanswertokens[j], keywords, distances, weightedquestionkeywords, weightedanswerkeywords, full=False)
                    if answer not in scores.keys():
                        scores[answer] = newscore
                    else:
                        scores[answer] += newscore
    return scores

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

# base scores on frequency within documents Google returns, not just the two corpora?
def calculateQuestionKeywordWeight(keyword, weightedquestionkeywords):
    return (200 / (weightedquestionkeywords[keyword][0] + 1)) # optimize, can include part of speech, can include inverse frequency in our results

# base scores on frequency within documents Google returns, not just the two corpora?
def calculateAnswerKeywordWeight(answertoken, weightedanswerkeywords):
    return (200 / (weightedanswerkeywords[answertoken][0] + 1)) # optimize, can include part of speech, can include inverse frequency in our results

def calculateDistanceWeight(distance):
    return (50 / (distance + 1)) # optimize

def compute_score(queryphrase="", keywords=[], answers=[], urls=[], rangevalue=50):

    # get urls
    if urls == []:
        urls = getGoogleLinks(queryphrase, 3) # may want to change this number

    # get question keywords
    if keywords == []:
        keywords = getSimpleQuestionKeywords(queryphrase)
        weightedquestionkeywords = getWeightedQuestionKeywords(queryphrase)
    print keywords
    print weightedquestionkeywords

    # get answer keywords
    weightedanswerkeywords = getAnswerKeywords(answers)
    print weightedanswerkeywords

    # get tokens from query
    querytokens = nltk.word_tokenize(queryphrase)

    # get tokens for combined urls
    combinedtokens = getTokens(urls)

    # find instances of keywords
    instances = getInstances(keywords, combinedtokens)

    # score the occurrences of answer phrases
    scores = getSimpleAnswerPhraseScores(answers, combinedtokens)
    print scores

    # score the occurrences of answer keywords
    scores = getSimpleAnswerKeywordScores(answers, combinedtokens)
    print scores

    # score the occurrences of answer keywords by weights related to occurrences of question keywords
    scores = getWeightedQuestionKeywordScores(answers, keywords, combinedtokens, instances, rangevalue)
    print scores

    # score the occurences of answer keywords by linear function related to occurrences of question keyword
    scores = getFunctionQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    print scores
    return scores

# WORDNET TESTING

def getSynonyms(keyword):
    synonyms = []
    for synset in wn.synsets(keyword):
        moresynonyms = []
        synonyms += synset.lemma_names
        moresynonyms = synset.hyponyms()
        moresynonyms = [lemma.name for synset in moresynonyms for lemma in synset.lemmas]
        synonyms += moresynonyms
    finalsynonyms = []
    for synonym in synonyms:
        if synonym not in finalsynonyms:
            finalsynonyms.append(synonym)
    print finalsynonyms
