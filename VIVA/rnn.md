````markdown id="4’wini28"
# EXP 7 : Simple RNN (Recurrent Neural Network)

## Aim
To develop a simple RNN model for sequence prediction and study:
- next-step text prediction
- effect of sequence length
- long-term dependency problem
- short vs long sequence performance

---

# What is RNN?

RNN (Recurrent Neural Network) is a neural network designed for:
- sequential data
- text
- time series
- speech

Unlike normal neural networks:
```text id="5’wini29"
RNN remembers previous information
````

using hidden states.

---

# Why RNN Needed?

Normal neural networks:

```text id="6’wini30"
process inputs independently
```

But text has:

```text id="7’wini31"
sequence dependency
```

Example:

```text id="8’wini32"
"I am going to ____"
```

Next word depends on previous words.

---

# RNN Flow

Input Word
↓
Hidden State Memory
↓
Next Input
↓
Updated Memory
↓
Prediction

---

# Important Concepts

## 1. Sequence Prediction

RNN predicts:

```text id="9’wini33"
next word/character in sequence
```

Example:

Input:

```text id="0’wini34"
"I love deep"
```

Prediction:

```text id="1’wini35"
learning
```

---

## 2. Hidden State

Hidden state stores:

```text id="2’wini36"
previous sequence information
```

Acts like:

```text id="3’wini37"
memory of the network
```

---

# RNN Hidden State Formula

h_t=f(Wx_t+Uh_{t-1}+b)

where:

* (x_t) = current input
* (h_{t-1}) = previous hidden state
* (h_t) = current hidden state

---

# Output Formula

y_t=Wh_t+b

---

## 3. Sequence Length

Sequence length =

```text id="4’wini38"
number of previous words/tokens used
```

Example:

Sequence length = 3

Input:

```text id="5’wini39"
"I love deep"
```

Predict:

```text id="6’wini40"
learning
```

---

# Short Sequence Length

Advantages:

* faster training
* simpler learning

Disadvantages:

* less context

---

# Long Sequence Length

Advantages:

* more context
* better language understanding

Disadvantages:

* harder training
* memory issues

---

## 4. Long-Term Dependency Problem

Simple RNN struggles to remember:

```text id="7’wini41"
very old information
```

called:

```text id="8’wini42"
long-term dependency problem
```

---

# Example

Sentence:

```text id="9’wini43"
"The movie released in 1990 was very famous because ..."
```

RNN may forget:

```text id="0’wini44"
earlier words
```

in long sequences.

---

## 5. Vanishing Gradient Problem

During backpropagation:

```text id="1’wini45"
gradients become very small
```

Effects:

* poor learning
* memory loss
* difficulty learning long sequences

This is major limitation of simple RNN.

---

# Why LSTM/GRU Introduced?

To solve:

```text id="2’wini46"
long-term dependency problem
```

using:

* memory cells
* gates

---

# Important Layers

## Embedding Layer

Converts words into vectors.

Example:

```python id="3’wini47"
Embedding(vocab_size, embedding_dim)
```

---

## SimpleRNN Layer

Processes sequential information.

Example:

```python id="4’wini48"
SimpleRNN(64)
```

Meaning:

* 64 hidden units

---

## Dense Layer

Final prediction layer.

---

# Changes To Demonstrate

## 1. Change Sequence Length

Example:

```python id="5’wini49"
sequence_length = 3
```

Change to:

```python id="6’wini50"
sequence_length = 10
```

Observe:

* prediction quality
* training difficulty

---

# Expected Effects

## Small Sequence Length

* less context
* faster training

---

## Large Sequence Length

* more context
* harder learning
* possible vanishing gradients

---

## 2. Change RNN Units

Example:

```python id="7’wini51"
SimpleRNN(32)
```

Change to:

```python id="8’wini52"
SimpleRNN(128)
```

Observe:

* model capacity
* computation increase

---

## 3. Change Epochs

Example:

```python id="9’wini53"
epochs=5
```

Observe:

* convergence
* overfitting

---

## 4. Compare Short vs Long Sequences

Use:

* short sentences
* long sentences

Observe:

* prediction accuracy
* memory limitations

---

# Short vs Long Sequences

| Short Sequence         | Long Sequence          |
| ---------------------- | ---------------------- |
| easier learning        | harder learning        |
| faster training        | slower training        |
| limited context        | better context         |
| better RNN performance | memory issues possible |

---

# Important Viva Questions

## What is RNN?

Neural network designed for sequential data.

---

## Why RNN different from MLP?

RNN remembers previous inputs using hidden states.

---

## What is hidden state?

Memory storing previous sequence information.

---

## What is sequence length?

Number of previous tokens used for prediction.

---

## What is long-term dependency problem?

Difficulty remembering information from earlier time steps.

---

## What is vanishing gradient?

Gradients become very small during backpropagation.

---

## Why simple RNN struggles with long sequences?

Due to vanishing gradients and memory limitations.

---

## Why LSTM better than simple RNN?

LSTM can remember long-term information using gates and memory cells.

---

# Important Parameters

## RNN Units

```python id="0’wini54"
SimpleRNN(64)
```

---

## Sequence Length

Controls amount of context.

---

## Embedding Dimension

Controls vector representation size.

---

## Epochs

Controls training duration.

---

# Observations

* RNN successfully predicted next sequence elements.
* Longer sequences provided better context.
* Very long sequences caused memory difficulties.
* Simple RNN struggled with long-term dependencies.
* Increasing sequence length increased computation.

---

# Conclusion

Simple RNN models can learn sequential patterns for next-step prediction but face limitations in remembering long-term dependencies due to vanishing gradients. Sequence length significantly affects prediction accuracy and model performance.

```
```
