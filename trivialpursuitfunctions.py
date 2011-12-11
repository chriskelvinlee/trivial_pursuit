import time
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
         # may need to adjust 0 value here
         answertokens = [t for t in answertokens if len(t) > 0 and (t.lower() not in ignored_words)]
         tagged = nltk.pos_tag(answertokens)
         for pair in tagged:
             frequency = browndist[pair[0]] + reutersdist[pair[0]]
             answerfrequencies[pair[0]] = (frequency, pair[1])
    return answerfrequencies # add stemming or synonyms? add phrases?

def getTokens(urls):
    combinedtokens = []
    
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    
    for url in urls:
        html = urlopen(url).read()
        # Change back from Mike's fix
        # req = urllib2.Request(url,None,headers)
        # html = urlopen(req).read()
        raw = nltk.clean_html(html)
        combinedtokens += nltk.word_tokenize(raw)
    # may need to adjust 0 value here
    combinedtokens = [t for t in combinedtokens if len(t) > 0 and t.lower() not in ignored_words]
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

def NLTK_parse(queryphrase="", answers=[], urls=[], scoringFunction = getSimpleAnswerPhraseScores):

    # Get urls
    url_start_time = time.time()
    if urls == []:
        urls = getGoogleLinks(queryphrase, 5) # may want to change this number
    url_stop_time = time.time()        

    # Get question keywords
    keyword_q_start_time = time.time()
    keywords = getSimpleQuestionKeywords(queryphrase)
    keyword_q_stop_time = time.time()
    
    # Get weighted question keywords
    keyword_q_weighted_start_time = time.time()        
    weightedquestionkeywords = getWeightedQuestionKeywords(queryphrase)
    keyword_q_weighted_stop_time = time.time()

    # Get answer keywords
    keyword_a_start_time = time.time()   
    weightedanswerkeywords = getAnswerKeywords(answers)
    keyword_a_stop_time = time.time()

    # Get tokens from query
    tokens_q_start_time = time.time()
    querytokens = nltk.word_tokenize(queryphrase)
    tokens_q_stop_time = time.time()

    # Get tokens for combined urls
    tokens_url_start_time = time.time()
    combinedtokens = getTokens(urls)
    tokens_url_stop_time = time.time()

    # Find instances of keywords
    instances_start_time = time.time()
    instances = getInstances(keywords, combinedtokens)
    instances_stop_time = time.time()
    
    # Calculate time
    url =       (url_stop_time - url_start_time)
    keyword_q = (keyword_q_stop_time - keyword_q_start_time)
    keyword_a = (keyword_a_stop_time - keyword_a_start_time)
    token_q =   (tokens_q_stop_time - tokens_q_start_time)
    token_url = (tokens_url_stop_time - tokens_url_start_time)
    instances_t = (instances_stop_time - instances_start_time)

    NLTK = [keywords, weightedquestionkeywords, weightedanswerkeywords, querytokens, combinedtokens, instances]
    TIME = [url, keyword_q, keyword_a, token_q, token_url, instances_t]
    
    return [NLTK, TIME]
    

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
