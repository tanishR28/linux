from nltk.tokenize import word_tokenize

words = ["unhappiness", "replayed", "international"]

prefixes = ["un", "re", "inter"]
suffixes = ["ness", "ed", "al"]

for word in words:

    print("\nWord:", word)

    for p in prefixes:
        if word.startswith(p):
            print(p, "-> Bound Morpheme")

    for s in suffixes:
        if word.endswith(s):
            print(s, "-> Bound Morpheme")

    # Root words
    if word == "unhappiness":
        print("happy -> Free Morpheme")

    elif word == "replayed":
        print("play -> Free Morpheme")

    elif word == "international":
        print("nation -> Free Morpheme")