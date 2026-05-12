from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Load Dataset
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

# Build Model
model = Sequential()

model.add(Embedding(5000, 32))

model.add(SimpleRNN(32))

model.add(Dense(1, activation='sigmoid'))

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(
    x_train,
    y_train,
    epochs=1,
    batch_size=64
)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)

print("Accuracy:", accuracy)