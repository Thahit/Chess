import pygame
import sys

white={"king": "♔", "queen": "♕", "rook":"♖", "bishop": "♗","knight":"♘", "pawn":"♙"}
black={"king": "♚", "queen": "♛", "rook":"♛", "bishop": "♝","knight":"♞", "pawn":"♟"}

print("balck pieces: ", black["king"], black["queen"],black["rook"],black["bishop"],black["knight"],black["pawn"],)
print("white pieces: ", white["king"], white["queen"],white["rook"],white["bishop"],white["knight"],white["pawn"],)
#___________________________pieces___________________________________________________________________________
class bRook():
    def __init__(self):
        self.val=5

    def show(self):
        pass

    def move(self):
        pass


class bKing():
    def __init__(self):
        self.val = float("inf")


class bKnight():
    def __init__(self):
        self.val = 5


class bQueen():
    def __init__(self):
        self.val = 9


class bBishop():
    def __init__(self):
        self.val = 3


class bPawn():
    def __init__(self):
        self.val = 1


class wRook():
    def __init__(self):
        self.val = 5


class wKing():
    def __init__(self):
        self.val = float("inf")


class wKnight():
    def __init__(self):
        self.val = 3


class wQueen():
    def __init__(self):
        self.val = 9


class wBishop():
    def __init__(self):
        self.val = 3


class wPawn():
    def __init__(self):
        self.val = 1
#________________________________________________________________________________________________



#window
pygame.init()
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("img/Icon.png"))


gridsize=65
width=800
border=30
height=gridsize*8+ 2*border
font = pygame.font.Font('freesansbold.ttf', 20)
screen = pygame.display.set_mode((width, height))

def drawGrid(surface):
    for y in range(border, (border+8*gridsize),gridsize): # grid
        for x in range(border, (border+8*gridsize),gridsize):
            if (x+y)%2 == 0:
                lightr = pygame.Rect((x, y), (gridsize,gridsize))
                pygame.draw.rect(surface,(120,220,220), lightr)
            else:
                darkr = pygame.Rect((x, y), (gridsize,gridsize))#dark squares
                pygame.draw.rect(surface, (64,74,90), darkr)



def main():
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    alive=True
    while (alive):

        pygame.time.Clock().tick(10)#slow game down
        drawGrid(surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # stop game
                alive = False
        screen.blit(surface, (0, 0))
        pygame.display.update()

main()