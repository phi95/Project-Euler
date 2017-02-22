#!/usr/bin/python
import math
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def solve(number):
    if(number == 2):
        return 2
    while(number % 2 == 0):
        number /= 2
    for i in range(3, math.ceil(math.sqrt(number))):
        while(number%i == 0):
            maxNum = i
            number /= i
        i+=2
    if(number > 2):
        return number
    return maxNum
