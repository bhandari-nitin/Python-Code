import pyspark

spark = pyspark.sql.SparkSession.builder.appName('test')

spark.range(10).collect()