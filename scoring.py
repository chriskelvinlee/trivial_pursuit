import nltk

# score by simply counting instances of answer phrases, without question keywords
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

def findrange(number=0):
    return range(number)

# score by simply counting instances of answer keywords, without question keywords
def getSimpleAnswerKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    scores = {}
    tokenrange = findrange(len(combinedtokens))
    for answer in answers:
        answertokens = nltk.word_tokenize(answer)
        print answertokens
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
def getWeightedQuestionKeywordScores(answers, keywords, combinedtokens, instances, weightedquestionkeywords, weightedanswerkeywords):
    rangevalue = 50
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
