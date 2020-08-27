import pygame


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
#___________________________pieces___________________________________________________________________________
class bRook():
    def __init__(self, y, x):
        self.val=5
        self.x=x
        self.y=y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["rook"],(posx,posy))

    def move(self):
        pass


class bKing():
    def __init__(self, y, x):
        self.val = float("inf")

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["king"],(posx,posy))


class bKnight():
    def __init__(self, y, x):
        self.val = 5

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["knight"],(posx,posy))

class bQueen():
    def __init__(self, y, x):
        self.val = 9

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["queen"],(posx,posy))

class bBishop():
    def __init__(self, y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["bishop"],(posx,posy))

class bPawn():
    def __init__(self, y, x):
        self.val = 1

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(black["pawn"],(posx,posy))

class wRook():
    def __init__(self, y, x):
        self.val = 5

        self.x = x
        self.y = y

    def show(self):
        posx=(self.x-1)*gridsize+border+5
        posy= (8-self.y)*gridsize+border+5
        screen.blit(white["rook"],(posx,posy))


class wKing():
    def __init__(self, y, x):
        self.val = float("inf")

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["king"], (posx, posy))


class wKnight():
    def __init__(self, y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["knight"], (posx, posy))


class wQueen():
    def __init__(self, y, x):
        self.val = 9

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["queen"], (posx, posy))


class wBishop():
    def __init__(self,y, x):
        self.val = 3

        self.x = x
        self.y = y

    def show(self):
        posx = (self.x - 1) * gridsize + border + 5
        posy = (8 - self.y) * gridsize + border + 5
        screen.blit(white["bishop"], (posx, posy))


class wPawn():
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


        pygame.display.update()
main()