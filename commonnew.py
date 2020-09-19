# Databricks notebook source
def commonfunnew():
  file_location = "/FileStore/tables/googleplaystore.csv"
  file_type = "csv"
  #amit
  # CSV options
  infer_schema = "false"
  first_row_is_header = "true"
  delimiter = ","

  # The applied options are for CSV files. For other file types, these will be ignored.
  dfamitnew = spark.read.format(file_type) \
    .option("inferSchema", infer_schema) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .load(file_location)
  return dfamitnew
