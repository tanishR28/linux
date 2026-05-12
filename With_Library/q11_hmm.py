import numpy as np
from hmmlearn import hmm

# Observation sequence
X = np.array([[0], [1], [0], [1]])

# Create HMM Model
model = hmm.MultinomialHMM(n_components=2)

# Transition Probabilities
model.transmat_ = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# Emission Probabilities
model.emissionprob_ = np.array([
    [0.9, 0.1],
    [0.2, 0.8]
])

# Start Probabilities
model.startprob_ = np.array([0.6, 0.4])

# Predict Hidden States
states = model.predict(X)

print("Hidden States:")
print(states)