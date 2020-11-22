#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:52:32 2020

@author: jeet
"""

#Function 1
def first_occur(seq, elem):
    '''This function takes as inputs a sequence (i.e., a list or string) seq and an element elem, 
    and returns the index of the first occurrence of elem in seq'''
    if seq ==[] or seq == '':
        return -1
    elif seq[0] == elem:
        return 0
    else:
        x = first_occur(seq[1:], elem)
        if x ==-1:
            return -1
        else:
            return x+1
            
#Function 2
def last_occur(seq, elem):
    '''This function takes as inputs a sequence (i.e., a string or list) seq and an element elem
    and returns the index of the last occurrence of elem in seq'''
    if seq ==[] or seq == '':
        return -1
    elif seq[-1] == elem:
        return len(seq)-1
    else:
        x = last_occur(seq[:-1], elem)
        if x ==-1:
            return -1
        else:
            return x
    
#Function 3
#help function
def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest
    
#Function 3 itself
def jscore(s1, s2):
    '''This function takes two strings s1 and s2 as inputs and returns the Jotto score 
    of s1 compared with s2 – i.e., the number of characters in s1 that are shared by s2'''
    if s1 == [] or s2 == [] or s1 =='' or s2 == '':
        return 0
    else:
        x = jscore(s1[1:],rem_first(s1[0],s2))
        if s1[0] in s2:   
            return 1 + x
        if x == 0:
            return 0 
        else:
            return x 