#!/usr/bin/python

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(x):
    total = 0
    for i in range(1, x+1):
        total += i**2
    return total

def squareOfSum(x):
    total = 0
    for i in range(1, x+1):
        total += i
    return total**2

def solve(x):
    return squareOfSum(x) - sumOfSquares(x)
