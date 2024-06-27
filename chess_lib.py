#####
## lib adapted for version v3.+
#####
import pygame
import style.style as sty
## constants
empty = 'none', 'empty', None
scale_piece_img_rate = 0.6

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

# give the initial piece in the address name
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

    if name in white_pawn: return 'white', 'pawn', sty.white_pawn_logo
    elif name in white_rook: return 'white', 'rook', sty.white_rook_logo
    elif name in white_knight: return 'white', 'knight', sty.white_knight_logo
    elif name in white_bishop: return 'white', 'bishop', sty.white_bishop_logo
    elif name in white_queen: return 'white', 'queen', sty.white_queen_logo 
    elif name in white_king: return 'white', 'king', sty.white_king_logo

    elif name in black_pawn: return 'black', 'pawn', sty.black_pawn_logo
    elif name in black_rook: return 'black', 'rook', sty.black_rook_logo
    elif name in black_knight: return 'black', 'knight', sty.black_knight_logo
    elif name in black_bishop: return 'black', 'bishop', sty.black_bishop_logo
    elif name in black_queen: return 'black', 'queen', sty.black_queen_logo
    elif name in black_king: return 'black', 'king', sty.black_king_logo
    else: return empty

# check if maviment is valid
# True when valid, False when invalid
def validMoviment(start_position, end_position, piece):
    if type(piece) == type(Piece()):
        piece_color = piece.color
        piece_type  = piece.name
    else: piece_color, piece_type,  piece_logo = piece

    start_position_row_index = getRowIndex(start_position[0])
    start_position_column_index  = getColumnIndex(start_position[1])

    end_position_row_index  = getRowIndex(end_position[0])
    end_position_column_index  = getColumnIndex(end_position[1])

    delta_row = end_position_row_index - start_position_row_index
    delta_column = end_position_column_index - start_position_column_index

    if piece_type == "king":
        print(delta_row, delta_column)
        if (delta_row in range(-1,2)) and (delta_column in range(-1,2)): 
            print("valid movimente returning True")
            return True
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
            ## moviment case
            if delta_column == 0 and (delta_row == 1 or (delta_row == 2 and start_position_row_index == 1)): return True
            ## killinig case
            elif abs(delta_column) == 1 and delta_row == 1: return True
            else: return False
        
        if piece_color == "black":
            ## moviment case
            if delta_column == 0 and (delta_row == -1 or (delta_row == -2 and start_position_row_index == 6)): return True
            ## killinig case
            elif abs(delta_column) == 1 and delta_row == -1: return True
            else: return False

def pathFree(start_position, end_position, piece_moving, board, board_address_dict):
    start_position_row_index = getRowIndex(start_position[0])
    start_position_column_index  = getColumnIndex(start_position[1])

    end_position_row_index  = getRowIndex(end_position[0])
    end_position_column_index  = getColumnIndex(end_position[1])

    delta_row = end_position_row_index - start_position_row_index
    delta_column = end_position_column_index - start_position_column_index
    
    if piece_moving.name == "knight" or piece_moving.name == "pawn" or piece_moving.name == "king":
        return True
    else:
        if delta_row == 0:
            # move to right
            print("delta_row:",delta_row)
            print("delta_column:",delta_column)
            if delta_column > 0:
                cell_name = start_position
                position_column_index = start_position_column_index + 1
                cell_name = cell_name[0] + getColumnName(position_column_index)
                for i in range(0,delta_column-1):
                    print(i)
                    print(cell_name)
                    print(board[board_address_dict[cell_name]].piece.name)
                    print(empty[1])
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_column_index = position_column_index + 1
                    cell_name = cell_name[0] + getColumnName(position_column_index)
                return True
            # move to left
            elif delta_column < 0:
                cell_name = start_position
                position_column_index = start_position_column_index - 1
                cell_name = cell_name[0] + getColumnName(position_column_index)
                for i in range(delta_column,-1):
                    print(i)
                    print(cell_name)
                    print(board[board_address_dict[cell_name]].piece.name)
                    print(empty[1])
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_column_index = position_column_index - 1
                    cell_name = cell_name[0] + getColumnName(position_column_index)
                return True
        elif delta_column == 0:
            # move up
            print("delta_row:",delta_row)
            print("delta_column:",delta_column)
            if delta_row > 0:
                cell_name = start_position
                position_row_index = start_position_row_index + 1
                cell_name = getRowName(position_row_index) + cell_name[1]
                for i in range(0,delta_row-1):
                    print(i)
                    print(cell_name)
                    print(board[board_address_dict[cell_name]].piece.name)
                    print(empty[1])
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_row_index = position_row_index + 1
                    cell_name = getRowName(position_row_index) + cell_name[1]
                return True
            # move to down
            elif delta_row < 0:
                cell_name = start_position
                position_row_index = start_position_row_index - 1
                cell_name = getRowName(position_row_index) + cell_name[1]
                for i in range(delta_row,-1):
                    print(i)
                    print(cell_name)
                    print(board[board_address_dict[cell_name]].piece.name)
                    print(empty[1])
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_row_index = position_row_index - 1
                    cell_name = getRowName(position_row_index) + cell_name[1]
                return True
        #diagonal
        else:
            # move up
            if delta_row > 0:
                print("delta_row:",delta_row)
                print("delta_column:",delta_column)
                # move up and right
                if delta_column > 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index + 1
                    position_column_index = start_position_column_index + 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(0,delta_column-1):
                        print(i)
                        print(cell_name)
                        print(board[board_address_dict[cell_name]].piece.name)
                        print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index + 1
                        position_column_index = start_position_column_index + 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True
                # move up and left
                elif delta_column < 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index + 1
                    position_column_index = start_position_column_index - 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(delta_column,-1):
                        print(i)
                        print(cell_name)
                        print(board[board_address_dict[cell_name]].piece.name)
                        print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index + 1
                        position_column_index = start_position_column_index - 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True
            # move down
            elif delta_row < 0 :
                print("delta_row:",delta_row)
                print("delta_column:",delta_column)
                # move down and right
                if delta_column > 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index - 1
                    position_column_index = start_position_column_index + 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(0,delta_column-1):
                        print(i)
                        print(cell_name)
                        print(board[board_address_dict[cell_name]].piece.name)
                        print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index - 1
                        position_column_index = start_position_column_index + 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True
                # move down and left
                elif delta_column < 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index - 1
                    position_column_index = start_position_column_index - 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(delta_column,-1):
                        print(i)
                        print(cell_name)
                        print(board[board_address_dict[cell_name]].piece.name)
                        print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index - 1
                        position_column_index = start_position_column_index - 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True


def validPlay(start_position, end_position, piece_moving, piece_on_destiny, board, board_address_dict):
    start_position_row_index = getRowIndex(start_position[0])
    start_position_column_index  = getColumnIndex(start_position[1])

    end_position_row_index  = getRowIndex(end_position[0])
    end_position_column_index  = getColumnIndex(end_position[1])

    delta_row = end_position_row_index - start_position_row_index
    delta_column = end_position_column_index - start_position_column_index
    
    if validMoviment(start_position, end_position, piece_moving):
        if piece_on_destiny.name == empty[1]:   
            # if moving is pawn
            if piece_moving.name == "pawn":
                # pawn walk position in front him
                if delta_column == 0:
                    return True
                # pawn walk position in diogonal
                elif abs(delta_column) == 1:
                    return False
            else:
                if pathFree(start_position, end_position, piece_moving, board, board_address_dict):
                    print("validMoviment returning True")
                    return True
        elif piece_on_destiny.color != piece_moving.color:
            # if moving is pawn
            if piece_moving.name == "pawn":
                # pawn walk position in front him
                if delta_column == 0:
                    return False
                # pawn walk position in diogonal
                elif abs(delta_column) == 1:
                    return True
            else:
                if pathFree(start_position, end_position, piece_moving, board, board_address_dict):
                    print("validMoviment returning True")
                    return True
        else:
            return False
        
    else: return False

    # if destiny king, True (end game)


# building
def initBoard(board_size, board_cell_size, board_margin_size):
    return None

# not in use til v2.* (not finished)
class Board:
    def __init__(self, rect, cells):
        self.rect = rect
        self.cells = cells

class Cell:
    def __init__(self, rect, color, addr, selected, piece):
        self.rect = rect
        self.color = color
        self.addr = addr
        self.selected = selected
        self.piece = piece

class Piece:
    def __init__(self, *args):
        # empty obj call like lib.Piece()
        if len(args) == 0: 
            self.color, self.name, self.logo = empty

        # build with start board address call like lib.Piece(addr)
        elif len(args) == 1:
            self.color, self.name, self.logo = setInitialPiece(args[0])
        
        # build with piece color, piece name and piece logo image
        # call like lib.Piece(color, name, logo)
        elif len(args) == 3:
            self.color = args[0]
            self.name = args[1]
            self.logo = args[2]




        