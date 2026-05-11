````markdown id="pjlwm65"
# EXP 2 : CNN (Convolutional Neural Network)

## Aim
To develop a CNN-based image classification model and study:
- CNN vs Fully Connected Model (MLP)
- Effect of Pooling Layers
- Feature Maps
- Effect of Convolution Parameters

---

# CNN Architecture Flow

Image
↓
Conv2D
↓
ReLU
↓
MaxPooling2D
↓
Conv2D
↓
MaxPooling2D
↓
Flatten
↓
Dense
↓
Output

---

# Important Concepts

## 1. Conv2D Layer
Used for feature extraction.

Example:
```python
Conv2D(32, (3,3), activation='relu')
````

Meaning:

* 32 filters
* kernel size = 3x3
* ReLU activation

CNN learns:

* edges
* textures
* patterns
* shapes

---

## 2. Kernel / Filter

Small matrix scanning image to detect patterns.

Example:

```python
(3,3)
```

Smaller kernels:

* capture fine details
* computationally efficient

Larger kernels:

* capture larger patterns
* increase computation

---

## 3. Pooling Layer

Used to reduce image dimensions.

Example:

```python
MaxPooling2D((2,2))
```

Advantages:

* reduces overfitting
* reduces computation
* keeps important features

Pooling keeps important values only.

---

## 4. Flatten Layer

Converts feature maps into 1D vector before Dense layers.

Example:

```python
Flatten()
```

---

## 5. Dense Layer

Fully connected layer used for classification.

Example:

```python
Dense(128, activation='relu')
```

---

# Changes To Demonstrate

## 1. Change Number of Filters

Example:

```python
Conv2D(32, (3,3), activation='relu')
```

Change to:

```python
Conv2D(64, (3,3), activation='relu')
```

Effect:

* learns more features
* higher accuracy possible
* increased computation

---

## 2. Change Kernel Size

Example:

```python
(3,3)
```

Change to:

```python
(5,5)
```

Effect:

* larger receptive field
* captures larger patterns
* slower computation

---

## 3. Remove / Add Pooling Layer

Remove:

```python
MaxPooling2D((2,2))
```

Effect:

* larger feature maps
* more computation
* higher overfitting possible

Add Pooling:

* reduced dimensions
* less overfitting
* faster training

---

## 4. Change Number of CNN Layers

Example:

One Conv Layer:

```python
Conv2D(...)
MaxPooling2D(...)
```

Two Conv Layers:

```python
Conv2D(...)
MaxPooling2D(...)

Conv2D(...)
MaxPooling2D(...)
```

Effect:

* deeper CNN learns more complex features
* better feature extraction
* increased training time

---

# CNN vs MLP

## MLP

* Flattens image immediately
* Loses spatial information
* Lower image accuracy

## CNN

* Preserves image structure
* Learns local patterns
* Better image classification accuracy

---

# Feature Maps

Feature map = output of convolution layer.

Early CNN layers learn:

* edges
* textures

Deeper layers learn:

* shapes
* object structures

Feature maps help visualize what CNN learns.

---

# Important Viva Questions

## Why CNN better than MLP?

CNN preserves spatial information and learns local image features.

---

## What is Conv2D?

Feature extraction layer using filters/kernels.

---

## What is pooling?

Dimension reduction operation reducing overfitting and computation.

---

## Why ReLU used?

* faster convergence
* avoids vanishing gradient

---

## Why Flatten used?

Dense layers require 1D input.

---

## What is filter/kernel?

Small matrix used to detect image features.

---

# Important Parameters

## Filters

```python
Conv2D(32,...)
```

## Kernel Size

```python
(3,3)
```

## Pool Size

```python
(2,2)
```

## Activation Function

```python
activation='relu'
```

---

# Observations

* CNN generally achieves higher accuracy than MLP.
* Pooling reduces overfitting and computation.
* Increasing filters improves feature extraction.
* Larger kernels increase computation.
* Deeper CNNs learn more complex patterns.

---

# Conclusion

CNN successfully classifies images by extracting spatial features using convolution operations. Pooling layers reduce dimensions and overfitting, while deeper CNN architectures improve feature learning and classification accuracy.

```
```
