#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:00:42 2020

@author: jeet
"""


# function 1
def reverse(s):
    '''This function  takes a string input 
    s and returns a string in which the characters 
    of s have been reversed'''
    return s[-1::-1]

# function 2
def ends_match(s):
    '''This function takes a string input s and returns 
    True if the first character in s matches the last 
    character in s, and False otherwise'''
    if s[0] == s[-1]:
        return True
    else:
        return False
    
# function 3
def replace_start(values, new_start_vals):
    '''This function takes as inputs a list values and 
    another list new_start_vals, and that returns a new 
    list in which the elements in new_start_vals have replaced 
    the first n elements of the list values, where n is the length 
    of new_start_vals'''
    newlist = len(new_start_vals)
    values = values[newlist::1]
    return new_start_vals + values


# function 4
def adjust(s, length): 
    '''This function takes as inputs a string s and an integer length, 
    and that returns a string in which the value of s has been adjusted
    as necessary to produce a string with the specified length.'''
    if len(s)<length:
        z = length-len(s)
        return s + z*s[-1]
    elif len(s)>length:
        return s[0:length:1]
    elif len(s)==length:
        return s