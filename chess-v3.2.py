###############################
###                         ###
###    CHESS by Theo v3.2   ###
###                         ###   
###############################
### last_update: 30/06/2024 ###
###############################
### Nota da versão:
### - 
### - 
### - 
### - 
###############################
###############################
### Melhorias a realizar:
### - estruturar variaveis de controle e criar metodo para iniciar e reinicia-las
### - verificar se o rei está em check
### - não permitir colocar seu proprio rei em check
### - criar maquina de estados(state machine)?
### - expandir sistema de promoção do peao para escolha de peça
### - abandonar pysimpleGUI e usar Tkinter
### - adicionar timer
### - ideia (possivel V4): primeiro criar o tabuleiro(board) garantir que seja uma matrix e depois adicionar as peças
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

game_size_aspect_ratio = 2 ## to default keep 1 (for monitor w/ 1080px height res. max recomended is 2.2, min 0.9)

# board cell definitions
board_cell_size = 50*game_size_aspect_ratio # using initBoard default 50 (50px)
board_cell_dimension = board_cell_size , board_cell_size
board_cell_white_color = sty.wood_light # using initBoard
board_cell_black_color = sty.wood_dark # using initBoard
board_cell_sellected_color = sty.wood_select
board_cell_moviment_highlight_color_light = (0,200,0) 
board_cell_moviment_highlight_color_dark = (0,100,0) 

# board definitions
board_margin_size = 20*game_size_aspect_ratio # using initBoard default 20 (20px)

board_size = 8*board_cell_size + 2*board_margin_size # internal in initBoard
board_dimension = board_size, board_size
board_color = sty.wood_board

screen_dimension = board_size, board_size

### templates ###
template_number = 3
board_cell_white_color = sty.template[template_number][0]
board_cell_black_color = sty.template[template_number][1]
board_color = sty.template[template_number][2]
board_cell_sellected_color = sty.template[template_number][3]


###############

# pygame setup
pygame.init()
screen = pygame.display.set_mode(screen_dimension)
clock = pygame.time.Clock()
pygame.display.set_caption('Chess by Theo')
running = True
#dt = 0

active_cell = None
board = []
posX = 0 #distance from left
posY = 0 #distance from top
color = board_cell_black_color
addr = None
selected = False

turn = "white"
check_mate = False
white_king_pos = "1e"
black_king_pos = "8e"

# castling control variable
rook_1a_first_moviment = True
white_king_first_moviment = True
rook_1h_first_moviment = True
rook_8a_first_moviment = True
black_king_first_moviment = True
rook_8h_first_moviment = True

castlingStatus = [
    rook_1a_first_moviment,
    white_king_first_moviment,
    rook_1h_first_moviment,
    rook_8a_first_moviment,
    black_king_first_moviment,
    rook_8h_first_moviment,
]

piece = None #piece color, piece name, piece logo
cell_empty = lib.Piece() #object piece with empty values - means cell empty 
origin_cell_index = None
origin_cell_name = None
#destiny_cell = None
moving_piece = None
moving_status = False

menu = True
menu_font_size = 20*game_size_aspect_ratio
menu_font_type = 'arial'
menu_font_color = sty.ivory
#menu_bg_img = sty.menu_bg_img_ratio_1
menu_bg_img = sty.menu_bg_img_ratio_2
text_menu = "ESC to Resume | SPACE to New Game | Q to Quit"

## initializating board ##
[board_address_dict, board_rect, board] = lib.initBoard(board_cell_white_color, board_cell_black_color, board_cell_size, board_margin_size)

print("White's Turn")
while running:

    if menu == False: 
    ## drawing board ##
        lib.drawBoard(screen, board_color, board_rect, board_cell_sellected_color, board)
        if check_mate == True:
            lib.drawCheckMate(screen, board_rect, menu_bg_img, menu_font_type, menu_font_size, sty.night, check_mate_text)

    ## drawing menu ##
    if menu == True:
        lib.drawMenu(screen, board_rect, menu_bg_img, menu_font_type, menu_font_size, menu_font_color, text_menu)

    
    # poll for events
    
    for event in pygame.event.get():
        
        # press keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                template_number = 0
                board_cell_white_color = sty.template[template_number][0]
                board_cell_black_color = sty.template[template_number][1]
                board_color = sty.template[template_number][2]
                board_cell_sellected_color = sty.template[template_number][3]

            if event.key == pygame.K_1:
                template_number = 1
                board_cell_white_color = sty.template[template_number][0]
                board_cell_black_color = sty.template[template_number][1]
                board_color = sty.template[template_number][2]
                board_cell_sellected_color = sty.template[template_number][3]

            if event.key == pygame.K_2:
                template_number = 2
                board_cell_white_color = sty.template[template_number][0]
                board_cell_black_color = sty.template[template_number][1]
                board_color = sty.template[template_number][2]
                board_cell_sellected_color = sty.template[template_number][3]

            if event.key == pygame.K_3:
                template_number = 3
                board_cell_white_color = sty.template[template_number][0]
                board_cell_black_color = sty.template[template_number][1]
                board_color = sty.template[template_number][2]
                board_cell_sellected_color = sty.template[template_number][3]


            
            
            if event.key == pygame.K_ESCAPE:
                print("ESC!")
                if menu == True: menu = False
                else: menu = True
            if event.key == pygame.K_SPACE:
                print("SPACE!")
                if menu == True: 
                    [board_address_dict, board_rect, board] = lib.initBoard(board_cell_white_color, board_cell_black_color, board_cell_size, board_margin_size)
                    castlingStatus
                    turn = "white"
                    check_mate = False
                    menu = False
                #call reset board
            if event.key == pygame.K_q:
                print("Q!")
                running = False


        ## clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left button
                for index, cell in enumerate(board):
                    ## click on cell
                    if menu == False and cell.rect.collidepoint(event.pos):
                        # make a play
                        clicked_cell_index = index # active_cell is a number, it is the index for adressed the cell in the board
                        r = lib.makeaPlay(clicked_cell_index, origin_cell_index, board, board_address_dict, moving_piece, cell_empty, moving_status,  castlingStatus, turn, check_mate, white_king_pos, black_king_pos)
                        clicked_cell_index, origin_cell_index, board, board_address_dict, moving_piece, cell_empty, moving_status,  castlingStatus, turn, check_mate, white_king_pos, black_king_pos = r
                        if check_mate == True and turn != "end":
                            check_mate_text = "The "+turn+" king is dead. Check Mate!"
                            print("The",turn,"king is dead. Check Mate!")
                            turn = "end"


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