from pyspark.sql.functions import col, lower, regexp_replace, split, trim
from spark_config import create_spark_session

def preprocess_text_data(input_path: str, output_path: str):
    spark = create_spark_session()
    
    try:
        # Load TinyStories dataset
        df = spark.read.text(input_path)
        print(f"Loaded {df.count()} stories from {input_path}")
        
        # Rename column
        df = df.withColumnRenamed("value", "text")
        
        # Cleaning
        df = df.withColumn("text", lower(col("text")))
        df = df.withColumn("text", regexp_replace(col("text"), "[^a-zA-Z\\s]", ""))
        df = df.withColumn("text", regexp_replace(col("text"), "\\s+", " "))
        df = df.withColumn("text", trim(col("text")))
        
        # Remove empty/short stories
        df = df.filter(col("text") != "")
        df = df.filter(col("text").rlike(".{20,}"))  # Longer min for stories
        
        # Tokenization
        df = df.withColumn("tokens", split(col("text"), " "))
        
        # Save as Parquet
        df.write.mode("overwrite").parquet(output_path)
        print(f"Saved {df.count()} processed stories to {output_path}")
        
        # Show sample
        df.show(3, truncate=100)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    preprocess_text_data("tinystories.txt", "../processed_data/tinystories_cleaned")