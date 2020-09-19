# Databricks notebook source
dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

dbutils.widgets.get("X123")

# COMMAND ----------

#from pyspark.sql.functions import sum

#file_location = "/FileStore/tables/googleplaystore.csv"
#file_type = "csv"
##amit
## CSV options
#infer_schema = "false"
#first_row_is_header = "true"
#delimiter = ","

## The applied options are for CSV files. For other file types, these will be ignored.
#dfamitnew = spark.read.format(file_type) \
#  .option("inferSchema", infer_schema) \
#  .option("header", first_row_is_header) \
#  .option("sep", delimiter) \
#  .load(file_location)

#df5 = dfamitnew
#display(df5.select('category','rating').where(df5.Rating != 'NaN').groupBy('category').agg(sum('Rating')))
