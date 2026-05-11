````markdown id="jlwm84"
# EXP 1 : MLP (Multilayer Perceptron)

## Aim
To develop a neural network for digit classification and study:
- Effect of activation functions
- Effect of hidden layers / model depth
- Convergence and accuracy
- Training stability

---

# MLP Architecture Flow

Input Image
↓
Flatten
↓
Dense Hidden Layer(s)
↓
Activation Function
↓
Output Layer (Softmax)

---

# Important Concepts

## 1. Sequential Model

```python
Sequential()
````

Layers are added sequentially one after another.

Flow:

```text id="jlwm85"
Input → Hidden → Output
```

---

## 2. Flatten Layer

```python
Flatten(input_shape=(28,28))
```

Converts:

```text id="xjlwm86"
28×28 image
```

into:

```text id="yjlwm87"
784-element vector
```

because:

```text id="zjlwm88"
28 × 28 = 784
```

Dense layers require 1D input.

---

## 3. Dense Layer

```python
Dense(128, activation='relu')
```

Fully connected layer.

Meaning:

* 128 neurons
* ReLU activation

Dense layers learn:

* edges
* curves
* digit patterns

---

## 4. Activation Function

Activation function introduces non-linearity.

Common activations:

* ReLU
* Sigmoid
* Tanh

---

### ReLU

```python
activation='relu'
```

Advantages:

* faster convergence
* avoids vanishing gradient
* most commonly used

---

### Sigmoid

```python
activation='sigmoid'
```

Output range:

```text id="0jlwm89"
0 to 1
```

May cause:

* vanishing gradient
* slower training

---

### Tanh

```python
activation='tanh'
```

Output range:

```text id="1jlwm90"
-1 to 1
```

Better than sigmoid but slower than ReLU.

---

## 5. Output Layer

```python
Dense(10, activation='softmax')
```

Used for:

```text id="2jlwm91"
multi-class classification
```

Softmax converts outputs into probabilities.

Digits:

```text id="3jlwm92"
0 to 9
```

---

## 6. One-Hot Encoding

```python
to_categorical(y_train, 10)
```

Converts:

```text id="4jlwm93"
5
```

into:

```text id="5jlwm94"
[0 0 0 0 0 1 0 0 0 0]
```

Required for categorical classification.

---

## 7. Optimizer

```python
optimizer='adam'
```

Optimizer updates weights to reduce loss.

Adam:

* fast convergence
* stable training
* adaptive learning

---

## 8. Loss Function

```python
loss='categorical_crossentropy'
```

Measures prediction error.

Lower loss:

```text id="6jlwm95"
better model
```

---

## 9. Epoch

1 epoch =

```text id="7jlwm96"
one complete pass through training dataset
```

---

## 10. Batch Size

```python
batch_size=128
```

Model trains on:

```text id="8jlwm97"
128 samples at a time
```

Advantages:

* faster training
* less memory usage

---

## 11. Convergence

Convergence means:

```text id="9jlwm98"
loss decreases and model stabilizes during training
```

Observed using:

* loss curves
* accuracy improvement

---

## 12. Vanishing Gradient

Problem where gradients become very small during backpropagation.

Effects:

* slow learning
* unstable training

Common in:

* sigmoid
* deep networks

ReLU helps reduce this problem.

---

# Changes To Demonstrate

## 1. Change Activation Function

### ReLU

```python
activation='relu'
```

### Sigmoid

```python
activation='sigmoid'
```

### Tanh

```python
activation='tanh'
```

### Observe:

* accuracy
* convergence speed
* training stability

Expected:

* ReLU performs best
* Sigmoid slower
* Tanh moderate

---

## 2. Change Hidden Layers / Model Depth

### 1 Hidden Layer

```python
Dense(128)
```

### 2 Hidden Layers

```python
Dense(128)
Dense(64)
```

### 3 Hidden Layers

```python
Dense(256)
Dense(128)
Dense(64)
```

### Observe:

* accuracy changes
* convergence changes
* training time changes

---

## 3. Change Epochs

Example:

```python
epochs=5
```

Change to:

```python
epochs=15
```

Observe:

* improved learning initially
* possible overfitting at large epochs

---

## 4. Change Batch Size

Example:

```python
batch_size=128
```

Observe:

* training speed
* memory usage
* convergence behavior

---

# Important Viva Questions

## What is MLP?

Feedforward neural network using fully connected layers.

---

## What is Flatten?

Converts image matrix into vector.

---

## What is Dense Layer?

Fully connected layer learning features using weights.

---

## Why ReLU better?

* avoids vanishing gradient
* converges faster

---

## What is optimizer?

Algorithm updating weights to reduce loss.

---

## What is convergence?

Model loss decreasing and stabilizing during training.

---

## What is model depth?

Number of hidden layers.

---

## What is overfitting?

Model memorizes training data and performs poorly on unseen data.

---

## Why softmax used?

For multi-class classification.

---

# Observations

* ReLU achieved highest accuracy.
* Increasing hidden layers improved feature learning.
* Very deep models increased training time.
* Proper convergence observed through decreasing loss.
* Sigmoid showed slower convergence due to vanishing gradients.

---

# Conclusion

MLP successfully classified handwritten digits from the MNIST dataset. Activation functions and model depth significantly affected convergence speed, training stability, and classification accuracy.

```
```
