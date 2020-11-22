#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        '''This method constructs a new AIPlayer object.'''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    
    def __repr__(self):
        '''This method returns a string representing an AIPlayer object. 
        This method overrides/replaces the __repr__ method that is inherited from Player.'''
        if self.checker == 'X':
            return 'Player X (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        else:
            return 'Player O (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        
    def max_score_column(self, scores):
        '''This method takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score.'''
        max_score = []
        for j in range(len(scores)):
            if scores[j] == max(scores):
                max_score += [j]
        if self.tiebreak == 'LEFT':
            return max_score[0]
        elif self.tiebreak == 'RIGHT':
            return max_score[-1]
        else:
            return random.choice(max_score)
        
        
    def scores_for(self, b):
        '''This method takes a Board object b and determines the called AIPlayer‘s 
        scores for the columns in b.'''
        scores = [0] * b.width
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                scores[i] = 100 - max(opp_scores)
                b.remove_checker(i)
        return scores
        
    def next_move(self, b):
        '''This method overrides (i.e., replaces) the next_move method that is inherited from Player. 
        Rather than asking the user for the next move, this version of next_move should return the called 
        AIPlayer‘s judgment of its best possible move.'''
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))