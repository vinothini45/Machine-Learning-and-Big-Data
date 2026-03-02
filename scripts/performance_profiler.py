import time
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel

spark = SparkSession.builder.getOrCreate()

test_data = spark.read.parquet("data/processed/test_features")
lr_model = LogisticRegressionModel.load("models/lr_model")

results = []

for partitions in [100, 200, 400]:
    spark.conf.set("spark.sql.shuffle.partitions", partitions)

    start = time.time()
    _ = lr_model.transform(test_data).count()
    end = time.time()

    execution_time = end - start

    results.append({
        "Partitions": partitions,
        "Execution_Time": execution_time
    })

    print(f"Partitions: {partitions}, Time: {execution_time}")

# Save results
pd.DataFrame(results).to_csv("data/exports/scalability_results.csv", index=False)

print("Performance profiling completed.")