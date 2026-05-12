import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize

text = "NLP is interesting. It is used in AI."

# Sentence Tokenization
sentences = sent_tokenize(text)

print("Sentences:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)

print("\nWords:")
print(words)

# Total Tokens
print("\nTotal Tokens:", len(words))