from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("LargeScaleTextProcessing") \
        .config("spark.executor.memory", "2g") \
        .config("spark.driver.memory", "2g") \
        .getOrCreate()