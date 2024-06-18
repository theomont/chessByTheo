###############################
###                         ###
###    CHESS by Theo v2.0   ###
###                         ###   
###############################
### last_update: 12/06/2024 ###
###############################
### Nota da versão:
### - usando pygame
### 
### 
###############################
###############################
### Melhorias a realizar:
### - capturar 'name' e mover peça
### - Não parmitir que o jogador mexa a pedra do adversario
### 
###############################

# local path E:/dev/chess/chessVenv/Lib/site-packages/pygame/docs/generated/index.html
# python -m pygame.docs

#ref1 https://www.youtube.com/watch?v=Ro82dac_J1Y
#ref2 https://pygame.readthedocs.io/en/latest/rect/rect.html

import pygame
import chess_lib as lib 

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
piece = None #piece name, team color

origin_cell = None
destiny_cell = None
moving_piece = piece
moving_status = False



for i in range(0,8):
    posX = i*board_cell_size + board_margin_size
    if color == board_cell_white_color: color = board_cell_black_color
    else:  color = board_cell_white_color
    for j in range(0,8):
        posY = j*board_cell_size + board_margin_size
        name = lib.getRowName(7-j)+lib.getColumnName(i)
        print("name:", name)
        piece = lib.setInitialPiece(name)
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
        if cell[3]==False: 
            pygame.draw.rect(screen, color, rect)
            #rect.center = center
            if cell[4][2] != None:
                img = cell[4][2]
                img.convert()
                img = pygame.transform.rotozoom(img,0,lib.scale_piece_img_rate)
                img_rect = img.get_rect(center = rect.center)
                screen.blit(img, img_rect)

        else:  
            pygame.draw.rect(screen, board_cell_sellected_color, rect)
            img = cell[4][2]
            img.convert()
            img = pygame.transform.rotozoom(img,0,lib.scale_piece_img_rate)
            img_rect = img.get_rect(center = rect.center)
            screen.blit(img, img_rect)
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, cell in enumerate(chess):
                    rect, color, name, selected, piece = cell
                    if cell[0].collidepoint(event.pos):
                        active_cell = num
                        if chess[num][3] == False: 
                            if moving_status == False and chess[num][4] != lib.empty:   
                                chess[num][3] = True
                                moving_status = True
                                origin_cell = num
                                moving_piece = piece
                                print("get piece", piece, name)
                            elif moving_status == True: 
                                chess[origin_cell][3] = False
                                chess[origin_cell][4] = lib.empty
                                chess[num][4] = moving_piece
                                print("release piece", moving_piece, name)
                                moving_status = False
                                origin_cell = None
                                moving_piece = None      
                        elif chess[num][3] == True: 
                            chess[num][3] = False
                            moving_status = False
                            origin_cell = None
                            moving_piece = None
                            print("deselect", piece, name)


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