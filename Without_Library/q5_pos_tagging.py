sentence = "The cat runs quickly and played happily"

words = sentence.split()

for w in words:

    # Rule-based POS tagging

    if w.endswith("ly"):
        pos = "Adverb"

    elif w.endswith("ing") or w.endswith("ed"):
        pos = "Verb"

    elif w.lower() in ["the", "a", "an"]:
        pos = "Article"

    elif w.lower() in ["and", "or", "but"]:
        pos = "Conjunction"

    else:
        pos = "Noun"

    print(w, "->", pos)