#
# ps2pr6.py - Problem Set 2, Problem 6
#
# Writing list comprehensions
#
# Computer Science 111
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [ x**2 for x in range(7)]

# part b
words = ['do', 'you', 'comprehend', 'list', 'comprehensions?']
lc2 = [  w[::-1] for w in words]

# part c
lc3 = [   w[0]+w[-1]  for w in ['python', 'is', 'very', 'fun!']]

# part d
lc4 = [  y%2     for y in range(2, 8)]

# part e
lc5 = [   c    for c in 'abracadabra' if     c not in 'aeiou'       ]


# Problem 6-2: Put your definition of the multiples_of() function below.

def multiples_of(x, num):
    ''' This function takes a number 'x' as input and a positive integer 'num'
    and returns a list containing first 'num' multiples of 'x' beggining with x itself'''
    return [x*num for num in range(1, num+1)]


# Problem 6-3: Put your definition of the longer_than() function below.

def longer_than(n, wordlist):
    '''This function takes an integer 'n' and a list of strings 'wordlist' and returns a 
    list consiting of all the words from wordlist that are longer than n'''
    return [wordlist for wordlist in wordlist if n<len(wordlist)]


# The code below prints the values of your expressions
# from 6-1. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(1, 6):
        lc_var = 'lc' + str(n)
        if lc_var in dir():
            print(lc_var, '=', eval(lc_var))
