import pygame
from board import Board
from const import *





class Show:
    def __init__(self,board,dragger):
        self.board=board
        self.dragger = dragger
        
    
    def show_pieces(self,surface):
    
        dragged_piece = self.dragger.dragged_piece()
        for row in range(rows):
            for col in range(cols):
               square=self.board.squares[row][col]
               if square.has_piece():
                 piece = square.piece
                 if piece!=dragged_piece:
                   piece.set_img(size=80)
                   img=pygame.image.load(piece.img_url)
                   img_center=col*sqsize+sqsize//2 + 300, row*sqsize + sqsize//2 +45
                   piece.img_rect=img.get_rect(center=img_center)
                   surface.blit(img,piece.img_rect)
        
        
        
        
        
              