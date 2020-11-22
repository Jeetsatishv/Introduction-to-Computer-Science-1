#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 02:21:05 2020

@author: jeet
"""
#Function 1
def bitwise_and(b1, b2):
    '''This function takes as inputs two strings b1 and b2 that represent 
    binary numbers and computes the bitwise AND of the two numbers and 
    returns the result in the form of a string.'''
    if len(b1)>len(b2):
        ext = (len(b1)-len(b2))*'0'
        b2 = ext + b2
    if len(b2)>len(b1):
        ext = (len(b2)-len(b1))*'0'
        b1 = ext + b1
    if b1 == '' and b2 =='':
        return ''
    if b1 == '':
        return len(b2)*'0'
    if b2 =='':
        return len(b1)*'0'
    else:
       x = bitwise_and(b1[1:], b2[1:])
       if b1[0] == '1' and b2[0] == '1':
           return '1' + x
       else:
           return '0' + x
       
#Function 2
def add_bitwise(b1, b2):
    '''This function adds two binary numbers.'''
    if b1 == '' and b2 =='':
        return ''
    if b1 == '':
        return b2
    if b2 =='':
        return b1
    else:
        x = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return x + '0'
        if b1[-1] == '1' and b2[-1] == '0':
            return x + '1'
        if b1[-1] == '0' and b2[-1] == '1':
            return x + '1'
        return add_bitwise(x, '1') + '0'
    
         