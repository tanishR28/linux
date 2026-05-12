subjects = ["Ram", "Shyam", "He"]
verbs = ["eats", "likes", "plays"]
objects = ["mango", "cricket", "football"]

sentence = "Ram eats mango"

words = sentence.split()

if (words[0] in subjects and
    words[1] in verbs and
    words[2] in objects):

    print("Valid Sentence")

else:
    print("Invalid Sentence")


#

# Grammar Rules

grammar = {
    "SUBJECT": ["ram", "john", "she", "he", "they"],
    "VERB": ["eats", "runs", "writes", "plays"],
    "OBJECT": ["apple", "football", "book"]
}

# User Input
sentence = input("Enter sentence: ")

words = sentence.lower().split()

pattern = []

# Identify each word type
for w in words:

    if w in grammar["SUBJECT"]:
        pattern.append("SUBJECT")

    elif w in grammar["VERB"]:
        pattern.append("VERB")

    elif w in grammar["OBJECT"]:
        pattern.append("OBJECT")

    else:
        pattern.append("UNKNOWN")

# Valid CFG patterns
valid_patterns = [
    ["SUBJECT", "VERB"],
    ["SUBJECT", "VERB", "OBJECT"]
]

# Check validity
if pattern in valid_patterns:
    print("Valid Sentence")
else:
    print("Invalid Sentence")

print("Pattern:", pattern)