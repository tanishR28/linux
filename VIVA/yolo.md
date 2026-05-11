````markdown id="7jlwm11"
# EXP 6 : Object Detection

## Aim
To apply a pretrained object detection model and study:
- object identification
- confidence scores
- detection accuracy
- failure cases
- effect of image quality on detection performance

---

# What is Object Detection?

Object Detection means:
```text id="8’wini12"
identifying and locating objects inside an image
````

Unlike image classification:

* classification predicts only object category
* object detection predicts:

  * object class
  * object location

---

# Object Detection Output

Object detection provides:

* class label
* confidence score
* bounding box coordinates

Example:

```text id="9’wini13"
Person → 98%
Car → 95%
Dog → 92%
```

with rectangles around objects.

---

# Object Detection Flow

Input Image
↓
Pretrained Detection Model
↓
Feature Extraction
↓
Object Localization
↓
Class Prediction
↓
Bounding Boxes + Confidence Scores

---

# Common Object Detection Models

Examples:

* YOLO
* SSD
* Faster R-CNN
* MobileNet SSD

These models are pretrained on datasets like:

```text id="0’wini14"
COCO Dataset
```

---

# Important Concepts

## 1. Bounding Box

Rectangle drawn around detected object.

Represented by:

* x coordinate
* y coordinate
* width
* height

Purpose:

```text id="1’wini15"
locate object position
```

---

## 2. Confidence Score

Confidence score indicates:

```text id="2’wini16"
how confident the model is about detection
```

Example:

```text id="3’wini17"
Dog → 95%
```

means:
model is highly confident object is a dog.

---

# High Confidence Score

```text id="4’wini18"
better prediction reliability
```

---

# Low Confidence Score

Possible reasons:

* blur
* occlusion
* poor lighting
* small object
* unusual orientation

---

## 3. Detection Accuracy

Measures:

```text id="5’wini19"
how correctly objects are detected and localized
```

Depends on:

* image quality
* object visibility
* model quality

---

## 4. Feature Extraction

Detection model extracts:

* edges
* textures
* object patterns

using CNN layers.

---

## 5. Localization

Localization means:

```text id="6’wini20"
finding object position in image
```

using bounding boxes.

---

# Changes To Demonstrate

## 1. Change Confidence Threshold

Example:

```python id="7’wini21"
confidence > 0.5
```

Change to:

```python id="8’wini22"
confidence > 0.8
```

Observe:

* fewer detections
* more reliable predictions

---

# Effects

## Lower Threshold

* more objects detected
* more false positives possible

---

## Higher Threshold

* fewer detections
* higher reliability

---

## 2. Test Multiple Images

Use:

* clear image
* blurry image
* low-light image
* noisy image

Observe:

* confidence changes
* detection failures

---

## 3. Resize Image

Example:

```python id="9’wini23"
cv2.resize(image, ...)
```

Observe:

* detection accuracy
* object visibility

---

## 4. Detect Multiple Objects

Use image containing:

* people
* vehicles
* animals

Observe:

* multiple bounding boxes
* multiple confidence scores

---

# Important Failure Cases

## 1. Blurry Images

Effects:

* unclear edges
* weak feature extraction

---

## 2. Low Resolution Images

Effects:

* small objects difficult to detect

---

## 3. Occlusion

Object partially hidden.

Example:

```text id="0’wini24"
car behind another car
```

---

## 4. Poor Lighting

Effects:

* weak features
* reduced confidence

---

## 5. Unusual Object Orientation

Example:

```text id="1’wini25"
upside-down object
```

Model may fail if training data lacked similar examples.

---

# Image Quality Effects

| Image Quality   | Detection Performance     |
| --------------- | ------------------------- |
| high resolution | better detection          |
| blurry image    | poor confidence           |
| noisy image     | false detections possible |
| low lighting    | weaker detection          |

---

# Important Viva Questions

## What is object detection?

Identifying and locating objects in images.

---

## Difference between classification and detection?

### Classification

Only predicts object class.

### Detection

Predicts:

* class
* object location

---

## What is confidence score?

Probability/confidence of predicted object class.

---

## What is bounding box?

Rectangle locating object position.

---

## Why detection may fail?

* blur
* occlusion
* low resolution
* poor lighting
* noisy images

---

## What dataset used for pretrained detection models?

Usually:

```text id="2’wini26"
COCO Dataset
```

---

## What is localization?

Finding object position using bounding boxes.

---

# Important Parameters

## Confidence Threshold

```python id="3’wini27"
0.5
```

---

## Image Resolution

Higher resolution:

* better detection
* more computation

---

## Input Image Quality

Affects:

* feature extraction
* confidence score

---

# Observations

* High-quality images achieved better detection accuracy.
* Confidence scores reduced for blurry and noisy images.
* Multiple objects were detected using separate bounding boxes.
* Small and partially hidden objects were difficult to detect.
* Increasing confidence threshold reduced false detections.

---

# Conclusion

Pretrained object detection models successfully identified and localized multiple objects in images using bounding boxes and confidence scores. Detection performance strongly depended on image quality, visibility, and confidence threshold settings.

```
```
