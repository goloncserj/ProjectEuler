'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

five = 5
three = 3
multiples = 0
zero = 0
firstElement = 1
lastElement = 1000

for i in range(firstElement,lastElement):
	if i%three == zero or i%five == zero:
		multiples += i

print(multiples)