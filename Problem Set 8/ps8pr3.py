
#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Markov text generation 
#

import random

def create_dictionary(filename):
    '''This function takes a string representing the name of a text
    file, and that returns a dictionary of key-value pairs'''
    txtfile = open(filename, 'r')
    txt = txtfile.read()
    txtfile.close()
    words = txt.split()
    j = {}
    moment = '$'
    for later in words:
        if moment not in j:
            j[moment] = [later]
        else:
            j[moment] += [later]
        if '.' in later or '?' in later or '!' in later:
            moment = '$'
        else:
            moment = later
    return j


def generate_text(word_dict, num_words):
    '''This function takes as a parameter a dictionary of word transitions,
    and then generates and prints num_words words with space after each word'''
    moment = '$'
    for z in range(num_words):
        later = random.choice(word_dict[moment])
        print(later, end = ' ')
        if '.' in later or '?' in later or '!' in later:
            moment = '$'
        else:
            moment = later