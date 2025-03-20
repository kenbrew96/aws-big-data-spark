from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()

data = [("John", 25), ("Jane", 30), ("Sam", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
