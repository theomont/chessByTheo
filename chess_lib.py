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

# update castlingStatus
# format white rook_a, white king, white rook_h, black rook_a, black king, black rook_h
def updateCastlingStatus(moving_piece, origin_cell, castlingStatus):
    if moving_piece.name == "king":
        if moving_piece.color == "white": castlingStatus[1] = False
        else: castlingStatus[4] = False
    elif moving_piece.name == "rook":
        if moving_piece.color == "white":
            if origin_cell.addr[1] == "a": castlingStatus[0] = False
            else: castlingStatus[2] = False
        else:
            if origin_cell.addr[1] == "a": castlingStatus[3] = False
            else: castlingStatus[5] = False
    

    return castlingStatus

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
        #print(delta_row, delta_column)
        if (delta_row in range(-1,2)) and (delta_column in range(-1,2)): 
            print("valid movimente returning True")
            return True
        elif piece.color == "white" and start_position == "1e" and abs(delta_column) == 2:
            return True
        elif piece.color == "black" and start_position == "8e" and abs(delta_column) == 2:
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
    
    if piece_moving.name == "knight" or piece_moving.name == "pawn":
        return True
    else:
        if delta_row == 0:
            # move to right
            #print("delta_row:",delta_row)
            #print("delta_column:",delta_column)
            if delta_column > 0:
                cell_name = start_position
                position_column_index = start_position_column_index + 1
                cell_name = cell_name[0] + getColumnName(position_column_index)
                for i in range(0,delta_column-1):
                    #print(i)
                    #print(cell_name)
                    #print(board[board_address_dict[cell_name]].piece.name)
                    #print(empty[1])
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
                    #print(i)
                    #print(cell_name)
                    #print(board[board_address_dict[cell_name]].piece.name)
                    #print(empty[1])
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_column_index = position_column_index - 1
                    cell_name = cell_name[0] + getColumnName(position_column_index)
                return True
        elif delta_column == 0:
            # move up
            #print("delta_row:",delta_row)
            #print("delta_column:",delta_column)
            if delta_row > 0:
                cell_name = start_position
                position_row_index = start_position_row_index + 1
                cell_name = getRowName(position_row_index) + cell_name[1]
                for i in range(0,delta_row-1):
                    print(i)
                    print(cell_name)
                    #print(board[board_address_dict[cell_name]].piece.name)
                    print(empty[1])
                    print(type(cell_name))
                    print(type(board_address_dict['2a']))
                    print(type(board[board_address_dict[cell_name]]))
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
                    print(type(cell_name))
                    print(type(board_address_dict[cell_name]))
                    print(type(board[board_address_dict[cell_name]]))
                    if board[board_address_dict[cell_name]].piece.name != empty[1]:
                        return False
                    position_row_index = position_row_index - 1
                    cell_name = getRowName(position_row_index) + cell_name[1]
                return True
        #diagonal
        else:
            # move up
            if delta_row > 0:
                #print("delta_row:",delta_row)
                #print("delta_column:",delta_column)
                # move up and right
                if delta_column > 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index + 1
                    position_column_index = start_position_column_index + 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(0,delta_column-1):
                        #print(i)
                        #print(cell_name)
                        #print(board[board_address_dict[cell_name]].piece.name)
                        #print(empty[1])
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
                        #print(i)
                        #print(cell_name)
                        #print(board[board_address_dict[cell_name]].piece.name)
                        #print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index + 1
                        position_column_index = start_position_column_index - 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True
            # move down
            elif delta_row < 0 :
                #print("delta_row:",delta_row)
                #print("delta_column:",delta_column)
                # move down and right
                if delta_column > 0:
                    cell_name = start_position
                    position_row_index = start_position_row_index - 1
                    position_column_index = start_position_column_index + 1
                    cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    for i in range(0,delta_column-1):
                        #print(i)
                        #print(cell_name)
                        #print(board[board_address_dict[cell_name]].piece.name)
                        #print(empty[1])
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
                        #print(i)
                        #print(cell_name)
                        #print(board[board_address_dict[cell_name]].piece.name)
                        #print(empty[1])
                        if board[board_address_dict[cell_name]].piece.name != empty[1]:
                            return False
                        position_row_index = start_position_row_index - 1
                        position_column_index = start_position_column_index - 1
                        cell_name = getRowName(position_row_index) + getColumnName(position_column_index)
                    return True


def validPlay(start_position, end_position, piece_moving, piece_on_destiny, board, board_address_dict, castlingStatus):
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
                    if piece_moving.name == "king":
                        if abs(delta_column) == 2:
                            if piece_moving.color == "white" and delta_column > 0:
                                if castlingStatus[1] and castlingStatus[2]:
                                    print("casting white king side")
                                    #print(board[board_address_dict["1f"]].piece.name, piece_moving.name )
                                    #board[board_address_dict["1f"]].piece = piece_moving
                                    print(board[board_address_dict["1f"]].piece.name, board[board_address_dict["1h"]].piece.name )
                                    board[board_address_dict["1f"]].piece = board[board_address_dict["1h"]].piece
                                    board[board_address_dict["1h"]].piece = Piece()
                                    castlingStatus[1], castlingStatus[2] = False, False
                                    return True

                            elif piece_moving.color == "white" and delta_column < 0:
                                if castlingStatus[0] and castlingStatus[1]:
                                    #board[board_address_dict["1d"]].piece = piece_moving
                                    board[board_address_dict["1d"]].piece = board[board_address_dict["1a"]].piece
                                    board[board_address_dict["1a"]].piece = Piece()
                                    castlingStatus[0], castlingStatus[1] = False, False
                                    return True

                            elif piece_moving.color == "black" and delta_column > 0:
                                if castlingStatus[4] and castlingStatus[5]:
                                    #board[board_address_dict["8f"]].piece = piece_moving
                                    board[board_address_dict["8f"]].piece = board[board_address_dict["8h"]].piece
                                    board[board_address_dict["8h"]].piece = Piece()
                                    castlingStatus[4], castlingStatus[5] = False, False
                                    return True

                            elif piece_moving.color == "black" and delta_column < 0:
                                if castlingStatus[3] and castlingStatus[4]:
                                    #board[board_address_dict["8d"]].piece = piece_moving
                                    board[board_address_dict["8d"]].piece = board[board_address_dict["8a"]].piece
                                    board[board_address_dict["8a"]].piece = Piece()
                                    castlingStatus[3], castlingStatus[4] = False, False
                                    return True
                            else: return False
                        else: return True
                    else: return True
                else: return False
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
#def initBoard(board_size, board_cell_size, board_margin_size):
#    return None

############
def initBoard(board_cell_white_color, board_cell_black_color, board_cell_size, board_margin_size):
    board = []
    posX = 0 #distance from left
    posY = 0 #distance from top
    color = board_cell_black_color
    addr = None
    selected = False

    board_size = 8*board_cell_size + 2*board_margin_size

    board_address_dict = {}
    board_rect = pygame.Rect(0,0,board_size,board_size)

    for i in range(0,8):
        posX = i*board_cell_size + board_margin_size
        if color == board_cell_white_color: color = board_cell_black_color
        else:  color = board_cell_white_color
        for j in range(0,8):
            posY = j*board_cell_size + board_margin_size
            addr = getRowName(7-j)+getColumnName(i)
            piece = Piece(addr)
            cell =  Cell(pygame.Rect(posX,posY,board_cell_size,board_cell_size), color, addr, selected, piece)
            board.append(cell)
            if color == board_cell_white_color: color = board_cell_black_color
            else:  color = board_cell_white_color
        
    ## checking set-up ##
    for board_index, cell in enumerate(board):
        #print(cell.addr, cell.piece.color, cell.piece.name)
        print(cell.addr, board_index)
        
        board_address_dict[cell.addr] = board_index # ex.: {"1a": 1}

    return [board_address_dict, board_rect, board]

def drawBoard(screen, board_color, board_rect, board_cell_sellected_color, board):
    pygame.draw.rect(screen, board_color, board_rect)
    
    for cell in board:   
        if cell.selected == False: 
            pygame.draw.rect(screen, cell.color, cell.rect)
            if cell.piece.logo != None:
                img = cell.piece.logo
                img.convert()
                img = pygame.transform.rotozoom(img,0,scale_piece_img_rate)
                img_rect = img.get_rect(center = cell.rect.center)
                screen.blit(img, img_rect)
        elif cell.selected == True:  
            pygame.draw.rect(screen, board_cell_sellected_color, cell.rect)
            img = cell.piece.logo
            img.convert()
            img = pygame.transform.rotozoom(img,0,scale_piece_img_rate)
            img_rect = img.get_rect(center = cell.rect.center)
            screen.blit(img, img_rect)

def drawMenu(screen, board_rect, menu_bg_img, menu_font_type, menu_font_size, menu_font_color, text_menu):
    screen.blit(menu_bg_img,(0,0))
    font = pygame.font.SysFont(menu_font_type, menu_font_size)
    font_img = font.render(text_menu, True, menu_font_color)
    font_img_rect = font_img.get_rect(center = board_rect.center)
    screen.blit(font_img,font_img_rect)

def drawCheckMate(screen, board_rect, menu_bg_img, menu_font_type, menu_font_size, menu_font_color, text_menu):
    #screen.blit(menu_bg_img,(0,0))
    font = pygame.font.SysFont(menu_font_type, menu_font_size)
    font_img = font.render(text_menu, True, menu_font_color)
    font_img_rect = font_img.get_rect(center = board_rect.center)
    screen.blit(font_img,font_img_rect)

def makeaPlay(clicked_cell_index, origin_cell_index, board, board_address_dict, moving_piece, cell_empty, moving_status,  castlingStatus, turn, check_mate):
    ## click on cell
    cell = board[clicked_cell_index]

    print("DEBUG: makeaPlay L0")
    if board[clicked_cell_index].selected == False: 
        print("DEBUG: makeaPlay L1.1")
        print(board[clicked_cell_index])
        print(cell)
        ## grab piece to move
        if moving_status == False and board[clicked_cell_index].piece.name != cell_empty.name and board[clicked_cell_index].piece.color == turn:
            print("DEBUG: makeaPlay L2.1")
            
            ## if board[clicked_cell_index].piece.name == "king": isKing = True
               
            board[clicked_cell_index].selected = True
            moving_status = True
            origin_cell_index = clicked_cell_index
            #origin_cell_name = board[clicked_cell_index].addr
            moving_piece = cell.piece
            
            
            print("grabbed", cell.piece.color, cell.piece.name, "from", cell.addr)
        elif moving_status == True:
            print("DEBUG: makeaPlay L2.2")
            print(board[origin_cell_index].addr, board[origin_cell_index].addr, moving_piece)
            
            ## move piece to a new cell
            if validPlay(board[origin_cell_index].addr, board[clicked_cell_index].addr, moving_piece, board[clicked_cell_index].piece, board, board_address_dict, castlingStatus):
                print("DEBUG: makeaPlay L3.1")    
                board[origin_cell_index].selected = False
                board[origin_cell_index].piece = cell_empty #lib.Piece()
                
                if board[clicked_cell_index].piece.name == "king":
                    check_mate = True

                ## promote pawn
                if moving_piece.name == "pawn":
                    if moving_piece.color == "white" and board[clicked_cell_index].addr[0] == '8':
                        moving_piece = Piece(moving_piece.color,'queen',sty.white_queen_logo)
                    elif moving_piece.color == "black" and board[clicked_cell_index].addr[0] == '1':
                        moving_piece = Piece(moving_piece.color,'queen',sty.black_queen_logo)

                board[clicked_cell_index].piece = moving_piece
                print("placed", moving_piece.color, moving_piece.name, "on", cell.addr)
                castlingStatus = updateCastlingStatus(moving_piece,  board[origin_cell_index], castlingStatus)
                print(castlingStatus)
                moving_status = False
                origin_cell_index = None
                moving_piece = None
                if turn == "white":
                    turn = "black" 
                    print("Black's Turn")
                else: 
                    turn = "white"
                    print("White's Turn") 
            else:
                print("DEBUG: makeaPlay L3.2")  
                print("invalid moviment")
    ## release piece back, deselect piece, give up to move that piece now
    elif board[clicked_cell_index].selected == True: 
        print("DEBUG: makeaPlay L1.2")
        board[clicked_cell_index].selected = False
        moving_status = False
        origin_cell_index = None
        moving_piece = None
        print("release", cell.piece.color, cell.piece.name, "back to", cell.addr)

    return clicked_cell_index, origin_cell_index, board, board_address_dict, moving_piece, cell_empty, moving_status,  castlingStatus, turn, check_mate



####
## Classes Def.
####
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




        