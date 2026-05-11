````markdown id="6jlwm90"
# EXP 5 : Performance Analysis of CNN

## Aim
To analyse the performance of a CNN model by studying:
- learning rate
- epochs
- overfitting
- convergence
- validation loss
- hyperparameter tuning

---

# CNN Performance Analysis Flow

Input Image
↓
CNN Model
↓
Training
↓
Loss & Accuracy Analysis
↓
Hyperparameter Comparison

---

# Important Concepts

## 1. Learning Rate

Learning rate controls:
```text id="7jlwm91"
how much weights are updated during training
````

Represented as:

```text id="8jlwm92"
η (eta)
```

Weight update formula:

w_{new}=w_{old}-\eta\frac{\partial L}{\partial w}

where:

* (w) = weights
* (L) = loss
* (η) = learning rate

---

# Small Learning Rate

Example:

```python
0.0001
```

Effects:

* slow learning
* stable convergence
* longer training time

---

# Large Learning Rate

Example:

```python
0.1
```

Effects:

* fast updates
* unstable training
* may overshoot minimum loss

---

# Moderate Learning Rate

Example:

```python id="9jlwm93"
0.001
```

Usually provides:

* stable convergence
* good accuracy

---

# 2. Convergence

Convergence means:

```text id="0jlwm94"
model loss decreases and stabilizes during training
```

Good convergence:

* smooth decreasing loss
* stable accuracy improvement

---

# 3. Epochs

1 epoch =

```text id="1jlwm95"
one complete pass through training dataset
```

Example:

```python id="2jlwm96"
epochs=5
```

---

# Effect of Increasing Epochs

## Too Few Epochs

* underfitting
* poor learning

---

## Too Many Epochs

* overfitting possible
* model memorizes training data

---

# 4. Overfitting

Overfitting means:

```text id="3jlwm97"
model performs well on training data but poorly on unseen data
```

Symptoms:

* training loss decreases
* validation loss increases

---

# 5. Generalization

Generalization means:

```text id="4jlwm98"
model performs well on unseen test data
```

Good generalization:

* similar train & validation accuracy

---

# 6. Validation Loss

Validation loss measures:

```text id="5jlwm99"
model performance on unseen validation data
```

Used to detect:

* overfitting
* convergence quality

---

# 7. Hyperparameters

Hyperparameters are:

```text id="6jlwm00"
parameters set before training
```

Examples:

* learning rate
* epochs
* batch size
* filters
* kernel size

---

# Important CNN Layers

## Conv2D

Feature extraction.

---

## MaxPooling2D

Reduces dimensions and overfitting.

---

## Flatten

Converts feature maps into vector.

---

## Dense

Classification layer.

---

# Changes To Demonstrate

## 1. Change Learning Rate

Example:

```python id="7jlwm01"
learning_rate = 0.001
```

Change to:

```python id="8jlwm02"
0.01
```

or:

```python id="9jlwm03"
0.0001
```

Observe:

* convergence speed
* training stability
* validation accuracy

---

# Expected Observations

## Very Small Learning Rate

* slow convergence

---

## Very Large Learning Rate

* unstable loss
* poor convergence

---

## Moderate Learning Rate

* stable training
* best accuracy

---

## 2. Change Number of Epochs

Example:

```python id="0jlwm04"
epochs=5
```

Change to:

```python id="1jlwm05"
epochs=20
```

Observe:

* overfitting
* validation loss behavior

---

# Expected Observations

## Low Epochs

* underfitting

---

## High Epochs

* overfitting possible

---

## Balanced Epochs

* proper generalization

---

## 3. Plot Loss Curves

Example:

```python id="2jlwm06"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
```

Purpose:

* analyse convergence
* detect overfitting

---

# Interpretation

## Good Model

Training and validation loss both decrease smoothly.

---

## Overfitting

Training loss decreases but validation loss increases.

---

## Underfitting

Both losses remain high.

---

## 4. Change Batch Size

Example:

```python id="3jlwm07"
batch_size=32
```

Change to:

```python id="4jlwm08"
batch_size=128
```

Observe:

* training speed
* convergence stability

---

# Batch Size Effects

| Small Batch        | Large Batch         |
| ------------------ | ------------------- |
| stable learning    | faster training     |
| slower computation | less stable updates |

---

## 5. Change Number of Filters

Example:

```python id="5jlwm09"
Conv2D(32,...)
```

Change to:

```python id="6’wini10"
Conv2D(64,...)
```

Observe:

* feature extraction capability
* computation increase

---

# Important Viva Questions

## What is learning rate?

Controls magnitude of weight updates.

---

## What is convergence?

Loss decreasing and stabilizing during training.

---

## What is overfitting?

Model memorizes training data and performs poorly on unseen data.

---

## What is underfitting?

Model fails to learn patterns properly.

---

## Why validation loss important?

Used to evaluate generalization performance.

---

## What are hyperparameters?

Parameters manually set before training.

---

## Why smaller learning rate used?

Provides stable convergence.

---

## How to detect overfitting?

Validation loss increases while training loss decreases.

---

# Training vs Validation Loss Curves

## Good Convergence

Both curves decrease smoothly.

---

## Overfitting

Validation loss increases after certain epochs.

---

## Underfitting

Both losses remain high.

---

# Hyperparameter Comparison

| Hyperparameter | Effect             |
| -------------- | ------------------ |
| Learning Rate  | convergence speed  |
| Epochs         | training duration  |
| Batch Size     | stability & speed  |
| Filters        | feature extraction |
| Kernel Size    | receptive field    |

---

# Observations

* Moderate learning rate achieved best convergence.
* Increasing epochs improved learning initially.
* Very high epochs caused overfitting.
* Validation loss helped detect generalization quality.
* Hyperparameters significantly affected CNN performance.

---

# Conclusion

CNN performance is strongly influenced by hyperparameters such as learning rate, epochs, batch size, and filters. Proper tuning improves convergence, stability, and generalization while reducing overfitting.

```
```
