

import pygame
import os
from const import *
from text import Text

class Main:
  
  def menu(self):
     from game import game
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
     running=True

     # Menu
     while running:
       game_window.blit(frames[frame_index],(0,0))
       frame_index = (frame_index + 1)% len(frames)
       mouse=pygame.mouse.get_pos()
         

      
       if 50<=mouse[0]<=220 and 150<=mouse[1]<=200:
          pygame.draw.rect(game_window,color_light,[45,150,200,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[45,150,200,45])     

       if 50<=mouse[0]<=220 and 250<=mouse[1]<=300:
          pygame.draw.rect(game_window,color_light,[45,250,200,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[45,250,200,45])
       if 50<=mouse[0]<=220 and 350<=mouse[1]<=400:
          pygame.draw.rect(game_window,color_light,[45,350,200,45])  
       else:
          pygame.draw.rect(game_window,color_dark,[45,350,200,45])
       #pygame.draw.rect(game_window,highlight_color,[400,250,1100,55])
          
       Text.text_screen("THEME-01",35,brown,50,150,game_window)  
       Text.text_screen("THEME-02",35,brown,50,250,game_window)
       Text.text_screen("THEME-03",35,brown,50,350,game_window)
       Text.text_screen("CHESS",50,cream,730,200,game_window)
       Text.text_screen("THE BATTLE OF MINDS",50,cream,530,260,game_window)

       
       pygame.display.update()     

       for event in pygame.event.get():
         if event.type==pygame.QUIT:
            pygame.quit()
            return
         if event.type==pygame.MOUSEBUTTONDOWN:
             if event.button==1:  
               
               if 50<=mouse[0]<=220 and 150<=mouse[1]<=200:
                 g.gb_01()
               if 50<=mouse[0]<=220 and 250<=mouse[1]<=300:
                 g.gb_02()
                 return
               if 50<=mouse[0]<=220 and 350<=mouse[1]<=400:
                 g.gb_03() 
                 return
               
                 
       clock.tick(fps)     
     


obj = Main()
obj.menu()









































































