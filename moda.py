# -*- coding: utf-8 -*-
"""Moda.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qEuCrCvKVhh2GP30W2ugCFCX1uCD53OM
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Notas de estudiantes").getOrCreate()

spark

data = [("Alex", 20), ("Luisa", 18), ("Carlos", 15), ("Lucas", 14), ("Sara", 18),("Aron", 16),("Camila", 13),("Susana", 19),("Alfredo", 5),("Alonso", 11),("Karen", 9),("Alexa", 8),("Hellen", 2),("Mauricio", 6),("Luciana", 12),("Jacob", 18),("Estefani", 19),("Daniela", 17)]
columns = ["Nombre", "Notas"]
variable = spark.createDataFrame(data, columns)

var_moda = variable.groupBy("Notas").count().orderBy(col("count").desc()).first()

print("La moda es:", var_moda["Notas"])