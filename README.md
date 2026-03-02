# Scalable Multi-Class Sentiment Classification using PySpark

## Project Overview

This project implements a distributed Big Data machine learning pipeline
for multi-class sentiment classification using Amazon Reviews 2023 dataset.

The system is built using:

- PySpark (Distributed ML)
- Hugging Face Datasets (Streaming Big Data)
- MLlib Algorithms
- Tableau for Visualization
- Docker for Reproducibility

---

## Dataset

Dataset: McAuley-Lab/Amazon-Reviews-2023  
Category: raw_review_Electronics  
Size: 22GB full dataset  
Used subset: ~1–1.5GB (controlled streaming sample)

Features:
- Review Text
- Rating (1–5 stars)

Task:
Predict review rating from text (multi-class classification).

---

## Project Structure

### Option 1: Local Python
├── notebooks/
├── scripts/
├── config/
├── data/
├── models/
├── tableau/
├── Dockerfile
├── requirements.txt
└── README.md



---

## Machine Learning Models Implemented

1. Logistic Regression
2. Naive Bayes
3. Random Forest
4. Support Vector Machine (OneVsRest)

---

## Pipeline Overview

1. Streaming ingestion from Hugging Face
2. Controlled sampling (~1GB)
3. Parquet storage
4. TF-IDF feature engineering
5. Distributed model training
6. Cross-validation
7. Model evaluation
8. Scalability profiling
9. Tableau dashboard export

---

## How to Run

---

## Tableau Dashboards

1. Data Quality Overview
2. Model Performance Comparison
3. Business Insights
4. Scalability & Cost Analysis

---

## Scalability Analysis

- Strong scaling tested via partition tuning
- Weak scaling evaluated using increasing dataset size
- Performance profiling implemented in performance_profiler.py

---

