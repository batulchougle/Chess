import os

class Piece:
    def __init__(self,name,color,value,row,col,img_url=None,img_rect=None):
        self.name=name
        self.color=color
        value_sign=1 if color=='white' else -1
        self.value=value*value_sign
        self.img_url=img_url
        self.set_img()
        self.img_rect=img_rect
        self.row=row
        self.col=col
        self.moves=[]
        self.moved = False


        
    
        
        
    def add_moves(self,move):
        self.moves.append(move)
        
    def set_img(self,size=80):
        self.img_url=os.path.join(f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')    

    def clear_moves(self):
        self.moves=[]    

    def __eq__(self, other):
        return isinstance(other, Piece) and self.name==other.name and self.color==other.color and self.row==other.row and self.col==other.col

class Pawn(Piece):

    def __init__(self,color,row,col):
        self.dir=-1 if color=='white' else 1
        self.en_passant=False
        super().__init__('pawn',color,1.0,row,col) 

class Knight(Piece):

    def __init__(self,color,row,col):
        super().__init__('knight',color,3.0,row,col)

class Bishop(Piece):

    def __init__(self,color,row,col):
        super().__init__('bishop',color,3.001,row,col)

class Queen(Piece):

    def __init__(self,color,row,col):
        super().__init__('queen',color,9.0,row,col)

class Rook(Piece):

    def __init__(self,color,row,col):
        super().__init__('rook',color,5.0,row,col)

class King(Piece):

    def __init__(self,color,row,col):
        self.left_rook=None
        self.right_rook=None
        super().__init__('king',color,1000.0,row,col)


                