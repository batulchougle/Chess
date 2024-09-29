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
      
       pygame.init()
       clock=pygame.time.Clock()
       
       while True:
         game_window.fill(white)
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
      pygame.init()
      clock=pygame.time.Clock()
             
      while True:
        game_window.fill(white)
        self.board.create(game_window,dark_blue,cream)
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
                self.board.cal_move(piece,clicked_row,clicked_col)
                self.dragger.save_initial(event.pos)
                self.dragger.drag_piece(piece) 
                self.board.create(game_window,light_green,dark_green)
                self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
                self.show.show_pieces(game_window)
          
          #mouse motion 
          elif  event.type==pygame.MOUSEMOTION:
         
             if self.dragger.dragging:
               self.dragger.update_mouse(event.pos)
             
          # click release
          elif event.type==pygame.MOUSEBUTTONUP:
             self.dragger.undrag_piece() 
                  
          elif event.type==pygame.QUIT:
             pygame.quit()
             return   
        clock.tick(40)        
             
             

   # TIME-BOUND GAME BOARD
 def time_gb(self):
         pygame.init()
         clock=pygame.time.Clock()
                
         while True:
           game_window.fill(white)
           self.board.create(game_window,grey_dark,grey_light)
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
                   self.board.cal_move(piece,clicked_row,clicked_col)
                   self.dragger.save_initial(event.pos)
                   self.dragger.drag_piece(piece) 
                   self.board.create(game_window,light_green,dark_green)
                   self.show_moves.show_moves(game_window,move_color_lg,move_color_dg)
                   self.show.show_pieces(game_window)
             
             #mouse motion 
             elif  event.type==pygame.MOUSEMOTION:
            
                if self.dragger.dragging:
                  self.dragger.update_mouse(event.pos)
                
             # click release
             elif event.type==pygame.MOUSEBUTTONUP:
                self.dragger.undrag_piece() 
                     
             elif event.type==pygame.QUIT:
                pygame.quit()
                return   
           clock.tick(40)        
          

   # TUTORIAL
 def tutorial():
      clock=pygame.time.Clock()
       
       
      while True:
         game_window.fill(white)
         Text.text_screen("TUTORIAL",50,black,300,200)
         pygame.display.update()   

         for event in pygame.event.get():
           if event.type==pygame.QUIT:
              pygame.quit()
              return
           
         clock.tick(40)  
            
   

               
            
              

   