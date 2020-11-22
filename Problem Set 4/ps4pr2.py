#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:20:28 2020

@author: jeet
"""

from ps4pr1 import *

#Function 1
def mul_bin(b1, b2):
    '''This function takes as inputs two strings b1 and b2 that represent 
    binary numbers and multiplies the numbers and returns the 
    result in the form of a string that represents a binary number.'''
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b = dec_to_bin(n1*n2)
    return b


#Function 2
def add_bytes(b1, b2):
    '''This function takes as inputs two strings b1 and b2 that represent bytes 
    (i.e., 8-bit binary numbers) and computes the sum of the two 
    bytes and returns that sum in the form of a string that represents an 8-bit 
    binary number.'''
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    x = dec_to_bin(n1 + n2)
    if len(x) < 8:
        z = 8-len(x)
        return z*'0' + x
    elif len(x)>8:
        return x[-8::]
        
    
        