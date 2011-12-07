# GENERAL TEST RESULTS

# compute_score(queryphrase="Which of these describes the tail of a healthy platypus", answers=["fat and strong", "long and squishy", "short and pinkish"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['platypus', 'tail', 'describes', 'healthy']
{'fat and strong': 32, 'short and pinkish': 21, 'long and squishy': 63} [INCORRECT]
{'fat and strong': 87440, 'short and pinkish': 43, 'long and squishy': 41261} [CORRECT]"""

# compute_score(queryphrase="Which sport do players use a stick to cradle the ball", answers=["field hockey", "ice hockey", "lacrosse"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['sport', 'players', 'stick', 'ball'] [BAD: WHY NOT 'CRADLE'?]
{'lacrosse': 1790, 'ice hockey': 28, 'field hockey': 294} [CORRECT]
{'lacrosse': 281420, 'ice hockey': 5544, 'field hockey': 71962} [CORRECT]"""

# compute_score(queryphrase="Whose favorite place to swim is in his money bin", answers=["Scrooge McDuck", "Richie Rich", "Ebenezer Scrooge"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['Whose', 'bin', 'favorite'] [WANT TO INCLUDE PLACE, SWIM]
{'Richie Rich': 13, 'Ebenezer Scrooge': 346, 'Scrooge McDuck': 1075} [CORRECT]
{'Richie Rich': 18, 'Ebenezer Scrooge': 1259, 'Scrooge McDuck': 4261} [CORRECT]"""

# compute_score(queryphrase="What material makes up the most kind of trash in US landfills", answers=["paper", "plastic", "metal"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['landfills', 'trash', 'US', 'material', 'makes', 'kind'] [DOES NOT CAPTURE IDEA OF MOST]
{'paper': 1710, 'metal': 90, 'plastic': 1790} [INCORRECT]
{'paper': 10130, 'metal': 120, 'plastic': 16120} [INCORRECT]"""

# compute_score(queryphrase="What material makes up the most kind of trash in US landfills", keywords=["landfills", "trash", "material", "most"], answers=["paper", "plastic", "metal"])

"""['landfills', 'trash', 'material', 'most']
{'paper': 1710, 'metal': 90, 'plastic': 1790}
{'paper': 6060, 'metal': 120, 'plastic': 10710}"""

# compute_score(queryphrase="What material makes up the most kind of trash in US landfills", keywords=["landfills", "trash", "material", "most"], answers=["paper", "plastic", "metal"])

"""Jacking up keyword scores 100/10 and 1/5 does not help,
['landfills', 'trash', 'material', 'most']
{'paper': 17100, 'metal': 900, 'plastic': 17900}
{'paper': 1026243000, 'metal': 3600, 'plastic': 11125468700}"""

# compute_score(queryphrase="Where's your funny bone located", answers=["near your elbow", "on your wrist", "just below your shoulder"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
[''s', 'bone', 'funny', 'located'] [WANT TO ELIMINATE THE FIRST FRAGMENT]
{'on your wrist': 3, 'near your elbow': 75, 'just below your shoulder': 4} [CORRECT]
{'on your wrist': 26, 'near your elbow': 392258114, 'just below your shoulder': 4184} [CORRECT]"""

# compute_score(queryphrase="What did the word dude mean 100 years ago", answers=["a crook", "a cowboy", "a classy dresser"])

# [NOTE: removed quotes around "dude"--make this automatic]
"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['dude', 'word', 'mean'] [NO SENSE HERE OF THE PAST]
{'a classy dresser': 3, 'a cowboy': 36} [INCORRECT]
{'a classy dresser': 5, 'a cowboy': 92} [INCORRECT]"""

# compute_score(queryphrase="How long does it take an albatross egg to hatch", answers=["1 week", "1 month", "80 days"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['albatross', 'egg'] [WANT TO INCLUDE LONG, HATCH]
{'1 month': 5, '1 week': 5, '80 days': 172} [CORRECT]
{'1 month': 8, '1 week': 6, '80 days': 1085} [CORRECT]"""

# compute_score(queryphrase="What kind of dive is a full gainer", answers=["a forward dive with a twist", "a forward dive with a somersault", "a backward dive with a twist"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['gainer', 'dive', 'kind'] [WANT TO INCLUDE FULL]
{'a forward dive with a somersault': 22, 'a backward dive with a twist': 1, 'a forward dive with a twist': 23} [CLOSE, INCORRECT]
{'a forward dive with a somersault': 26, 'a backward dive with a twist': 1, 'a forward dive with a twist': 27} [CLOSE, INCORRECT]"""

# compute_score(queryphrase="What kind of dive is a full gainer", keywords= ["full", "gainer", "dive"], answers=["a forward dive with a twist", "a forward dive with a somersault", "a backward dive with a twist"])

"""['full', 'gainer', 'dive']
{'a forward dive with a somersault': 22, 'a backward dive with a twist': 1, 'a forward dive with a twist': 23}
{'a forward dive with a somersault': 26, 'a backward dive with a twist': 1, 'a forward dive with a twist': 27}"""

# compute_score(queryphrase="What kind of dive is a full gainer", keywords= ["full", "gainer", "dive"], answers=["a forward dive with a twist", "a forward dive with a somersault", "a backward dive with a twist"])

# HARD QUESTION: dive involves both forward and backward elements: base = "https://www.google.com/search?gcx=w&ix=c1&sourceid=chrome&ie=UTF-8&q=What+kind+of+dive+is+a+full+gainer#hl=en&safe=off&sa=X&ei=_PbaTvzBHKbZ0QG5h_XADQ&ved=0CBgQvgUoAA&q=What+kind+of+dive+is+a+full+gainer&nfpr=1&bav=on.2,or.r_gc.r_pw.,cf.osb&fp=f694e5d8525906a7&biw=1063&bih=565"

# compute_score(queryphrase="What does xylophone music sound the most like", answers=["bells", "drums", "rattles"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['xylophone', 'music', 'sound'] [WANT TO INCLUDE LIKE COMPARISON]
{'rattles': 10, 'drums': 290, 'bells': 140} [INCORRECT]
{'rattles': 20, 'drums': 860, 'bells': 640} [INCORRECT]"""

# compute_score(queryphrase="What does xylophone music sound the most like", keywords=["xylophone", "music", "sound", "most", "like"], answers=["bells", "drums", "rattles"])

"""['xylophone', 'music', 'sound', 'most', 'like']
{'rattles': 10, 'drums': 290, 'bells': 140}
{'rattles': 20, 'drums': 6070, 'bells': 2140}"""

# compute_score(queryphrase="What does xylophone music sound the most like", keywords=["xylophone", "music", "sound", "most", "like"], answers=["bells", "drums", "rattles"])

"""Jacking up keyword scores 100/10 fragments 1/5 does not help:
['xylophone', 'music', 'sound', 'most', 'like']
{'rattles': 100, 'drums': 2900, 'bells': 1400}
{'rattles': 1000, 'drums': 10153653500, 'bells': 123323000}"""

# compute_score(queryphrase="What do they say instead of hello in France", answers=["bonjour", "bon appetit", "tres bien"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['hello', 'instead', 'France']
{'tres bien': 18, 'bonjour': 170, 'bon appetit': 6} [CORRECT]
{'tres bien': 24, 'bonjour': 82900, 'bon appetit': 7} [CORRECT]"""

# compute_score(queryphrase="Which of these is supposed to bring good luck", answers=["seeing three butterflies", "spilling salt", "eating black-eyed peas on New Year's Day"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['luck', 'supposed']
{'seeing three butterflies': 16, 'spilling salt': 17, "eating black-eyed peas on New Year's Day": 523} [CORRECT]
{'seeing three butterflies': 1221, 'spilling salt': 1151, "eating black-eyed peas on New Year's Day": 1416} [CORRECT BUT GETTING WORSE!]"""

# compute_score(queryphrase="What was illegal for kids to do on a Sunday in a colonial New England village", answers=["walk to church", "kiss their parents", "eat lunch"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['colonial', 'kids', 'illegal', 'village', 'Sunday', 'England']
{'kiss their parents': 35, 'eat lunch': 34, 'walk to church': 106} [INCORRECT]
{'kiss their parents': 3541, 'eat lunch': 892, 'walk to church': 3866} [CLOSE BUT INCORRECT]"""

# compute_score(queryphrase="What was illegal for kids to do on a Sunday in a colonial New England village", keywords=["colonial", "kids", "illegal", "village", "Sunday", "New England"], answers=["walk to church", "kiss their parents", "eat lunch"])

"""['colonial', 'kids', 'illegal', 'village', 'Sunday', 'New England']
{'kiss their parents': 35, 'eat lunch': 34, 'walk to church': 106}
{'kiss their parents': 2511, 'eat lunch': 891, 'walk to church': 3744}"""

# compute_score(queryphrase="What was illegal for kids to do on a Sunday in a colonial New England village", keywords=["colonial", "kids", "illegal", "village", "Sunday", "New England"], answers=["walk to church", "kiss their parents", "eat lunch"])

"""With jacked up scores: new score 100/times 10, fragment 1/times 5
['colonial', 'kids', 'illegal', 'village', 'Sunday', 'New England']
{'kiss their parents': 35, 'eat lunch': 34, 'walk to church': 106}
{'kiss their parents': 11516763, 'eat lunch': 2065038, 'walk to church': 8025882} [NOW CORRECT, WITH EMPHASIS ON KEYWORDS 100/10/1/5!]"""


# compute_score(queryphrase="Which of these sea creatures is not a mammal", answers=["a sea cow", "a sea lion", "a sea horse"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['mammal', 'creatures', 'sea'] [HARD QUESTION, WANT TO CAPTURE NEGATION]
{'a sea lion': 10, 'a sea cow': 5, 'a sea horse': 4} [INCORRECT]
{'a sea lion': 37, 'a sea cow': 8, 'a sea horse': 4} [INCORRECT]"""

# compute_score(queryphrase="What is each member of a winning Super Bowl team given", answers=["a bronzed jersey", "a green jacket", "a ring"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['Bowl', 'Super', 'winning', 'team', 'member']
{'a green jacket': 4, 'a bronzed jersey': 1, 'a ring': 60} [CORRECT]
{'a green jacket': 4194572, 'a bronzed jersey': 2, 'a ring': 8814712766} [CORRECT]"""

# compute_score(queryphrase="What goes clink, clink, clink in a song about the wheels of a bus going round and round", answers=["the brakes", "the windshield wipers", "the money"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['clink', 'wheels', 'bus', 'song', 'goes', 'round', 'going']
{'the money': 28, 'the windshield wipers': 36} [INCORRECT]
{'the money': 145725194754, 'the windshield wipers': 53643839744} [CORRECT, BY A LITTLE]"""

# compute_score(queryphrase="How much time does it take for the space shuttle to get into space", answers=["about 10 minutes", "4 hours", "2 days"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['shuttle', 'space'] [WANT TO INCLUDE TIME]
{'about 10 minutes': 64, '4 hours': 37, '2 days': 36} [CORRECT]
{'about 10 minutes': 116327, '4 hours': 65805, '2 days': 1249} [CORRECT]"""

# compute_score(queryphrase="How do you make bagels shiny", answers=["boil them before baking", "buff them", "add vegetable oil to the dough"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['bagels', 'shiny']
{'add vegetable oil to the dough': 687, 'boil them before baking': 355} [INCORRECT]
{'add vegetable oil to the dough': 5111, 'boil them before baking': 5715} [CORRECT, BY A LITTLE]"""

# compute_score(queryphrase="Which face on Mount Rushmore was actually blown up and sculpted again in a better location", answers=["Washington", "Jefferson", "Lincoln"])

"""Results, with answer choices broken into fragments, with scores of 1 for fragment, 10 for whole answer, times 2 if near keywords:
['Rushmore', 'sculpted', 'blown', 'Mount', 'location', 'actually', 'face'] [WANT CAPTURE BLOWN AND SCULPTED AGAIN]
{'Lincoln': 2950, 'Jefferson': 820, 'Washington': 2400} [INCORRECT]
{'Lincoln': 97412080, 'Jefferson': 29111570, 'Washington': 8466910} [INCORRECT]"""

# compute_score(queryphrase="Which face on Mount Rushmore was actually blown up and sculpted again in a better location", keywords=["Rushmore", "sculpted", "blown up", "actually", "Mount", "location", "face"], answers=["Washington", "Jefferson", "Lincoln"])

# Lincoln wins this with more keywords -- need to emphasize "blown up" in particular

"""['Rushmore', 'sculpted', 'blown up', 'face']
{'Lincoln': 2950, 'Jefferson': 820, 'Washington': 2400}
{'Lincoln': 86130, 'Jefferson': 206060, 'Washington': 35550} [NOW CORRECT WITH NEW KEYWORDS, SAME OLD 10/2/1/2 SCORING, NEED TO USE 'BLOWN UP'!]"""

"""['Rushmore', 'sculpted', 'blown up', 'face']
{'Lincoln': 111013167476500 (15), 'Jefferson': 10011012455538900 (17), 'Washington': 2013458743500} WITH JACKED-UP KEYWORDS"""
