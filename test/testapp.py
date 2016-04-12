#!/usr/local/share/spark1626/bin/pyspark
import os
import sys

# Set the path for spark installation
# this is the path where you have built spark using sbt/sbt assembly
os.environ['SPARK_HOME'] = "/usr/local/share/spark1626"
# os.environ['SPARK_HOME'] = "/home/jie/d2/spark-0.9.1"
# Append to PYTHONPATH so that pyspark could be found
sys.path.append("/usr/local/share/spark1626/python")
# sys.path.append("/home/jie/d2/spark-0.9.1/python")

# Now we are ready to import Spark Modules
try:
    from pyspark import SparkContext
    from pyspark import SparkConf

except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)

conf=SparkConf()
#conf.setMaster("spark://172.18.109.87:7077")
conf.setMaster("local")
conf.setAppName("spark_svm")
conf.set("spark.executor.memory", "3g")
sc = SparkContext(conf=conf)
sample = sc.textFile("sample")
print sample.count()
