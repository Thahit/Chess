import pygame
from abc import ABC

#img from https://en.wikipedia.org/wiki/Chess_piece
white={"king": pygame.image.load("img/wKing.png"), "queen": pygame.image.load("img/wQueen.png"), "rook":pygame.image.load("img/wRook.png"),
       "bishop": pygame.image.load("img/wBishop.png"),"knight":pygame.image.load("img/wKnight.png"), "pawn":pygame.image.load("img/wPawn.png")}
black={"king": pygame.image.load("img/bKing.png"), "queen": pygame.image.load("img/bQueen.png"), "rook":pygame.image.load("img/bRook.png"),
       "bishop": pygame.image.load("img/bBishop.png"),"knight":pygame.image.load("img/bKnight.png"), "pawn":pygame.image.load("img/bPawn.png")}



#window
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
#to check for allies/enemies
class Black(ABC):
    def __init__(self, y, x):
        self.x=x
        self.y=y
    def arraypos(self, array):  # where is it in array
        return (8 - self.y, self.x - 1)

    def show(self):
        pass

class White(ABC):
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def arraypos(self, array):  # where is it in array
        return (8 - self.y, self.x - 1)
    def show(self):
        pass
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



class bKnight(Black):
    def __init__(self, y, x):
        self.val = 5

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["knight"],(posx,posy))


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



class wKnight(White):
    def __init__(self, y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["knight"], (posx, posy))


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
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, wBishop(6,3), 0, wBishop(6,5), 0, 0, 0],
        [0, 0, 0, bQueen(5,4),0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return array

def showPieces(array):
    for row in array:
        for p in row:
            if p !=0: # if piece is there
                p.show()

def main():
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    alive=True
    array=gameStart()


    while (alive):
        pygame.time.Clock().tick(10)#slow game down
        drawGrid(surface)
        screen.blit(surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # stop game
                alive = False

        showPieces(array)

        print(array[3][3].legal(array))
        pygame.display.update()
main()