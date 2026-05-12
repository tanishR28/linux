from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Two vectors
A = np.array([[1, 2, 3]])
B = np.array([[2, 1, 3]])

# Cosine Similarity
similarity = cosine_similarity(A, B)

print("Cosine Similarity:")
print(similarity)