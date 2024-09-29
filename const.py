
import pygame
#COLOR
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
brown=(196, 164, 132)
color_light = (129, 133, 137) 
move_color_lg='#C86464'
move_color_dg='#C84646'
dark_blue=(0,68,116)
cream=(248,231,187)
color_dark = (52,52,52) 
highlight_color = (234, 221, 202)
light_green=(234,235,200)
dark_green=(119,154,88)
light_brown=(193, 154, 107)
dark_brown=(149, 69, 53)
grey_dark=(44,43,41)
grey_light=(75,72,71)
width=600
height=600
rows=8
cols=8
sqsize=width//cols


#WINDOW
game_window=pygame.display.set_mode((1200,700))
pygame.display.set_caption("CHESS")
