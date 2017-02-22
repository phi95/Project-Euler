#!/usr/bin/python

from problems import *

x = "Problem {}: {}"

print (x.format(1, problem1.solve(1000)))
print (x.format(2, problem2.solve(1,2,4000000)))
print (x.format(3, problem3.solve(600851475143)))
print (x.format(4, problem4.solve(3)))
print (x.format(5, problem5.solve(1,20)))
