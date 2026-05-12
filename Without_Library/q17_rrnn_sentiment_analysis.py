from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Load dataset
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

# Build Model
model = Sequential()

model.add(Embedding(5000, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

# Compile Model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train Model
model.fit(x_train, y_train,
          epochs=1,
          batch_size=64)

# Evaluate
loss, acc = model.evaluate(x_test, y_test)

print("Accuracy:", acc)



#
import nltk
import numpy as np
from nltk.corpus import movie_reviews

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Download dataset
nltk.download('movie_reviews')

# Load movie reviews
documents = []

for category in movie_reviews.categories():

    for fileid in movie_reviews.fileids(category):

        review = movie_reviews.raw(fileid)

        documents.append((review, category))

# Separate texts and labels
texts = [doc[0] for doc in documents]
labels = [doc[1] for doc in documents]

# Convert labels into numbers
encoder = LabelEncoder()

labels = encoder.fit_transform(labels)

# Tokenization
tokenizer = Tokenizer(num_words=5000)

tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)

# Padding
X = pad_sequences(sequences, maxlen=200)

y = np.array(labels)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build RNN Model
model = Sequential()

model.add(Embedding(input_dim=5000, output_dim=64, input_length=200))

model.add(SimpleRNN(64))

model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=3, batch_size=32)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("Accuracy:", accuracy)