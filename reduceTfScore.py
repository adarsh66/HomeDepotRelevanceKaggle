#!/usr/bin/python

import sys
import math


def main():
        for line in sys.stdin:
		try:
			num_files= 0
			tf_frequency = 0
			line = line.rstrip('\n')
			word, total_count, index_map = line.split(':')
			word = word.strip()
			#removing all the chars not required to break down this token further
			index_map = index_map.replace('{','').replace('}','').replace('(','')
			for file_index in index_map.split('),'):
				file_name, count = file_index.split(',')
				count = count.replace(')','').strip()
				file_name = file_name.strip()
				num_files+=1
				tf_frequency += int(count)
				idf_term = calc_idf(num_files)
				#Changingg the below to log function to avoid potential underflow
				tf_idf_score = math.log10(tf_frequency) + math.log10(idf_term)
				emit(word, file_name, tf_idf_score)
		except ValueError:
			print (line)
	
def calc_idf(num_files):
	''' calculate the idf value for the term based on the number of files in which its found '''
	N = 124428
	return math.log10(N/(1+num_files))

def emit(word, file_name, tf_idf_score):
	''' print out the tf score for the terms to std out in the format required '''
	print word + ', ' + file_name + ' ,' + str(tf_idf_score)

if __name__ == '__main__':
        main()

