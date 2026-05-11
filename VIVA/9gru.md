````markdown id="4grumd01"
# EXP 9 : GRU (Gated Recurrent Unit)

## Aim
To develop a GRU-based sequence model and study:
- faster sequence learning
- comparison with LSTM/RNN
- efficiency vs accuracy trade-off
- suitability for real-time applications

---

# What is GRU?

GRU =
```text id="gru01"
Gated Recurrent Unit
````

It is an advanced recurrent neural network similar to:

```text id="gru02"
LSTM
```

but:

* simpler architecture
* fewer parameters
* faster training

---

# Why GRU Introduced?

Simple RNN suffers from:

* vanishing gradients
* poor long-term memory

LSTM solves this but:

* computationally expensive
* more complex

GRU was introduced to:

```text id="gru03"
achieve similar performance with simpler structure
```

---

# GRU Flow

Input Sequence
↓
Update Gate
↓
Reset Gate
↓
Hidden State Update
↓
Prediction

---

# Important Concepts

## 1. Gates in GRU

GRU uses:

* Update Gate
* Reset Gate

Unlike LSTM:

```text id="gru04"
GRU does NOT use separate memory cell
```

This makes GRU:

* simpler
* faster

---

## 2. Update Gate

Controls:

```text id="gru05"
how much previous memory should be retained
```

Acts similarly to:

```text id="gru06"
forget + input gates in LSTM
```

---

## 3. Reset Gate

Controls:

```text id="gru07"
how much old information should be ignored
```

Helps model:

* reset unnecessary memory
* focus on current input

---

# GRU Hidden State Formula

h_t=(1-z_t)h_{t-1}+z_t\tilde{h_t}

where:

* (z_t) = update gate
* (h_t) = hidden state

---

# Reset Gate Formula

r_t=\sigma(W_r x_t+U_r h_{t-1})

---

# Why GRU Faster?

Because:

* fewer gates
* fewer parameters
* no separate cell state

So computation becomes:

```text id="gru08"
lighter and faster
```

---

# Important Layers

## Embedding Layer

Converts tokens into vectors.

Example:

```python
Embedding(vocab_size, embedding_dim)
```

---

## GRU Layer

Processes sequential data using gated memory.

Example:

```python
GRU(64)
```

Meaning:

* 64 GRU units

---

## Dense Layer

Final prediction layer.

---

# Comparison : RNN vs LSTM vs GRU

| Simple RNN          | LSTM                 | GRU                |
| ------------------- | -------------------- | ------------------ |
| simple architecture | complex architecture | simpler than LSTM  |
| poor long memory    | strong long memory   | good long memory   |
| vanishing gradients | reduced problem      | reduced problem    |
| fastest computation | slowest computation  | faster than LSTM   |
| lower accuracy      | high accuracy        | near-LSTM accuracy |

---

# Changes To Demonstrate

## 1. Compare GRU vs LSTM

### LSTM

```python
LSTM(64)
```

### GRU

```python
GRU(64)
```

Observe:

* training time
* convergence
* prediction quality

---

# Expected Observation

## GRU

* faster training
* fewer parameters
* slightly lower or similar accuracy

---

## 2. Change GRU Units

Example:

```python
GRU(32)
```

Change to:

```python
GRU(128)
```

Observe:

* learning capacity
* training time increase

---

## 3. Change Sequence Length

Example:

```python
sequence_length = 5
```

Change to:

```python
sequence_length = 15
```

Observe:

* memory handling
* prediction quality

---

## 4. Change Epochs

Example:

```python
epochs=5
```

Observe:

* convergence
* overfitting

---

# Efficiency vs Accuracy Trade-Off

## Smaller GRU

* faster
* less memory
* lower accuracy possible

---

## Larger GRU

* better learning
* slower computation
* higher memory usage

---

# Why GRU Good For Real-Time Applications?

Because GRU:

* trains faster
* fewer parameters
* lower latency
* lower memory usage

Useful for:

* mobile devices
* speech recognition
* chatbots
* real-time NLP

---

# Real-Time Applications

Examples:

* voice assistants
* predictive typing
* live translation
* streaming sequence prediction

---

# Important Viva Questions

## What is GRU?

Simplified gated recurrent neural network.

---

## Why GRU faster than LSTM?

GRU has fewer gates and fewer parameters.

---

## What gates used in GRU?

* update gate
* reset gate

---

## Difference between LSTM and GRU?

### LSTM

* 3 gates
* separate cell state

### GRU

* 2 gates
* no separate cell state

---

## Why GRU suitable for real-time systems?

Lower computation and faster inference.

---

## Does GRU solve vanishing gradient problem?

Yes, significantly better than simple RNN.

---

## Which is more accurate: LSTM or GRU?

Usually similar, but depends on dataset.

---

# Important Parameters

## GRU Units

```python
GRU(64)
```

---

## Sequence Length

Controls context size.

---

## Embedding Dimension

Controls token vector size.

---

## Epochs

Controls training duration.

---

# Observations

* GRU trained faster than LSTM.
* GRU achieved good sequence prediction accuracy.
* Memory mechanisms improved long-sequence learning.
* GRU reduced computational complexity.
* GRU was suitable for real-time sequence tasks.

---

# Conclusion

GRU successfully handled sequence learning with faster training and lower computational complexity compared to LSTM. Its gated memory mechanism improved long-term dependency learning while making it suitable for real-time applications.

```
```
