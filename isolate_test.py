class ObjOfMine:
    def __init__(self, name):
        self.name = name


A = ObjOfMine("A")
B = ObjOfMine("B")
C = ObjOfMine("C")

#print(A.name,B.name, C.name)

A = B

#print("A:",A.name,"B:",B.name)
#print("A id:",id(A),"B id:",id(B))

B.name = "new_B"

#print("A:",A.name,"B:",B.name)
#print("A id:",id(A),"B id:",id(B))
#############################################################
delta_row = 1
delta_column = -1

#print(delta_row in range(-1,1))
#print(delta_column in range(-1,1))

#print((delta_row in range(-1,1)) and (delta_column in range(-1,1)))
#############################################################
theo = "theo"
#print(theo)

#print(theo[1])

#theo[1] = "e"
theo = theo[0]+"e"+theo[2]+theo[3]

#print(theo)
#############################################################

#for i in range(-5,0):
#    print(i)

def getCastlingStatus(white_castling_conditions, black_castling_conditions):
    castlingStatus["white"] = white_castling_conditions[0] and white_castling_conditions[1] and white_castling_conditions[2]
    castlingStatus["black"] = black_castling_conditions[0] and black_castling_conditions[1] and black_castling_conditions[2]
    return castlingStatus

# rook, king, rook
white_castling_conditions = [True, True, True]
black_castling_conditions = [True, True, True]
castlingStatus = {"white":True, "black":True}

print(castlingStatus)

castlingStatus = getCastlingStatus(white_castling_conditions, black_castling_conditions)
if castlingStatus["white"]: print(castlingStatus["white"])
if castlingStatus["black"]: print(castlingStatus["black"])

black_castling_conditions[1] = False

castlingStatus = getCastlingStatus(white_castling_conditions, black_castling_conditions)
if castlingStatus["white"]: print(castlingStatus["white"])
if castlingStatus["black"]: print(castlingStatus["black"])



