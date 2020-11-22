#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:55:21 2020

@author: jeet
"""


# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Creating recursive function
#


#Function 1
def repeat(s, n):
    """ This function takes a string s and an integer n, 
    and uses recursion to create and return a string in 
    which n copies of s have been concatenated together"""
    if n<= 0 :
        return ''
    if n == 1:
        return s
    else:
        rep = repeat(s, n-1)
        return rep + s
    
#Function 2
def contains(s, c):
    """ This function takes an arbitrary string s and a 
    single-character c as inputs and uses recursion to 
    determine if s contains the character c, returning
    True if it does and False if it does not. """
    if s == '':
        return False
    if s[0] == c:
        return True
    else:
       char = contains(s[1:], c)
       return char
   
        
#Function 3
def add(vals1, vals2):
    """ This function takes as inputs two lists of numbers, 
    vals1 and vals2, and that uses recursion to construct and 
    return a new list in which each element is the sum of the 
elements at the corresponding positions in the original lists."""
    if len(vals1) != len(vals2):
         return []
    if vals1 == [] or vals2==[]:
         return []
    else: 
         x = vals1[0]+vals2[0]
         z = add(vals1[1:], vals2[1:])
         return [x] + z
    
    
        
                 