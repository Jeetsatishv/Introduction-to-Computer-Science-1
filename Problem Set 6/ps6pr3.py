#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:49:37 2020

@author: jeet
"""

# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions with loops
#

#Function 1
def add_spaces(s):
    '''The function takes a string 's' as input and uses for loop to form 
    and return the string formed by adding a space between each pair of 
    characters in the string.'''
    result = ''
    for x in s:
            result = result + x + ' ' 
    return result[0:-1]


#Function 2
def merge(s1, s2):
    '''The function takes as an input 2 strings and uses a for loop to
    merge the characters in the string s1 and s2 and return the new string'''
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        if s1[i] == s2[i]:
            result = result + s1[i]
        else:
            result = result + s1[i] + s2[i]
    if len(s1)>len(s2):
        x = len(s1) - len(s2)
        result = result + s1[-x::]
    elif len(s2)>len(s1):
        x = len(s2) - len(s1)
        result = result + s2[-x::]
    return result


#Function 3
def contains(s, c):
    '''This function takes a string and a single-character c, and uses a for loop
    to determine if the character exists in the string. It returns true if it does
    or false if it does not.'''
    for i in range(len(s)):
        if s[i] == c:
            return True
    return False
                  