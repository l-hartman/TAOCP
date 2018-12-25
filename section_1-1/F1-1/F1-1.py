#!/usr/bin/python3

'''
TAOCP - Algorithm F1.1

This is a python implementation of Euclid's algorithm for
finding the greatest common divisor of two given integers.

This is a more efficient version of algorithm E1.1.
The algorithm works without making trivial replacement
operations like "m <- n".

Usage: python3 gcd.py m n     # m,n are positive integers.
'''

import sys

def euclidCompute(m, n):
    if m < n:
        m,n = n,m
    while m > 1:
        m = m % n
        if m  == 0:
            return n    
        n = n % m
        if n == 0:
            return m

def main():
    ans = euclidCompute(int(sys.argv[1]), int(sys.argv[2]))
    print(ans)

main()
