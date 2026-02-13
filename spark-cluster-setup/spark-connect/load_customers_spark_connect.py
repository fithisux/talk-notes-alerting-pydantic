# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder.remote("sc://127.0.0.1:15002").getOrCreate() 

df = spark.read.csv('customers-100.csv')
df.show()

spark.stop()