from dragger import *
from const import *
from piece import *

class Show_move:

    

    def __init__(self,dragger):
        self.dragger = dragger
    
    def show_moves(self,surface,color1,color2):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                color=color1 if(move.final.row + move.final.col)%2==0 else color2
                rect=((move.final.col*sqsize)+300,(move.final.row*sqsize)+45,sqsize,sqsize)
                pygame.draw.rect(surface,color,rect)
        

