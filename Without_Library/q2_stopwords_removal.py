text = "this is a simple NLP program"

stopwords = ["is", "a", "the", "in"]

words = text.split()

cleaned = []

for w in words:
    if w not in stopwords:
        cleaned.append(w)

print("Cleaned Text:", " ".join(cleaned))