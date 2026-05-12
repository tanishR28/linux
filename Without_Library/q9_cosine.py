import math

A = [1, 2, 3]
B = [2, 1, 3]

# Dot Product
dot = 0

for i in range(len(A)):
    dot += A[i] * B[i]

# Magnitude of A
magA = math.sqrt(sum(x*x for x in A))

# Magnitude of B
magB = math.sqrt(sum(x*x for x in B))

# Cosine Similarity
cosine = dot / (magA * magB)

print("Dot Product:", dot)
print("Magnitude A:", round(magA, 2))
print("Magnitude B:", round(magB, 2))
print("Cosine Similarity:", round(cosine, 2))


#bigger example with text

import math

doc1 = "NLP is easy"
doc2 = "NLP is powerful"

# Tokenization
words1 = doc1.lower().split()
words2 = doc2.lower().split()

# Unique words
all_words = list(set(words1 + words2))

# Create vectors
v1 = []
v2 = []

for w in all_words:

    v1.append(words1.count(w))
    v2.append(words2.count(w))

# Dot product
dot = 0

for i in range(len(v1)):
    dot += v1[i] * v2[i]

# Magnitudes
mag1 = math.sqrt(sum(x*x for x in v1))
mag2 = math.sqrt(sum(x*x for x in v2))

# Cosine similarity
similarity = dot / (mag1 * mag2)

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Cosine Similarity:", round(similarity, 2))