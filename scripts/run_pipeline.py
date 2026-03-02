import itertools
import pandas as pd
import time
from datasets import load_dataset
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression


# ----------------------------
# Spark Session
# ----------------------------
spark = SparkSession.builder \
    .appName("AmazonReviewsPipeline") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()


# ----------------------------
# Load Streaming Dataset
# ----------------------------
print("Loading dataset...")

dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023",
    "raw_review_Electronics",
    split="full",
    streaming=True
)

target_rows = 1_000_000
batch_size = 100_000
iterator = iter(dataset)

spark_df = None
processed = 0

while processed < target_rows:
    batch = list(itertools.islice(iterator, batch_size))
    if not batch:
        break

    pdf = pd.DataFrame(batch)
    sdf = spark.createDataFrame(pdf)

    spark_df = sdf if spark_df is None else spark_df.union(sdf)
    processed += len(batch)

    print(f"Processed {processed} rows")

# ----------------------------
# Preprocessing
# ----------------------------
df = spark_df.select(
    col("text").alias("review_text"),
    col("rating").alias("stars")
)

df = df.withColumn("label", col("stars") - 1)

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# ----------------------------
# NLP Pipeline
# ----------------------------
tokenizer = Tokenizer(inputCol="review_text", outputCol="words")
remover = StopWordsRemover(inputCol="words", outputCol="filtered")
hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=20000)
idf = IDF(inputCol="rawFeatures", outputCol="features")

pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf])
model = pipeline.fit(train_df)

train_data = model.transform(train_df)
test_data = model.transform(test_df)

# ----------------------------
# Train Logistic Regression
# ----------------------------
print("Training Logistic Regression...")

lr = LogisticRegression(featuresCol="features", labelCol="label", maxIter=20)

start = time.time()
lr_model = lr.fit(train_data)
end = time.time()

print("Training Time:", end - start)

# Save model
lr_model.write().overwrite().save("models/lr_model")

# Save processed data
train_data.write.mode("overwrite").parquet("data/processed/train_features")
test_data.write.mode("overwrite").parquet("data/processed/test_features")

print("Pipeline completed successfully.")