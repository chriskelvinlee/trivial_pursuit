# Contains all the questions we use to run tests

#global tp_Questions0


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

tp_Questions2 = [
    ["Which of these numbers is a thousand thousands", ["a million", "a billion", "a trillion"],0,7],
    ["Where did the bear go to see what he could see in a popular old song", ["under the sea", "over the mountain", "through the woods"],1,8],
    ["What stroke do swimmers usually use in a freestyle race", ["front crawl", "butterfly", "breaststroke"],0,9]
    ]


tp_Questions3 = [
    ["What kind of beans are used to make Boston baked beans", ["black beans", "navy beans", "lima beans"],1,10], #brown33
    ["What does an Elvis impersonator usually wear", ["a rhinestone jumpsuit", "a big cowbow hat", "a black satin cape"],0,11], #blue33
    ["Where did Aesop write most of his animal fables", ["on safari", "in prison", "at zoo"], 1, 12] #yellow91
]

tp_Questions4 = [
    ["What is the weather forecast if there is a red sky at night", ["fair", "cloudy", "storm coming"],0,13], #pink3
    ["What sport do you lunge, thrust, and parry in", ["croquet", "bowling", "fencing"],2,14], #orange3
    ["Which country did Lizzie McGuire travel to in the first Lizzie McGuire movie", ["Italy", "France", "England"], 0, 15] #green3
]   

tp_Questions5 = [
    ["What is the nickname for a fighter pilot", ["top banana", "top dog", "top gun"],2,16], #brown3
    ["What words does The Gold rule begin with", ["Thou shall not", "Do unto others", "All that glitters"],1,17], #blue3
    ["What did the words yankee doodle mean at the time of the Revolution", ["a fashionable dude", "a dishonest fool", "a proper gentleman"], 1, 18] #yellow3
]

tp_Questions6 = [
    ["Which of these describes the tail of a healthy platypus", ["fat and strong", "long and squishy", "short and pinkish"],0,19],
    ["Which sport do players use a stick to cradle the ball", ["field hockey", "ice hockey", "lacrosse"],2,20],
    ["Whose favorite place to swim is in his money bin", ["Scrooge McDuck", "Richie Rich", "Ebenezer Scrooge"],0,21]
]

tp_Questions7 = [
    ["What material makes up the most kind of trash in US landfills", ["paper", "plastic", "metal"],0,22],
    ["Where's your funny bone located", ["near your elbow", "on your wrist", "just below your shoulder"],0,23],
    ["What did the word dude mean 100 years ago", ["a crook", "a cowboy", "a classy dresser"],2,24]
]

tp_Questions8 = [
    ["How long does it take an albatross egg to hatch", ["1 week", "1 month", "80 days"],2,25],
    ["What kind of dive is a full gainer", ["a forward dive with a twist", "a forward dive with a somesault", "a backward dive with a twist"],0,26],
    ["What does xylphone music sound the most like", ["bells", "drums", "rattles"],0,27]
]

tp_Questions9 = [
    ["What do they say instead of hello in France", ["bonjour", "bon appetit", "tres bien"],0,28],
    ["Which of these is supposed to bring good luck", ["seeing three butterflies", "spilling salt", "eating black-eyed peas on New Year's Day"],2,29],
    ["What was illegal for kids to do on a Sunday in a colonial New England village", ["walk to church", "kiss their parents", "eat lunch"],1,30]
]

tp_Questions10 = [
    ["Which of these sea creatures is not a mammal", ["a sea cow", "a sea lion", "a sea horse"],2,31],
    ["What goes clink, clink, clink in a song about the wheels of a bus going round and round", ["the brakes", "the windshield wipers", "the money"],2,32],
    ["How much time does it take for the space shuttle to get into space", ["about 10 minutes", "4 hours", "2 days"],0,33]
]

tp_Questions11 = [
    ["How do you make bagels shiny", ["boil them before baking", "buff them", "add vegetable oil to the dough"],0,34],
    ["Which face on Mount Rushmore was actually blown up and sculpted again in a better location", ["Washington", "Jefferson", "Lincoln"],1,35],
    ["What does the Sphinx wear on its head", ["a crown", "a headdress", "a helmet"],1,36]
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
