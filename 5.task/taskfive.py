'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

smallestSolution = 0
smallestFlag = 0
counter = 20
numberIsOk = 1

while(smallestFlag == 0):
    for i in xrange(1,20):
        division = counter % i
        if(division != 0):
            numberIsOk = 0

    if(numberIsOk == 1):
        smallestSolution = counter
        smallestFlag = 1

    numberIsOk = 1
    counter = counter + 20

print(smallestSolution)

