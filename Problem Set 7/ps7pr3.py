#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *


def alive_neighbors(posnr, posnc, grid):
    '''This function returns the number of alive neighbors 
    of the cell at position [posnr][posnc] in the specified grid'''
    count = 0
    for r in range(posnr-1,posnr+2):
        for c in range(posnc-1,posnc+2):
            if grid[r][c] == 1:
                if r == posnr and c == posnc:
                    count += 0
                else:
                    count += 1
    return count


def next_gen(grid):
    '''This function takes a 2-D list called grid that represents the current 
    generation of cells, and that uses the rules of the Game of Life to create 
    and return a new 2-D list representing the next generation of cells.'''
    new_grid = copy(grid)
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            memalive = alive_neighbors(r, c, grid)
            if memalive<2:
                new_grid[r][c]=0
            if memalive>3:
                new_grid[r][c]=0
            if grid[r][c] == 0 and memalive == 3:
                new_grid[r][c]=1
    return new_grid
    