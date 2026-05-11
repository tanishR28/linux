````markdown id="qjlwm44"
# EXP 3 : Transfer Learning

## Aim
To adapt a pretrained CNN model for a new image classification task using transfer learning and study:
- Feature extraction
- Frozen layers
- Partial fine-tuning
- Training efficiency
- Effect of pretrained features on small datasets

---

# What is Transfer Learning?

Transfer Learning means:
Using a pretrained model trained on a large dataset (like ImageNet) and adapting it for a new classification task.

Instead of training a CNN from scratch:
- reuse learned features
- reduce training time
- improve accuracy on small datasets

---

# Common Pretrained Models

Examples:
- MobileNetV2
- VGG16
- ResNet50
- EfficientNet

These models are pretrained on:
```text id="rjlwm45"
ImageNet Dataset
````

which contains millions of images.

---

# Transfer Learning Flow

Input Image
↓
Pretrained CNN
↓
Feature Extraction
↓
New Dense Layer
↓
Output Classes

---

# Important Concepts

## 1. Feature Extraction

Feature extraction means:
Using pretrained CNN layers to extract useful image features.

The pretrained model already knows:

* edges
* textures
* shapes
* object patterns

Only new classification layers are trained.

---

## 2. Frozen Layers

Frozen layers:

```text id="sjlwm46"
weights are NOT updated during training
```

Example:

```python id="tjlwm47"
base_model.trainable = False
```

Meaning:

* pretrained knowledge preserved
* only final Dense layers train

Advantages:

* faster training
* less overfitting
* lower computation

Disadvantage:

* limited adaptation to new dataset

---

## 3. Fine-Tuning

Fine-tuning means:
Allowing pretrained layers to update during training.

---

## 4. Partial Fine-Tuning

Some layers:

```text id="ujlwm48"
frozen
```

Some layers:

```text id="vjlwm49"
trainable
```

Usually:

* early CNN layers frozen
* deeper layers trainable

Reason:

* early layers learn generic features
* deeper layers learn task-specific patterns

---

# Example of Partial Fine-Tuning

```python id="wjlwm50"
for layer in base_model.layers[:-10]:
    layer.trainable = False

for layer in base_model.layers[-10:]:
    layer.trainable = True
```

Meaning:

* first layers frozen
* last 10 layers trainable

---

# Why Transfer Learning Useful?

Advantages:

* faster convergence
* high accuracy
* less training data required
* reduced computation

Especially useful for:

```text id="xjlwm51"
small datasets
```

---

# Important Layers

## GlobalAveragePooling2D

Reduces feature maps before Dense layers.

---

## Dense Layer

Final classification layer.

Example:

```python id="yjlwm52"
Dense(num_classes, activation='softmax')
```

---

# Changes To Demonstrate

## 1. Frozen Layers vs Fine-Tuning

### Freeze Entire Model

```python id="zjlwm53"
base_model.trainable = False
```

Observe:

* faster training
* less computation
* decent accuracy

---

### Partial Fine-Tuning

```python id="0jlwm54"
for layer in base_model.layers[-10:]:
    layer.trainable = True
```

Observe:

* better adaptation
* higher accuracy possible
* slower training

---

## 2. Change Number of Trainable Layers

Example:

```python id="1jlwm55"
layers[-5:]
```

Change to:

```python id="2jlwm56"
layers[-20:]
```

Effect:

* more trainable parameters
* increased computation
* possible accuracy improvement

---

## 3. Change Learning Rate

Example:

```python id="3jlwm57"
learning_rate = 0.001
```

Fine-tuning often requires:

```text id="4jlwm58"
smaller learning rate
```

such as:

```python id="5jlwm59"
0.0001
```

Reason:

* avoid destroying pretrained weights

---

## 4. Change Dense Layers

Example:

```python id="6jlwm60"
Dense(128, activation='relu')
```

Add more Dense layers:

* improves learning capacity
* may increase overfitting

---

# Frozen Layers vs Fine-Tuning

| Frozen Layers              | Partial Fine-Tuning         |
| -------------------------- | --------------------------- |
| faster training            | slower training             |
| fewer trainable parameters | more trainable parameters   |
| less overfitting           | better adaptation           |
| lower computation          | higher computation          |
| decent accuracy            | potentially better accuracy |

---

# Important Viva Questions

## What is transfer learning?

Using pretrained models for new tasks.

---

## Why transfer learning useful?

* faster training
* small dataset support
* better accuracy

---

## What are frozen layers?

Layers whose weights are not updated during training.

---

## What is fine-tuning?

Updating pretrained layers for better adaptation.

---

## Why freeze early layers?

Early layers learn generic image features useful for all tasks.

---

## Why use smaller learning rate during fine-tuning?

To prevent large weight updates from destroying pretrained knowledge.

---

## What dataset are pretrained models trained on?

Usually:

```text id="7jlwm61"
ImageNet
```

---

# Observations

* Transfer learning achieved good accuracy even on small datasets.
* Frozen layers trained faster and reduced overfitting.
* Partial fine-tuning improved adaptation to the new dataset.
* Fine-tuning increased computation and training time.
* Pretrained features significantly improved convergence.

---

# Conclusion

Transfer learning successfully reused pretrained CNN knowledge for a new classification task. Frozen layers improved training efficiency, while partial fine-tuning improved adaptation and classification accuracy.

```
```
