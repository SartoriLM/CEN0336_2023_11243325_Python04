#!/usr/bin/env python3

#Print out the length and the sequence, separated by a tab. The output should look like:
#14	ATGCCCGGCCCGGC
#25	GCGTGCTAGCAATACGATAAACCGG
#12	ATATATATCGAT
#8	ATGGGCCC

list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for x in list:
	length = str(len (x)) 
	print (length + '\t' + x)
