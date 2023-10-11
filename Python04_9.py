#!/usr/bin/env python3

#Create a new script that uses list comprehension to do the same thing as problem 8. (Use range() to print out every number between 1 and 100.)

#usando list comprehension
list = [x for x in range (1, 101)] 
print ("list:", list)

#imprimindo cada elemento da lista como no exercício 8, como solicitado
for x in list:
	print ("list elements:", x)

