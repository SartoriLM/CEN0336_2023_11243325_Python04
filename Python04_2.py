#!/usr/bin/env python3

#Write a script that splits a string into a list:

#Save the string sapiens, erectus, neanderthalensis as a variable named taxa.
taxa = 'sapiens, erectus, neanderthalensis'

#Print taxa 
print ("taxa:", taxa)

#Print taxa[1], what do you get?
print ("taxa[1]:", taxa[1])

#Print type(taxa). What is it's type?
print ("type:", type (taxa))

#Split taxa into individual words and print the result of the split. (Think about the ', '.)
taxa.split (', ')

#Store the result of split in a new variable named species.
species = taxa.split (', ')

#Print species.
print ("species:", species)

#Print the species[1], What do you get?
print ('species[1]:', species[1])

#Print type(species). What is it's type?
print ('type:', type(species))

#Sort the list alphabetically and print (hint: lookup the function sorted()).
sorted_list = sorted (species)
print ("sorted list:", sorted_list)

#Sort the list by length of each string and print. (The shortest string should be first).
sorted_list_len = sorted (species, key=len)
print ("lenght sorted list:", sorted_list_len)
