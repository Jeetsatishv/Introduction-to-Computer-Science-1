# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def root(x):
    """ returns the square root of its input
        input x: any number (int or float)
    """
    return x**0.5

# function 2
def gap(num1, num2):
    ''' returns the gap between 2 of its iputs
    input num1, num2: any number (int or float)
    
    '''
    if num1>num2:
        return num1-num2
    elif num2>num1:
        return num2-num1
    else: 
        return 0
    
# function 3
def larger_gap(a1, a2, b1, b2):
    onegap = gap(a1, a2)
    twogap = gap(b1, b2)
    if onegap>twogap:
        return onegap
    elif twogap>onegap:
        return twogap
    elif onegap==twogap:
        return onegap or twogap


# function 4
def median(a,b,c):
    if b<=a<=c or c<=a<=b:
        return a
    if a<=b<=c or c<=b<=a:
        return b
    if b<=c<=a or a<=c<=b:
        return c


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
