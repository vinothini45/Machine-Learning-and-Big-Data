import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.getOrCreate()

test_data = spark.read.parquet("data/processed/test_features")
lr_model = LogisticRegressionModel.load("models/lr_model")

predictions = lr_model.transform(test_data)

# ----------------------------
# Model Performance
# ----------------------------
evaluator_acc = MulticlassClassificationEvaluator(metricName="accuracy")
evaluator_f1 = MulticlassClassificationEvaluator(metricName="f1")

accuracy = evaluator_acc.evaluate(predictions)
f1 = evaluator_f1.evaluate(predictions)

performance_df = pd.DataFrame([{
    "Model": "Logistic Regression",
    "Accuracy": accuracy,
    "F1 Score": f1
}])

performance_df.to_csv("data/exports/model_performance.csv", index=False)


# ----------------------------
# Confusion Matrix
# ----------------------------
conf_df = predictions.groupBy("label", "prediction").count().toPandas()
conf_df.to_csv("data/exports/confusion_matrix.csv", index=False)


# ----------------------------
# Business Insights
# ----------------------------
from pyspark.sql.functions import length

business_df = predictions.withColumn("review_length", length("review_text")) \
    .groupBy("label") \
    .avg("review_length") \
    .toPandas()

business_df.to_csv("data/exports/business_insights.csv", index=False)

print("Tableau export completed.")