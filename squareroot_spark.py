from pyspark import SparkContext
from operator import add
import re

# calculate the average of all square roots within a range
# map ech element in RDD to roots. 
# reduce to sum and divide by key count

if __name__ == '__main__': 
    sc = SparkContext("local", "sqrt avg")

    roots = sc.parallelize(range(1, 1001)).map(lambda x: x ** 0.5)
  
    avg = roots.fold(0, add) / roots.count()

    print("average of square roots below 1001:", avg)
