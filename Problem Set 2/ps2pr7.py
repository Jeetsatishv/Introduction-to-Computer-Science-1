#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:24:06 2020

@author: jeet
"""

#Function 1
def letter_score(letter):
    """ This function takes in a lowercase letter as an input
    and returns the value of that as a scrabble tie"""
    assert(len(letter) == 1)
    
    if letter in ['b', 'c', 'm', 'p']:   # letters with a score of 3
        return 3
    elif letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j', 'x']:
        return 8 
    elif letter in ['q', 'z']:
        return 10 
    else:
        return 0

#Function 2
def scrabble_score(word):
    '''This function takes as an input string and returns the 
    scrabble score of that string'''
    if word == '':
        return 0
    else: 
        x = scrabble_score(word[1:])
        z = x + letter_score(word[0])
        return z
        
#Function 3
def smaller_of(vals1, vals2):
    '''This function takes as inputs two lists vals1 and vals2 and uses 
    recursion to construct and return a new list in which each element is 
    the the smaller of the corresponding elements from the original lists'''
    if vals1==[] or vals2==[]:
        if len(vals1)>len(vals2):
            return vals2
        else:
            return vals1
    else:
        x = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] > vals2[0]:
            z = vals2[0]
        else:
            z = vals1[0]
        return [z] + x
    
    
#Function 4
def merge(s1, s2):
    '''takes as inputs two strings s1 and s2 and returns a new string that is 
    formed by “merging” together the characters in the strings s1 and s2 to create 
    a single string'''
    if s1== '' or s2=='':
        if len(s1)>len(s2):
            return s1
        if len(s2)>len(s1):
            return s2
        elif len(s1) == len(s2):
            return ''
    else:
        x = merge(s1[1:], s2[1:])
        if s1[0] ==s2[0]: 
            return s1[0] + x 
        else:
            return  s1[0] + s2[0] + x
    
'''In the function above I chose to not use any other external variable
such as 'z' (like i did in other question)because I wanted to keep the code short and simple'''
    

    
    
    
    
    
    
    
    
    