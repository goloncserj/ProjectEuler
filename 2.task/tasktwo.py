fourmillion = 4000000
fibonacciList = [1,2]
resultSum = 0

for i in fibonacciList:
	newMember = fibonacciList[-1]+fibonacciList[-2]
	if (newMember < fourmillion):
		fibonacciList.append(newMember)

for i in fibonacciList:
	if(i % 2 == 0):
		resultSum += i

print(resultSum)

















