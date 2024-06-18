import pygame
## constants
empty = 'none','empty', None
scale_piece_img_rate = 0.6

## piece images
white_pawn_logo = pygame.image.load('./style/white_pawn.png')
white_rook_logo = pygame.image.load('./style/white_rook.png')
white_knight_logo = pygame.image.load('./style/white_knight.png')
white_bishop_logo = pygame.image.load('./style/white_bishop.png')
white_queen_logo = pygame.image.load('./style/white_queen.png')
white_king_logo = pygame.image.load('./style/white_king.png')

black_pawn_logo = pygame.image.load('./style/black_pawn.png')
black_rook_logo = pygame.image.load('./style/black_rook.png')
black_knight_logo = pygame.image.load('./style/black_knight.png')
black_bishop_logo = pygame.image.load('./style/black_bishop.png')
black_queen_logo = pygame.image.load('./style/black_queen.png')
black_king_logo = pygame.image.load('./style/black_king.png')

## methods and functions
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

    if name in white_pawn: return 'white', 'pawn', white_pawn_logo
    elif name in white_rook: return 'white', 'rook', white_rook_logo
    elif name in white_knight: return 'white', 'knight', white_knight_logo
    elif name in white_bishop: return 'white', 'bishop', white_bishop_logo
    elif name in white_queen: return 'white', 'queen', white_queen_logo 
    elif name in white_king: return 'white', 'king', white_king_logo

    elif name in black_pawn: return 'black', 'pawn', black_pawn_logo
    elif name in black_rook: return 'black', 'rook', black_rook_logo
    elif name in black_knight: return 'black', 'knight', black_knight_logo
    elif name in black_bishop: return 'black', 'bishop', black_bishop_logo
    elif name in black_queen: return 'black', 'queen', black_queen_logo
    elif name in black_king: return 'black', 'king', black_king_logo
    else: return empty

## versão pré-pygame (requer update)
# Verifica se movimento é valido
# True when valid, False when invalid
def validMoviment(start_position, end_position, piece):
    piece_color, piece_type,  piece_logo = piece

    start_position_row_index = getRowIndex(start_position[0])
    start_position_column_index  = getColumnIndex(start_position[1])

    end_position_row_index  = getRowIndex(end_position[0])
    end_position_column_index  = getColumnIndex(end_position[1])

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
        if piece_color == "white":
            if delta_column == 0 and (delta_row == 1 or (delta_row == 2 and start_position_row_index == 1)): return True
            elif abs(delta_column) == 1 and delta_row == 1: return True
            else: return False
        
        if piece_color == "black":
            if delta_column == 0 and (delta_row == -1 or (delta_row == -2 and start_position_row_index == 6)): return True
            elif abs(delta_column) == 1 and delta_row == -1: return True
            else: return False
