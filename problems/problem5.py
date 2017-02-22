#!/usr/bin/python

from functools import reduce
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primes_in_range(minimum, maximum):
    array = []
    for i in range(minimum, maximum+1):
        for n in range (2, i):
            if i % n == 0:
                break
        else:
            array.append(i)
    return array

def solve(minimum, maximum):
    num = 0
    array1 = primes_in_range(minimum, maximum)
    array2 =list(array1)
    for i in array1:
        if i == 1:
            continue
        temp = i*i
        while temp < maximum:
            array2.append(i)
            temp *= i
    return reduce(lambda x,y: x*y, array2)
