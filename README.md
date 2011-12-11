#Answering Trivial Pursuit questions
This project provides code that uses natural language processing to answer trivia questions. 

##Summary of included files
* determine.py: Given results, determines answer and confidence
* googleResults.py: Returns the top pages returned by Google, given a query
* importcache.py: Reads in previously cached results
* output.py: Caches results
* questions.py: Encoded triplets of sample questions and answers for testing
* scoring.py: 4 ways to calculate scores, and a method to use them all
* test.py: Runs provided questions through given scoring function
* tp.py: Wrapper to handle import and update
* trivialpursuitfunctions.py: Given a question and answer options, finds keywords and instances of them
* weights.py: Functions to determine how heavily each kind of keyword should be weighted
