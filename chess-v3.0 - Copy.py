###############################
###                         ###
###    CHESS by Theo v3.0   ###
###                         ###   
###############################
### last_update: 18/06/2024 ###
###############################
### Nota da versão:
### - encapsular rotinas - criar funções de play_game_p2p, menu, etc
### - utilizando objetos para cell e piece
### - alterado nome de variavel board e chess no fluxo do programa
### - criado em chess_lib função validPlay verificando quando peça adversaria e incluindo movimento peculiar do peão  
###############################
###############################
### Melhorias a realizar:
### - avaliar fazer O.O. para board
### - corrigir captura de cliques de jogo na tela de menu
### - migrar ou recriar sistema de turnos
### - Não permitir que o jogador mexa a pedra do adversario
### - verificar obstrução
### - não permitir que peça mate peça aliada
### - abandonar pysimpleGUI e usar Tkinter
### - recriar menu
### - recriar morte do rei
### - adicionar sistema de peça matar peça
### - adicionar propriedade pawn substituir peça
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
#window_size = (440, 440)

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
board = []
posX = 0 #distance from left
posY = 0 #distance from top
color = board_cell_black_color
addr = None
selected = False

turn = "white"

piece = None #piece color, piece name, piece logo
cell_empty = lib.Piece() #object piece with empty values - means cell empty 
origin_cell = None
destiny_cell = None
moving_piece = None
moving_status = False

menu = True
menu_font_size = 20
text_menu = "ESC to Resume | SPACE to New Game | Q to Quit"

## initializating board ##
board_rect = pygame.Rect(0,0,board_size,board_size)

for i in range(0,8):
    posX = i*board_cell_size + board_margin_size
    if color == board_cell_white_color: color = board_cell_black_color
    else:  color = board_cell_white_color
    for j in range(0,8):
        posY = j*board_cell_size + board_margin_size
        addr = lib.getRowName(7-j)+lib.getColumnName(i)
        piece = lib.Piece(addr)
        cell =  lib.Cell(pygame.Rect(posX,posY,board_cell_size,board_cell_size), color, addr, selected, piece)
        board.append(cell)
        if color == board_cell_white_color: color = board_cell_black_color
        else:  color = board_cell_white_color
    
    ## checking set-up ##
    for cell in board:
        print(cell.addr, cell.piece.color, cell.piece.name )

while running:
    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("white")

    ## drawing board ##
    pygame.draw.rect(screen, board_color, board_rect)
# color, name, logo
    for cell in board:
        #print("DEBUG cell: ",type(cell))
        #rect, color, name, selected, piece = cell
        #print("get cell", name, color)
        if menu == False:    
            print("DEBUG: ", cell.selected)
            if cell.selected == False: 
                pygame.draw.rect(screen, cell.color, cell.rect)
                #rect.center = center
                #print("DEBUG:",cell.piece.color, cell.piece.name, cell.piece.logo)
                #print("DEBUG piece: ", type(cell.piece), cell.piece)
                if cell.piece.logo != None:
                    img = cell.piece.logo
                    img.convert()
                    img = pygame.transform.rotozoom(img,0,lib.scale_piece_img_rate)
                    img_rect = img.get_rect(center = cell.rect.center)
                    screen.blit(img, img_rect)
            elif cell.selected == True:  
                pygame.draw.rect(screen, board_cell_sellected_color, cell.rect)
                img = cell.piece.logo
                img.convert()
                img = pygame.transform.rotozoom(img,0,lib.scale_piece_img_rate)
                img_rect = img.get_rect(center = cell.rect.center)
                screen.blit(img, img_rect)
    
    if menu == True:
        # menu ESC =  Resume | SPACE = Restart | Q = Quit
        #print(text_menu)
        #screen.fill(sty.night)
        screen.blit(sty.menu_bg_img,(0,0))
        font = pygame.font.SysFont('arial', menu_font_size)
        font_img = font.render(text_menu, True, sty.ivory)
        font_img_rect = font_img.get_rect(center = board_rect.center)
        screen.blit(font_img,font_img_rect)  
    
    # poll for events
    
    for event in pygame.event.get():
        
        # press keys on menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC!")
                if menu == True: menu = False
                else: menu = True
            if event.key == pygame.K_SPACE:
                print("SPACE!")
                if menu == True: menu = False
                else: menu = True
                #call reset board
            if event.key == pygame.K_q:
                print("Q!")
                running = False


        ## click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left button
                for num, cell in enumerate(board):
                    #rect, color, name, selected, piece = cell
                    ## click on cell
                    if cell.rect.collidepoint(event.pos): ##possivel bosta pela mudança pra obj
                        active_cell = num
                        if board[num].selected == False: 
                            #print("L1")
                            if moving_status == False and board[num].piece.name != cell_empty.name:
                                #print("L1.1")   
                                board[num].selected = True
                                moving_status = True
                                origin_cell = num
                                origin_cell_name = board[num].addr
                                moving_piece = cell.piece
                                print("grabbed", cell.piece.color, cell.piece.name, "from", cell.addr)
                            elif moving_status == True: 
                                #print("L1.2")
                                if lib.validPlay(origin_cell_name, board[num].addr, moving_piece, board[num].piece):
                                    #print("L1.2.1")
                                    #print("valid")    
                                    board[origin_cell].selected = False
                                    board[origin_cell].piece = cell_empty #lib.Piece()
                                    board[num].piece = moving_piece
                                    print("placed", moving_piece.color, moving_piece.name, "on", cell.addr)
                                    moving_status = False
                                    origin_cell = None
                                    moving_piece = None
                                else: 
                                    print("L1.2.2")
                                    print("invalid moviment")

                        elif board[num].selected == True: 
                            print("L2")
                            board[num].selected = False
                            moving_status = False
                            origin_cell = None
                            moving_piece = None
                            print("release", cell.piece.color, cell.piece.name, "back to", cell.addr)
        
        ## close window - window X button
        # pygame.QUIT event means the user clicked X to close your window
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