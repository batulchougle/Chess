

import pygame
import os
from const import *
from text import Text
from game import game

class Main:
  
  def menu(self):

     pygame.init()
     game_window=pygame.display.set_mode((1200,700))
     pygame.display.set_caption("CHESS")
     
     # LOAD GIF FRAMES
     frame_folder = "D:\Batul\mp\Frames"
     frames=[]
     for frame in sorted(os.listdir(frame_folder)):
         if frame.endswith(".png"):
             frame_path = os.path.join(frame_folder, frame)
             try:
                 image=pygame.image.load(frame_path)
                 resized_image=pygame.transform.scale(image,(1200,700))
                 frames.append(resized_image)
             except pygame.error as e:
                 print(f"Error loading frame {frame_path}: {e}")     

     # MAIN MENU 
         
     # VARIABLES
     fps=40
     clock=pygame.time.Clock()
     frame_index=0     

     g = game()

     # Menu
     while True:
       game_window.blit(frames[frame_index],(0,0))
       frame_index = (frame_index + 1)% len(frames)
       mouse=pygame.mouse.get_pos()
         

      
       if 50<=mouse[0]<=330 and 150<=mouse[1]<=200:
          pygame.draw.rect(game_window,color_light,[45,150,310,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[45,150,310,45])     

       if 50<=mouse[0]<=335 and 250<=mouse[1]<=300:
          pygame.draw.rect(game_window,color_light,[45,250,310,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[45,250,310,45])
       if 700<=mouse[0]<=995 and 150<=mouse[1]<=200:
          pygame.draw.rect(game_window,color_light,[695,150,380,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[695,150,380,45])
       if 770<=mouse[0]<=970 and 250<=mouse[1]<=300:
          pygame.draw.rect(game_window,color_light,[765,250,200,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[765,250,200,45])  
       pygame.draw.rect(game_window,highlight_color,[215,550,800,65])
          
       
          
       
     

       Text.text_screen("GAME BOARD-01",35,brown,50,150,game_window)  
       Text.text_screen("GAME BOARD-02",35,brown,50,250,game_window)
       Text.text_screen("GAME BOARD-03",35,brown,700,150,game_window)
       Text.text_screen("TUTORIAL",35,brown,770,250,game_window)
       title=Text.text_screen("CHESS-BATTLE OF THE MINDS",50,black,220,550,game_window)
       
       pygame.display.update()     

       for event in pygame.event.get():
         if event.type==pygame.QUIT:
            pygame.quit()
            return
         if event.type==pygame.MOUSEBUTTONDOWN:
             if event.button==1:  
               
               if 50<=mouse[0]<=330 and 150<=mouse[1]<=200:
                 g.gb_01()
                 pygame.display.update()
               if 50<=mouse[0]<=335 and 250<=mouse[1]<=300:
                 g.gb_02()
               if 700<=mouse[0]<=995 and 150<=mouse[1]<=200:
                 g.time_gb() 
               
               if 770<=mouse[0]<=970 and 250<=mouse[1]<=300:
                 g.tutorial()
               
                 
       clock.tick(fps)     
     


obj = Main()
obj.menu()









































































