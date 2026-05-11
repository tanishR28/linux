````markdown
# Deep Learning Lab Environment Setup

## 1. Create Project Folder

```bash
mkdir DL_LAB
cd DL_LAB
````

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv dl_lab
```

Activate:

```bash
dl_lab\Scripts\activate
```

### Linux / Ubuntu

```bash
python3 -m venv dl_lab
```

Activate:

```bash
source dl_lab/bin/activate
```

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install Required Libraries

```bash
pip install tensorflow notebook ipykernel numpy pandas matplotlib scikit-learn seaborn opencv-python pillow jupyter keras torchvision timm nltk imageio
```

Optional:

```bash
pip install tensorflow-text
```

---

## 5. Register Jupyter Kernel

```bash
python -m ipykernel install --user --name=dl_lab
```

---

## 6. Open VS Code

```bash
code .
```

---

## 7. Install VS Code Extensions

Install:

* Python
* Jupyter

---

## 8. Select Correct Kernel

Inside notebook (.ipynb):

Top Right → Select Kernel → `dl_lab`

---

## 9. Verify Installation

Create notebook and run:

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print("TensorFlow Version:", tf.__version__)

from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(X_train.shape)
```

Expected Output:

```text
TensorFlow Version: <version>
(60000, 28, 28)
```

---

## 10. Common Commands

Activate venv (Windows):

```bash
dl_lab\Scripts\activate
```

Activate venv (Linux):

```bash
source dl_lab/bin/activate
```

Deactivate venv:

```bash
deactivate
```

---

## 11. Recommended Folder Structure

```text
DL_LAB/
│
├── dl_lab/
│
├── exp1_mlp.ipynb
├── exp2_cnn.ipynb
├── exp3_transfer.ipynb
├── exp4_compare.ipynb
├── exp5_analysis.ipynb
├── exp6_object_detection.ipynb
├── exp7_rnn.ipynb
├── exp8_lstm.ipynb
├── exp9_gru.ipynb
├── exp10_gan.ipynb
│
├── datasets/
│
└── README.md
```

---

## 12. Datasets Used

* MNIST
* Fashion-MNIST
* CIFAR-10
* Cats vs Dogs
* COCO Dataset
* Custom Images
* Text Dataset

---

## 13. Final Notes

Before exam:

* Test all notebooks once
* Ensure correct kernel selected
* Keep datasets downloaded
* Practice changing:

  * activation functions
  * hidden layers
  * learning rate
  * epochs

```
```
