
from const import *
import pygame
class Text:
    def text_screen(text,size,color,x,y,screen):
      font=pygame.font.SysFont('comic sans' ,size)
      text_surface=font.render(text,True,color)
      screen.blit(text_surface,[x,y])
      
