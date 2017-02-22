#!/usr/bin/python

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def prime_number(number):
    i = 1
    q = 0
    while True:
        i += 1
        for n in range (2, i):
            if i % n == 0:
                break
        else:
            q += 1
            if q == number:
                return i

def solve(number):
    return prime_number(number)
