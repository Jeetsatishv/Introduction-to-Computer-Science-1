#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:25:12 2020

@author: jeet
"""

def log(b,n):
    '''This function returns the logarithm to the base b of a number n 
    – or, in cases in which n is not an integral power of b, an integer 
    estimate of the log.'''
    count = 0
    while n>1:
        j = n
        n = n//b
        count += 1
        print('dividing', j, 'by', b, 'gives', n)
    return count


def add_powers(m, n):
    '''This function takes a positive integer m and an arbitrary integer n, 
    and adds together the first m powers of n (from n**0 up to and including
    n**(m-1) power) and that returns the resulting sum.'''
    csum = 0
    for i in range(m):
        print(n, '**', i, '=', n**i)
        csum += n**i
    return csum


def negate_odds(values):
    '''This function takes a list of integers called values, and that modifies 
    the list so that all of its odd-valued elements are replaced with their negated 
    values, but all of its even-valued elements are left unchanged.'''
    for i in range(len(values)):
        if values[i] % 2 == 0:
            values[i] = values[i]
        else:
            values[i] = -values[i]