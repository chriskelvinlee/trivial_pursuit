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
from scoring import *

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

def compute_score(queryphrase="", keywords=[], answers=[], urls=[], scoringFunction = getSimpleAnswerPhraseScores):

    # get urls
    if urls == []:
        urls = getGoogleLinks(queryphrase, 3) # may want to change this number

    # get question keywords
    if keywords == []:
        keywords = getSimpleQuestionKeywords(queryphrase)
        weightedquestionkeywords = getWeightedQuestionKeywords(queryphrase)
    #print keywords
    #print weightedquestionkeywords

    # get answer keywords
    weightedanswerkeywords = getAnswerKeywords(answers)
    #print weightedanswerkeywords

    # get tokens from query
    querytokens = nltk.word_tokenize(queryphrase)

    # get tokens for combined urls
    combinedtokens = getTokens(urls)

    # find instances of keywords
    instances = getInstances(keywords, combinedtokens)

    # using the specified function, compute the scores
    scores = scoringFunction(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    
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
