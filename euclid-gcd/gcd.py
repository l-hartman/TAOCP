#!/usr/bin/python3

'''
TAOCP - Algorithm 1.1E

This is a python implementation of Euclid's algorithm for
finding the greatest common divisor of two given integers.

Usage: python3 gcd.py m n     # m,n are positive integers.
'''

import sys

def euclidCompute(m, n):
    if m < n:
        m,n = n,m
    while m > 1:
        r = m % n
        if r == 0:
            return n    
        m,n = n,r

def main():
    ans = euclidCompute(int(sys.argv[1]), int(sys.argv[2]))
    print(ans)

main()
