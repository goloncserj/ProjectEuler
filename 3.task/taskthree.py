'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

number = 600851475143
largestPrimeFactor = 0
divisibleCounter = 0

for i in range(1,number):
	if(i % 2 != 0):
		if(number % i == 0):
			for j in range(1,i):
				if(i % j == 0):
					divisibleCounter = divisibleCounter + 1
					if(divisibleCounter > 2):
						divisibleCounter = 0
						continue
					else:
						largestPrimeFactor = i

print(i)