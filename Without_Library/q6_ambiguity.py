sentence = "I saw the man with a telescope"

# Words that usually create semantic ambiguity
semantic_words = ["bank", "bat", "crane", "park"]

# Words/patterns that may create syntactic ambiguity
syntactic_patterns = ["with", "on", "in"]

words = sentence.lower().split()

flag = False

# Check semantic ambiguity
for w in words:
    if w in semantic_words:
        print("Semantic Ambiguity Detected")
        flag = True
        break

# Check syntactic ambiguity
if not flag:
    for w in words:
        if w in syntactic_patterns:
            print("Syntactic Ambiguity Detected")
            flag = True
            break

# No ambiguity
if not flag:
    print("No Ambiguity Detected")