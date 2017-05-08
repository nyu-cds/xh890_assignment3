from pyspark import SparkContext
from operator import mul
import re

# calculate the factorial of 1000
# RDD from 1 to  1001 and apply a "rolling multiply" on each element

if __name__ == '__main__':
	sc = SparkContext("local", "1-1000 Folded Product")
	
	product = sc.parallelize(range(1, 1001)).fold(1, mul)

	print("Factorial of 1000:", product)
