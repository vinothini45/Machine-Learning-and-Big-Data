# Tableau Dashboard Documentation  
## Amazon Reviews Big Data ML Project

---

## 1. Overview

This Tableau workbook presents interactive dashboards developed from a distributed
PySpark machine learning pipeline applied to the Amazon Reviews 2023 dataset.

The dashboards support:

- Big Data monitoring
- Model performance evaluation
- Business insight generation
- Scalability and distributed computing analysis

All visualizations were generated using CSV exports produced from the Spark pipeline.

---

## 2. Data Sources

The dashboards use the following exported datasets:

| File | Purpose |
|------|----------|
| business_insights.csv | Review length statistics and rating distribution |
| model_performance.csv | Accuracy and F1 comparison across models |
| confusion_matrix.csv | Prediction vs actual classification counts |
| scalability_results.csv | Execution time vs partition counts |

These files were generated using:
`scripts/export_for_tableau.py` and `scripts/performance_profiler.py`.

---

## 3. Dashboard Descriptions

---

### Dashboard 1: Data Quality Overview

**Purpose:**  
Monitor dataset health and rating distribution.

**Visualizations:**
- Rating distribution bar chart
- Average review length by rating
- Total record count KPI

**Key Insights:**
- Class imbalance between 1-star and 5-star reviews
- Review length variation across sentiment categories

**Techniques Used:**
- Calculated fields
- KPI cards
- Interactive filters

---

### Dashboard 2: Model Performance Comparison

**Purpose:**  
Compare distributed ML model performance.

**Visualizations:**
- Accuracy comparison bar chart
- F1 score comparison
- Confusion matrix heatmap

**Models Compared:**
- Logistic Regression
- Naive Bayes
- Random Forest
- Support Vector Machine

**Advanced Features:**
- Parameter control for model selection
- LOD Expression:



This ensures stable aggregated performance metrics.

---

### Dashboard 3: Business Insights

**Purpose:**  
Translate machine learning outputs into business understanding.

**Visualizations:**
- Average review length vs rating
- Sentiment distribution trend
- Highlight table for sentiment dominance

**Business Interpretation:**
- Positive reviews are longer and more descriptive
- Majority of customer feedback is positive
- Insight can guide product improvement strategies

---

### Dashboard 4: Scalability & Distributed Performance

**Purpose:**  
Demonstrate Big Data scalability.

**Visualizations:**
- Execution time vs shuffle partitions (line chart)
- Strong scaling analysis
- Weak scaling reference comparison

**Interpretation:**
- Increasing partitions reduces execution time up to optimal threshold
- Excessive partitions introduce shuffle overhead
- Distributed computing improves computational efficiency

---

## 4. Big Data Visualization Strategy

To handle large-scale outputs efficiently:

- Tableau extracts were used instead of live connections
- Data was pre-aggregated in Spark to reduce load
- Only evaluation-level data was exported to CSV
- Hyper extract format recommended for performance

---

## 5. Interactive Features Implemented

✔ Parameter controls for model selection  
✔ Action filters between dashboards  
✔ LOD expressions for accurate aggregation  
✔ Tooltip enhancements  
✔ Mobile-responsive layout considerations  

---

## 6. Data Storytelling Flow

The dashboards follow a structured narrative:

1. **Data Quality** → Understand dataset characteristics  
2. **Model Performance** → Evaluate algorithm effectiveness  
3. **Business Insights** → Interpret ML outputs practically  
4. **Scalability Analysis** → Demonstrate distributed efficiency  

This sequence ensures a logical flow from data to insight to engineering validation.

---

## 7. Performance Optimization

To improve Tableau performance:

- Data extracts used instead of live Spark connection
- Aggregated datasets exported from PySpark
- Limited fields included in CSV exports
- Optimized data types (numeric for metrics)

---

## 8. Limitations

- Only a controlled 1–1.5GB subset was used due to cloud runtime constraints
- Real-time streaming visualization was not implemented
- Confusion matrix limited to aggregated counts

---

## 9. Recommendations

Future enhancements could include:

- Real-time dashboard updates via Spark streaming
- Word cloud visualization of top tokens
- Cost-performance cloud resource visualization
- Model drift monitoring dashboard

---
