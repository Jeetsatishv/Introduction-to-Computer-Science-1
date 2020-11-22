#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:21:39 2020

@author: jeet
"""

# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# Creating functions
#

#Function 1
def move_to_end(s, n):
    '''This function will takes as inputs a string value s 
    and an integer n, and returns the a new string in 
    which the first n characters of s have been moved to the 
    end of the string'''
    return s[n::] + s[0:n]

#Function 2
def reverse_last(vals, n):
    '''This function takes as inputs a list vals and an integer n, 
    and returns a new list in which the last n values of vals are 
    reversed and all other values from vals remain in their original positions'''
    if n <len(vals):
        return vals[0:(len(vals)-n)] + vals[len(vals):-n-1:-1]
    else:
        return vals[-1::-1]
                    