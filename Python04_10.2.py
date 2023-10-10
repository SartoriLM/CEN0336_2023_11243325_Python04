#!/usr/bin/env python3

#Modify your script so that it will only print the number if it is odd.

import sys

num1 = int(sys.argv [1])
num2 = int(sys.argv [2]) + 1

for x in range (num1, num2):
	if x % 2 != 0:
		print (x)
