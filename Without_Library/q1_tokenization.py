text = "NLP is interesting. It is used in AI."

# Sentence Tokenization
sentences = text.split(".")

# Remove empty strings and spaces
sentences = [s.strip() for s in sentences if s.strip()]

# Word Tokenization
words = text.replace(".", "").split()

print("Sentences:", sentences)
print("Words:", words)
print("Total Tokens:", len(words))