````markdown id="ganexp10"
# EXP 10 : GAN (Generative Adversarial Network)

## Aim
To implement a GAN model and study:
- synthetic data generation
- generator vs discriminator learning
- training improvement over iterations
- quality and limitations of generated samples

---

# What is GAN?

GAN =
```text id="gan01"
Generative Adversarial Network
````

GAN is a deep learning model used to:

```text id="gan02"
generate new synthetic data samples
```

such as:

* images
* faces
* handwritten digits
* art
* text

---

# Main Idea of GAN

GAN contains:

* Generator
* Discriminator

These two networks:

```text id="gan03"
compete against each other
```

during training.

---

# GAN Architecture Flow

Random Noise
↓
Generator
↓
Fake Image
↓
Discriminator
↓
Real or Fake Prediction

---

# Important Components

# 1. Generator

Generator:

```text id="gan04"
creates fake/synthetic samples
```

Input:

```text id="gan05"
random noise vector
```

Output:

```text id="gan06"
generated image/data
```

Goal:

```text id="gan07"
fool discriminator
```

---

# 2. Discriminator

Discriminator:

```text id="gan08"
detects whether sample is real or fake
```

Input:

* real image
* generated image

Output:

```text id="gan09"
probability of being real
```

Goal:

```text id="gan10"
correctly classify real vs fake
```

---

# GAN Training Process

## Step 1

Generator creates fake images.

---

## Step 2

Discriminator compares:

* real images
* fake images

---

## Step 3

Discriminator learns to detect fake images.

---

## Step 4

Generator improves to fool discriminator.

---

# Adversarial Learning

GAN training is:

```text id="gan11"
a competition between two networks
```

Generator tries to:

```text id="gan12"
generate realistic samples
```

Discriminator tries to:

```text id="gan13"
detect fake samples
```

---

# GAN Loss Concept

Generator wants:

```text id="gan14"
low discriminator accuracy
```

Discriminator wants:

```text id="gan15"
high classification accuracy
```

---

# GAN Objective Formula

\min_G\max_D V(D,G)=E_{x\sim p_{data}}[\log D(x)] + E_{z\sim p_z}[\log(1-D(G(z)))]

where:

* (G) = Generator
* (D) = Discriminator

---

# Important Layers

## Dense Layer

Used in generator/discriminator.

---

## Conv2D / Conv2DTranspose

Used for image generation.

---

## LeakyReLU

Helps stable GAN training.

---

## BatchNormalization

Improves training stability.

---

# Changes To Demonstrate

## 1. Increase Training Epochs

Example:

```python
epochs=1000
```

Observe:

* generated images improve gradually

---

# Expected Observation

## Early Epochs

* noisy outputs
* unclear digits/images

---

## Later Epochs

* clearer generated samples
* realistic patterns

---

## 2. Change Noise Vector Size

Example:

```python
noise_dim = 100
```

Change to:

```python
noise_dim = 50
```

Observe:

* generation diversity
* image quality

---

## 3. Compare Generator vs Discriminator Loss

Plot:

```python
generator_loss
discriminator_loss
```

Observe:

* balance between both networks

---

# Important Concept

If discriminator becomes:

```text id="gan16"
too strong
```

generator cannot learn properly.

---

If generator becomes:

```text id="gan17"
too strong
```

discriminator fails to detect fake images.

---

# Balanced Training Important

Good GAN training requires:

```text id="gan18"
balance between generator and discriminator
```

---

## 4. Generate Multiple Samples

Observe:

* sample diversity
* realism
* noise artifacts

---

# Quality Evaluation

Generated sample quality depends on:

* training duration
* dataset quality
* generator strength
* discriminator balance

---

# Common GAN Problems

## 1. Mode Collapse

Generator produces:

```text id="gan19"
very similar outputs repeatedly
```

---

## 2. Unstable Training

GAN training can oscillate:

* generator improves
* discriminator dominates
* instability occurs

---

## 3. Noisy Outputs

Early training produces:

* blurry images
* distorted samples

---

## 4. High Computational Cost

GANs require:

* large training time
* GPU resources

---

# Important Viva Questions

## What is GAN?

Generative model using generator and discriminator networks.

---

## What does generator do?

Creates fake synthetic samples.

---

## What does discriminator do?

Detects whether samples are real or fake.

---

## Why called adversarial network?

Because generator and discriminator compete against each other.

---

## What is random noise vector?

Random input used to generate synthetic samples.

---

## Why generated images improve over epochs?

Generator gradually learns data distribution.

---

## What is mode collapse?

Generator repeatedly produces similar outputs.

---

## Why GAN training unstable?

Generator and discriminator compete continuously.

---

# Important Parameters

## Noise Dimension

```python
noise_dim = 100
```

---

## Epochs

Controls training duration.

---

## Learning Rate

Controls training stability.

---

## Batch Size

Controls training updates.

---

# Generator vs Discriminator Comparison

| Generator                   | Discriminator               |
| --------------------------- | --------------------------- |
| creates fake data           | classifies real/fake        |
| improves realism            | improves detection          |
| tries to fool discriminator | tries to catch fake samples |

---

# Observations

* GAN generated synthetic images successfully.
* Generated outputs improved over training iterations.
* Early outputs were noisy and unclear.
* Generator and discriminator losses competed during training.
* GAN training required balance for stable learning.

---

# Conclusion

GAN successfully generated synthetic data samples through adversarial learning between generator and discriminator networks. Generated sample quality improved gradually over training, though challenges such as instability and mode collapse were observed.

```
```
