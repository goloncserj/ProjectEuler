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