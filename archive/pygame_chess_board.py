# from pygame docs
# local path E:/dev/chess/chessVenv/Lib/site-packages/pygame/docs/generated/index.html
# python -m pygame.docs

#ref1 https://www.youtube.com/watch?v=Ro82dac_J1Y
#ref2 https://pygame.readthedocs.io/en/latest/rect/rect.html

import pygame

def getColumnIndex(name):
    if name == 'a': column = 0 
    elif name == 'b': column = 1
    elif name == 'c': column = 2
    elif name == 'd': column = 3
    elif name == 'e': column = 4
    elif name == 'f': column = 5
    elif name == 'g': column = 6
    elif name == 'h': column = 7

    return column

def getColumnName(index):
    if index == 0: column = 'a'
    elif index == 1: column = 'b'
    elif index == 2: column = 'c'
    elif index == 3: column = 'd'
    elif index == 4: column = 'e'
    elif index == 5: column = 'f'
    elif index == 6: column = 'g'
    elif index == 7: column = 'h'

    return column

def getRowIndex(name):
    if name == '1': row = 0 
    elif name == '2': row = 1
    elif name == '3': row = 2
    elif name == '4': row = 3
    elif name == '5': row = 4
    elif name == '6': row = 5
    elif name == '7': row = 6
    elif name == '8': row = 7

    return row

def getRowName(index):
    if index == 0: row = '1'
    elif index == 1: row = '2'
    elif index == 2: row = '3'
    elif index == 3: row = '4'
    elif index == 4: row = '5'
    elif index == 5: row = '6'
    elif index == 6: row = '7'
    elif index == 7: row = '8'

    return row

def setInitialPiece(name):

    white_pawn = ["2a","2b","2c","2d","2e","2f","2g","2h"]
    white_rook = ["1a","1h"]
    white_knight = ["1b","1g"]
    white_bishop = ["1c","1f"]
    white_queen = ["1d"]
    white_king = ["1e"]

    black_pawn = ["7a","7b","7c","7d","7e","7f","7g","7h"]
    black_rook = ["8a","8h"]
    black_knight = ["8b","8g"]
    black_bishop = ["8c","8f"]
    black_queen = ["8d"]
    black_king = ["8e"]

    if name in white_pawn: return 'white', 'pawn'
    elif name in white_rook: return 'white', 'rook'
    elif name in white_knight: return 'white', 'knight'
    elif name in white_bishop: return 'white', 'bishop'
    elif name in white_queen: return 'white', 'queen' 
    elif name in white_king: return 'white', 'king'

    elif name in black_pawn: return 'black', 'pawn'
    elif name in black_rook: return 'black', 'rook'
    elif name in black_knight: return 'black', 'knight'
    elif name in black_bishop: return 'black', 'bishop'
    elif name in black_queen: return 'black', 'queen'
    elif name in black_king: return 'black', 'king'
    else: return 'none','empty'

#### Definitions ####
window_size = (400, 400)

ivory = (255,255,240) #FFFFF0
night = (12, 12, 12) #0C0C0C

wood_light = (191,178,161)
wood_dark = (154,89,56)
wood_board = (86,72,59)

dark_cyan = (55, 147, 146) #379392
steel_blue = (77, 126, 168) #4D7EA8
lapis_lazuli = (55, 105, 150) #376996

board_cell_size = 50
board_cell_dimension = board_cell_size , board_cell_size
board_cell_white_color = wood_light
board_cell_black_color = wood_dark
board_cell_sellected_color = (0,255,0)
board_cell_moviment_highlight_color_light = (0,200,0) 
board_cell_moviment_highlight_color_dark = (0,100,0) 

board_margin_size = 20
board_size = 8*board_cell_size + 2*board_margin_size
board_dimension = board_size, board_size
board_color = wood_board

screen_dimension = board_size, board_size

# pygame setup
pygame.init()
screen = pygame.display.set_mode(screen_dimension)
clock = pygame.time.Clock()
running = True
dt = 0

active_cell = None
chess = []
posX = 0 #distance from left
posY = 0 #distance from top
color = board_cell_black_color
name = None
selected = False

board = pygame.Rect(0,0,board_size,board_size)
#pygame.draw.rect(screen, board_color, board)
piece = () #piece name, team color

for i in range(0,8):
    posX = i*board_cell_size + board_margin_size
    if color == board_cell_white_color: color = board_cell_black_color
    else:  color = board_cell_white_color
    for j in range(0,8):
        posY = j*board_cell_size + board_margin_size
        name = getRowName(7-j)+getColumnName(i)
        print("name:", name)
        piece = setInitialPiece(name)
        print("piece", piece)
        cell =  [pygame.Rect(posX,posY,board_cell_size,board_cell_size), color, name, selected, piece]
        #if cell[3]==False: pygame.draw.rect(screen, color, cell[0])
        #else: pygame.draw.rect(screen, board_cell_sellected_color, cell[0])
        chess.append(cell)
        if color == board_cell_white_color: color = board_cell_black_color
        else:  color = board_cell_white_color
    
    for cell in chess:
        print(cell[2], cell[4])

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, board_color, board)

    for cell in chess:
        rect, color, name, selected, piece = cell
        #print("get cell", name, color)
        if cell[3]==False: pygame.draw.rect(screen, color, rect)
        else: 
            pygame.draw.rect(screen, board_cell_sellected_color, rect)
            #print("selected")
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, cell in enumerate(chess):
                    rect, color, name, selected, piece = cell
                    if cell[0].collidepoint(event.pos):
                        active_cell = num
                        if chess[num][3] == False: chess[num][3] = True
                        else: chess[num][3] = False
                        #pygame.draw.rect(screen, board_cell_sellected_color, chess[num][0])
                        print(cell[2], piece, num, event.pos)
        if event.type == pygame.QUIT:
            running = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()