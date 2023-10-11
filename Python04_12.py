#!/usr/bin/env python3

# Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].


list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC' ]

#list comprehension:

tuples_list = []

tuples_list = [(len(x), x) for x in list]

print ("lista de tuplas:", tuples_list)

#imprimindo cada componente da lista separadamente:
position = 0

for comp in tuples_list:
	position += 1
	print ('tupla:', position, '\t', comp[0], '\t', comp[1])
