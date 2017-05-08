from pyspark import SparkContext
import re

# count the distinct number of words 
# remove any non-words and split lines into separate words
# convert all words to lowercase

def splitter(line):
	line = re.sub(r'^\W+|\W+$', '', line)
	return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "distinct_word_count")
	
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	words_mapped = words.map(lambda x: (x,1))

	counts = words_mapped.reduceByKey(lambda x,y: 1) #Meaningless function, just aggregating keys
	print("Distinct Words:", counts.count())
