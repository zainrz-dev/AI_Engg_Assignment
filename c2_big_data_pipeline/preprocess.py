from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split
import os
import sys

# -----------------------------
# Spark Session Setup
# -----------------------------
def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("LargeScalePreprocessing")
        .config("spark.sql.parquet.writeLegacyFormat", "true")  # Avoid some Parquet issues
        .config("spark.hadoop.validateOutputSpecs", "false")    # Skip Hadoop native permission checks
        .getOrCreate()
    )
    # Reduce logging verbosity
    spark.sparkContext.setLogLevel("WARN")
    return spark

spark = create_spark_session()

# -----------------------------
# Paths
# -----------------------------
raw_path = "sample_raw.txt"
output_path = "../processed_data/cleaned_data"

# Ensure output folder exists (avoid Windows/Hadoop mkdir issues)
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# -----------------------------
# Load and preprocess
# -----------------------------
df = spark.read.text(raw_path)
df = df.withColumnRenamed("value", "text")

# Basic cleaning
df = df.withColumn("text", lower(col("text")))
df = df.withColumn("text", regexp_replace(col("text"), "[^a-zA-Z ]", ""))

# Remove empty or short rows
df = df.filter((col("text") != "") & (col("text").rlike(".{10,}")))

# Tokenization
df = df.withColumn("tokens", split(col("text"), " "))

# -----------------------------
# Save processed data
# -----------------------------
df.write.mode("overwrite").parquet(output_path)

print("Data preprocessing complete!")

spark.stop()