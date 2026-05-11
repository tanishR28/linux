````markdown id="8jlwm62"
# EXP 4 : CNN vs Transfer Learning

## Aim
To compare the performance of:
- CNN trained from scratch
- Pretrained Transfer Learning model

and study:
- accuracy
- training time
- dataset size impact
- efficiency of transfer learning

---

# What is CNN From Scratch?

A CNN built and trained entirely on the current dataset.

Example:
```python
Conv2D → Pooling → Conv2D → Dense → Output
````

Characteristics:

* random weight initialization
* learns features from beginning
* requires larger dataset
* longer training time

---

# What is Transfer Learning?

Transfer learning uses:

```text id="9jlwm63"
pretrained CNN models
```

trained on large datasets like:

```text id="0jlwm64"
ImageNet
```

Examples:

* MobileNetV2
* VGG16
* ResNet50

Instead of learning from scratch:

* reuse pretrained features
* adapt model to new task

---

# CNN vs Transfer Learning Flow

## CNN From Scratch

Input Image
↓
Conv Layers
↓
Pooling
↓
Dense
↓
Output

All weights learned from beginning.

---

## Transfer Learning

Input Image
↓
Pretrained CNN
↓
Feature Extraction
↓
New Dense Layer
↓
Output

Most features already learned.

---

# Important Concepts

## 1. Feature Extraction

Pretrained CNN already knows:

* edges
* textures
* shapes
* object patterns

These learned features are reused.

---

## 2. Frozen Layers

```python id="1jlwm65"
base_model.trainable = False
```

Meaning:

* pretrained weights fixed
* only final Dense layers train

Advantages:

* faster training
* less overfitting

---

## 3. Fine-Tuning

Allowing some pretrained layers to update during training.

Example:

```python id="2jlwm66"
layer.trainable = True
```

Used for:

* better adaptation
* improved accuracy

---

# Comparison Between CNN and Transfer Learning

| CNN From Scratch           | Transfer Learning            |
| -------------------------- | ---------------------------- |
| learns from beginning      | reuses pretrained knowledge  |
| needs large dataset        | works well on small datasets |
| slower training            | faster training              |
| more computation           | less computation             |
| may overfit small datasets | better generalization        |
| longer convergence         | faster convergence           |

---

# Changes To Demonstrate

## 1. Train CNN From Scratch

Example architecture:

```python
Conv2D(...)
MaxPooling2D(...)
Flatten()
Dense(...)
```

Observe:

* training time
* accuracy
* convergence

---

## 2. Use Transfer Learning Model

Example:

```python id="3jlwm67"
MobileNetV2(weights='imagenet')
```

Observe:

* faster convergence
* improved accuracy
* reduced training time

---

## 3. Freeze Entire Pretrained Model

```python id="4jlwm68"
base_model.trainable = False
```

Effect:

* very fast training
* fewer trainable parameters
* lower computation

---

## 4. Partial Fine-Tuning

```python id="5jlwm69"
for layer in base_model.layers[-10:]:
    layer.trainable = True
```

Effect:

* better adaptation
* improved accuracy
* increased training time

---

## 5. Change Dataset Size

Use:

* smaller subset
* larger subset

Observe:

### CNN From Scratch

Performance decreases significantly on small datasets.

### Transfer Learning

Still performs well because pretrained features already exist.

---

# Important Parameters

## Filters

```python id="6jlwm70"
Conv2D(32,...)
```

---

## Kernel Size

```python id="7jlwm71"
(3,3)
```

---

## Pool Size

```python id="8jlwm72"
(2,2)
```

---

## Learning Rate

```python id="9jlwm73"
0.001
```

Fine-tuning usually requires:

```text id="0jlwm74"
smaller learning rate
```

such as:

```python id="1jlwm75"
0.0001
```

---

# Important Viva Questions

## What is transfer learning?

Using pretrained models for new tasks.

---

## Why transfer learning useful?

* faster training
* small dataset support
* higher accuracy

---

## Why CNN from scratch requires more data?

Because model must learn all features from beginning.

---

## Why pretrained models converge faster?

Features already learned from large datasets.

---

## What are frozen layers?

Layers whose weights are not updated during training.

---

## What is fine-tuning?

Updating pretrained layers to adapt model.

---

## Which performs better on small datasets?

Transfer learning.

---

## Why?

Because pretrained features improve generalization.

---

# Dataset Size Impact

## Small Dataset

### CNN From Scratch

* poor generalization
* overfitting possible

### Transfer Learning

* good accuracy
* stable learning

---

## Large Dataset

CNN from scratch improves significantly with enough data.

Transfer learning still useful but advantage reduces.

---

# Observations

* Transfer learning converged faster.
* Transfer learning required less training time.
* CNN from scratch required more data.
* Transfer learning performed better on small datasets.
* Fine-tuning improved adaptation and accuracy.

---

# Scenarios Where Transfer Learning Beneficial

Transfer learning is preferred when:

* dataset is small
* limited training time
* limited computational resources
* fast convergence required

---

# Conclusion

Transfer learning achieved faster convergence and better accuracy compared to CNN trained from scratch, especially on small datasets. Pretrained features improved generalization and reduced training time significantly.

```
```
