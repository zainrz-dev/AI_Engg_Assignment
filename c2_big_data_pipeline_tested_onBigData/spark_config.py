import os
from pyspark.sql import SparkSession

# Fix for Windows Hadoop issue
os.environ['HADOOP_HOME'] = 'C:\\hadoop'

def create_spark_session():
    """
    Create SparkSession with basic memory configuration.
    For local development/testing with moderate-sized datasets.
    """
    return (SparkSession.builder
        .appName("LargeScaleTextProcessing")
        .config("spark.executor.memory", "2g")
        .config("spark.driver.memory", "2g")
        .config("spark.sql.adaptive.enabled", "true")
        .getOrCreate())