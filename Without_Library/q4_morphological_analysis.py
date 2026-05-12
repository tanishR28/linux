words = {
    "unhappiness": ["un", "happy", "ness"],
    "replayed": ["re", "play", "ed"],
    "international": ["inter", "nation", "al"]
}

bound = ["un", "re", "ed", "ness", "al", "inter"]

for word, morphemes in words.items():

    print("\nWord:", word)

    for m in morphemes:

        if m in bound:
            print(m, "-> Bound Morpheme")

        else:
            print(m, "-> Free Morpheme")