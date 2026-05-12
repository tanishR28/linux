import nltk
from nltk import CFG

# Define Grammar
grammar = CFG.fromstring("""

S -> NP VP
NP -> 'Ram'
VP -> V NP
V -> 'eats'
NP -> 'mango'

""")

# Parser
parser = nltk.ChartParser(grammar)

sentence = "Ram eats mango".split()

# Check Validity
for tree in parser.parse(sentence):
    print("Valid Sentence")
    print(tree)