````markdown id="9’wini55"
# EXP 8 : LSTM (Long Short-Term Memory)

## Aim
To implement an LSTM model for sequential data and study:
- long-term dependency handling
- comparison with simple RNN
- convergence improvement
- memory mechanisms in sequence learning

---

# What is LSTM?

LSTM =
```text id="0’wini56"
Long Short-Term Memory
````

It is an advanced type of RNN designed to:

```text id="1’wini57"
remember long-term information
```

and solve:

```text id="2’wini58"
vanishing gradient problem
```

---

# Why LSTM Needed?

Simple RNN struggles with:

* long sequences
* memory retention
* long-term dependencies

LSTM solves this using:

* memory cells
* gates

---

# LSTM Flow

Input Sequence
↓
Memory Cell
↓
Forget Gate
↓
Input Gate
↓
Output Gate
↓
Prediction

---

# Important Concepts

## 1. Long-Term Dependency

Long-term dependency means:

```text id="3’wini59"
important information from earlier sequence steps affects later predictions
```

Example:

```text id="4’wini60"
"The movie released in 1990 was ..."
```

Model should remember:

```text id="5’wini61"
1990
```

even after many words.

---

# Problem in Simple RNN

Simple RNN:

```text id="6’wini62"
forgets old information
```

due to:

```text id="7’wini63"
vanishing gradients
```

---

# 2. Memory Cell

LSTM contains:

```text id="8’wini64"
cell state
```

which acts as:

```text id="9’wini65"
long-term memory
```

It stores important sequence information across time steps.

---

# 3. Gates in LSTM

LSTM uses gates to control information flow.

---

## Forget Gate

Decides:

```text id="0’wini66"
what information to remove
```

---

## Input Gate

Decides:

```text id="1’wini67"
what new information to store
```

---

## Output Gate

Decides:

```text id="2’wini68"
what information to output
```

---

# Why Gates Important?

Gates help:

* preserve important memory
* remove unnecessary information
* improve long sequence learning

---

# LSTM Cell State Formula

C_t=f_t*C_{t-1}+i_t*\tilde{C_t}

where:

* (C_t) = current memory
* (f_t) = forget gate
* (i_t) = input gate

---

# Hidden State Formula

h_t=o_t*tanh(C_t)

---

# Important Layers

## Embedding Layer

Converts words/tokens into vectors.

Example:

```python id="3’wini69"
Embedding(vocab_size, embedding_dim)
```

---

## LSTM Layer

Processes sequential information using memory cells.

Example:

```python id="4’wini70"
LSTM(64)
```

Meaning:

* 64 memory units

---

## Dense Layer

Final prediction layer.

---

# Comparison : RNN vs LSTM

| Simple RNN                  | LSTM                       |
| --------------------------- | -------------------------- |
| short memory                | long-term memory           |
| vanishing gradient problem  | reduced vanishing gradient |
| poor long-sequence learning | better sequence learning   |
| simpler architecture        | gate-based architecture    |
| weaker prediction quality   | better prediction quality  |

---

# Changes To Demonstrate

## 1. Compare RNN vs LSTM

### Simple RNN

```python id="5’wini71"
SimpleRNN(64)
```

### LSTM

```python id="6’wini72"
LSTM(64)
```

Observe:

* convergence
* prediction quality
* sequence memory

---

# Expected Observation

## LSTM

* better sequence prediction
* smoother convergence
* improved memory handling

---

## 2. Change Sequence Length

Example:

```python id="7’wini73"
sequence_length = 5
```

Change to:

```python id="8’wini74"
sequence_length = 15
```

Observe:

* long-term learning
* prediction quality

---

## 3. Change LSTM Units

Example:

```python id="9’wini75"
LSTM(32)
```

Change to:

```python id="0’wini76"
LSTM(128)
```

Observe:

* learning capacity
* computation increase

---

## 4. Change Epochs

Example:

```python id="1’wini77"
epochs=5
```

Observe:

* convergence
* overfitting

---

# Loss Convergence Analysis

Plot:

```python id="2’wini78"
history.history['loss']
```

Observe:

* smoother loss decrease in LSTM
* better convergence than simple RNN

---

# Prediction Quality

LSTM predictions:

* more context-aware
* more meaningful
* better long-sequence understanding

---

# Memory Mechanism

LSTM memory cells:

* retain important information
* forget unnecessary information
* improve long-sequence learning

---

# Important Viva Questions

## What is LSTM?

Advanced RNN designed for long-term dependencies.

---

## Why LSTM better than simple RNN?

LSTM uses memory cells and gates to preserve information.

---

## What problem does LSTM solve?

Vanishing gradient and long-term dependency problems.

---

## What is cell state?

Long-term memory in LSTM.

---

## What are gates in LSTM?

Mechanisms controlling information flow.

---

## Why forget gate important?

Removes unnecessary information.

---

## What is long-term dependency?

Earlier sequence information affecting later predictions.

---

## Why LSTM useful in NLP?

Can remember long text context.

---

# Important Parameters

## LSTM Units

```python id="3’wini79"
LSTM(64)
```

---

## Sequence Length

Controls context size.

---

## Embedding Dimension

Controls word vector size.

---

## Epochs

Controls training duration.

---

# Observations

* LSTM handled long sequences better than simple RNN.
* LSTM achieved smoother loss convergence.
* Prediction quality improved significantly.
* Memory cells preserved important sequence information.
* Long-term dependencies were captured effectively.

---

# Conclusion

LSTM models successfully handled long-term dependencies using memory cells and gates. Compared to simple RNNs, LSTMs achieved better convergence, improved prediction quality, and more effective sequence learning.

```
```
