
#Challenge 2: Large-Scale Data Preprocessing with PySpark
Overview
A distributed text preprocessing pipeline built with PySpark to handle multi-gigabyte raw text datasets. This pipeline performs cleaning, filtering, and tokenization, then saves the processed data in Parquet format for efficient downstream consumption by machine learning models.

Features
1. Distributed Processing with PySpark
Leverages Spark's distributed computing capabilities to process datasets larger than available memory

Configured with optimized memory settings for local development (spark.executor.memory=2g, spark.driver.memory=2g)

Uses Spark's adaptive query execution for improved performance

2. Text Cleaning Pipeline
Lowercasing: Standardizes all text to lowercase

Special Character Removal: Strips non-alphabetic characters using regex ([^a-zA-Z\s])

Whitespace Normalization: Removes extra spaces and trims text

Length Filtering: Filters out texts shorter than 10 characters to ensure meaningful content

3. Tokenization
Splits cleaned text into word tokens using space delimiter

Stores tokens as array column for easy feature extraction

Preserves original cleaned text alongside tokenized version

4. Efficient Output Format
Saves processed data in Parquet format for columnar storage and compression

Enables fast I/O for downstream model training

Maintains schema integrity for reliable data pipelines

## Setup
```bash
pip install pyspark

python preprocess.py

