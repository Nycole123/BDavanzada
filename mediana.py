# -*- coding: utf-8 -*-
"""Mediana.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1In0sifEBJWq_i7h5d7XseZR8hlBrjuGR
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Notas de estudiantes").getOrCreate()

spark

data = [("Alex", 20), ("Luisa", 18), ("Carlos", 15), ("Lucas", 14), ("Sara", 18),("Aron", 16),("Camila", 13),("Susana", 19),("Alfredo", 5),("Alonso", 11),("Karen", 9),("Alexa", 8),("Hellen", 2),("Mauricio", 6),("Luciana", 12),("Jacob", 18),("Estefani", 19),("Daniela", 17)]
columns = ["Nombre", "Edad"]
variable = spark.createDataFrame(data, columns)

var_mediana = variable.approxQuantile("Edad", [0.5], 0.0)

print("La mediana es:", var_mediana)