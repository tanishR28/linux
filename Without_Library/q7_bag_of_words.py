sentences = [
    "I like NLP",
    "I like AI",
    "AI is powerful"
]

# Step 1: Create Vocabulary
vocab = []

for s in sentences:
    for word in s.split():

        # Convert to lowercase
        word = word.lower()

        if word not in vocab:
            vocab.append(word)

print("Vocabulary:")
print(vocab)

# Step 2: Create BoW Matrix
print("\nBag of Words Matrix:")

for s in sentences:

    vector = []

    words = s.lower().split()

    for v in vocab:
        vector.append(words.count(v))

    print(vector)