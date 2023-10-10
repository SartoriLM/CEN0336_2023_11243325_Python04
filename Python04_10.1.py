#!/usr/bin/env python3

#Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

import sys

num1 = int(sys.argv [1])
num2 = int(sys.argv [2]) + 1

for x in range (num1, num2):
	print (x)
