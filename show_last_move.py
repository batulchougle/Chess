from const import *
from piece import *
from board import Board

class Show_last_move:
    def __init__(self,board):
        self.board=board    

    def show_last_move(self, surface):
        if self.board.last_move:
                    initial = self.board.last_move.initial
                    final = self.board.last_move.final        

                    for pos in [initial, final]:
                        # color
                        color =(244,247,116) if (pos.row + pos.col) % 2 == 0 else (172,195,51)
                        # rect
                        rect = ((pos.col * sqsize)+300, (pos.row * sqsize)+45, sqsize, sqsize)
                        # blit
                        pygame.draw.rect(surface, color, rect)