python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
