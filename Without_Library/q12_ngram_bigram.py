text = "I love NLP and I love AI"

words = text.split()

# Create bigrams
bigrams = {}

for i in range(len(words)-1):

    current_word = words[i]
    next_word = words[i+1]

    # Store next word
    bigrams[current_word] = next_word

print("Bigrams:")
print(bigrams)

# Generate Text
word = "I"

generated = word

for i in range(5):

    if word in bigrams:

        next_word = bigrams[word]

        generated += " " + next_word

        word = next_word

print("\nGenerated Text:")
print(generated)