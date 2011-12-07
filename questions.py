# Contains all the questions we use to run tests

global tp_Questions0


tp_Questions0 = [
    ["What is each member of a winning Super Bowl team given", ["a bronzed jersey", "a green jacket", "a ring"], 2, 1],
    ["How much time does it take for the space shuttle to get into space", ["about 10 minutes", "4 hours", "2 days"], 0, 2],
    ["Who were named lobsterbacks during the Amrican Revolution", ["maine fisherman", "the redcoats", "the minuteman"],1,3]
]

tp_Questions1 = [
    ["What does a pugilist wear on his hands", ["ski gloves", "boxing gloves", "oven mitts"],1,4], #blue5
    ["How is the mail order bridge Sarah described in a book title", ["plump and pretty", "plain and tall", "long and skinny"],1,5], #green5
    ["What was discovered in the Klondike back in the 1890s", ["the abominable snowman", "a flying saucer", "gold"], 2, 6] #yellow5
]   


tp_Questions3 = [
    ["What kind of beans are used to make Boston baked beans", ["black beans", "navy beans", "lima beans"],1,10], #brown33
    ["What does an Elvis impersonator usually wear", ["a rhinestone jumpsuit", "a big cowbow hat", "a black satin cape"],0,11], #blue33
    ["Where did Aesop write most of his animal fables", ["on safari", "in prison", "at zoo"], 1, 12] #yellow91
]

tp_Questions4 = [
    ["What is the weather forecast if tere is a red sky at night", ["fair", "cloudy", "storm coming"],0,13], #pink3
    ["What sport do you lunge, thrust, and parry in", ["croquet", "bowling", "fencing"],2,14], #orange3
    ["Which country did Lizzie McGuire travel to in the first Lizzie McGuire movie", ["Italy", "France", "England"], 0, 15] #green3
]   

tp_Questions5 = [
    ["What is the nickname for a fighter pilot", ["top banana", "top dog", "top gun"],2,16], #brown3
    ["What words does The Gold rule begin with", ["Thou shall not", "Do unto others", "All that glitters"],1,17], #blue3
    ["What did the words yankee doodle mean at the time of the Revolution", ["a fashionable dude", "a dishonest fool", "a proper gentleman"], 1, 18] #yellow3
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