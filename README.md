# DataScienceProject
Final Project for Data Science Course
Statistical and Mashine Learning-based Identification of Random Number Generators for Cryptographic Applications

Research Question
Is it possible to distinguish between different types of random number generators (TRNG and PRNG) using statistical features and machine learning, and how do these generators compare in terms of suitability for cryptographic applications according to AIS31?

# Project Structure

This project analyzes different random number generators (TRNG and PRNG) using statistical methods inspired by NIST SP 800-22 and machine learning techniques, with interpretation aligned to AIS 31 requirements.

---

## 📁 Directory Structure

```
project-root/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   ├── trng_hex.txt
│   │   ├── prng_embedded_hex.txt
│   │   └── prng_python_hex.txt
│   │
│   └── processed/
│       ├── trng_bits.npy
│       ├── prng_embedded_bits.npy
│       └── prng_python_bits.npy
│
├── notebooks/
│   ├── 00_main.ipynb                # Main orchestrator notebook
│   ├── 01_data_preparation.ipynb    # Loading + hex → bits + grouping
│   ├── 02_statistical_tests.ipynb   # NIST-inspired tests
│   ├── 03_feature_engineering.ipynb # Feature extraction
│   ├── 04_machine_learning.ipynb    # ML models (LR, RF)
│   ├── 05_evaluation.ipynb          # Results + AIS31 interpretation
│
├── src/
│   ├── data_loader.py              # Reading hex files, conversion to bits
│   ├── preprocessing.py            # Grouping and chunking logic
│   ├── nist_tests.py               # Implemented statistical tests
│   ├── features.py                 # Feature extraction functions
│   ├── models.py                   # ML model training and evaluation
│   └── utils.py                    # Helper functions
│
├── results/
│   ├── figures/
│   ├── tables/
│   └── reports/
│
└── config/
    └── config.yaml                # Parameters (chunk size, paths, etc.)
```

---

## 📓 Main Notebook (Main_notebook.ipynb)

The main notebook acts as an orchestrator and runs the full pipeline:

1. Data preparation
2. Statistical testing
3. Feature extraction
4. Machine learning
5. Evaluation and interpretation

Each step imports functions or executes other notebooks.

---

## 🔧 Modules Overview

### data_loader.py

* Load hexadecimal data
* Convert to binary sequences

### preprocessing.py

* Group 128-bit numbers into longer sequences (e.g. 1024 bits)
* Create datasets

### nist_tests.py

Implements a subset of tests inspired by NIST SP 800-22:

* Frequency (Monobit)
* Runs Test
* Longest Run of Ones
* Approximate Entropy
* Serial Test

---

### features.py

Extracts statistical features:

* Mean, variance, bias
* Entropy
* Runs and average run length
* Autocorrelation
* Pattern frequencies

---

### models.py

Implements:

* Logistic Regression
* Random Forest

Includes:

* Training
* Prediction
* Evaluation metrics

---

### utils.py

* Visualization helpers
* Metrics formatting
* File utilities

---

## 📊 Workflow Overview

```
Raw Hex Data
    ↓
Bit Conversion
    ↓
Grouping (128 → 1024 bits)
    ↓
Statistical Tests (NIST-inspired)
    ↓
Feature Extraction
    ↓
Machine Learning Classification
    ↓
Evaluation (Accuracy, Feature Importance)
    ↓
AIS31 Interpretation
```

---

## 🎯 Project Goal

* Determine whether different RNG sources can be distinguished
* Evaluate their statistical properties
* Assess their suitability for cryptographic use in the context of AIS 31

---

