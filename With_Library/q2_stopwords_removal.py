import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

sentence = "this is a simple NLP program"

# Stopword List
stop_words = stopwords.words('english')

words = sentence.split()

cleaned = []

for w in words:
    if w not in stop_words:
        cleaned.append(w)

print("Cleaned Text:")
print(" ".join(cleaned))