###############################
###                         ###
###    CHESS by Theo v2.1   ###
###                         ###   
###############################
### last_update: 18/06/2024 ###
###############################
### Nota da versão:
### - adicionando menu do jogo
### - adicionando ao launcher
###############################
###############################
### Melhorias a realizar:
### - fazer O.O.
### - migrar ou recriar sistema de turnos
### - Não parmitir que o jogador mexa a pedra do adversario
### - verificar obstrução
### - não permitir que peça mate peça aliada
### - abandonar pysimpleGUI e usar Tkinter
### - recriar menu
### - recriar morte do rei
### - adicionar timer
###############################

#### REF ####
# local path E:/dev/chess/chessVenv/Lib/site-packages/pygame/docs/generated/index.html
# python -m pygame.docsu
#ref1 https://www.youtube.com/watch?v=Ro82dac_J1Y
#ref2 https://pygame.readthedocs.io/en/latest/rect/rect.html
#ref2 pygamekey https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/

import pygame
import chess_lib as lib
import style.style as sty

#### Definitions ####
window_size = (400, 400)

# board cell definitions
board_cell_size = 50
board_cell_dimension = board_cell_size , board_cell_size
board_cell_white_color = sty.wood_light
board_cell_black_color = sty.wood_dark
board_cell_sellected_color = (0,255,0)
board_cell_moviment_highlight_color_light = (0,200,0) 
board_cell_moviment_highlight_color_dark = (0,100,0) 

# board definitions
board_margin_size = 20
board_size = 8*board_cell_size + 2*board_margin_size
board_dimension = board_size, board_size
board_color = sty.wood_board

screen_dimension = board_size, board_size

# pygame setup
pygame.init()
screen = pygame.display.set_mode(screen_dimension)
clock = pygame.time.Clock()
pygame.display.set_caption('Chess by Theo')
running = True
dt = 0

active_cell = None
chess = []
posX = 0 #distance from left
posY = 0 #distance from top
color = board_cell_black_color
name = None
selected = False

piece = None #piece color, piece name, piece logo
origin_cell = None
destiny_cell = None
moving_piece = None
moving_status = False

## initializating board ##
board = pygame.Rect(0,0,board_size,board_size)

for i in range(0,8):
    posX = i*board_cell_size + board_margin_size
    if color == board_cell_white_color: color = board_cell_black_color
    else:  color = board_cell_white_color
    for j in range(0,8):
        posY = j*board_cell_size + board_margin_size
        name = lib.getRowName(7-j)+lib.getColumnName(i)
        piece = lib.setInitialPiece(name)
        cell =  [pygame.Rect(posX,posY,board_cell_size,board_cell_size), color, name, selected, piece]
        chess.append(cell)
        if color == board_cell_white_color: color = board_cell_black_color
        else:  color = board_cell_white_color
    
    ## checking set-up ##
    for cell in chess:
        print(cell[2], cell[4][0], cell[4][1] )


while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    ## drawing board ##
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC!")

        ## click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left button
                for num, cell in enumerate(chess):
                    rect, color, name, selected, piece = cell
                    ## click on cell
                    if cell[0].collidepoint(event.pos):
                        active_cell = num
                        if chess[num][3] == False: 
                            if moving_status == False and chess[num][4] != lib.empty:   
                                chess[num][3] = True
                                moving_status = True
                                origin_cell = num
                                origin_cell_name = chess[num][2]
                                moving_piece = piece
                                print("grabbed", piece[0], piece[1], "from", name)
                            elif moving_status == True: 
                                if lib.validMoviment(origin_cell_name, chess[num][2], moving_piece):
                                    #print("valid")    
                                    chess[origin_cell][3] = False
                                    chess[origin_cell][4] = lib.empty
                                    chess[num][4] = moving_piece
                                    print("placed", moving_piece[0], moving_piece[1], "on", name)
                                    moving_status = False
                                    origin_cell = None
                                    moving_piece = None
                                else: print("invalid moviment")      
                        elif chess[num][3] == True: 
                            chess[num][3] = False
                            moving_status = False
                            origin_cell = None
                            moving_piece = None
                            print("release", piece[0], piece[1], "back to", name)
        ## close window - window X button
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    #dt = clock.tick(60) / 1000

pygame.quit()

print("---------------------- end ----------------------\n\n") 