import nltk
from urllib import urlopen
from nltk.collocations import *
url = "http://www.nytimes.com/2011/11/18/nyregion/protesters-clash-with-police-in-lower-manhattan.html"
html = urlopen(url).read()
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.collocations() # THIS GENERATES BIGRAMS
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(tokens)
finder.apply_word_filter(lambda w: len(w) < 3)
finder.apply_freq_filter(3)
scored = finder.score_ngrams(trigram_measures.raw_freq)
print(scored) # THIS PRINTS TRIGRAMS