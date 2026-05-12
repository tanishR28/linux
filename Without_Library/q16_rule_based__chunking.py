sentence = "The big dog runs"

words = sentence.lower().split()

# Word categories
det = ["the", "a", "an"]
adj = ["big", "small", "smart"]
noun = ["dog", "cat", "student"]

# Chunking Rule: Det + Adj + Noun

if (len(words) >= 3 and
    words[0] in det and
    words[1] in adj and
    words[2] in noun):

    print("Noun Phrase Found:")
    print(words[0], words[1], words[2])

else:
    print("No Noun Phrase Found")