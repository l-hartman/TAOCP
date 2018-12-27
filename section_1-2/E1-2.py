#!/usr/bin/python3

'''
TAOCP - Algorithm E1.2

This is a python implementation of (extended) Euclid's algorithm for
finding the greatest common divisor of two given integers.

This is a more efficient version of algorithm E1.1.
The algorithm works without making trivial replacement
operations like "m <- n".

Usage: python3 gcd.py m n     # m,n are positive integers.
'''

import sys

def euclidCompute(m, n):
    # E1 Initialize 
    d = n
    c = m
    b_ = 0
    a = b_
    b = 1
    a_ = b

    while d > 1:
        # E2 Divide
        q = c // d #can this be done in python in one line??
        r = c % d
        
        # E3 Remainder zero?
        if r == 0:
          return a,m,b,n,d
  
        # E4 Recycle
        c = d 
        d = r
        t = a_
        a_ = a
        a = t - q*a
        t = b_
        b_ = b 
        b = t - q*b 
        

def main():
    a,m,b,n,d = euclidCompute(int(sys.argv[1]), int(sys.argv[2]))
    print("a*m + b*n = d")
    print(a, "*", m, " + ", b, "*", n, " = ", d) 


main()
