# Contains all the questions we use to run tests

global tp_Questions
tp_Questions = [
["What is each member of a winning Super Bowl team given", ["a bronzed jersey", "a green jacket", "a ring"], 2],
["How much time does it take for the space shuttle to get into space", ["about 10 minutes", "4 hours", "2 days"], 0],
]


"""debug code for interpreter
queryphrase="What is each member of a winning Super Bowl team given"
answers=["a bronzed jersey", "a green jacket", "a ring"]
urls = getGoogleLinks(queryphrase, 1)
keywords = getSimpleQuestionKeywords(queryphrase)
weightedquestionkeywords = getWeightedQuestionKeywords(queryphrase)
weightedanswerkeywords = getAnswerKeywords(answers)
querytokens = nltk.word_tokenize(queryphrase)
combinedtokens = getTokens(urls)
instances = getInstances(keywords, combinedtokens)

"""