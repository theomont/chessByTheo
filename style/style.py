import pygame

# colors available
# pallet 1
wood_light = (191,178,161) #BFB2A1
wood_dark = (154,89,56) #9A5938
wood_board = (86,72,59) #56483b
wood_select = (0, 255, 0) 
#####

# pallet 2
snow = (255, 251, 252)
black_olive = (48, 51, 46)
black_board = (1, 4, 0)
verdigris = (98, 187, 193)

# pallet 3
#FFFFF0 ivory
plum = (143, 57, 133) #8F3985
space_cadet = (37, 40, 61) #25283D
light_sea_green = (7, 190, 184) #07BEB8

# pallet 3
#FFFFF0 ivory
paynes_gray = (76, 92, 104) #4C5C68
outer_space = (70, 73, 76) #46494C
blue_munsell = (25, 133, 161) #1985A1

dark_cyan = (4, 138, 129)
vivid_sky_blue = (84, 198, 235)



# pallet 3
ivory = (255,255,240) #FFFFF0
night = (12, 12, 12) #0C0C0C  # bad to see the black pieces on black cell

cerulean = (28, 110, 140) #1C6E8C
bright_pink = (237, 107, 134) #ED6B86 bright_pink (craiola)

state_grey = (125, 132, 1450) #7D8491
rose_red = (179, 57, 81) #B33951

coral = (255, 120, 79) #FF784F
process_cyan = (8, 178, 227) #08B2E3



dark_cyan = (55, 147, 146) #379392
steel_blue = (77, 126, 168) #4D7EA8
lapis_lazuli = (55, 105, 150) #376996

##############
## Templates
##############
## pattern:
## white cell, black cell, board margin, highlight cell
template = []
## Template Default (wood) ##
template.append([wood_light, wood_dark, wood_board, wood_select])

## Alter. template 1 ##
template.append([ivory, black_olive, dark_cyan, vivid_sky_blue])

## Alter. template 2 ##
template.append([ivory, plum, space_cadet, light_sea_green])

## Alter. template 3 ##
template.append([ivory, paynes_gray, outer_space, blue_munsell])


########################
## images ##

#menu_bg
helm_440 = pygame.image.load('./style/menu_bg.png')
helm_880 = pygame.image.load('./style/menu_bg2.png')

menu_bg_img_ratio_1 = helm_440
menu_bg_img_ratio_2 = helm_880

#board_bg
wood = pygame.image.load('./style/wood_board.png')
dark_marble = pygame.image.load('./style/dark_marble.jpg')

## pieces image logo
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