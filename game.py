import pygame
from const import *
from text import Text
from board import Board
from show import Show
from dragger import Dragger
from show_moves import Show_move
from square import Square
from move import Move
from show_last_move import Show_last_move
from config import Config
from text import Text

class game:
    #GAME BOARD-01
 def __init__(self):  
    
    self.dragger = Dragger()
    self.board=Board()
    self.show = Show(self.board,self.dragger)
    self.show_moves=Show_move(self.dragger)
    self.show_last_move=Show_last_move(self.board)
    self.config=Config()

 def play_sound(self, captured=False):
    if captured:
        self.config.capture_sound.play()
    else:
        self.config.move_sound.play()   
    
 def gb_01(self):
       from main import Main
       self.main=Main()
       pygame.init()
       clock=pygame.time.Clock()
       running=True
       
       while running:
         game_window.fill(white)
         Text.text_screen("START WITH WHITE PIECES",20,black,30,10,game_window)
         mouse=pygame.mouse.get_pos()
         if 30<=mouse[0]<=150 and 50<=mouse[1]<=100:
              pygame.draw.rect(game_window,light_green,[25,50,130,45])  
         else:
              pygame.draw.rect(game_window,dark_green,[25,50,130,45])
         Text.text_screen("BACK",40,black,30,45,game_window) 
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # If the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button==1:    
                if 30 <= mouse[0] <= 170 and 50 <= mouse[1] <= 100:
                    self.main.menu()
                    running = False  
                    break  
         self.board.create(game_window,light_green,dark_green)
         self.show_last_move.show_last_move(game_window)
         self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
         self.show.show_pieces(game_window)
      
         if self.dragger.dragging:
            self.dragger.update_blit(game_window)

         pygame.display.update()   

         for event in pygame.event.get():
           #click
           if event.type==pygame.MOUSEBUTTONDOWN:
              self.dragger.update_mouse(event.pos)
              clicked_row=(self.dragger.mouseY-45)//sqsize 
              clicked_col=(self.dragger.mouseX-300)//sqsize 

           #checking if clicked square has piece
              if self.board.squares[clicked_row][clicked_col].has_piece():
                 
                 piece=self.board.squares[clicked_row][clicked_col].piece
                 if piece.color == self.board.next_player:
                    self.board.cal_move(piece,clicked_row,clicked_col,bool=True)
                    self.dragger.save_initial(event.pos)
                    self.dragger.drag_piece(piece) 

                    self.board.create(game_window,light_green,dark_green)
                    self.show_last_move.show_last_move(game_window)
                    self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
                    self.show.show_pieces(game_window)
           
           #mouse motion 
           elif  event.type==pygame.MOUSEMOTION:

          
              if self.dragger.dragging:
                self.dragger.update_mouse(event.pos)
              
           # click release
           elif event.type==pygame.MOUSEBUTTONUP:
              if self.dragger.dragging:
                 self.dragger.update_mouse(event.pos)
                 released_row=(self.dragger.mouseY-45)//sqsize
                 released_col=(self.dragger.mouseX-300)//sqsize

                 #create possible move
                 initial=Square(self.dragger.initial_row,self.dragger.initial_col)
                 final=Square(released_row,released_col)
                 move=Move(initial,final)


                 if self.board.valid_move(self.dragger.piece,move):
                   #normal capture
                   captured = self.board.squares[released_row][released_col].has_piece()
                   self.board.move(self.dragger.piece,move)
                   self.board.set_true_en_passant(self.dragger.piece)
                   self.play_sound(captured)
                   self.board.create(game_window,light_green,dark_green)
                   self.show_last_move.show_last_move(game_window)
                   self.show.show_pieces(game_window)
                   self.board.next_turn()
                   result=self.board.game_over(piece,move)
                   if result:
                      self.dragger.undrag_piece() 
                      self.board.create(game_window, light_green, dark_green)
                      self.show_last_move.show_last_move(game_window)
                      self.show.show_pieces(game_window)
                      self.board.display_result(game_window)
                      pygame.time.wait(4000)    
              self.dragger.undrag_piece()          
           elif event.type==pygame.QUIT:
              pygame.quit()
              return   
         clock.tick(40)        
   

   # GAME BOARD-02
 def gb_02(self):
      from main import Main
      self.main=Main()
      pygame.init()
      clock=pygame.time.Clock()
      running=True
             
      while running:
        game_window.fill(white)
        Text.text_screen("START WITH WHITE PIECES",20,black,30,10,game_window)
        mouse=pygame.mouse.get_pos()
        if 30<=mouse[0]<=150 and 50<=mouse[1]<=100:
             pygame.draw.rect(game_window,cream,[25,50,130,45])  
        else:
             pygame.draw.rect(game_window,dark_blue,[25,50,130,45])
        Text.text_screen("BACK",40,black,30,45,game_window) 
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               return
           
           # If the user clicks
           if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button==1:    
               if 30 <= mouse[0] <= 170 and 50 <= mouse[1] <= 100:
                   self.main.menu()
                   running = False  
                   break  
        self.board.create(game_window,cream,dark_blue)
        self.show_last_move.show_last_move(game_window)
        self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
        self.show.show_pieces(game_window)
        if self.dragger.dragging:
           self.dragger.update_blit(game_window)
        pygame.display.update()   
        for event in pygame.event.get():
          #click
          if event.type==pygame.MOUSEBUTTONDOWN:
             self.dragger.update_mouse(event.pos)
             clicked_row=(self.dragger.mouseY-45)//sqsize 
             clicked_col=(self.dragger.mouseX-300)//sqsize 
          #checking if clicked square has piece
             if self.board.squares[clicked_row][clicked_col].has_piece():
                
                piece=self.board.squares[clicked_row][clicked_col].piece
                if piece.color == self.board.next_player:
                   self.board.cal_move(piece,clicked_row,clicked_col,bool=True)
                   self.dragger.save_initial(event.pos)
                   self.dragger.drag_piece(piece) 
                   self.board.create(game_window,cream,dark_blue)
                   self.show_last_move.show_last_move(game_window)
                   self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
                   self.show.show_pieces(game_window)
          
          #mouse motion 
          elif  event.type==pygame.MOUSEMOTION:
         
             if self.dragger.dragging:
               self.dragger.update_mouse(event.pos)
             
          # click release
          elif event.type==pygame.MOUSEBUTTONUP:
             if self.dragger.dragging:
                self.dragger.update_mouse(event.pos)
                released_row=(self.dragger.mouseY-45)//sqsize
                released_col=(self.dragger.mouseX-300)//sqsize
                #create possible move
                initial=Square(self.dragger.initial_row,self.dragger.initial_col)
                final=Square(released_row,released_col)
                move=Move(initial,final)
                if self.board.valid_move(self.dragger.piece,move):
                  #normal capture
                  captured = self.board.squares[released_row][released_col].has_piece()
                  self.board.move(self.dragger.piece,move)
                  self.board.set_true_en_passant(self.dragger.piece)
                  self.play_sound(captured)
                  self.board.create(game_window,cream,dark_blue)
                  self.show_last_move.show_last_move(game_window)
                  self.show.show_pieces(game_window)
                  self.board.next_turn()
                  result=self.board.game_over(piece,move)
                  if result:
                     self.dragger.undrag_piece() 
                     self.board.create(game_window,cream, dark_blue)
                     self.show_last_move.show_last_move(game_window)
                     self.show.show_pieces(game_window)
                     self.board.display_result(game_window)
                     pygame.time.wait(4000)    
             self.dragger.undrag_piece()          
          elif event.type==pygame.QUIT:
             pygame.quit()
             return   
        clock.tick(40)           

   # TIME-BOUND GAME BOARD
 def gb_03(self):
         from main import Main
         self.main=Main()
         pygame.init()
         clock=pygame.time.Clock()
         running=True
                
         while running:
           game_window.fill(white)
           Text.text_screen("START WITH WHITE PIECES",20,black,30,10,game_window)
           mouse=pygame.mouse.get_pos()
           if 30<=mouse[0]<=150 and 50<=mouse[1]<=100:
                pygame.draw.rect(game_window,grey_light,[25,50,130,45])  
           else:
                pygame.draw.rect(game_window,grey_dark,[25,50,130,45])
           Text.text_screen("BACK",40,black,30,45,game_window) 
           for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  return
              
              # If the user clicks
              if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:    
                  if 30 <= mouse[0] <= 170 and 50 <= mouse[1] <= 100:
                      self.main.menu()
                      running = False  
                      break  
           self.board.create(game_window,grey_light,grey_dark)
           self.show_last_move.show_last_move(game_window)
           self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
           self.show.show_pieces(game_window)
           if self.dragger.dragging:
              self.dragger.update_blit(game_window)
           pygame.display.update()   
           for event in pygame.event.get():
             #click
             if event.type==pygame.MOUSEBUTTONDOWN:
                self.dragger.update_mouse(event.pos)
                clicked_row=(self.dragger.mouseY-45)//sqsize 
                clicked_col=(self.dragger.mouseX-300)//sqsize 
             #checking if clicked square has piece
                if self.board.squares[clicked_row][clicked_col].has_piece():
                   
                   piece=self.board.squares[clicked_row][clicked_col].piece
                   if piece.color == self.board.next_player:
                      self.board.cal_move(piece,clicked_row,clicked_col,bool=True)
                      self.dragger.save_initial(event.pos)
                      self.dragger.drag_piece(piece) 
                      self.board.create(game_window,grey_light,grey_dark)
                      self.show_last_move.show_last_move(game_window)
                      self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
                      self.show.show_pieces(game_window)
             
             #mouse motion 
             elif  event.type==pygame.MOUSEMOTION:
            
                if self.dragger.dragging:
                  self.dragger.update_mouse(event.pos)
                
             # click release
             elif event.type==pygame.MOUSEBUTTONUP:
                if self.dragger.dragging:
                   self.dragger.update_mouse(event.pos)
                   released_row=(self.dragger.mouseY-45)//sqsize
                   released_col=(self.dragger.mouseX-300)//sqsize
                   #create possible move
                   initial=Square(self.dragger.initial_row,self.dragger.initial_col)
                   final=Square(released_row,released_col)
                   move=Move(initial,final)
                   if self.board.valid_move(self.dragger.piece,move):
                     #normal capture
                     captured = self.board.squares[released_row][released_col].has_piece()
                     self.board.move(self.dragger.piece,move)
                     self.board.set_true_en_passant(self.dragger.piece)
                     self.play_sound(captured)
                     self.board.create(game_window,grey_light,grey_dark)
                     self.show_last_move.show_last_move(game_window)
                     self.show.show_pieces(game_window)
                     self.board.next_turn()
                     result=self.board.game_over(piece,move)
                     if result:
                        self.dragger.undrag_piece() 
                        self.board.create(game_window,grey_light,grey_dark)
                        self.show_last_move.show_last_move(game_window)
                        self.show.show_pieces(game_window)
                        self.board.display_result(game_window)
                        pygame.time.wait(4000)    
                self.dragger.undrag_piece()          
             elif event.type==pygame.QUIT:
                pygame.quit()
                return   
           clock.tick(40)         
                            
         

                     
                     

                        
                     
                                

            