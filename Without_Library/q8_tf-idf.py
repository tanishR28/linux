text = "NLP is easy and NLP is powerful"

words = text.lower().split()

total_words = len(words)

unique_words = set(words)

print("Word\tCount\tTF")

for w in unique_words:

    count = words.count(w)

    tf = count / total_words

    print(w, "\t", count, "\t", round(tf, 2))

#tf-idf
import math

documents = [
    "NLP is easy",
    "NLP is powerful"
]

# Convert documents into word lists
docs = [doc.lower().split() for doc in documents]

# All unique words
all_words = set()

for d in docs:
    all_words.update(d)

print("Word\tTF\tIDF\tTF-IDF")

# Using first document
words = docs[0]

total_words = len(words)

for w in all_words:

    # TF
    count = words.count(w)
    tf = count / total_words

    # IDF
    doc_count = 0

    for d in docs:
        if w in d:
            doc_count += 1

    idf = math.log(len(documents) / doc_count)

    # TF-IDF
    tfidf = tf * idf

    print(w, "\t", round(tf,2), "\t", round(idf,2), "\t", round(tfidf,2))