#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 01:48:01 2020

@author: jeet
"""

#Function 1
def cube_evens_lc(values):
    '''This function returns the cubes of even numbers in values'''
    return [   x**3   for x in values if x%2==0]

#Function 2
def cube_evens_rec(values):
    '''This function returns the cubes of even numbers in values'''
    if values==[]:
            return []
    else:
        x = cube_evens_rec(values[1:])
        if values[0]%2==0:
            z = values[0]**3
            return [z] + x
        else:
            return x

#Function 3
def num_occur(c, s):
    '''This function takes a single character c and an arbitrary string s and 
    returns the number of times that c occurs in s'''
    z = [ x  for x in s if c in x ]
    return len(z)

#Function 4
def most_occur(c, words):
    '''This function  takes a single character c and a list of one or more strings 
    called words and returns the string in the list with the most occurrences of c'''
    x = [[num_occur(c, words), words] for words in words ]
    needed = max(x)
    return needed[1]

#Function 5
def price_string(cents):
    '''This function takes as input a positive integer 'cents' representing a price given 
    in cents, and then returns a string in which the price is expressed as 
    a combination of dollars and cents'''
    d = (cents//100)
    c = (cents%100)
    vocab1 = ' dollars '
    vocab2 = ' cents'
    
    if cents<100:
        if cents==1:
            vocab2 = ' cent'
            return str(cents) + vocab2
        else: 
            return str(cents) + vocab2
    elif cents==100:
        vocab1 = ' dollar'
        return str(d) + vocab1
    elif c==0:
        vocab1 = ' dollars'
        return str(d) + vocab1 
    elif c==1 and d!=1:
        vocab2 = ' cent'
        return str(d) + vocab1 + 'and ' + str(c) + vocab2
    elif d==1 and c==1:
        vocab1 = ' dollar '
        vocab2 = ' cent'
        return str(d) + vocab1 + 'and ' +str(c) + vocab2
    elif d==1 and c!=1:
        vocab1 = ' dollar '
        vocab2 = ' cents'
        return str(d) + vocab1 + 'and ' +str(c) + vocab2
    else:
        return str(d) + vocab1 + 'and ' +str(c) + vocab2
        

    
    