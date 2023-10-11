#!/usr/bin/env python3
# Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")


list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
position = 0

for x in list:
	position += 1
	length = str(len(x))
	print (position, '\t', length, '\t', x)
