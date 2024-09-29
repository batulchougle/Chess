from const import *
import pygame
from piece import *
from square import Square
from move import Move
from sound import Sound
import os
import copy
from text import Text


class Board:

    def __init__(self):
      self.squares=[[0,0,0,0,0,0,0,0] for col in range (cols)] 
      self.last_move=None 
      self._createSq()
      self._add_pieces('white')    
      self._add_pieces('black') 
      self.next_player='white'
    


    def move(self,piece,move,testing=False):
        initial=move.initial
        final=move.final

        en_passant_empty=self.squares[final.row][final.col].isempty()

        #console board move update
        self.squares[initial.row][initial.col].piece=None
        self.squares[final.row][final.col].piece=piece
        

        piece.row = final.row
        piece.col = final.col

        
        if isinstance(piece,Pawn):
            #en passant capture
            diff=final.col-initial.col
            if diff!=0 and en_passant_empty:
                #console board move update
                self.squares[initial.row][initial.col+diff].piece=None
                self.squares[final.row][final.col].piece=piece
                if not testing:
                  sound=Sound(os.path.join('assets/sounds/capture.wav'))
                  sound.play()
            #pawn en passant    
            
            
            #pawn promotion
            self.pawn_promotion(piece,final)

        #king castling
        if isinstance(piece,King):
            if self.castling(initial,final) and not testing:
                diff=final.col-initial.col
                rook=piece.left_rook if (diff<0) else piece.right_rook
                self.move(rook, rook.moves[-1])
        
        piece.moved=True

        piece.clear_moves()

        #set last move
        self.last_move=move


    

    def valid_move(self, piece, move):
          return move in piece.moves
        
    def pawn_promotion(self,piece,final):
        if final.row==0 or final.row==7:
            self.squares[final.row][final.col].piece=Queen(piece.color,final.row,final.col)

    def castling(self,initial,final):
        return abs(initial.col - final.col)==2
    
    
    def set_true_en_passant(self,piece):
        if not isinstance(piece,Pawn):
            return
        for row in range(rows):
            for col in range(cols):
                if isinstance(self.squares[row][col].piece, Pawn):
                    self.squares[row][col].piece.en_passant=False
        piece.en_passant=True            
                   

    def in_check(self,piece,move):
        temp_piece=copy.deepcopy(piece)
        temp_board=copy.deepcopy(self)
        temp_board.move(temp_piece,move,testing=True)
        for row in range (rows):
            for col in range (cols):
                if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p=temp_board.squares[row][col].piece
                    temp_board.cal_move(p,row,col,bool=False)
                    for m in p.moves:
                        if isinstance(m.final.piece, King):
                            return True
        return False                

    def cal_move(self,piece,row,col,bool=True):
        self.append_move = False
        
        def knight_moves():
            # 8 possible moves
            possible_moves=[
                (row-2,col+1),
                (row-1,col+2),
                (row+1,col+2),
                (row+2,col+1),
                (row+2,col-1),
                (row+1,col-2),
                (row-1,col-2),
                (row-2,col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row,possible_move_col = possible_move

                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        initial=Square(row,col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final=Square(possible_move_row,possible_move_col,final_piece)
                        move=Move(initial,final)
                        if bool:
                          if not self.in_check(piece,move):
                             piece.add_moves(move)
                             self.append_move=True
                             
                          else:
                              break   
                        else:
                             piece.add_moves(move) 
                             self.append_move=True
                             
                                  
        def pawn_moves():
            # steps
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # create a new move
                        move = Move(initial, final)
                        #check potential checks
                        if bool:
                           if not self.in_check(piece,move):
                              piece.add_moves(move)
                              self.append_move=True
                             
                               
                        else:
                            piece.add_moves(move)
                            self.append_move=True
                              
                                   
                    # blocked
                    else: break
                # not in range
                else: break
                
        
            # diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # create initial and final move squares
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        # create a new move
                        move = Move(initial, final)
                        if bool:
                            if not self.in_check(piece,move):
                                piece.add_moves(move)
                                self.append_move=True
                             
                            
                        else:
                               piece.add_moves(move)
                               self.append_move=True
                             
                                
                
            #en passant moves
            r= 3 if piece.color=='white' else 4
            fr=2 if piece.color=='white' else 5
            #left en passant
            if Square.in_range(col-1) and piece.row==r:
                if self.squares[row][col-1].has_enemy_piece(piece.color):
                    p = self.squares[row][col-1].piece
                    if isinstance(p,Pawn):
                        if p.en_passant:
                             initial = Square(row, col)
                             final = Square(fr, col-1, p)
                             # create a new move
                             move = Move(initial, final)
                             if bool:
                                 if not self.in_check(piece,move):
                                      piece.add_moves(move)
                                      self.append_move=True
                             
                                       
                             else:
                                  piece.add_moves(move) 
                                  self.append_move=True
                             
                                  
                                    
            #right en-passant                      
            if Square.in_range(col+1) and piece.row==r:
                if self.squares[row][col+1].has_enemy_piece(piece.color):
                    p = self.squares[row][col+1].piece
                    if isinstance(p,Pawn):
                        if p.en_passant:
                             initial = Square(row, col)
                             final = Square(fr, col+1, p)
                             # create a new move
                             move = Move(initial, final)
                             if bool:
                                 if not self.in_check(piece,move):
                                      piece.add_moves(move)
                                      self.append_move=True
                             
                                      
                             else:
                                  piece.add_moves(move)
                                  self.append_move=True
                             
                                  
                                    
                                             
                        

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create squares of the possible new move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        # create a possible new move
                        move = Move(initial, final)

                        # empty = continue looping
                        if self.squares[possible_move_row][possible_move_col].isempty():
                                # append new move
                            if bool:
                               if not self.in_check(piece,move):
                                    piece.add_moves(move)
                                    self.append_move=True
                             
                                    
                            else:
                               piece.add_moves(move)
                               self.append_move=True
                                 
                                
                            
                        # has enemy piece = add move + break
                        elif self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            # append new move
                            if bool:
                               if not self.in_check(piece,move):
                                   piece.add_moves(move)
                                   self.append_move=True
                             
                                   
                            else:
                               piece.add_moves(move) 
                               self.append_move=True
                             
                                    
                            break
                            
                        # has team piece = break
                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                        
                    # not in range
                    else: break

                    # incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
                 
                
        def king_moves():
            adjs = [
                (row-1, col+0), # up
                (row-1, col+1), # up-right
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1, col-1), # up-left
            ]

            # normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece=piece
                        # create new move
                        move = Move(initial, final)
                        if bool:
                           if not self.in_check(piece,move):
                              piece.add_moves(move)
                              self.append_move=True
                             
                           else:
                               break   
                        else:
                              piece.add_moves(move)
                              self.append_move=True
                              
                                   
                
            #castling moves
            if not piece.moved:
                left_rook=self.squares[row][0].piece
                if isinstance(left_rook,Rook):
                    if not left_rook.moved:
                        for c in range(1,4):
                            if self.squares[row][c].has_piece():
                                break
                            if c==3:
                                piece.left_rook=left_rook #piece is king

                                #rook move
                                initial=Square(row,0)
                                final=Square(row,3)
                                moveR=Move(initial,final)
                            

                                #king move
                                initial=Square(row,0)
                                final=Square(row,2)
                                moveK=Move(initial,final)
                                

                                if bool:
                                  if not self.in_check(piece,moveK) and not self.in_check(left_rook,moveR):
                                      left_rook.add_moves(moveR)
                                      piece.add_moves(moveK)
                                      self.append_move=True
                             
                                else:
                                      left_rook.add_moves(moveR)
                                      piece.add_moves(moveK)
                                      self.append_move=True
                                   
    
                right_rook=self.squares[row][7].piece
                if isinstance(right_rook,Rook):
                    if not right_rook.moved:
                        for c in range(5,7):
                            if self.squares[row][c].has_piece():
                                break
                            if c==6:
                                piece.right_rook=right_rook #piece is king
                                #rook move
                                initial=Square(row,7)
                                final=Square(row,5)
                                moveR=Move(initial,final)
                            
                                #king move
                                initial=Square(row,col)
                                final=Square(row,6)
                                moveK=Move(initial,final)
                                  

                                if bool:
                                   if not self.in_check(piece,moveK) and not self.in_check(right_rook,moveR):
                                       right_rook.add_moves(moveR)
                                       piece.add_moves(moveK)
                                       self.append_move=True
                             
                                else:
                                   right_rook.add_moves(moveR)
                                   piece.add_moves(moveK)   
                                   self.append_move=True
                                                  
                


        if isinstance(piece,Knight):
            knight_moves()
        elif isinstance(piece, Pawn): 
            pawn_moves()
        elif isinstance(piece, Bishop): 
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])
        elif isinstance(piece, Rook): 
            straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])
        elif isinstance(piece, Queen): 
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])
        elif isinstance(piece, King):
            king_moves()


    def create(self,surface,color1,color2):
       for row in range(rows):
           for col in range(cols):
               if(row+col)%2==0:
                   color=color1
               else:
                   color=color2
               rect=((col*sqsize)+300,(row*sqsize)+45,sqsize,sqsize)  
               pygame.draw.rect(surface,color,rect)


    def _createSq(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col]=Square(row,col)


    def _add_pieces(self, color):

        row_pawn, row_other = (6,7) if color=='white' else (1,0)

        #pawns
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color,row_pawn,col))

        #knights
            self.squares[row_other][1]=Square(row_other, 1, Knight(color,row_other,1))    
            self.squares[row_other][6]=Square(row_other, 6, Knight(color,row_other,6))

        # bishops
            self.squares[row_other][2]=Square(row_other, 2, Bishop(color,row_other,2)) 
            self.squares[row_other][5]=Square(row_other, 5, Bishop(color,row_other,5))
            

        #rooks
            self.squares[row_other][0]=Square(row_other, 0, Rook(color,row_other,0)) 
            self.squares[row_other][7]=Square(row_other, 7, Rook(color,row_other,7))
           

        #queen
            self.squares[row_other][3]=Square(row_other, 3,Queen(color,row_other,3))  

        #king
            self.squares[row_other][4]=Square(row_other, 4, King(color,row_other,4)) 

    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def opponent_in_check(self, piece, move):
         temp_piece = copy.deepcopy(piece)
         temp_board = copy.deepcopy(self)
         temp_board.move(temp_piece, move, testing=True)

         # Find the opponent's king
         opponent_king = None
         for row in range(rows):
             for col in range(cols):
                 temp_piece = temp_board.squares[row][col].piece
                 if isinstance(temp_piece, King) and temp_piece.color != piece.color:
                     opponent_king = temp_piece
                     break

         # If no opponent's king is found, something is wrong
         if not opponent_king:
             print("Could not find opponent's king!")
             return False

         # Check if any of the current player's pieces are attacking the opponent's king
         for row in range(rows):
             for col in range(cols):
                 attacking_piece = temp_board.squares[row][col].piece
                 if attacking_piece and attacking_piece.color == piece.color:
                     temp_board.cal_move(attacking_piece, row, col, bool=True)

                     # Check if this piece can attack the opponent's king
                     for m in attacking_piece.moves:
                         if m.final.piece == opponent_king:
                             return True

         return False
    
    
    def game_over(self,piece,move):
        c=piece.color    
        any_valid_move = False
        if self.opponent_in_check(piece,move):
            for row in range (rows):
                for col in range (cols):
                   if self.squares[row][col].has_piece(): 
                       p=self.squares[row][col].piece
                       if p.color!=c:  
                                self.cal_move(p,row,col,bool=True)  
                                if self.append_move:
                                      any_valid_move = True      
            if not any_valid_move:
                return True
        return False
    
    def display_result(self,screen):
        Text.text_screen("CHECKMATE!!",100,red,260,450,screen)
        pygame.display.update()
        




        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        

    
    
    
    
    