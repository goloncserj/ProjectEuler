'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

numberOne = 999
numberTwo = 999
biggestPalindromeNumber = 0

for i in xrange(numberOne, 101, -1):
      for j in xrange(numberTwo, 101, -1):
            multiplication = i * j
            multiplicationString = str(multiplication)
            multiplicationStringReverse = multiplicationString[::-1]
            if(multiplicationString == multiplicationStringReverse):
                  if(multiplication > biggestPalindromeNumber):
                        biggestPalindromeNumber = multiplication

print (biggestPalindromeNumber)