import copy

class ObjOfMine:
    def __init__(self, name):
        self.name = name


A = ObjOfMine("A")
B = ObjOfMine("B")
C = ObjOfMine("C")

#print(A.name,B.name, C.name)

L = [3,A,B,C]
L1 = copy.copy(L)
L2 = copy.deepcopy(L)
print(hex(id(L)),L)
print(hex(id(L1)),L1)
print(hex(id(L2)),L2)


L[0] = 1
print(hex(id(L)),L)
print(hex(id(L2)),L2)

## endereço da variavel A
auxA = A
auxL = L
A = 0
L = copy.deepcopy(0)
print(hex(id(0)), "Endereço da Variavel 0(&0)")
print(hex(id(A)), "Endereço da Variavel A(&A)")
print(hex(id(L)), "Endereço da Variavel L(&L)")
A = 0
L = 1
print(hex(id(A)), "Endereço da Variavel A(&A)")
print(hex(id(L)), "Endereço da Variavel L(&L)")


A = auxA
print(hex(id(A)), "Endereço do objeto referenciado por A, ou valor da variavel(A)")

print(A, "Objeto apontado por A, conteudo no endereço armazenado em *A")
#########
auxL = L
L = 0
print(hex(id(L)), "Endereço da Variavel L(&L)")

L = auxL
print(hex(id(L)), "Endereço do objeto referenciado por L, ou valor da variavel(L)")

print(L, "Objeto apontado por L, conteudo no endereço armazenado em *L")


#print("A id:",id(A))

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

#print(castlingStatus)
"""
castlingStatus = getCastlingStatus(white_castling_conditions, black_castling_conditions)
if castlingStatus["white"]: print(castlingStatus["white"])
if castlingStatus["black"]: print(castlingStatus["black"])

black_castling_conditions[1] = False

castlingStatus = getCastlingStatus(white_castling_conditions, black_castling_conditions)
if castlingStatus["white"]: print(castlingStatus["white"])
if castlingStatus["black"]: print(castlingStatus["black"])


myDict = {
    "1a": 1,
    "2a": 2,
}
var = "1a"
varValue = myDict[var]

print(myDict)
print(myDict['1a'])
print(myDict[var])
print(varValue)
"""
