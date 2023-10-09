#!/usr/bin/env python3

# Write a script that uses a while loop to calculate the factorial of 1000.

#f = fatorial
#n = número

f = 1
n = 1000

while n > 0:
  f = f * n
  n -= 1

print ("fatorial is:", f)
