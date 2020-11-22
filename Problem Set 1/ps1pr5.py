#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:05:49 2020

@author: jeet
"""
#function 1
def last_first(values):
    """ This function returns a new list containing 
    the last value of the original list followed by 
    the first value of the original list """
    last = values[-1]
    first = values[0]
    return [last, first]


#function 2
def every_other(values):
    """ This function takes as input a list values 
    and returns a list containing every other value 
    from the original list"""
    ans = values[0::2]
    return ans

#function 3
def begins_with(word, prefix):
    """This function takes as inputs two string values
    word and prefix, and that returns True if the string 
    word begins with the string prefix, and False otherwise"""
    
    size = len(prefix)
    if word[0:size] == prefix:
        return True
    else:
        return False