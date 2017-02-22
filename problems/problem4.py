#!/usr/bin/python

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(x):
    return str(x) == str(x)[::-1]

def solve(digits):
    minimum = "1"
    maximum = ""
    for i in range(0,digits):
        maximum += "9"
        if i>0:
            minimum += "0"

    minimum = int(minimum)
    maximum = int(maximum)

    array = []
    for n in range(minimum, maximum+1):
        for j in range(minimum, maximum+1):
            temp = n*j
            if isPalindrome(temp):
                array.append(temp)

    return max(array)
