## PROJECT 4: Big Data Processing with Apache Spark

### 📁 GitHub Structure
```
aws-big-data-spark/
├── spark_job.py
```

### 📄 `spark_job.py`
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
```
**Explanation**: This script initializes Spark, loads sample data, and prints it.
