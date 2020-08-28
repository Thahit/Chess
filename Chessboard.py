import pygame
from abc import ABC
print("Imports complete.")

#img from https://en.wikipedia.org/wiki/Chess_piece
white={"king": pygame.image.load("img/wKing.png"), "queen": pygame.image.load("img/wQueen.png"),
       "rook": pygame.image.load("img/wRook.png"),"bishop": pygame.image.load("img/wBishop.png"),
       "knight": pygame.image.load("img/wKnight.png"),"pawn": pygame.image.load("img/wPawn.png")}
black={"king": pygame.image.load("img/bKing.png"), "queen": pygame.image.load("img/bQueen.png"),
       "rook": pygame.image.load("img/bRook.png"), "bishop": pygame.image.load("img/bBishop.png"),
       "knight": pygame.image.load("img/bKnight.png"), "pawn": pygame.image.load("img/bPawn.png")}

whiteW={"king": "♔", "queen": "♕", "rook":"♖", "bishop": "♗","knight":"♘", "pawn":"♙"}
blackW={"king": "♚", "queen": "♛", "rook":"♛", "bishop": "♝","knight":"♞", "pawn":"♟"}

#window setting
pygame.init()
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("img/bKnight.png"))

gridsize=55
width=700
border=30
height=gridsize*8+ 2*border
font = pygame.font.Font('freesansbold.ttf', 20)
screen = pygame.display.set_mode((width, height))
#__________________________class types______________________________________________
#to check for allies/enemies the pieces need to be part of a class/type
class Black(ABC):
    def __init__(self, y, x):
        self.x=x
        self.y=y
    def arraypos(self, array):  # where is it in array
        return (8 - self.y, self.x - 1)

class White(ABC):
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def arraypos(self, array):  # where is it in array
        return (8 - self.y, self.x - 1)

#get pos from index
def idxToPos(tuple): #not sure if ti will get used
    x=tuple[0]+8
    y=tuple[1]+1
    return (x,y)
#___________________________pieces___________________________________________________________________________
class bRook(Black):
    def __init__(self, y, x):
        self.val=5
        self.x=x
        self.y=y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["rook"],(posx,posy))

    def legal(self, field): # show legal moves  works
        idx= self.arraypos(field)  #return tuple(idx1, idx2)
        legal=[] #list of legal moves

        i=-1
        up=True
        while up: #nothing in between     move up
            if idx[0]+i>=0:
                if field[idx[0]+i][idx[1]] ==0:# no piece
                    legal.append((idx[0]+i, idx[1]))
                elif isinstance(field[idx[0]+i][idx[1]] , White):#if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    up=False
                else:#friendly piece
                    up=False
                i-=1
            else:#out of array
                up=False

        i=1
        down=True
        while down: #nothing in between     move up
            if idx[0]+i<=7:
                if field[idx[0]+i][idx[1]] ==0:# no piece
                    legal.append((idx[0]+i, idx[1]))
                elif isinstance(field[idx[0]+i][idx[1]] , White):#if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    down=False
                else:#friendly piece
                    down=False
                i+=1
            else:#out of array
                down=False

        i = 1
        right = True
        while right:  # nothing in between     move up
            if idx[1] + i <= 7:
                if field[idx[0]][idx[1]+i] == 0:  # no piece
                    legal.append((idx[0] , idx[1]+ i))
                elif isinstance(field[idx[0] ][idx[1]+ i], White):  # if enemy piece
                    legal.append((idx[0] , idx[1]+ i))
                    right = False
                else:  # friendly piece
                    right = False
                i += 1
            else:  # out of array
                right = False

        i = -1
        left = True
        while left:  # nothing in between     move up
            if idx[1] + i >= 0:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], White):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    left = False
                else:  # friendly piece
                    left = False
                i -= 1
            else:  # out of array
                left = False

        return legal


class bKing(Black):
    def __init__(self, y, x):
        self.val = float("inf")

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["king"],(posx,posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        #right down
        if idx[0] + 1 <8 and idx[1] + 1<8:
            if field[idx[0] + 1][idx[1] + 1] == 0 or isinstance(field[idx[0] + 1][idx[1] + 1], White):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] + 1))
        #right
        if idx[1] + 1<8:
            if field[idx[0] ][idx[1] + 1] == 0 or isinstance(field[idx[0] ][idx[1] + 1], White):  # no piece/enemy
                legal.append((idx[0], idx[1] + 1))
        #right up
        if idx[0] - 1 >=0 and idx[1] + 1<8:
            if field[idx[0] - 1][idx[1] + 1] == 0 or isinstance(field[idx[0] - 1][idx[1] + 1], White):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] + 1))
        #up
        if idx[0] - 1 >=0:
            if field[idx[0] - 1][idx[1] ] == 0 or isinstance(field[idx[0] - 1][idx[1] ], White):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] ))
        #left up
        if idx[0] - 1 >=0 and idx[1] - 1>=0:
            if field[idx[0] - 1][idx[1] - 1] == 0 or isinstance(field[idx[0] - 1][idx[1] - 1], White):  # no piece/enemy
                legal.append((idx[0] -1, idx[1] - 1))
        #left
        if  idx[1] - 1>=0:
            if field[idx[0] ][idx[1] - 1] == 0 or isinstance(field[idx[0] ][idx[1] - 1], White):  # no piece/enemy
                legal.append((idx[0] , idx[1] - 1))
        #left down
        if idx[0] + 1 <8 and idx[1] - 1>=0:
            if field[idx[0] + 1][idx[1] - 1] == 0 or isinstance(field[idx[0] + 1][idx[1] - 1], White):  # no piece/enemy
                legal.append((idx[0] +1, idx[1] - 1))
        #down
        if idx[0] + 1 <8:
            if field[idx[0] + 1][idx[1] ] == 0 or isinstance(field[idx[0] + 1][idx[1] ], White):  # no piece/enemy
                legal.append((idx[0] +1, idx[1] ))

        return legal



class bKnight(Black):
    def __init__(self, y, x):
        self.val = 5

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["knight"],(posx,posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves
        #right down
        if idx[0] + 2 <8 and idx[1] + 1<8:
            if field[idx[0] + 2][idx[1] + 1] == 0 or isinstance(field[idx[0] + 2][idx[1] + 1], White):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] + 1))
        if idx[0] + 1 < 8 and idx[1] + 2 < 8:
            if field[idx[0] + 1][idx[1] + 2] == 0 or isinstance(field[idx[0] + 1][idx[1] + 2], White):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] + 2))

        #right up
        if idx[0] + 2 <8 and idx[1] - 1>=0:
            if field[idx[0] + 2][idx[1] - 1] == 0 or isinstance(field[idx[0] + 2][idx[1] - 1], White):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] - 1))
        if idx[0] + 1 < 8 and idx[1] - 2 >=0:
            if field[idx[0] + 1][idx[1] - 2] == 0 or isinstance(field[idx[0] + 1][idx[1] - 2], White):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] - 2))

        #left up
        if idx[0] - 2 >=0 and idx[1] - 1>=0:
            if field[idx[0] - 2][idx[1] - 1] == 0 or isinstance(field[idx[0] - 2][idx[1] - 1], White):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] - 1))
        if idx[0] - 1 >=0 and idx[1] - 2 >=0:
            if field[idx[0] - 1][idx[1] - 2] == 0 or isinstance(field[idx[0] - 1][idx[1] - 2], White):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] - 2))

        #left down
        if idx[0] - 2 >=0 and idx[1] + 1<8:
            if field[idx[0] - 2][idx[1] + 1] == 0 or isinstance(field[idx[0] - 2][idx[1] + 1], White):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] + 1))
        if idx[0] - 1 >=0 and idx[1] + 2 <8:
            if field[idx[0] - 1][idx[1] + 2] == 0 or isinstance(field[idx[0] - 1][idx[1] + 2], White):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] + 2))

        return legal


class bQueen(Black):
    def __init__(self, y, x):
        self.val = 9

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["queen"],(posx,posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        i = -1
        lup = True
        while lup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1]+ i >=0:
                if field[idx[0] + i][idx[1]+ i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]+ i))
                elif isinstance(field[idx[0] + i][idx[1]+ i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]+ i))
                    lup = False
                else:  # friendly piece
                    lup = False
                i -= 1
            else:  # out of array
                lup = False

        i = -1
        rup = True
        while rup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1] - i<=7:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    rup = False
                else:  # friendly piece
                    rup = False
                i -= 1
            else:  # out of array
                rup = False

        i = 1
        ldown = True
        while ldown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] - i>=0:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    ldown = False
                else:  # friendly piece
                    ldown = False
                i += 1
            else:  # out of array
                ldown = False

        i = 1
        rdown = True
        while rdown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] + i <=7:
                if field[idx[0] + i][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] + i))
                elif isinstance(field[idx[0] + i][idx[1] + i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] + i))
                    rdown = False
                else:  # friendly piece
                    rdown = False
                i += 1
            else:  # out of array
                rdown = False

        i = -1
        up = True
        while up:  # nothing in between     move up
            if idx[0] + i >= 0:
                if field[idx[0] + i][idx[1]] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]))
                elif isinstance(field[idx[0] + i][idx[1]], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    up = False
                else:  # friendly piece
                    up = False
                i -= 1
            else:  # out of array
                up = False

        i = 1
        down = True
        while down:  # nothing in between     move up
            if idx[0] + i <= 7:
                if field[idx[0] + i][idx[1]] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]))
                elif isinstance(field[idx[0] + i][idx[1]], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    down = False
                else:  # friendly piece
                    down = False
                i += 1
            else:  # out of array
                down = False

        i = 1
        right = True
        while right:  # nothing in between     move up
            if idx[1] + i <= 7:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], White):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    right = False
                else:  # friendly piece
                    right = False
                i += 1
            else:  # out of array
                right = False

        i = -1
        left = True
        while left:  # nothing in between     move up
            if idx[1] + i >= 0:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], White):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    left = False
                else:  # friendly piece
                    left = False
                i -= 1
            else:  # out of array
                left = False

        return legal



class bBishop(Black):
    def __init__(self, y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["bishop"],(posx,posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        i = -1
        lup = True
        while lup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1]+ i >=0:
                if field[idx[0] + i][idx[1]+ i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]+ i))
                elif isinstance(field[idx[0] + i][idx[1]+ i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]+ i))
                    lup = False
                else:  # friendly piece
                    lup = False
                i -= 1
            else:  # out of array
                lup = False

        i = -1
        rup = True
        while rup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1] - i<=7:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    rup = False
                else:  # friendly piece
                    rup = False
                i -= 1
            else:  # out of array
                rup = False

        i = 1
        ldown = True
        while ldown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] - i>=0:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    ldown = False
                else:  # friendly piece
                    ldown = False
                i += 1
            else:  # out of array
                ldown = False

        i = 1
        rdown = True
        while rdown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] + i <=7:
                if field[idx[0] + i][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] + i))
                elif isinstance(field[idx[0] + i][idx[1] + i], White):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] + i))
                    rdown = False
                else:  # friendly piece
                    rdown = False
                i += 1
            else:  # out of array
                rdown = False

        return legal


class bPawn(Black):
    def __init__(self, y, x):
        self.val = 1

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["pawn"],(posx,posy))

    def legal(self, field): # show legal moves   works
        idx= self.arraypos(field)  #return tuple(idx1, idx2)
        legal=[] #list of legal moves

        if idx[0] + 1 <8 and idx[1] + 1<8:#take right
            if isinstance(field[idx[0] + 1][idx[1] + 1], White):  # enemy
                legal.append((idx[0] + 1, idx[1] + 1))

        if idx[0] + 1 <8 and idx[1] - 1>=0:#take left
            if isinstance(field[idx[0] + 1][idx[1] - 1], White):  # enemy
                legal.append((idx[0] + 1, idx[1] - 1))

        # walk
        if idx[0] + 1 <8 :
            if field[idx[0] + 1][idx[1] ] == 0 :  # no piece
                legal.append((idx[0] + 1, idx[1] ))

        if idx[0] + 2 <8 :
            if field[idx[0] + 2][idx[1] ] == 0:  # no piece
                legal.append((idx[0] + 2, idx[1] ))

###############################White#############################################
class wRook(White):
    def __init__(self, y, x):
        self.val = 5

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(white["rook"],(posx,posy))

    def legal(self, field): # show legal moves   works
        idx= self.arraypos(field)  #return tuple(idx1, idx2)
        legal=[] #list of legal moves

        i=-1
        up=True
        while up: #nothing in between     move up
            if idx[0]+i>=0:
                if field[idx[0]+i][idx[1]] ==0:# no piece
                    legal.append((idx[0]+i, idx[1]))
                elif isinstance(field[idx[0]+i][idx[1]] , Black):#if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    up=False
                else:#friendly piece
                    up=False
                i-=1
            else:#out of array
                up=False

        i=1
        down=True
        while down: #nothing in between     move up
            if idx[0]+i<=7:
                if field[idx[0]+i][idx[1]] ==0:# no piece
                    legal.append((idx[0]+i, idx[1]))
                elif isinstance(field[idx[0]+i][idx[1]] , Black):#if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    down=False
                else:#friendly piece
                    down=False
                i+=1
            else:#out of array
                down=False

        i = 1
        right = True
        while right:  # nothing in between     move up
            if idx[1] + i <= 7:
                if field[idx[0]][idx[1]+i] == 0:  # no piece
                    legal.append((idx[0] , idx[1]+ i))
                elif isinstance(field[idx[0] ][idx[1]+ i], Black):  # if enemy piece
                    legal.append((idx[0] , idx[1]+ i))
                    right = False
                else:  # friendly piece
                    right = False
                i += 1
            else:  # out of array
                right = False

        i = -1
        left = True
        while left:  # nothing in between     move up
            if idx[1] + i >= 0:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], Black):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    left = False
                else:  # friendly piece
                    left = False
                i -= 1
            else:  # out of array
                left = False

        return legal


class wKing(White):
    def __init__(self, y, x):
        self.val = float("inf")

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["king"], (posx, posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        #right down
        if idx[0] + 1 <8 and idx[1] + 1<8:
            if field[idx[0] + 1][idx[1] + 1] == 0 or isinstance(field[idx[0] + 1][idx[1] + 1], Black):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] + 1))
        #right
        if idx[1] + 1<8:
            if field[idx[0] ][idx[1] + 1] == 0 or isinstance(field[idx[0] ][idx[1] + 1], Black):  # no piece/enemy
                legal.append((idx[0], idx[1] + 1))
        #right up
        if idx[0] - 1 >=0 and idx[1] + 1<8:
            if field[idx[0] - 1][idx[1] + 1] == 0 or isinstance(field[idx[0] - 1][idx[1] + 1], Black):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] + 1))
        #up
        if idx[0] - 1 >=0:
            if field[idx[0] - 1][idx[1] ] == 0 or isinstance(field[idx[0] - 1][idx[1] ], Black):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] ))
        #left up
        if idx[0] - 1 >=0 and idx[1] - 1>=0:
            if field[idx[0] - 1][idx[1] - 1] == 0 or isinstance(field[idx[0] - 1][idx[1] - 1], Black):  # no piece/enemy
                legal.append((idx[0] -1, idx[1] - 1))
        #left
        if  idx[1] - 1>=0:
            if field[idx[0] ][idx[1] - 1] == 0 or isinstance(field[idx[0] ][idx[1] - 1], Black):  # no piece/enemy
                legal.append((idx[0] , idx[1] - 1))
        #left down
        if idx[0] + 1 <8 and idx[1] - 1>=0:
            if field[idx[0] + 1][idx[1] - 1] == 0 or isinstance(field[idx[0] + 1][idx[1] - 1], Black):  # no piece/enemy
                legal.append((idx[0] +1, idx[1] - 1))
        #down
        if idx[0] + 1 <8:
            if field[idx[0] + 1][idx[1] ] == 0 or isinstance(field[idx[0] + 1][idx[1] ], Black):  # no piece/enemy
                legal.append((idx[0] +1, idx[1] ))

        return legal




class wKnight(White):
    def __init__(self, y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["knight"], (posx, posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves
        #right down
        if idx[0] + 2 <8 and idx[1] + 1<8:
            if field[idx[0] + 2][idx[1] + 1] == 0 or isinstance(field[idx[0] + 2][idx[1] + 1], Black):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] + 1))
        if idx[0] + 1 < 8 and idx[1] + 2 < 8:
            if field[idx[0] + 1][idx[1] + 2] == 0 or isinstance(field[idx[0] + 1][idx[1] + 2], Black):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] + 2))

        #right up
        if idx[0] + 2 <8 and idx[1] - 1>=0:
            if field[idx[0] + 2][idx[1] - 1] == 0 or isinstance(field[idx[0] + 2][idx[1] - 1], Black):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] - 1))
        if idx[0] + 1 < 8 and idx[1] - 2 >=0:
            if field[idx[0] + 1][idx[1] - 2] == 0 or isinstance(field[idx[0] + 1][idx[1] - 2], Black):  # no piece/enemy
                legal.append((idx[0] + 1, idx[1] - 2))

        #left up
        if idx[0] - 2 >=0 and idx[1] - 1>=0:
            if field[idx[0] - 2][idx[1] - 1] == 0 or isinstance(field[idx[0] - 2][idx[1] - 1], Black):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] - 1))
        if idx[0] - 1 >=0 and idx[1] - 2 >=0:
            if field[idx[0] - 1][idx[1] - 2] == 0 or isinstance(field[idx[0] - 1][idx[1] - 2], Black):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] - 2))

        #left down
        if idx[0] - 2 >=0 and idx[1] + 1<8:
            if field[idx[0] - 2][idx[1] + 1] == 0 or isinstance(field[idx[0] - 2][idx[1] + 1], Black):  # no piece/enemy
                legal.append((idx[0] + 2, idx[1] + 1))
        if idx[0] - 1 >=0 and idx[1] + 2 <8:
            if field[idx[0] - 1][idx[1] + 2] == 0 or isinstance(field[idx[0] - 1][idx[1] + 2], Black):  # no piece/enemy
                legal.append((idx[0] - 1, idx[1] + 2))

        return legal


class wQueen(White):
    def __init__(self, y, x):
        self.val = 9

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["queen"], (posx, posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        i = -1
        lup = True
        while lup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1]+ i >=0:
                if field[idx[0] + i][idx[1]+ i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]+ i))
                elif isinstance(field[idx[0] + i][idx[1]+ i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]+ i))
                    lup = False
                else:  # friendly piece
                    lup = False
                i -= 1
            else:  # out of array
                lup = False

        i = -1
        rup = True
        while rup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1] - i<=7:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    rup = False
                else:  # friendly piece
                    rup = False
                i -= 1
            else:  # out of array
                rup = False

        i = 1
        ldown = True
        while ldown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] - i>=0:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    ldown = False
                else:  # friendly piece
                    ldown = False
                i += 1
            else:  # out of array
                ldown = False

        i = 1
        rdown = True
        while rdown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] + i <=7:
                if field[idx[0] + i][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] + i))
                elif isinstance(field[idx[0] + i][idx[1] + i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] + i))
                    rdown = False
                else:  # friendly piece
                    rdown = False
                i += 1
            else:  # out of array
                rdown = False

        i = -1
        up = True
        while up:  # nothing in between     move up
            if idx[0] + i >= 0:
                if field[idx[0] + i][idx[1]] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]))
                elif isinstance(field[idx[0] + i][idx[1]], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    up = False
                else:  # friendly piece
                    up = False
                i -= 1
            else:  # out of array
                up = False

        i = 1
        down = True
        while down:  # nothing in between     move up
            if idx[0] + i <= 7:
                if field[idx[0] + i][idx[1]] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]))
                elif isinstance(field[idx[0] + i][idx[1]], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]))
                    down = False
                else:  # friendly piece
                    down = False
                i += 1
            else:  # out of array
                down = False

        i = 1
        right = True
        while right:  # nothing in between     move up
            if idx[1] + i <= 7:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], Black):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    right = False
                else:  # friendly piece
                    right = False
                i += 1
            else:  # out of array
                right = False

        i = -1
        left = True
        while left:  # nothing in between     move up
            if idx[1] + i >= 0:
                if field[idx[0]][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0], idx[1] + i))
                elif isinstance(field[idx[0]][idx[1] + i], Black):  # if enemy piece
                    legal.append((idx[0], idx[1] + i))
                    left = False
                else:  # friendly piece
                    left = False
                i -= 1
            else:  # out of array
                left = False

        return legal


class wBishop(White):
    def __init__(self,y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["bishop"], (posx, posy))

    def legal(self,field):
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        i = -1
        lup = True
        while lup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1]+ i >=0:
                if field[idx[0] + i][idx[1]+ i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1]+ i))
                elif isinstance(field[idx[0] + i][idx[1]+ i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1]+ i))
                    lup = False
                else:  # friendly piece
                    lup = False
                i -= 1
            else:  # out of array
                lup = False

        i = -1
        rup = True
        while rup:  # nothing in between     move up
            if idx[0] + i >= 0 and idx[1] - i<=7:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    rup = False
                else:  # friendly piece
                    rup = False
                i -= 1
            else:  # out of array
                rup = False

        i = 1
        ldown = True
        while ldown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] - i>=0:
                if field[idx[0] + i][idx[1] - i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] - i))
                elif isinstance(field[idx[0] + i][idx[1] - i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] - i))
                    ldown = False
                else:  # friendly piece
                    ldown = False
                i += 1
            else:  # out of array
                ldown = False

        i = 1
        rdown = True
        while rdown:  # nothing in between     move up
            if idx[0] + i <= 7 and idx[1] + i <=7:
                if field[idx[0] + i][idx[1] + i] == 0:  # no piece
                    legal.append((idx[0] + i, idx[1] + i))
                elif isinstance(field[idx[0] + i][idx[1] + i], Black):  # if enemy piece
                    legal.append((idx[0] + i, idx[1] + i))
                    rdown = False
                else:  # friendly piece
                    rdown = False
                i += 1
            else:  # out of array
                rdown = False

        return legal


class wPawn(White):
    def __init__(self, y, x):
        self.val = 1

        self.x = x #7
        self.y = y#1-8

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["pawn"], (posx, posy))

    def legal(self, field):  # show legal moves   works
        idx = self.arraypos(field)  # return tuple(idx1, idx2)
        legal = []  # list of legal moves

        if idx[0] - 1 >= 0 and idx[1] + 1 < 8:  # take right
            if isinstance(field[idx[0] + 1][idx[1] + 1], Black):  # enemy
                legal.append((idx[0] - 1, idx[1] + 1))

        if idx[0] - 1 >= 0 and idx[1] - 1 >= 0:  # take left
            if isinstance(field[idx[0] - 1][idx[1] - 1], Black):  # enemy
                legal.append((idx[0] - 1, idx[1] - 1))

        # walk
        if idx[0] - 1 >= 0:
            if field[idx[0] - 1][idx[1]] == 0:  # no piece
                legal.append((idx[0] - 1, idx[1]))

        if idx[0] - 2 >= 0:
            if field[idx[0] - 2][idx[1]] == 0 :  # no piece
                legal.append((idx[0] - 2, idx[1]))

#________________________________________________________________________________________________


def drawGrid(surface):
    for y in range(border, (border+8*gridsize),gridsize): # grid
        for x in range(border, (border+8*gridsize),gridsize):
            if (x+y)%2 == 0:
                lightr = pygame.Rect((x, y), (gridsize,gridsize))
                pygame.draw.rect(surface,(120,220,220), lightr)
            else:
                darkr = pygame.Rect((x, y), (gridsize,gridsize))#dark squares
                pygame.draw.rect(surface, (64,74,90), darkr)

def gameStart():
    array=[
        [bRook(8,1), bKnight(8,2), bBishop(8,3), bQueen(8,4), bKing(8,5), bBishop(8,6), bKnight(8,7), bRook(8,8)],
        [bPawn(7,1), bPawn(7,2),bPawn(7,3), bPawn(7,4), bPawn(7,5), bPawn(7,6), bPawn(7,7), bPawn(7,8)],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [wPawn(2,1), wPawn(2,2), wPawn(2,3), wPawn(2,4), wPawn(2,5), wPawn(2,6), wPawn(2,7), wPawn(2,8)],
        [wRook(1,1), wKnight(1,2), wBishop(1,3), wQueen(1,4), wKing(1,5), wBishop(1,6), wKnight(1,7), wRook(1,8)]
    ]
    return array

def gameStart(): #for testing
    array=[
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, bBishop(7,3), 0, 0, 0, 0, 0],
        [0, 0, 0, 0, wBishop(6,5), 0, 0, 0],
        [0, 0, 0, bKing(5,4),0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return array

def showPieces(array):#draw all pieces
    for row in array:
        for p in row:
            if p !=0: # if piece is there
                p.show()

def selectPieceLegal(array, x, y):#returns legal moves and piece
    print(array[x][y].legal(array))
    return (array[x][y].legal(array), array[x][y])

#_______________________________main______________________________________________________
def main():
    surface = pygame.Surface(screen.get_size())
    # surface = surface.convert()
    drawGrid(surface)
    alive=True
    array=gameStart()
    selected = None

    while (alive):
        pygame.time.Clock().tick(10)#slow game down
        drawGrid(surface)
        screen.blit(surface, (0, 0))

        #player interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # stop game
                alive = False

            #mousebuttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1: #= if leftclick
                    if selected==None:  # makeing the controlls for selected and unselected looks stupid, but checking later makes it way more annoying in my oppinion ( but this version looks more stupid)
                        #row 8
                        if (border <event.pos[0] < border +gridsize) and (border <event.pos[1] < border +gridsize):#(8,1)
                            if array[0][0] !=0:
                                l = selectPieceLegal(array, 0, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize <event.pos[0] < border +gridsize*2) and (border <event.pos[1] < border +gridsize):#(8,2)
                            if array[0][1] !=0:
                                l = selectPieceLegal(array, 0, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border < event.pos[1] < border + gridsize):# (8,3)
                            if array[0][2] != 0:
                                l = selectPieceLegal(array, 0, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border < event.pos[1] < border + gridsize):# (8,4)
                            if array[0][3] != 0:
                                l = selectPieceLegal(array, 0, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border < event.pos[1] < border + gridsize):# (8,5)
                            if array[0][4] != 0:
                                l = selectPieceLegal(array, 0, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border < event.pos[1] < border + gridsize):# (8,6)
                            if array[0][5] != 0:
                                l = selectPieceLegal(array, 0, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border < event.pos[1] < border + gridsize):# (8,7)
                            if array[0][6] != 0:
                                l = selectPieceLegal(array, 0, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border < event.pos[1] < border + gridsize):# (8,8)
                            if array[0][7] != 0:
                                l = selectPieceLegal(array, 0, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row7
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize <event.pos[1] < border +gridsize*2):#(7,1)
                            if array[1][0] !=0:
                                l = selectPieceLegal(array, 1, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize <event.pos[0] < border +gridsize*2) and (border+gridsize <event.pos[1] < border +gridsize*2):#(7,2)
                            if array[1][1] !=0:
                                l = selectPieceLegal(array, 1, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,3)
                            if array[1][2] != 0:
                                l = selectPieceLegal(array, 1, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,4)
                            if array[1][3] != 0:
                                l = selectPieceLegal(array, 1, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,5)
                            if array[1][4] != 0:
                                l = selectPieceLegal(array, 1, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,6)
                            if array[1][5] != 0:
                                l = selectPieceLegal(array, 1, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,7)
                            if array[1][6] != 0:
                                l = selectPieceLegal(array, 1, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize <event.pos[1] < border +gridsize*2):# (7,8)
                            if array[1][7] != 0:
                                l = selectPieceLegal(array, 1, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row6
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):#(6,1)
                            if array[2][0] !=0:
                                l = selectPieceLegal(array, 2, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize <event.pos[0] < border +gridsize*2) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):#(6,2)
                            if array[2][1] !=0:
                                l = selectPieceLegal(array, 2, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,3)
                            if array[2][2] != 0:
                                l = selectPieceLegal(array, 2, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,4)
                            if array[2][3] != 0:
                                l = selectPieceLegal(array, 2, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,5)
                            if array[2][4] != 0:
                                l = selectPieceLegal(array, 2, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,6)
                            if array[2][5] != 0:
                                l = selectPieceLegal(array, 2, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,7)
                            if array[2][6] != 0:
                                l = selectPieceLegal(array, 2, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*2 <event.pos[1] < border +gridsize*3):# (6,8)
                            if array[2][7] != 0:
                                l = selectPieceLegal(array, 2, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row 5
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):#(5,1)
                            if array[3][0] !=0:
                                l = selectPieceLegal(array, 3, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+55 <event.pos[0] < border +gridsize*2) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):#(5,2)
                            if array[3][1] !=0:
                                l = selectPieceLegal(array, 3, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,3)
                            if array[3][2] != 0:
                                l = selectPieceLegal(array, 3, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,4)
                            if array[3][3] != 0:
                                l = selectPieceLegal(array, 3, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,5)
                            if array[3][4] != 0:
                                l = selectPieceLegal(array, 3, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,6)
                            if array[3][5] != 0:
                                l = selectPieceLegal(array, 3, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,7)
                            if array[3][6] != 0:
                                l = selectPieceLegal(array, 3, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*3 <event.pos[1] < border +gridsize*4):# (5,8)
                            if array[3][7] != 0:
                                l = selectPieceLegal(array, 3, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row 4
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):#(4,1)
                            if array[4][0] !=0:
                                l = selectPieceLegal(array, 4, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+55 <event.pos[0] < border +gridsize*2) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):#(4,2)
                            if array[4][1] !=0:
                                l = selectPieceLegal(array, 4, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,3)
                            if array[4][2] != 0:
                                l = selectPieceLegal(array, 4, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,4)
                            if array[4][3] != 0:
                                l = selectPieceLegal(array, 4, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,5)
                            if array[4][4] != 0:
                                l = selectPieceLegal(array, 4, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,6)
                            if array[4][5] != 0:
                                l = selectPieceLegal(array, 4, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,7)
                            if array[4][6] != 0:
                                l = selectPieceLegal(array, 4, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*4 <event.pos[1] < border +gridsize*5):# (4,8)
                            if array[4][7] != 0:
                                l = selectPieceLegal(array, 4, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row3
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):#(3,1)
                            if array[5][0] !=0:
                                l = selectPieceLegal(array, 5, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+55 <event.pos[0] < border +gridsize*2) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):#(3,2)
                            if array[5][1] !=0:
                                l = selectPieceLegal(array, 5, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,3)
                            if array[5][2] != 0:
                                l = selectPieceLegal(array, 5, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,4)
                            if array[5][3] != 0:
                                l = selectPieceLegal(array, 5, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,5)
                            if array[5][4] != 0:
                                l = selectPieceLegal(array, 5, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,6)
                            if array[5][5] != 0:
                                l = selectPieceLegal(array, 5, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,7)
                            if array[5][6] != 0:
                                l = selectPieceLegal(array, 5, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*5 <event.pos[1] < border +gridsize*6):# (3,8)
                            if array[5][7] != 0:
                                l = selectPieceLegal(array, 5, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row2
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):#(2,1)
                            if array[6][0] !=0:
                                l = selectPieceLegal(array, 6, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+55 <event.pos[0] < border +gridsize*2) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):#(2,2)
                            if array[6][1] ==0:
                                l = selectPieceLegal(array, 6, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,3)
                            if array[6][2] != 0:
                                l = selectPieceLegal(array, 6, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,4)
                            if array[6][3] != 0:
                                l = selectPieceLegal(array, 6, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,5)
                            if array[6][4] != 0:
                                l = selectPieceLegal(array, 6, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,6)
                            if array[6][5] != 0:
                                l = selectPieceLegal(array, 6, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,7)
                            if array[6][6] != 0:
                                l = selectPieceLegal(array, 6, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*6 <event.pos[1] < border +gridsize*7):# (2,8)
                            if array[6][7] != 0:
                                l = selectPieceLegal(array, 6, 7)
                                if len(l[0])>0:
                                    selected=l[1]
                        #row1
                        elif (border <event.pos[0] < border +gridsize) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):#(1,1)
                            if array[7][0] !=0:
                                l = selectPieceLegal(array, 7, 0)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+55 <event.pos[0] < border +gridsize*2) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):#(1,2)
                            if array[7][1] !=0:
                                l = selectPieceLegal(array, 7, 1)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*2 < event.pos[0] < border + gridsize*3) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,3)
                            if array[7][2] != 0:
                                l = selectPieceLegal(array, 7, 2)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*3 < event.pos[0] < border + +gridsize*4) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,4)
                            if array[7][3] != 0:
                                l = selectPieceLegal(array, 7, 3)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*4 < event.pos[0] < border + +gridsize*5) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,5)
                            if array[7][4] != 0:
                                l = selectPieceLegal(array, 7, 4)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*5 < event.pos[0] < border + +gridsize*6) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,6)
                            if array[7][5] != 0:
                                l = selectPieceLegal(array, 7, 5)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*6 < event.pos[0] < border + +gridsize*7) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,7)
                            if array[7][6] != 0:
                                l = selectPieceLegal(array, 7, 6)
                                if len(l[0])>0:
                                    selected=l[1]
                        elif (border+gridsize*7 < event.pos[0] < border + +gridsize*8) and (border+gridsize*7 <event.pos[1] < border +gridsize*8):# (1,8)
                            if array[7][7] != 0:
                                l = selectPieceLegal(array, 7, 7)
                                if len(l[0])>0:
                                    selected=l[1]

                elif event.button ==3:  #right mouse button  => unselect
                    selected=None



        showPieces(array)
        pygame.display.update()

if __name__ =="__main__":
    main()