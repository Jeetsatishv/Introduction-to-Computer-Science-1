#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
        s += '--' * (self.width)
        s += '-' + '\n'
        for col in range(self.width):
            s += ' ' + str(col%10)
        return s

    def add_checker(self, checker, col):
        '''This method adds a specified checker to the specified column 'col'.''' 
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        for r in range(0, self.height-1):
            if self.slots[r+1][col] == ' ':
                r += 1
            else:
                break
        self.slots[r][col] = checker
        
        
        
    def reset(self):
        '''This method resets the board by by setting all slots to contain a space character.'''
        self.__init__(self.height, self.width)
    
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def can_add_to(self, col):
        '''This method returns True if it is valid to place a 
        checker in the column col on the calling Board object, otherwise it gives false'''
        if col<0 or col>self.width-1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        return True

    def is_full(self):
        '''This method returns True if the called Board object is completely 
        full of checkers, and returns False otherwise.'''
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c] == ' ':
                    return False
        return True
    
    def remove_checker(self, col):
        '''This method removes the top checker from column col of the called Board object. 
        If the column is empty, then the method should do nothing.'''
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
            
            
    def is_horizontal_win(self, checker):
        '''This method checks if the specified checker has won horizonally'''
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
        return False

    def is_vertical_win(self, checker):
        '''This method checks if the specified checker has won vertically'''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                       return True
        return False
            
    def is_up_diagonal_win(self, checker):
        '''This method checks if the specified checker has won diagonally up'''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col-1] == checker and \
                   self.slots[row+2][col-2] == checker and \
                   self.slots[row+3][col-3] == checker:
                       return True
        return False
    
    def is_down_diagonal_win(self, checker):
        '''This method checks if the specified checker has won diagonally down'''
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
            
            
    def is_win_for(self, checker):
        '''This function checks if the specfied checker has won at all'''
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) == True or \
           self.is_horizontal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True:
            return True
        else:
            return False
