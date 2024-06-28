###############################
###                         ###
###    CHESS by Theo v3.1   ###
###                         ###   
###############################
### last_update: 28/06/2024 ###
###############################
### Nota da versão:
### - 
###############################
###############################
### Melhorias a realizar:
### - encapsular rotinas - criar funções de play_game_p2p, menu, etc 
### - criar maquina de estados(state machine)?
### - adicionar jogada especial Roque (castling)
### - avaliar fazer O.O. para board
### - corrigir captura de cliques de jogo na tela de menu
### - migrar ou recriar sistema de turnos
### - Não permitir que o jogador mexa a pedra do adversario
### - verificar obstrução
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
board_cell_size = 50 # using initBoard

board_cell_dimension = board_cell_size , board_cell_size
board_cell_white_color = sty.wood_light # using initBoard
board_cell_black_color = sty.wood_dark # using initBoard
board_cell_sellected_color = (0,255,0)
board_cell_moviment_highlight_color_light = (0,200,0) 
board_cell_moviment_highlight_color_dark = (0,100,0) 

# board definitions
board_margin_size = 20 # using initBoard

board_size = 8*board_cell_size + 2*board_margin_size # internal in initBoard
board_dimension = board_size, board_size
board_color = sty.wood_board

screen_dimension = board_size, board_size

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
origin_cell = None
destiny_cell = None
moving_piece = None
moving_status = False

menu = True
menu_font_size = 20
text_menu = "ESC to Resume | SPACE to New Game | Q to Quit"

## initializating board ##
[board_address_dict, board_rect, board] = lib.initBoard(board_cell_white_color, board_cell_black_color, board_cell_size, board_margin_size)

print("White's Turn")
while running:

    if menu == False: 
    ## drawing board ##
        lib.drawBoard(screen, board_color, board_rect, board_cell_sellected_color, board)

    ## menu ##
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
                if menu == True: 
                    [board_address_dict, board_rect, board] = lib.initBoard(board_cell_white_color, board_cell_black_color, board_cell_size, board_margin_size)
                    menu = False
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
                            if moving_status == False and board[num].piece.name != cell_empty.name and board[num].piece.color == turn:
                                #print("L1.1")   
                                board[num].selected = True
                                moving_status = True
                                origin_cell = num
                                origin_cell_name = board[num].addr
                                moving_piece = cell.piece
                                print("grabbed", cell.piece.color, cell.piece.name, "from", cell.addr)
                            elif moving_status == True: 
                                if lib.validPlay(origin_cell_name, board[num].addr, moving_piece, board[num].piece, board, board_address_dict, castlingStatus):
                                    #print("L1.2.1")
                                    #print("valid")    
                                    board[origin_cell].selected = False
                                    board[origin_cell].piece = cell_empty #lib.Piece()
                                    board[num].piece = moving_piece
                                    print("placed", moving_piece.color, moving_piece.name, "on", cell.addr)
                                    castlingStatus = lib.updateCastlingStatus(moving_piece,  board[origin_cell], castlingStatus)
                                    print(castlingStatus)
                                    moving_status = False
                                    origin_cell = None
                                    moving_piece = None
                                    if turn == "white":
                                        turn = "black" 
                                        print("Black's Turn")
                                    else: 
                                        turn = "white"
                                        print("White's Turn") 
                                else: 
                                    #print("L1.2.2")
                                    print("invalid moviment")

                        elif board[num].selected == True: 
                            #print("L2")
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