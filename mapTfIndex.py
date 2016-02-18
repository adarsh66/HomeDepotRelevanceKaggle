#!/usr/bin/python
import os
import sys
import string

def main():
        for line in sys.stdin:
		try:
                	product_uid, line = line.strip().split(',"', 1)
			for word in line.split():
				word = clean_puncs(word)
				if len(word) > 1:
					emit(word, product_uid)
		except:
			sys.stderr.write(line)

def emit(word, prod):
	print (word + '\t' + prod + '\t' + '1')

def clean_puncs(word):
	''' clean up any punctuations in the word'''
	punctuation_list = [',',':',';','{','}','[',']','(',')','.','?','|','!']
	for punc in punctuation_list:
		word = word.replace(punc, "")
	return word

#main() func is a recurring feature in all my code
#I like functions better than running the code like a script
#More readable for a human
if __name__ == '__main__':
        main()

