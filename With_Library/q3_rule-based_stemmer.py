import nltk

nltk.download('wordnet')

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

words = ["playing", "worked", "studies"]

# Stemmer
ps = PorterStemmer()

# Lemmatizer
lm = WordNetLemmatizer()

for w in words:

    stem = ps.stem(w)

    lemma = lm.lemmatize(w)

    print("Word:", w)
    print("Stem:", stem)
    print("Lemma:", lemma)
    print()