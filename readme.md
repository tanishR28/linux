```md
# Machine Learning Practical Theory Notes

---

# 1. K-Nearest Neighbors (KNN)

## Introduction
K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for classification and regression. It predicts output based on the nearest neighboring data points.

## Working Principle
1. Choose value of K
2. Calculate distance from test point to all training points
3. Select K nearest neighbors
4. Use majority voting for classification

## Distance Formula

Euclidean Distance:

:contentReference[oaicite:0]{index=0}

## Important Concepts
- Distance Metrics
- Majority Voting
- Lazy Learning
- Instance-Based Learning

## Advantages
- Simple and easy
- No training phase
- Good for small datasets

## Disadvantages
- Slow for large datasets
- Sensitive to noise
- Requires feature scaling

## Applications
- Recommendation systems
- Image classification
- Medical diagnosis

---

# 2. Linear Regression

## Introduction
Linear Regression is a supervised learning algorithm used for predicting continuous numerical values.

## Equation


::contentReference[oaicite:1]{index=1}


## Working Principle
- Finds best-fit straight line
- Minimizes prediction error

## Important Concepts
- Regression
- Best Fit Line
- Error Minimization
- Numerical Prediction

## Metrics Used
- MAE
- MSE
- RMSE
- R² Score

## Advantages
- Simple and fast
- Easy interpretation

## Disadvantages
- Works only for linear data
- Sensitive to outliers

## Applications
- Salary prediction
- House price prediction
- Sales forecasting

---

# 3. Decision Tree

## Introduction
Decision Tree is a supervised algorithm that works like a flowchart tree structure.

## Structure
- Root Node
- Decision Node
- Leaf Node

## Working Principle
- Splits data recursively
- Uses feature conditions
- Creates classification rules

## Gini Index Formula

:contentReference[oaicite:2]{index=2}

## Important Concepts
- Recursive Splitting
- Tree Traversal
- Impurity Reduction

## Advantages
- Easy visualization
- Handles non-linear data

## Disadvantages
- Overfitting
- Sensitive to noise

## Applications
- Fraud detection
- Medical diagnosis

---

# 4. Support Vector Machine (SVM) - Linear

## Introduction
SVM is a supervised algorithm used for classification by finding optimal separating hyperplane.

## Hyperplane Formula

:contentReference[oaicite:3]{index=3}

## Concepts Used
- Hyperplane
- Margin
- Support Vectors

## Advantages
- High accuracy
- Effective in high dimensions

## Disadvantages
- Slower on large datasets
- Hard parameter tuning

## Applications
- Face recognition
- Text classification

---

# 5. SVM for Non-Linear Data

## Introduction
Non-linear SVM uses kernel functions to separate complex datasets.

## Kernel Functions
- RBF Kernel
- Polynomial Kernel
- Sigmoid Kernel

## RBF Formula

:contentReference[oaicite:4]{index=4}

## Concepts Used
- Kernel Trick
- Feature Transformation
- Non-linear Classification

## Advantages
- Handles complex patterns
- Flexible classification

## Disadvantages
- Computationally expensive
- Parameter tuning needed

---

# 6. Random Forest (Bagging)

## Introduction
Random Forest is an ensemble learning algorithm using multiple Decision Trees.

## Working Principle
1. Generate random subsets
2. Train multiple trees
3. Combine outputs using voting

## Majority Voting Formula

:contentReference[oaicite:5]{index=5}

## Concepts Used
- Bagging
- Bootstrap Sampling
- Ensemble Learning

## Advantages
- High accuracy
- Reduces overfitting

## Disadvantages
- High memory usage
- Harder interpretation

## Applications
- Stock prediction
- Recommendation systems

---

# 7. AdaBoost / XGBoost (Boosting)

## Introduction
Boosting combines weak learners sequentially to improve performance.

## AdaBoost Formula

:contentReference[oaicite:6]{index=6}

## XGBoost Objective

:contentReference[oaicite:7]{index=7}

## Concepts Used
- Sequential Learning
- Error Correction
- Weak Learners

## Advantages
- Very accurate
- Handles complex datasets

## Disadvantages
- Slower training
- More tuning required

## Applications
- Fraud detection
- Ranking systems

---

# 8. K-Means Clustering

## Introduction
K-Means is an unsupervised learning algorithm used for clustering similar data points.

## Working Principle
1. Choose K clusters
2. Assign nearest points
3. Update centroids
4. Repeat until convergence

## Distance Formula

:contentReference[oaicite:8]{index=8}

## Concepts Used
- Clustering
- Centroids
- Euclidean Distance

## Advantages
- Simple and fast
- Easy implementation

## Disadvantages
- Sensitive to outliers
- Need predefined K

## Applications
- Customer segmentation
- Image compression

---

# 9. K-Modes Clustering

## Introduction
K-Modes is clustering algorithm for categorical data.

## Concepts Used
- Categorical Clustering
- Mode-Based Clustering
- Matching Dissimilarity

## Advantages
- Handles categorical values
- Simple implementation

## Disadvantages
- Choosing K is difficult
- Sensitive initialization

## Applications
- Market segmentation
- Survey analysis

---

# 10. Expectation Maximization (EM)

## Introduction
Expectation Maximization is a probabilistic clustering algorithm used to find hidden patterns in data.

## Working Principle

### E-Step
Calculate cluster probabilities.

### M-Step
Update parameters to maximize likelihood.

## Gaussian Mixture Formula

:contentReference[oaicite:9]{index=9}

## Concepts Used
- Probability Distribution
- Gaussian Mixture Model
- Soft Clustering

## Advantages
- Handles overlapping clusters
- Probabilistic output

## Disadvantages
- Slower than K-Means
- Sensitive initialization

## Applications
- Speech recognition
- Image segmentation

---

# 11. PCA (Principal Component Analysis)

## Introduction
PCA is dimensionality reduction technique used to reduce features while preserving important information.

## PCA Formula

:contentReference[oaicite:10]{index=10}

## Concepts Used
- Variance Maximization
- Feature Reduction
- Orthogonal Transformation

## Advantages
- Reduces dimensions
- Faster training

## Disadvantages
- Information loss possible
- Hard interpretation

## Applications
- Image compression
- Visualization

---

# 12. SVD (Singular Value Decomposition)

## Introduction
SVD is matrix factorization technique used for dimensionality reduction.

## Formula

:contentReference[oaicite:11]{index=11}

## Concepts Used
- Matrix Factorization
- Singular Values
- Low Rank Approximation

## Advantages
- Powerful decomposition method
- Useful in NLP and recommendation systems

## Disadvantages
- Computationally expensive

## Applications
- Recommendation systems
- Text mining

---

# 13. LDA (Linear Discriminant Analysis)

## Introduction
LDA is supervised dimensionality reduction technique maximizing class separability.

## Formula

:contentReference[oaicite:12]{index=12}

## Concepts Used
- Between-Class Variance
- Within-Class Variance
- Feature Extraction

## Advantages
- Improves class separation
- Useful for classification

## Disadvantages
- Assumes normal distribution
- Sensitive to outliers

## Applications
- Face recognition
- Pattern recognition

---
```
