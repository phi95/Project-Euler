#!/usr/bin/python

from problems import *

x = "Problem {}: {}"

print (x.format(1, problem1.solve(1000)))
print (x.format(2, problem2.solve(1,2,4000000)))
