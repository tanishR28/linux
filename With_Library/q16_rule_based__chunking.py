import nltk

# POS Tagged Sentence
sentence = [
    ("The", "DT"),
    ("big", "JJ"),
    ("dog", "NN"),
    ("runs", "VB")
]

# Chunk Grammar
grammar = "NP: {<DT><JJ><NN>}"

# Chunk Parser
cp = nltk.RegexpParser(grammar)

result = cp.parse(sentence)

print(result)