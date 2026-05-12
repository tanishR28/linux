import nltk

from nltk.util import bigrams

text = "I love NLP and I love AI"

words = text.split()

# Generate Bigrams
bg = list(bigrams(words))

print("Bigrams:")
print(bg)

# Generate Text
generated = ""

for b in bg:
    generated += b[0] + " "

generated += bg[-1][1]

print("\nGenerated Text:")
print(generated)