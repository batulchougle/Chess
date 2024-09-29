import pygame
from const import *

class Dragger:

    def __init__(self):
        self.piece=None
        self.dragging=False
        self.mouseX=0
        self.mouseY=0
        self.initial_row=0
        self.initial_col=0

    
    def update_blit(self,surface):
        self.piece.set_img(size=128) 
        img_url=self.piece.img_url
        img=pygame.image.load(img_url)
        img_center=(self.mouseX,self.mouseY)
        img_rect=img.get_rect(center=img_center)
        surface.blit(img,img_rect)
            

    def update_mouse(self,pos):
        self.mouseX,self.mouseY=pos  

    def drag_piece(self,piece):
        self.piece=piece
        self.dragging=True

    def save_initial(self,pos):
        self.initial_row=(pos[1]-45)//sqsize
        self.initial_col=(pos[0]-300)//sqsize

    def undrag_piece(self):
        self.piece=None
        self.dragging=False  

    def dragged_piece(self):
            return self.piece
         