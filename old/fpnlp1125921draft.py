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

ignored_words = stopwords.words('english')

def getGoogleLinks(query, pages = 1):
    links = []

    # Build request information:
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    query = query.lstrip().rstrip()
    query = re.sub('[ ]+', '+', query)
    base = "http://www.google.com/search?q=" + query

    for i in range(0, pages):
        # Get full page source
        url = base + "&start=" + str(i * 10)
        req = urllib2.Request(url,None,headers)
        f = urllib2.urlopen(req)
        source = f.read()

        # Cut out garbage
        source = source.partition("id=\"search\"")[2]
        source = source.partition("id=\"botstuff\"")[0]

        # Get external links (not Google's)
        l = re.findall("class=\"r\"><a href=\"(http://[^\"]*)",source)
        for link in l:
            links.append(link)
    return links

def getKeywords(query):
    browntext = brown.words()
    browndist = nltk.FreqDist(browntext)

    reuterstext = reuters.words()
    reutersdist = nltk.FreqDist(reuterstext)

    text = nltk.word_tokenize(query)

    tagged = nltk.pos_tag(text)
    filtered = []
    for pair in tagged:
        if pair[1] in ['JJ', 'N', 'NNP', 'VB', 'VBD', 'VBG', 'VBN', 'NUM']: # add numbers, dates
            filtered.append(pair[0])
    filtereddist = {}
    for word in filtered:
        filtereddist[word] = browndist[word] + reutersdist[word]
    sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
    keywords = [sortedlist[0][0], sortedlist[1][0]]
    return keywords

def findrange(number=0):
    return range(number)

def compute_score(queryphrase="", keywords=[], answers=[], urls=[], scorevalue=0, rangevalue=0, left=False, right=False):

    urls = getGoogleLinks(queryphrase, 3)
    if keywords == []:
        keywords = getKeywords(queryphrase)
    print(keywords)
    keyword = True
    
    combinedtokens = []
    for url in urls:
        html = urlopen(url).read()
        raw = nltk.clean_html(html)
        combinedtokens += nltk.word_tokenize(raw)
    combinedtokens = [t for t in combinedtokens if len(t) > 2 and t.lower() not in ignored_words]
    querytokens = nltk.word_tokenize(queryphrase)

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
        if len(keywords) != 1 and len(keywords) != 2:
            print "error, number of keywords must be one or two"
            return 4
        if len(keywords) == 2:
            for instanceone in instances[keywords[0]]:
                for instancetwo in instances[keywords[1]]:
                    if (instancetwo - instanceone) < 20 and (instanceone, instancetwo) not in combinedinstances:
                        combinedinstances.append((instanceone, instancetwo))
                    elif (instanceone - instancetwo) < 20 and (instancetwo, instanceone) not in combinedinstances:
                        combinedinstances.append((instancetwo, instanceone))
        # print(combinedinstances)
        relevanttokens = []
        if len(keywords) == 1:
            for instance in instances[keywords[0]]:
                relevanttokens += combinedtokens[instance - rangevalue : instance + rangevalue]
        else:
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
    
# Booth: 372, Mary: 15, "assassinated" and "Abraham"

compute_score(queryphrase="Who assassinated Abraham Lincoln", keywords=[], answers=["John Wilkes Booth", "Mary Todd Lincoln", "Stonewall Jackson", "Lee Harvey Oswald"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# 1919: 1275, 1815: 3, 1939: 40, 1914: 80, "Treaty" and "Versailles" [WANT: signed]

# compute_score(queryphrase="When was the Treaty of Versailles signed", keywords=[], answers=["1919", "1939", "1914", "1815"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# Robespierre: 11, Marie: 21, King Louis XVI: 71, "overthrown" and "king" [WANT: (K)ing?]

# compute_score(queryphrase="What king was overthrown during the French Revolution", keywords=[], answers=["Louis XIV", "Louis XVI", "Robespierre", "Marie Antoinette"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# 1976: 472, 1975: 137, 1974: 135, 1973: 105, "Zhou" and "Enlai" [WANT: die]

# compute_score(queryphrase="What year did Zhou Enlai die", keywords=[], answers=["1973", "1974", "1975", "1976"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# Kwame Nkrumah: 924, all others: 0, "first" and "Ghana" [WANT: president?]

# compute_score(queryphrase="Who was the first president of Ghana", keywords=[], answers=["Kofi Annan", "Kwame Nkrumah", "Nelson Mandela", "Idi Amin"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# 9: 305, 3: 93, 12: 12, 7: 45, "Beethoven" and "many", 5: 272

# compute_score(queryphrase="How many symphonies did Beethoven write", keywords=[], answers=["3", "7", "9", "5"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# 32: 198, 23: 36, 21: 131, 14: 36, "Beethoven" and "many"

# compute_score(queryphrase="How many piano sonatas did Beethoven write", keywords=[], answers=["32", "21", "14", "23"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# South Carolina: 133, Maryland: 6, Georgia: 27, Virginia: 34, "secede" and "Union"

# compute_score(queryphrase="What was the first state to secede from the Union", keywords=[], answers=["South Carolina", "Virginia", "Georgia", "Maryland"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# lab coat: 25

# compute_score(queryphrase="What did the trumpeter in the Art Ensemble of Chicago wear in concert", keywords=[], answers=["lab coat", "sunglasses", "suit", "hat"], urls=[], scorevalue=1, rangevalue=100, left=True, right=True)

# polo: 1, horse racing: 3, baseball: 154, football: 55, "organized" and "became", tightening range and only including keyword 1664 does not help horse racing beat baseball

# compute_score(queryphrase="What became America's first organized sport in 1664", keywords=["1664"], answers=["horse racing", "baseball", "football", "polo"], urls=[], scorevalue=1, rangevalue=10, left=True, right=True)

# compute_score(queryphrase="What French port did 200,000 British troops leave on June 4, 1940", keywords=["200,000", "1940"], answers=["Dunkirk", "Paris", "London", "Normandy"], urls=[], scorevalue=1, rangevalue=50, left=True, right=True)

# Better keyword generation (favor verbs?), accomodate more than two keywords, move beyond adjectives/nouns/verbs to include number, dates, etc. / favor verbs, proper nouns, dates

# Analyze question to filter answers

# Move beyond multiple choice to general N-grams

# Answer harder questions

# More precise selection of text from Google results (related to keywords)

# Different weights: different synonyms (original words higher), different combinations of keywords (most preferred keywords higher), different ranges (narrow ranges higher)

def getKeywordsDraft(query):
    browntext = brown.words()
    browndist = nltk.FreqDist(browntext)

    reuterstext = reuters.words()
    reutersdist = nltk.FreqDist(reuterstext)

    text = nltk.word_tokenize(query)

    tagged = nltk.pos_tag(text)

    print(tagged)

    filteredparts = []
    for pair in tagged:
        if pair[1] in ['FW', 'JJ', 'JJR', 'JJS', 'JJT', 'N', 'NN', 'NNP', 'NNS', 'NP', 'NPS', 'NR', 'RB', 'RBR', 'RBT' 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'NUM', 'CD', 'OD']:
            filteredparts.append(pair[0])
    print(filteredparts)
    filtereddist = {}
    for word in filteredparts:
        frequency = browndist[word] + reutersdist[word]
        print word
        print frequency
        if frequency < 600:
            filtereddist[word] = frequency
    sortedlist = sorted(filtereddist.items(), key=itemgetter(1))
    print(sortedlist)
    return sortedlist

getKeywordsDraft("What woman was arrested for voting in the 1872 election for U.S. president")
