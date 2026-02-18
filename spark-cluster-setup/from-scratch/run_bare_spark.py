# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder.master("spark://spark-master:7077").appName('bare-run').getOrCreate()

df = spark.range(10)

df.show()

df.write.csv("dddd.csv")

# df.show()

spark.stop()