from pyspark import SparkContext
from pyspark import SparkFiles
finddistance = "/home/maria_dev/finddistance.R"
finddistancename = "finddistance.R"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
print "Absolute Path -> %s" % SparkFiles.get(finddistancename)