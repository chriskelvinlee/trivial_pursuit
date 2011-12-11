import time
import nltk
from nltk.corpus import stopwords
from weights import *

ignored_words = stopwords.words('english')



def score(choices, nd, scoringFunction):
    answers                     = choices
    keywords                    = nd[0]
    combinedtokens              = nd[4]
    instances                   = nd[5]
    weightedquestionkeywords    = nd[1]
    weightedanswerkeywords      = nd[2]
    return scoringFunction(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)


# Use all scores
def useAllScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    time1_start_time = time.time()
    weights1 = getSimpleAnswerPhraseScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    time1_stop_time = time.time()
    
    time2_start_time = time.time()
    weights2 = getSimpleAnswerKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    time2_stop_time = time.time()   
    
    time3_start_time = time.time()
    weights3 =  getWeightedQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    time3_stop_time = time.time()  
    
    time4_start_time = time.time()       
    weights4 = getFunctionQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords)
    time4_stop_time = time.time()  
    
    # Calcualte time
    time1 =    (time1_stop_time - time1_start_time)
    time2 =    (time2_stop_time - time2_start_time)
    time3 =    (time3_stop_time - time3_start_time)
    time4 =    (time4_stop_time - time4_start_time)
    
    WEIGHTS = [weights1, weights2, weights3, weights4]
    TIMES = [time1, time2, time3, time4]
    
    return [WEIGHTS, TIMES]

def findrange(number=0):
    return range(number)


#########
## Score 1 ##   
# score by simply counting instances of answer phrases, without question keywords
#
#########

def getSimpleAnswerPhraseScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
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


#########
## Score 2 ##   
# score by simply counting instances of answer keywords, without question keywords
#
#########

def getSimpleAnswerKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        print answertokens
        answerrange = findrange(len(answertokens))
        # may need to adjust 0 value here
        splitanswertokens = [t for t in answertokens if len(t) > 0 and (t.lower() not in ignored_words)]
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

#########
## Score 3 ##   
# score using question keywords and fixed weights
#
#########

def getWeightedQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    rangevalue = getRangeValue()
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        # may need to adjust 0 value here
        splitanswertokens = [t for t in answertokens if len(t) > 0 and (t.lower() not in ignored_words)]
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

#########
## Score 4 ##   
# use function below to score, using question keywords and answer keywords
#
#########

def getFunctionQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        answerrange = findrange(len(answertokens))
        # may need to adjust 2 value here depending on answer choices
        splitanswertokens = [t for t in answertokens if len(t) > 0 and (t.lower() not in ignored_words)]
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
    
