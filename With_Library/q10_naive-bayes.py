from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training Data
texts = [
    "win money now",
    "claim your prize",
    "hello friend",
    "how are you"
]

# Labels
labels = ["spam", "spam", "ham", "ham"]

# Convert text to vectors
cv = CountVectorizer()

X = cv.fit_transform(texts)

# Train Model
model = MultinomialNB()

model.fit(X, labels)

# Test Sentence
test = ["win prize"]

test_vector = cv.transform(test)

# Prediction
prediction = model.predict(test_vector)

print("Prediction:", prediction[0])