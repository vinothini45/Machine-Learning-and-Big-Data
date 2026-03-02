import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.classification import LogisticRegressionModel


class TestBigDataPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Initialize Spark session once for all tests.
        """
        cls.spark = SparkSession.builder \
            .appName("PipelineUnitTest") \
            .master("local[*]") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    # ----------------------------------------
    # Test 1: Spark Session
    # ----------------------------------------
    def test_spark_session_created(self):
        self.assertIsNotNone(self.spark)

    # ----------------------------------------
    # Test 2: Load Processed Data
    # ----------------------------------------
    def test_load_processed_data(self):
        try:
            df = self.spark.read.parquet("data/processed/train_features")
            self.assertGreater(df.count(), 0)
        except Exception as e:
            self.fail(f"Loading processed data failed: {e}")

    # ----------------------------------------
    # Test 3: Feature Column Exists
    # ----------------------------------------
    def test_feature_column_exists(self):
        df = self.spark.read.parquet("data/processed/train_features")
        self.assertIn("features", df.columns)

    # ----------------------------------------
    # Test 4: Label Column Exists
    # ----------------------------------------
    def test_label_column_exists(self):
        df = self.spark.read.parquet("data/processed/train_features")
        self.assertIn("label", df.columns)

    # ----------------------------------------
    # Test 5: Model Loading
    # ----------------------------------------
    def test_model_loading(self):
        try:
            model = LogisticRegressionModel.load("models/lr_model")
            self.assertIsNotNone(model)
        except Exception as e:
            self.fail(f"Model loading failed: {e}")

    # ----------------------------------------
    # Test 6: Prediction Output
    # ----------------------------------------
    def test_model_prediction(self):
        df = self.spark.read.parquet("data/processed/test_features")
        model = LogisticRegressionModel.load("models/lr_model")

        predictions = model.transform(df)

        self.assertIn("prediction", predictions.columns)

    # ----------------------------------------
    # Test 7: No Null Labels
    # ----------------------------------------
    def test_no_null_labels(self):
        df = self.spark.read.parquet("data/processed/train_features")
        null_count = df.filter(col("label").isNull()).count()
        self.assertEqual(null_count, 0)


if __name__ == "__main__":
    unittest.main()