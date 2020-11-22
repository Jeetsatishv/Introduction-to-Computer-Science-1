#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:46:40 2020

@author: jeet
"""
#Function 1
def dec_to_bin(n):
    '''This function takes a non-negative integer n and uses recursion to convert 
    it from decimal to binary – constructing and returning a string version of the binary 
    representation of that number. '''
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    else:
        x = dec_to_bin(n//2)
        if n%2==1:
            return x +'1' 
        else: 
            return x +'0'
        
#Function 2
def bin_to_dec(b):
    ''' that takes a string b that represents a binary number and uses recursion to convert 
    the number from binary to decimal, returning the resulting integer.'''
    if len(b) == 1:
        if b == '1':
            return 1
        if b == '0':
            return 0
    else:
        x = bin_to_dec(b[:-1])
        if b[-1] =='1':
            return 2*x+1
        if b[-1] =='0':
            return 2*x
    