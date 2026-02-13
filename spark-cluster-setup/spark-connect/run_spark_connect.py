# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder.remote("sc://127.0.0.1:15002").getOrCreate() 

df = spark.range(100)

df.write.mode("overwrite").parquet("example.parquet")

df.show()

spark.stop()