###############################
###                         ###
###    CHESS by Theo v1.7   ###
###                         ###   
###############################
### last_update: 12/06/2024 ###
###############################
### Nota da versão:
### - tentar usar pygame
### - fork saindo de UI no console para GUI usandodo PySimpleGUI
### - - funçoes que serão impactadas def launch_menu, exit_game e draw_game
###############################
###############################
### Melhorias a realizar:
### - Tabuleiro apresenta peças brancas na parte de cima. Ficaria melhor que fosse o tabuleiro com elas pra baixo.
### - Não parmitir que o jogador mexa a pedra do adversario
###############################

import PySimpleGUI as sg

def init_game():
    ########################################################################
    ### Initializations
    ########################################################################   
    board = [] # 8x8 a A-H x 1-8

    empty = "[       ]" ## " "
    pawn = "pawn" ## i 
    king = "KING" ## I
    queen = "QUEN" ## Y
    bishop = "BSHP" ## A
    knight = "KNIT" ## S
    rook = "ROOK" ## H

    white_marker = "(WHT)"
    black_marker = "(BLK)"

    piece = {"pawn":pawn,\
             "king":king,\
             "queen":queen,\
             "bishop":bishop,\
             "knight":knight,\
             "rook":rook}

    #inicializando o tabuleiro (espaços vazios tem que ser iniciados também)
    for i in range(8):
        row = [empty for i in range(8)]
        board.append(row)

    board[0][0] = rook + white_marker
    board[0][7] = rook + white_marker
    board[7][0] = rook + black_marker
    board[7][7] = rook + black_marker

    board[0][1] = knight + white_marker
    board[0][6] = knight + white_marker
    board[7][1] = knight + black_marker
    board[7][6] = knight + black_marker

    board[0][2] = bishop + white_marker
    board[0][5] = bishop + white_marker
    board[7][2] = bishop + black_marker
    board[7][5] = bishop + black_marker

    board[0][4] = king + white_marker
    board[7][4] = king + black_marker

    board[0][3] = queen + white_marker
    board[7][3] = queen + black_marker

    board[1] = [pawn + white_marker for i in range(8)]
    board[6] = [pawn + black_marker for i in range(8)]

    rows_names = {
                  "1":0,
                  "2":1,
                  "3":2,
                  "4":3,
                  "5":4,
                  "6":5,
                  "7":6,
                  "8":7
                  }
    
    columns_names = {
                     "a":0,
                     "b":1,
                     "c":2,
                     "d":3,
                     "e":4,
                     "f":5,
                     "g":6,
                     "h":7
                     }
    
    # (piece_size + team_marker)*8 + 9 spaces 
    row_lenght = len(rook + white_marker + " ")*8 + 1

    sys = board, rows_names, columns_names, piece, white_marker, black_marker, empty

    return sys

# Função que desenha o tabuleiro
def draw_game(board):
    #draw_game_consoleUI(board)
    draw_game_GUI_pygame(board)

def draw_game_GUI_pygame(board):
    # Example file showing a circle moving on screen
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    
    #return None


def draw_game_consoleUI(board):
    #print("\n\n DEBUG: \n  row_lenght=",row_lenght,"len(board[0])",len(board[0]),"len(board[0][1])=",len(board[0][1]),"\n\n")    # debug

    row_lenght =  len(board[0][0])*8 + 9 # 8 x marker(pience and player) + margin(spaces)

    print("  +"+"-"*row_lenght+"+")
    for i in range(8):
        print(8-i,"| ",end="")
        for j in board[7-i]:
            print(j,end=" ")
        print("|")
    print("  +"+"-"*row_lenght+"+")
    print("    ",end="")
    for element in ['a','b','c','d','e','f','g','h']:
        print(" "*(len(board[0][0])//2) + element + " "*(len(board[0][0]) - len(board[0][0])//2),end="")
    print()

def getColumnIndex(position):
    if position[1] == 'a': column = 0 
    elif position[1] == 'b': column = 1
    elif position[1] == 'c': column = 2
    elif position[1] == 'd': column = 3
    elif position[1] == 'e': column = 4
    elif position[1] == 'f': column = 5
    elif position[1] == 'g': column = 6
    elif position[1] == 'h': column = 7

    return column

## pega a peça
def getPieceType(position):
    global sys
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys

    row = int(position[0]) - 1
    column = getColumnIndex(position)

    piece_representation = board[row][column]

    if board[row][column][0:4] == piece['king']:
        return "king"
    elif board[row][column][0:4] == piece['queen']:
        return "queen"
    elif board[row][column][0:4] == piece['bishop']:
        return "bishop"
    elif board[row][column][0:4] == piece['knight']:
        return "knight"
    elif board[row][column][0:4] == piece['rook']:
        return "rook"
    elif board[row][column][0:4] == piece['pawn']:
        return "pawn"
        

# Verifica se movimento é valido
# True when valid, False when invalid
def validMoviment(start_position, end_position, player_color):

    piece_type = getPieceType(start_position)

    start_position_row_index = int(start_position[0]) - 1
    start_position_column_index  = getColumnIndex(start_position)

    end_position_row_index  = int(end_position[0]) - 1
    end_position_column_index  = getColumnIndex(end_position)

    delta_row = end_position_row_index - start_position_row_index
    delta_column = end_position_column_index - start_position_column_index

    if piece_type == "king":
        if (delta_row in range(-1,1)) and (delta_column in range(-1,1)): return True
        else: return False

    elif piece_type == "queen":
        if abs(delta_row) == abs(delta_column): return True
        elif (delta_row != 0) and (delta_column == 0): return True
        elif (delta_row == 0) and (delta_column != 0): return True
        else: return False   

    elif piece_type == "bishop":
        if abs(delta_row) == abs(delta_column): return True
        else: return False   

    elif piece_type == "knight":
        if abs(delta_row) == 1 and abs(delta_column) == 2: return True
        elif abs(delta_row) == 2 and abs(delta_column) == 1: return True
        else: return False

    elif piece_type == "rook":
        if (delta_row != 0) and (delta_column == 0): return True
        elif (delta_row == 0) and (delta_column != 0): return True
        else: return False

    elif piece_type == "pawn":
        print("2 DEBUG player_color:", player_color)
        if player_color == "White":
            if delta_column == 0 and (delta_row == 1 or (delta_row == 2 and start_position_row_index == 1)): return True
            elif abs(delta_column) == 1 and delta_row == 1: return True
            else: return False
        
        if player_color == "Black":
            if delta_column == 0 and (delta_row == -1 or (delta_row == -2 and start_position_row_index == 6)): return True
            elif abs(delta_column) == 1 and delta_row == -1: return True
            else: return False

# Função que realiza a movimentação das peças. Retorna o tabuleiro atualizado e
# avisa se alguma peça foi removida do tabuleiro e se alguém venceu o jogo
def play(sys, player_color, start_position, end_position):
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys

    warning = ""

    line = int(start_position[0]) - 1
    if start_position[1] == 'a': column = 0 
    elif start_position[1] == 'b': column = 1
    elif start_position[1] == 'c': column = 2
    elif start_position[1] == 'd': column = 3
    elif start_position[1] == 'e': column = 4
    elif start_position[1] == 'f': column = 5
    elif start_position[1] == 'g': column = 6
    elif start_position[1] == 'h': column = 7

    moving_piece = board[line][column]
    board[line][column] = empty

    line = int(end_position[0]) - 1
    if end_position[1] == 'a': column = 0 
    elif end_position[1] == 'b': column = 1
    elif end_position[1] == 'c': column = 2
    elif end_position[1] == 'd': column = 3
    elif end_position[1] == 'e': column = 4
    elif end_position[1] == 'f': column = 5
    elif end_position[1] == 'g': column = 6
    elif end_position[1] == 'h': column = 7

    if board[line][column] != empty:
        if board[line][column][0:4] == piece['king']:
            warning = "King was killed! "+player_color+" won!"
        else:
            warning = "Piece killed!"
        
    board[line][column] = moving_piece
            
    return board, warning


def start_ai_game(sys):
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys
    print("Still not available, sorry")
    return True  
       
def start_friends_game(sys):
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys
    
    import pygame

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

    # draw board
    draw_game(board)

    quit_game = False
    both_kings_alive = True
    player_turn = "White"
    start_position = ""
    end_position = ""

    exit_key = "quit"
    input_origin_message = "Type de piece position from where you wish to move(row and collumn e.g. 7a)\n or type '"+exit_key+"' to quit this current game \n > "
    input_destiny_message = "Type your destiny:\n"
    
    while not quit_game and both_kings_alive:
        print()
        print(player_turn,"'s turn.",sep="")
        print()
        start_position = input(input_origin_message)
        if start_position == exit_key:
            quit_game = True
            return True
        elif len(start_position) == 2:
            if start_position[0] not in rows_names or start_position[1] not in columns_names:
                print("invalid position! Try again.")
            else:
                end_position = input(input_destiny_message)
                if len(end_position) == 2:
                    if end_position[0] not in rows_names or end_position[1] not in columns_names:
                        print("invalid position! Try again.")
                    elif not validMoviment(start_position, end_position, player_turn):
                        print("this moviment is not allowed for this type of piece! Try again.")
                    else: ## core code ##
                        print("Moving piece from", start_position,"to new position",end_position)
                        board, warning = play(sys, player_turn, start_position, end_position,)
                        print(warning)
                        draw_game(board)
                        if warning[0:4] == "King":
                            both_kings_alive = False
                            return player_turn
                        if player_turn == "White":
                            player_turn = "Black"
                        else:
                            player_turn = "White"
                else:
                    print("Comando invalido! Deve ser apenas dois caracter ou o comando 'sair'.")
        else:
            print("Comando invalido! Deve ser apenas dois caracter ou o comando 'sair'.")   

def show_settings():
    print("Still not available, sorry")
    return True

def exit_game(flow_control=True):
    return exit_game_consoleUI(flow_control=True)

def exit_game_GUI(flow_control=True): 
    print("not build")
            
def exit_game_consoleUI(flow_control=True):
    confirm_message = "Are you sure you wish to quit the game?"
    yes = "y"
    no = "n" 
    options_message = "Entry "+yes+" to confirm or "+no+" to ruturn."
    invalid_entry_message = "Wrong option, try again."

    sel = "" 
    while sel != yes and sel != no:
        print(confirm_message)
        print(options_message)
        sel = input(">>")
        if sel != yes and sel != no:
            print(invalid_entry_message)
        else:
            if sel == yes:
                flow_control = False
                return flow_control
            else:
                return True

def launch_menu(sys):
    #return launch_consoleUI_menu(sys)
    return launch_GUI_menu(sys)

def launch_GUI_menu(sys):
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys
    option = 0
    valid_option = [1,2,3,4]

    # All the stuff inside your window.
    layout = [  [sg.Text("Choose your option:")],
                [sg.Button('Play agaisnt A.I.')], [sg.Button('Play with friend')],
                [sg.Button('Settings')], [sg.Button('Quit Game')] ]
    
    # Create the Window
    window = sg.Window('Chess by Theo', layout, size=(250, 200), 
                   resizable=True)

    while True:
        event, values = window.read()

        if event == 'Play agaisnt A.I.': return start_ai_game(sys)
        elif event == 'Play with friend': 
            window.close()
            return start_friends_game(sys)
        elif event == 'Settings': return show_settings()
        elif event == sg.WIN_CLOSED or event == 'Quit Game': 
            window.close() #return exit_game()
            break

def launch_consoleUI_menu(sys):
    board, rows_names, columns_names, piece, white_marker, black_marker, empty = sys
    option = 0
    valid_option = [1,2,3,4]

    print("\n\n")
    print("--------- CHESS by Theo ---------")
    print("Choose your option:")
    print("1. Play agaisnt A.I.")
    print("2. Play with friend.")
    print("3. Settings")
    print("4. Quit game.")

    option = int(input())

    if option in valid_option:
        if option == 1: return start_ai_game(sys)
        elif option == 2: return start_friends_game(sys)
        elif option == 3: return show_settings()
        elif option == 4: return exit_game()
    else:
        print("invalid option, try again")
        return True
    



########################################################################    
### Code Flow ###
########################################################################   
repeat = True
while repeat:
    sys = init_game()

    repeat = launch_menu(sys)                  

print("----------- end -----------\n\n") 
