#!/usr/bin/env python3

#Calculate two cumulative sums, one of all the even values and one of all the odd values.
#Print only the final two sums. The output from your script should be:
#Sum of even numbers: 150 
#Sum of odds: 286

list = [101,2,15,22,95,33,2,27,72,15,52]

even_sum = 0
odd_sum = 0

for x in list:

	if x % 2 ==  0:
		even_sum  = even_sum + x

	else:
		odd_sum = odd_sum + x

print ("Sum of even numbers:", even_sum)
print ("Sum of odds:", odd_sum)

